import MaxPlus
import pymxs


# ------------------------------------------------------------------------------
def to_itab(elements):

    if isinstance(elements, MaxPlus.INodeTab):
        return elements

    # -- Create thte itab to put the items in
    itab = MaxPlus.INodeTab()

    if isinstance(elements, (list, tuple)):
        for element in elements:
            itab.Append(element)

    else:
        itab.Append(elements)

    return itab


# ------------------------------------------------------------------------------
def to_inode(element):
    if isinstance(element, MaxPlus.INode):
        return element

    elif isinstance(element, str):
        return MaxPlus.INode.GetINodeByName(element)

    elif isinstance(element, pymxs.MXSWrapperBase):
        return MaxPlus.INode.GetINodeByHandle(element.handle)

    return None


# ------------------------------------------------------------------------------
def to_pymxs(element):
    if isinstance(element, MaxPlus.INode):
        return pymxs.runtime.maxOps.getNodeByHandle(int(element.GetHandle()))

    elif isinstance(element, str):
        return pymxs.runtime.getNodeByName(element)

    elif isinstance(element, pymxs.MXSWrapperBase):
        return element

    return None

