from ._core import reroute
from ._core import UndefinedRouting


# ------------------------------------------------------------------------------
@reroute
def has(element):
    """
    Checks whether the given element has any constraints assigned
    to it.

    :param element: The element to check for constraints
    :type element: Host Specific

    :return: list(constraint, constraint, ...)
    """
    return None


# ------------------------------------------------------------------------------
def create(element, target, cns_type, compensate=True):
    """
    Creates a constraint on the given element, constraining it
    against the given target.

    :param element: The element to constrain
    :type element: Host Specific

    :param target: The element to constrain to
    :type target: Host Specific

    :param cns_type: Supported - general - constraint types are:
        >> position
        >> rotation
        >> transform
        Note: Specific host implementations may expose further
        constraint types.
    :type cns_type: str

    :param compensate: If True the current offset between the element
        and the target is retained during the constraint creation.
    :type compensate: bool

    :return: Constraint (Host Specific)
    """
    return None


# ------------------------------------------------------------------------------
def constrained_to(element):
    """
    This will return a list of objects the current element is
    constrained to.

    :param element: Element to inspect for constraints
    :type element: Host Specific

    :return: list(element, element, ...)
    """
    return list()


# ------------------------------------------------------------------------------
def clear(element):
    """
    Removes all the constraints from the given element

    :param element: Element to remove constraints from
    :type element: Host Specific

    :return: Number of constraints removed
    """
    return 0


# ------------------------------------------------------------------------------
# -- This is here to allow the module to dynamically re-route
# -- to any over-implemented functions within a host which is
# -- not defined in the base api.
UndefinedRouting.setup(__name__)