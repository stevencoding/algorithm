# http://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-mst/
import networkx as nx

class Solution:
    def find(self, subsets, node):
        # optimized using path compression
        if subsets[node]['parent'] != node:
            subsets[node]['parent'] = self.find(subsets, subsets[node]['parent'])
        return subsets[node]['parent']

    def union(self, subsets, node1, node2):
        # optimized using union by rank
        parent1 = self.find(subsets, node1)
        parent2 = self.find(subsets, node2)
        if subsets[parent1]['rank'] < subsets[parent2]['rank']:
            subsets[parent1]['parent'] = parent2
        elif subsets[parent1]['rank'] > subsets[parent2]['rank']:
            subsets[parent2]['parent'] = parent1
        else:
            subsets[parent1]['parent'] = parent2
            subsets[parent2]['rank'] += 1

    def MST(self, G):
        res = []
        # sort all the edges by weight
        edges = G.edges(data=True)
        edges.sort(key=lambda x: x[2]['weight'])
        # union find
        subsets = {node:{'parent':node, 'rank':0} for node in G.nodes()}
        for edge in edges:
            parent0 = self.find(subsets, edge[0])
            parent1 = self.find(subsets, edge[1])
            if parent0 != parent1:
                res.append(edge)
                self.union(subsets, parent0, parent1)
            if len(res) == G.number_of_nodes()-1: return res

if __name__ == "__main__":
    #          10
    #     0--------1
    #     |  \     |
    #    6|   5\   |15
    #     |      \ |
    #     2--------3
    #         4
    G = nx.Graph()
    G.add_edge(0,1,weight=10)
    G.add_edge(0,2,weight=6)
    G.add_edge(0,3,weight=5)
    G.add_edge(1,3,weight=15)
    G.add_edge(2,3,weight=4)
    sol = Solution()
    print sol.MST(G)
    print '2 -- 3 == 4'
    print '0 -- 3 == 5'
    print '0 -- 1 == 10'
