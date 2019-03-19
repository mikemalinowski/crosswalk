from ._core import reroute
from ._core import UndefinedRouting


# ------------------------------------------------------------------------------
@reroute
def new(name):
    """
    Creates a new visual layer

    :param name: Name of hte layer to create
    :type name: str

    :return: Host Specific
    """
    return None


# ------------------------------------------------------------------------------
@reroute
def all():
    """
    Returns all the visual layers

    :return: list(object, object, ...)
    """
    return list()


# ------------------------------------------------------------------------------
@reroute
def add_to(layer, elements):
    """
    Adds the given elements to the given layer

    :param layer: The layer to add the elements to
    :type layer: Host Specific

    :param elements: List of elements to add to the layer
    :type elements: list(element, element, ...)

    :return: None
    """
    return None


# ------------------------------------------------------------------------------
@reroute
def remove_from(layer, elements):
    """
    Removes the given elements from the given layer

    :param layer: The layer to remove items from
    :type layer: Host Specific

    :param elements: List of elements to remove from the given layer
    :type elements: list(element, element, ...)

    :return: None
    """
    return None


# ------------------------------------------------------------------------------
@reroute
def elements(layer):
    """
    Returns all the elements within the given visual layer

    :param layer: Layer to get elements from
    :type layer: Host Specific

    :return: list(element, element, ...)
    """
    return list()


# ------------------------------------------------------------------------------
# -- This is here to allow the module to dynamically re-route
# -- to any over-implemented functions within a host which is
# -- not defined in the base api.
UndefinedRouting.setup(__name__)