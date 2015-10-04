# http://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-mst/
import networkx as nx

class Solution:
    def MST(self, graph):
        return

if __name__ == "__main__":
    #          10
    #     0--------1
    #     |  \     |
    #    6|   5\   |15
    #     |      \ |
    #     2--------3
    #         4
    graph = nx.Graph()
    graph.add_edge(0,1,weight=10)
    graph.add_edge(0,2,weight=6)
    graph.add_edge(0,3,weight=5)
    graph.add_edge(1,3,weight=15)
    graph.add_edge(2,3,weight=4)
    nx.draw(graph)
