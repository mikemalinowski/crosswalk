from ._core import reroute, UndefinedRouting


# ------------------------------------------------------------------------------
@reroute
def mul(count):
    """
    As this is defining the Standard API we do not need to do 
    any actual functionality implementation here unless its a function
    which will only ever harness the Standard API functions to resolve
    something.
    
    The re-routing decorator ensures that any calls to this function
    will automatically get passed up to either chalk or cheese.
    
    :param count: 
    :return: 
    """
    pass


# ------------------------------------------------------------------------------
# -- This is here to allow the module to dynamically re-route
# -- to any over-implemented functions within a host which is
# -- not defined in the base api.
UndefinedRouting.setup(__name__)
