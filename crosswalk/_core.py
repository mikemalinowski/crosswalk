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

# -- Cache this modules name
MODULE_NAME = __name__.split('.')[0]

# -- Cache the host package prefix location
HOST_PREFIX = '%s.hosts.' % MODULE_NAME

# -- To optimise the dynamic rerouting we cache the routes
# -- we have found to prevent us from having to do it every
# -- time
_REROUTING_CACHE = dict()

# -- We also cache the active host so we dont have to
# -- continuously check
DEFAULT_API = None
APIS = dict()


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
        global DEFAULT_API
        global APIS

        # -- Check for a bespoke API request. If this function and API
        # -- has already been requested at any point in the interpreters
        # -- life span then this is hte only bit of logic we need before
        # -- attempting to call the mapped function
        requested_api = kwargs.pop('xapi', DEFAULT_API)

        try:
            # -- Look up the api module by the name
            expected_api = APIS[requested_api]

            # -- Attempt to call the module. Note that we only
            host_function = _REROUTING_CACHE[expected_api][func]

        except KeyError:

            # -- To get here we're either dealing with a scenario
            # -- where none of our API's are loaded (its our first
            # -- reroute request) or its the first time this function
            # -- is being called.
            # -- Start by ensuring the API's are warmed up.
            if not APIS:

                # -- Get the sub module name. This we expect
                # -- to find under the host prefix import
                func_address = str(func.__module__)
                module_name = '.' + '.'.join(func_address.split('.')[1:])

                # -- Cycle over each host to find out which ones
                # -- are available within this environment.
                for possible_host in HOSTS:

                    # -- Build up a fully qualified import path
                    host_api_name = HOST_PREFIX + possible_host + module_name

                    # -- If the host api imports we use it, otherwise we
                    # -- try the next one
                    try:
                        APIS[possible_host] = __import__(
                            host_api_name,
                            fromlist=[''],
                        )

                        # -- Take the first loadable as the default API
                        DEFAULT_API = DEFAULT_API or possible_host

                    except:
                        continue

            # -- We allow any function to go through a specific
            # -- api if it is explicitly requested otherwise
            # -- we simply fall back to the default api
            expected_api = APIS[requested_api or DEFAULT_API]

            # -- This may be the first time we're asking for something
            # -- from the api, in which case we initialise a dictionary
            # -- to store the function mapping within.
            if expected_api not in _REROUTING_CACHE:
                _REROUTING_CACHE[expected_api] = dict()

            # -- If for any reason we cannot get the function, we
            # -- assume its not implemented
            try:
                host_function = getattr(expected_api, func.__name__)
                _REROUTING_CACHE[expected_api][func] = host_function

            except:
                raise NotImplementedError()

        # -- Run the application implementation
        return host_function(*args, **kwargs)

    return wrapper


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