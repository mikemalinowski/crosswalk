"""
This is a stub file and will always be overridden by the application
implementation.
"""


def create(name: str, parent: object = None) -> object:
    """
    This should create a "basic" object within the application. A basic object is
    typically expected to be a transform with little or no visual output in the viewport

    The name will be assigned to the object and if a parent is given the object will
    be made a child of that parent.

    Args:
        name: The name to assign to the object
        parent: Optional node to act as the parent
    """
    return None


def exists(object_name: str or object) -> bool:
    """
    This will test whether an object in the scene exists

    Args:
        object_name: The name of the object to test
    """
    return None


def get_object(object_name: str or object) -> object:
    """
    Given a name, this will return an api specific object. This is variable dependant
    on the application.

    Note that if you are implementing this in an application you should always test
    whether the object_name is actually already an application object.

    Args:
        object_name: The name of the object to find

    Returns:
        The found object in the applications python api
    """
    return None


def get_name(object_: object or str) -> str:
    """
    This will return the name for the application object.

    Note that when implementing this function you should always test whether or not
    the given "object" is actually just a name already.

    Args:
        object_: The object to return the name for
    """
    return ""


def all_objects_with_attribute(attribute_name: str) -> list[object]:
    """
    This should return all objects which have an attribute with the given name

    Args:
        attribute_name: The name of the attribute to search for
    """
    return []


def get_children(object_: object or str) -> list[object]:
    """
    This should return all children of the given object

    Args:
        object_: The object to get the children of

    Returns:
        List of child objects
    """
    return []


def get_parent(object_: object or str) -> object:
    """
    This should return the parent of the given object

    Args:
        object_: The object to get the parent of
    Returns:
        The parent of the given object
    """
    return None


def set_parent(object_: object or str, parent: object or str) -> None:
    """
    This should return the parent of the given object

    Args:
        object_: The object to set the parent of
        parent: The parent object
    """
    pass


def delete(object_: object or str) -> None:
    """
    This should delete the given object

    Args:
        object_: The object to delete
    """
    pass
