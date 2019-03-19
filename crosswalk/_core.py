"""
This module handles all the code relating to function and 
module re-routing.
"""
import os
import sys


# -- Cache the directory to the hosts location
HOST_DIR = os.path.join(
    os.path.dirname(__file__),
    'hosts',
)

# -- We assume that we will not be dynamically adding hosts
# -- at execution time, so we cache the host list too
HOSTS = os.listdir(HOST_DIR)

# -- Cache the host package prefix location
HOST_PREFIX = 'crosswalk.hosts.'

# -- To optimise the dynamic rerouting we cache the routes
# -- we have found to prevent us from having to do it every
# -- time
_REROUTING_CACHE = dict()

# -- We also cache the active host so we dont have to
# -- continuously check
DEFAULT_API = None


# ------------------------------------------------------------------------------
def hosts():
    """
    Returns a list of available hosts

    :return:
    """
    return HOSTS


# ------------------------------------------------------------------------------
def reroute(func):
    """
    This is a decorator which will dynamically reroute the function 
    call to an equivelent function within the most approporate host 
    api.
    
    This function utilises caching to minimise call overheads, and will
    only attempt to load the different host api's once. Any host api's
    which are not able to be imported within the current environment will
    subsequently be ignored.
    
    Unless explicitely expressed, the API used will always be the first
    API which was successfully loaded. If there are multiple API's available
    within the interpreter environment you may utilise the xapi keyword
    to define exactly which api you want to utilse for your function
    call.
    """

    def wrapper(*args, **kwargs):

        # -- These are our global caches which we need
        # -- writable access to
        global _REROUTING_CACHE

        # -- Check for a bespoke API request. If this function and API
        # -- has already been requested at any point in the interpreters
        # -- life span then this is hte only bit of logic we need before
        # -- attempting to call the mapped function
        requested_api = kwargs.pop('xapi', GetDefaultApi())

        # -- Get the absolute path to the module containing
        # -- the desired function
        rerouted_module_path = 'crosswalk.hosts.' + requested_api + '.' + func.__module__[10:]

        # -- Now get the absolute path to the actual function
        # -- in question
        abs_func_address = rerouted_module_path + '.' + func.__name__

        # -- If the function is not already cached, cache the pointer
        # -- to it
        if abs_func_address not in _REROUTING_CACHE:

            # -- Import the module to give us access to the function
            rerouted_module = __import__(
                rerouted_module_path,
                fromlist=[''],
            )

            # -- Get the function/class from the module
            rerouted_func = getattr(rerouted_module, func.__name__)

            # -- Cache it
            _REROUTING_CACHE[abs_func_address] = rerouted_func

        # -- Utilise the cache to call the function
        return _REROUTING_CACHE[abs_func_address](*args, **kwargs)

    return wrapper


# ------------------------------------------------------------------------------
def GetDefaultApi():
    """
    Returns the default api - that is the api which is the first to
    validly import

    :return: tr
    """
    # -- We use a global for this to help performance
    global DEFAULT_API

    # -- If the global is already set then we do not have
    # -- to do anything more
    if DEFAULT_API:
        return DEFAULT_API

    # -- Cycle over each host to find out which ones
    # -- are available within this environment.
    for possible_host in HOSTS:

        # -- Build up a fully qualified import path
        host_api_name = HOST_PREFIX + possible_host

        # -- If the host api imports we use it, otherwise we
        # -- try the next one
        try:
            __import__(
                host_api_name,
                fromlist=[''],
            )

            # -- Take the first loadable as the default API
            DEFAULT_API = possible_host

            return DEFAULT_API

        except:
            print(sys.exc_info())
            continue


# ------------------------------------------------------------------------------
# -- This is used for dynamic function generation
_REROUTE_FUNC_CODE = """
@reroute
def _(): pass
"""


# ------------------------------------------------------------------------------
class UndefinedRouting(object):
    """
    This handles any rerouting to functions which exist in the 
    host but do not exist in the base API. This allows for hosts
    to 'over implement' without the user calling anything 
    differently.
    """

    def __init__(self, wrapped):
        self.wrapped = wrapped
        self._rerouted = dict()

    def __getattr__(self, name):
        try:
            return getattr(self.wrapped, name)

        except AttributeError:

            try:
                return self._rerouted[name]

            except KeyError:
                # -- Dynamically create a function with the
                # -- expected name and apply the rerouting decorator
                exec(_REROUTE_FUNC_CODE.replace('_', name))
                dynamic_function = eval(name)

                self._rerouted[name] = dynamic_function

                return dynamic_function


    @classmethod
    def setup(cls, module_name):
        sys.modules[module_name] = cls(sys.modules[module_name])

    def __dir__(self):
        return dir(self.wrapped)
