from ._core import reroute
from ._core import UndefinedRouting


# ------------------------------------------------------------------------------
@reroute
def rename(element, new_name):
    """
    This will rename the given element and return the newly
    assigned name.

    :param element: Element to rename
    :type element: Host Specific

    :param new_name: name to assign to the element
    :type wildcard: str

    :return: str
    """
    return None


# ------------------------------------------------------------------------------
@reroute
def delete(element):
    """
    Deletes the given element from the scene

    :param element: Element to delete
    :type element: Host Specific

    :return: True if the element was successfully removed
    """
    return False


# ------------------------------------------------------------------------------
@reroute
def create(element_type, name):
    """
    Creates an element of a specified type and assigns the given name
    to it.

    :param element_type: Type of element to create
    :type element_type: str

    :param name: Name to assign to the newly created element
    :type name: str

    :return: element created
    """
    return None


# ------------------------------------------------------------------------------
@reroute
def select(elements):
    """
    Selects a list of given elements

    :param elements: List of elements to select
    :type elements: list(Element, Element, ...)

    :return: None
    """
    return None


# ------------------------------------------------------------------------------
@reroute
def deselect(elements=None):
    """
    Deselects the given elements. If no elements are passed then all
    elements are deselected.

    :param elements: List of elements to deselect. If none are given
        then all elements are deselected.
    :type elements: list(Element, Element, ...)

    :return: None
    """
    return None



# ------------------------------------------------------------------------------
# -- This is here to allow the module to dynamically re-route
# -- to any over-implemented functions within a host which is
# -- not defined in the base api.
UndefinedRouting.setup(__name__)