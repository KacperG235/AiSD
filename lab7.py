from enum import Enum
from typing import Dict, List
from typing import Optional


class EdgeType(Enum):
    directed = 1
    undirected = 2

    def __init__(self, directed=1, undirected=2):
        self.directed = directed
        self.undirected = undirected


class Vertex:
    data: any
    index: int

    def __init__(self, data: any, index: int):
        self.data = data
        self.index = index

    def __repr__(self):
        return str(self.data)


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source: Vertex, destination: Vertex,
                 weight: Optional[float] = None):
        self.source = source
        self.destination = destination
        self.weight = weight


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self, adjacencies: Dict[Vertex, List[Edge]]):
        self.adjacencies = adjacencies

    def create_vertex(self, data: any) -> Vertex:
        id_g = 0
        for keys in self.adjacencies:
            id_g += 1
        temp1 = Vertex(data, id)
        temp2 = {temp1: []}
        self.adjacencies = self.adjacencies | temp2
        return temp1

    def add_directed_edge(self, source: Vertex, destination: Vertex,
                          weight: Optional[float] = None) -> None:
        temp = Edge(source, destination, weight)
        self.adjacencies[source] = temp

    def add_undirected_edge(self, source: Vertex, destination: Vertex,
                            weight: Optional[float] = None) -> None:
        temp = Edge(source, destination, weight)


def main():
    test = Graph({})
    test.create_vertex(1)

    print(test.adjacencies)


if __name__ == '__main__':
    main()
