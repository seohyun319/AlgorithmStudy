n = int(input())
nodes = []

for _ in range(n-1):
	nodes.append((input().split()))

print(nodes)

class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

root = Node(1)

for i in range(n-1):
	nodes[i][0]
