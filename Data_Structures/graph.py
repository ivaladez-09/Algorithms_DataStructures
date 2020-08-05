"""This module contains a graph structure and its corresponding methods."""
from collections import defaultdict


class Graph:
    """Class to create the object graph and being able to manipulate as it."""

    def __init__(self):
        """
        Create the graph structure {vertex: [edge1, edge2, ..., edge]}
        """
        self.graph = {}

    def add_edge(self, vertex, edge):
        """
        Add an edge (path between 2 vertices) to the graph
        :param vertex: Integer that represents the node
        :param edge: Path from given vertex to another node
        :return: None for error, and True for success
        """
        if vertex in self.graph:
            self.graph[vertex].append(edge)
            return True
        return None

    def add_vertex(self, vertex):
        """
        Add a vertex (node) to the graph
        :param vertex: Integer that represents the node
        :return: None for error, and True for success
        """
        if vertex in self.graph:
            return None
        self.graph[vertex] = []
        return True

    def display_graph(self):
        """Print all the content of the graph"""
        for vertex, edges in self.graph.items():
            print("Vertex: {} - Edges: {}".format(vertex, edges))

    def bfs(self, s):
        """
        Print a Breadth First Search (BFS) of graph
        :param s: Source node from start searching
        :return:
        """
        vertex_visited = [False] * (len(self.graph))
        queue = list()

        # Mark the source node as visited and enqueue it
        queue.append(s)
        vertex_visited[s] = True

        print("\nBFS: ", end=" ")
        while queue:
            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the dequeued vertex s. If a adjacent
            # has not been visited, then mark it visited and enqueue it
            for i in self.graph[s]:
                if not vertex_visited[i]:
                    queue.append(i)
                    vertex_visited[i] = True

    # A function used by DFS
    def dfs_util(self, v, visited):
        """

        :param v: vertex to start looking
        :param visited: list of vertex visited
        :return:
        """
        # Mark the current node as visited and print it
        visited[v] = True
        print(v, end=' ')

        # Recursive for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, s):
        """
        Print a Depth First Search (BFS) of graph
        :param s: Source node from start searching
        :return:
        """
        # Mark all the vertices as not visited
        vertex_visited = [False] * (max(self.graph) + 1)
        print("\nDFS: ", end=" ")
        # Call the recursive helper function to print DFS traversal
        self.dfs_util(s, vertex_visited)


if __name__ == "__main__":
    graph = Graph()
    for i in range(4):
        graph.add_vertex(i)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)
    graph.display_graph()
    graph.bfs(0)
    graph.dfs(0)
