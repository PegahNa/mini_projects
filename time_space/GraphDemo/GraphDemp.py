"""
1. Create a graph

   Example of a graph that we want to build
       a________b
       |        |
       |        |
      c|________|d
                |
                |
                |e 

"""

# Dict represent graph,
# where key is the name of a graph edge and
# values are graph edges

graph_elements = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}

print(graph_elements)


class Graph:

    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def get_vertices(self):
        """
        2. Display graph vertices

        - we need to get keys of the graph dict,
          because they represent vertices
        """
        return list(self.gdict.keys())

    def get_edges(self):
        """
        3. Display graph edges

        - we have to find each of the pairs of vertices which have an edge in between them.
        - create an empty list of edges
        - iterate through the edge values associated with each of the vertices
        - build a list containing the distinct group of edges found from the vertices
        """
        edge_names = []
        for vertex in self.gdict:
            for next_vertex in self.gdict[vertex]:
                if {next_vertex, vertex} not in edge_names:
                    edge_names.append({vertex, next_vertex})
        return edge_names

    def add_vertex(self, vertex):
        """
        4. Add a vertex
        - we need to add another additional key to the graph dictionary.
        """
        if vertex not in self.gdict:
            self.gdict[vertex] = []

    def add_edge(self, edge):
        """
        5. Adding an edge
        - treat the new vertex as a tuple
        - validate if the edge is already present
        - if not then add the edge
        """
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]


g = Graph(graph_elements)
print(g.get_vertices())
print(g.get_edges())

g.add_vertex("f")
print(g.get_vertices())

g.add_edge({'a', 'e'})
g.add_edge({'f', 'x'})
print(g.get_edges())

print(g.gdict)