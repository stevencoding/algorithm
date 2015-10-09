# http://www.geeksforgeeks.org/greedy-algorithms-set-3-huffman-coding/
import heapq

class HuffmanTreeNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

class HuffmanTree:
    def __init__(self, array):
        self.heap = [(freq, HuffmanTreeNode(char, freq)) for char, freq in array]
        self.buildTree(self.heap)

    def buildTree(self, heap):
        # elem in heap is not HuffmanTreeNode, but (freq, HuffmanTreeNode)
        # heapq can accept tuple and use first var in the tuple as key for comparison
        heapq.heapify(heap)
        while(len(heap)!=1):
            left = heapq.heappop(heap)[1]
            right = heapq.heappop(heap)[1]
            node = HuffmanTreeNode('$', left.freq+right.freq)
            node.left = left
            node.right = right
            heapq.heappush(heap, (left.freq+right.freq, node))

    def printCodes(self):
        root = heapq.heappop(self.heap)[1]
        self.traverse(root, '')

    def traverse(self, root, code):
        if root.left is not None:
            self.traverse(root.left, code+'0')
        if root.right is not None:
            self.traverse(root.right, code+'1')
        if (root.left is None) and (root.right is None):
            print root.char, '\t', code

if __name__ == "__main__":
    array = [('a', 5), ('b', 9), ('c', 12), ('d', 13), ('e', 16), ('f', 45)]
    tree = HuffmanTree(array)
    tree.printCodes()
