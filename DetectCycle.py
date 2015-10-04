# http://www.geeksforgeeks.org/union-find/
# http://www.geeksforgeeks.org/union-find-algorithm-set-2-union-by-rank/
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

    def isCycle(self, G):
        subsets = {node:{'parent':node, 'rank':0} for node in G.nodes()}
        for edge in G.edges():
            parent0 = self.find(subsets, edge[0])
            parent1 = self.find(subsets, edge[1])
            if parent0 == parent1:
                return True
            self.union(subsets, parent0, parent1)
        print subsets
        return False

if __name__ == "__main__":
    # /* Let us create following graph
    #  0
    # |  \
    # |    \
    # 1-----2 */
    G = nx.Graph()
    G.add_edge(0,1)
    G.add_edge(1,2)
    G.add_edge(0,2)
    sol = Solution()
    print sol.isCycle(G)
    print True
