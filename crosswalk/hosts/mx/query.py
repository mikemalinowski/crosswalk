import pymxs
import MaxPlus


# ------------------------------------------------------------------------------
def get(name):
    return MaxPlus.INode.GetINodeByName(name)


# ------------------------------------------------------------------------------
def find(wildcard, of_type=None):
    results = pymxs.runtime.execute("$%s as array" % wildcard)

    itab = MaxPlus.INodeTab()

    for result in results:
        if of_type:
            result_type = pymxs.runtime.execute(
                'ClassOf $%s as string' % (
                    result.name,
                ),
            )

            if of_type != result_type:
                continue

        itab.Append(MaxPlus.INode.GetINodeByName(result.name))

    return [

        node

        for node in itab

    ]


# ------------------------------------------------------------------------------
def selected():
    return [
        node
        for node in MaxPlus.SelectionManager.Nodes
    ]


# ------------------------------------------------------------------------------
def exists(name):
    try:
        MaxPlus.INode.GetINodeByName(name)
        return True

    except RuntimeError:
        return False

