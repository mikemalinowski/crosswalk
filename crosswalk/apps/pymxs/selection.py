from pymxs import runtime as rt


def select(object_):
    """
    This should select the given object
    """
    node = rt.getNodeByName(object_)

    if node:
        rt.select(node)


def selected():
    """
    This should return the objects which are currently selected
    """
    return rt.selection
