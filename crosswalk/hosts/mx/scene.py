import pymxs
import MaxPlus
from ._utils import to_itab


# ------------------------------------------------------------------------------
def rename(element, new_name):
    element.SetName(new_name)


# ------------------------------------------------------------------------------
def delete(element):
    for item in to_itab(element):
        item.Delete()


# ------------------------------------------------------------------------------
def create(element_type, name):
    node = MaxPlus.INode.GetINodeByName(
        pymxs.runtime.execute('%s()' % element_type).name,
    )
    
    node.SetName(name)
    
    return node


# ------------------------------------------------------------------------------
def select(elements):
    deselect()
    MaxPlus.SelectionManager.SelectNodes(
        to_itab(elements),
    )

    return None


# ------------------------------------------------------------------------------
def deselect(elements=None):
    if elements:
        MaxPlus.SelectionManager.DeselectNodes(to_itab(elements))

    else:
        MaxPlus.SelectionManager.ClearNodeSelection()

