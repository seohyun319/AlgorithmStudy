class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

n = int(input())

nodes = []
for _ in range(n):
	nodes.append((input().split()))

for i in range(n):
	root = Node(nodes[i][0])
	root.left = Node(nodes[i][1])
	root.right = Node(nodes[i][2])

# 전위 순회
def preorder(self, node):
	if node != None:
		print(node.data, end=' ')

		if node.left:
			self.preorder(node.left)
		if node.right:
			self.preorder(node.right)

#preorder(root)

# 중위 순회
def inorder(self, node):
	if node != None:
		if node.left:
			self.inorder(node.left)

		print(node.data, end=' ')

		if node.right:
			self.inorder(node.right)

# 후위 순회
def postorder(self, node):
	if node != None:
		if node.left:
			self.postorder(node.left)
		if node.right:
			self.postorder(node.right)

		print(node.data, end=' ')
