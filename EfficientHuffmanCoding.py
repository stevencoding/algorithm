# http://www.geeksforgeeks.org/greedy-algorithms-set-3-huffman-coding-set-2/

class HuffmanTreeNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

class HuffmanTree:
    def __init__(self, array):
        self.firstQueue = [HuffmanTreeNode(char, freq) for char, freq in array]
        self.secondQueue = []
        self.root = self.buildTree()

    def deque(self): # deque one elem from double queues
    	# print len(self.firstQueue), len(self.secondQueue)
    	if len(self.firstQueue) == 0:
    		return self.secondQueue.pop(0)
    	elif len(self.secondQueue) == 0:
    		return self.firstQueue.pop(0)
    	elif self.firstQueue[0].freq >= self.secondQueue[0].freq:
			return self.secondQueue.pop(0)
    	else:
    		return self.firstQueue.pop(0)

    def enque(self, node): # enque one elem into double queues
    	self.secondQueue.append(node) 

    def sizeOfQueues(self): # total number of elems in double queues
    	return len(self.firstQueue)+len(self.secondQueue)

    def buildTree(self):
        # elem in queue is HuffmanTreeNode
        while self.sizeOfQueues() > 1:
        	left = self.deque()
        	right = self.deque()
        	node = HuffmanTreeNode('$', left.freq+right.freq)
        	node.left = left
        	node.right = right
        	self.enque(node)
        return self.deque()

    def printCodes(self):
        self.traverse(self.root, '')

    def traverse(self, root, code):
        if root.left is not None:
            self.traverse(root.left, code+'0')
        if root.right is not None:
            self.traverse(root.right, code+'1')
        if (root.left is None) and (root.right is None):
            print root.char, '\t', code

if __name__ == "__main__":
	# input array must be sorted
    array = [('a', 5), ('b', 9), ('c', 12), ('d', 13), ('e', 16), ('f', 45)]
    tree = HuffmanTree(array)
    tree.printCodes()
