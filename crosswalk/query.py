from ._core import reroute
from ._core import UndefinedRouting


# ------------------------------------------------------------------------------
@reroute
def get(name):
    """
    This should get the element using the given name.

    :param name: Name of the element to get
    :type name: str

    :return: element (or None if not found)
    """
    return None


# ------------------------------------------------------------------------------
@reroute
def find(wildcard, of_type=None):
    """
    This will take in the given wildcard string and find all elements
    whose names match the given wildcard. The filtered list can be further
    refined using the 'of_type' variable where you can define the type
    of elements to return.

    :param wildcard: A wildcard string to search for
    :type wildcard: str

    :param of_type: A type classification
    :type of_type: str

    :return: list(element, element, element, ...)
    """
    return list()


# ------------------------------------------------------------------------------
@reroute
def selected():
    """
    Returns the list of elements currently selected

    :return: list(element, element, element, ...)
    """
    return list()


# ------------------------------------------------------------------------------
@reroute
def exists(name):
    """
    Checks wither an element with the given name exists within the scene

    :param name: Name to look for
    :type name: str

    :return: bool
    """
    return False


# ------------------------------------------------------------------------------
# -- This is here to allow the module to dynamically re-route
# -- to any over-implemented functions within a host which is
# -- not defined in the base api.
UndefinedRouting.setup(__name__)