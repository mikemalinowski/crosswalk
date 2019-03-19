from ._core import reroute
from ._core import UndefinedRouting


# ------------------------------------------------------------------------------
@reroute
def set_current(frame):
    """
    Sets the current frame
    
    :param frame: 
    :return: 
    """
    return None

# ------------------------------------------------------------------------------
@reroute
def start():
    """
    Returns the start time of the scene

    :return: int
    """
    return 0


# ------------------------------------------------------------------------------
@reroute
def set_start(frame):
    """
    Sets the start frame of the scene

    :param frame: The frame number to assign as the start frame
    :type frame: int

    :return: start frame
    """
    return 0


# ------------------------------------------------------------------------------
@reroute
def end():
    """
    Returns the end time of the scene

    :return: int
    """
    return 0


# ------------------------------------------------------------------------------
@reroute
def set_end(frame):
    """
    Sets the end frame of the scene

    :param frame: The frame number to assign as the end frame
    :type frame: int

    :return: end frame
    """
    return 0


# ------------------------------------------------------------------------------
def range():
    """
    Returns the currently active frame range

    :return: int
    """
    return end() - start()


# ------------------------------------------------------------------------------
def set_range(length):
    """
    Sets the end time appropriately based on the given range

    :param range: The range to assign to the scene
    :type range: int

    :return: end frame
    """
    return set_end(start() + length)


# ------------------------------------------------------------------------------
@reroute
def framerate():
    """
    Returns the current frame rate
    :return: int
    """
    return 0


# ------------------------------------------------------------------------------
# -- This is here to allow the module to dynamically re-route
# -- to any over-implemented functions within a host which is
# -- not defined in the base api.
UndefinedRouting.setup(__name__)
