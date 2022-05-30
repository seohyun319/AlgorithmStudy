#노드 초기화
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        
# 전위 순회
def preorder(self, node):
	if node != None:
		print(node.data, end=' ')

		if node.left:
			self.preorder(node.left)
		if node.right:
			self.preorder(node.right)
    
# 중위 순회
def inorder(self, node):
	if node != None:
		if node.left:
			self.inorder(node.left)

		print(node.data, end=' ')

		if node.right:
			self.inorder(node.right)

    
#후위 순회
def postorder(self, node):
	if node != None:
		if node.left:
			self.postorder(node.left)
		if node.right:
			self.postorder(node.right)

		print(node.data, end=' ')
 
n = int(input())
