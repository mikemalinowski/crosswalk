"""
This is a stub file and will always be overridden by the application
implementation.
"""
import typing



def add_string_attribute(object_: object, attribute_name: str, value: typing.Any) -> None:
    """
    This should add an attribute to the object, and where the attributes are
    typed, it should be a string

    Args:
        object_: The object or object name to add the attribute to
        attribute_name: The name of the attribute
        value: The value of the attribute
    """
    pass


def add_float_attribute(object_: object, attribute_name: str, value: typing.Any) -> None:
    """
    This should add an attribute to the object, and where the attributes are
    typed, it should be a float
    """
    pass


def set_attribute(object_: object, attribute_name: str, value: typing.Any) -> None:
    """
    This should set the attribute with the givne name on the given object to the
    given value
    """
    pass


def get_attribute(object_: object, attribute_name: str) -> typing.Any:
    """
    This should look on the object for an attribute of this name and return its value
    """
    return None


def has_attribute(object_: object, attribute_name: str) -> bool:
    """
    This should check if an object has an attribute of this name
    """
    return False
