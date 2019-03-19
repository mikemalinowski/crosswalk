from ._core import reroute
from ._core import UndefinedRouting


# ------------------------------------------------------------------------------
@reroute
def version():
    """
    Returns the version of the host application

    :return: str
    """
    return None


# ------------------------------------------------------------------------------
@reroute
def refresh():
    """
    Causes the application to refresh/evaluate

    :return: None
    """
    return None


# ------------------------------------------------------------------------------
@reroute
def load(filename, operation='open', force=False):
    """
    This will open a file. The type of open operation depends on
    the users input. The following are supported as a minimum:

        >> open
        >> import
        >> reference

    Note: Host implementations may extend this further.

    :param filename: The absolute path to the file to open
    :type filename: str

    :param operation: What type of opening operation to perform
    :type operation: str

    :param force: If true the operation will occur regardless of whether
        there are unsaved changes.
    :type force: bool

    :return: Elements opened
    """
    return list()


# ------------------------------------------------------------------------------
@reroute
def new(force=False):
    """
    This will create a new scene, closing the current scene.

    :param force: If true, the operation will occur regardless of whether
        there are unsaved changes.
    :type force: bool

    :return: None
    """
    return None


# ------------------------------------------------------------------------------
@reroute
def save(filename=None):
    """
    Saves the current scene. If no filename is given the save operation
    will be performed on the current filepath.

    :param filename: Optional, if given the save will occur to the
        given filename.
    :type filename: str

    :return: save path
    """
    return None


# ------------------------------------------------------------------------------
@reroute
def filepath():
    """
    Returns the current scene filepath

    :return: str
    """
    return None


# ------------------------------------------------------------------------------
@reroute
def is_silent():
    """
    Returns whether or not the application is running in silent mode

    :return: bool
    """
    return None


# ------------------------------------------------------------------------------
@reroute
def undo():
    """
    Performs an undo operation

    :return: None
    """
    return None


# ------------------------------------------------------------------------------
@reroute
def redo():
    """
    Perform a redo operation

    :return: None
    """
    return None


# ------------------------------------------------------------------------------
# -- This is here to allow the module to dynamically re-route
# -- to any over-implemented functions within a host which is
# -- not defined in the base api.
UndefinedRouting.setup(__name__)