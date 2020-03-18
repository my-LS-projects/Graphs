from util import Queue, Stack


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("Vertex does not exist")


def earliest_ancestor(ancestors, starting_node):
    """
    Return earliest known ancestor
    10
    /
    1   2   4  11
    \ /   / \ /
    3   5   8
    \ / \   \
        6   7   9

    """
    ### BFS
    # furthest distance from input individual (starting_node)
    # If there is more than one "earliest", return the one with the lowest ID
    # If input has no parents, return -1

    ### CREATE GRAPH
    g = Graph()
    # Left value = Parent
    # Right value = Child
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        g.add_vertex(parent)
        g.add_vertex(child)
        # edge going up instead of down
        g.add_edge(child, parent)

    # BFS
    q = Queue()
    q.enqueue([starting_node])

    longest_path_len = 1
    # set to -1 in case we never find an ancestor
    earliest_ancestor = -1

    while q.size() > 0:
        path = q.dequeue()
        current = path[-1]

        # update longest path length to match current path
        # update earliest ancestor to be last of path
        if (len(path) >= longest_path_len and current < earliest_ancestor) or len(
            path
        ) > longest_path_len:
            longest_path_len = len(path)
            earliest_ancestor = current

        neighbors = g.vertices[current]

        for ancestor in neighbors:
            copy = path.copy()
            copy.append(ancestor)
            q.enqueue(copy)

    return earliest_ancestor
