from ._core import reroute
from ._core import UndefinedRouting


# ------------------------------------------------------------------------------
@reroute
def add(element, name, property_type, value):
    """
    Adds an property to the given element.

    :param element: The element to add the property to
    :type element: Host Specific

    :param name: Name of the property to add
    :type name: str

    :param property_type: The type of property to be added to the element
    :type property_type: str

    :param value: The initial value to apply to the property
    :type value: variable

    :return: property (Host Specific)
    """
    return None


# ------------------------------------------------------------------------------
@reroute
def remove(property_name):
    """
    Removes the given property.

    :param property: The property (or property identifier) to remove
    :type property: Host Specific

    :return: True if the property was removed
    """
    return None


# ------------------------------------------------------------------------------
@reroute
def get_value(element, property_name):
    """
    Gets the value of the given property

    :param property: The property (or identifier) to get the value of
    :type property: Host Specific

    :return: value
    """
    return None


# ------------------------------------------------------------------------------
@reroute
def set_value(element, property_name, value):
    """
    Sets the value of the property.

    :param property: The property (or identifier) to set the value of
    :type property: Host Specific

    :param value: The value to set on the property
    :type value: variable

    :return: The value assigned
    """
    return None


# ------------------------------------------------------------------------------
@reroute
def link(source, destination):
    """
    Links two properties - from the source to the destination.

    :param source: The property to connect from
    :type source: Host Specific

    :param destination: The property to connect to
    :type destination: Host Specific

    :return: True if the connection was made
    """
    return None


# ------------------------------------------------------------------------------
@reroute
def unlink(destination, source=None):
    """
    This will unlink the connection between two properties. If no source
    is given all sources to the destination will be removed.

    :param destination: property to disconnect from
    :type destination: Host Specific

    :param source: If given, only links between the source property and
        the destination property will be unlinked.
    :type source: Host Specific

    :return: True if connections were unlinked
    """
    return


# ------------------------------------------------------------------------------
# -- This is here to allow the module to dynamically re-route
# -- to any over-implemented functions within a host which is
# -- not defined in the base api.
UndefinedRouting.setup(__name__)
