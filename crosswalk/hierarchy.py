from ._core import reroute
from ._core import UndefinedRouting


# ------------------------------------------------------------------------------
@reroute
def children(element, wildcard=None, recursive=None):
    """
    This will return all the children of the given element. If a
    wildcard is given then only objects whose names match that wildcard
    will be returned.

    :param element: Element to search from
    :type element: Host Specific

    :param wildcard: A string to match against, where * acts as a wildcard
    :type wildcard: str

    :param recursive: If true then all children and sub-chlldren will
        be returned (providing they match the wildcard). If False then
        only the elements immediate children are considered.

    :return: list(element, element, element, ...)
    """
    return list()


# ------------------------------------------------------------------------------
@reroute
def parent(element, index=0):
    """
    This will return the parent of the node. By default this will
    always return the first (immediate) parent, but you can utilise
    the index argument to specify a parent of a given level. For instance
    -1 is the top level parent.

    :param element: Element to get the parent from
    :type element: Host Specific

    :param index: The index to get a parent for - zero being the default
    :type index: int

    :return: Element
    """
    return None


# ------------------------------------------------------------------------------
@reroute
def add_child(element, child):
    """
    Adds a child to the given element.

    :param element: Element to add a child to
    :type element: Host Specific

    :param child: The child to give a new parent
    :type child: Host Specific

    :return: child
    """
    return None


# ------------------------------------------------------------------------------
@reroute
def set_parent(element, parent):
    """
    This will set the parent of the given element.

    :param element: Element to move under the new parent
    :type element: Host Specific

    :param parent: The element to add the new child to
    :type parent: Host Specific

    :return: element
    """
    return None


# ------------------------------------------------------------------------------
# -- This is here to allow the module to dynamically re-route
# -- to any over-implemented functions within a host which is
# -- not defined in the base api.
UndefinedRouting.setup(__name__)