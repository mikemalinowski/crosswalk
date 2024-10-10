from pymxs import runtime as mxs


def select(object_):
    """
    This should select the given object
    """
    mxs.select(object_)


def selected():
    """
    This should return the objects which are currently selected
    """
    return mxs.selection[0]

