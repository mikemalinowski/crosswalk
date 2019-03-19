from ._core import reroute
from ._core import UndefinedRouting


# ------------------------------------------------------------------------------
@reroute
def vertex_count(element):
    """
    This returns the total number of vertices in the mesh

    :param element: Element to move under the new parent
    :type element: Host Specific

    :return: int
    """
    return 0

# ------------------------------------------------------------------------------
@reroute
def vertex_position(element, index):
    """
    This will return the position of the vertex with the given index

    :param element: Element to query for vertex positions
    :type element: Host Specific

    :param index: Vertex Id to query
    :type index: int

    :return: list(x, y, z)
    """
    return list()


# ------------------------------------------------------------------------------
@reroute
def set_vertex_position(element, index, position):
    """
    This will return the position of the vertex with the given index

    :param element: Element to set the vertex position for
    :type element: Host Specific

    :param index: Vertex Id to set
    :type index: int

    :param position: The x, y, z vector (in object space)
    :type position: list(x, y, z)

    :return: None
    """
    return None


# ------------------------------------------------------------------------------
def positions(element):
    """
    Returns a generator of vertex positions

    :param element: Element to query for vertex positions
    :type element: Host Specific

    :return: generator
    """
    for vertex_id in range(vertex_count(element)):
        yield vertex_position(element, vertex_id)


# ------------------------------------------------------------------------------
def set_positions(element, positions):
    """
    Sets the positions of all the vertices on the element.

    :param element: Element to set the vertex positions for
    :type element: Host Specific

    :param position: A list of length 3 lists, where each length 3 list
        is the x, y, z coord to set the vertex position (in object space)
    :type position: list([x, y, z], [x, y, z])

    :return: None
    """
    for vertex_id, position in enumerate(positions):
        set_vertex_position(element, vertex_id, positions[vertex_id])


# ------------------------------------------------------------------------------
# -- This is here to allow the module to dynamically re-route
# -- to any over-implemented functions within a host which is
# -- not defined in the base api.
UndefinedRouting.setup(__name__)
