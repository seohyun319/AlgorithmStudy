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


# 참고 코드 
class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right


def preorder(node):  # 전위 순회
    print(node.item, end='')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])


def inorder(node):  # 중위 순회
    if node.left != '.':
        inorder(tree[node.left])
    print(node.item, end='')
    if node.right != '.':
        inorder(tree[node.right])


def postorder(node):  # 후위 순회
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.item, end='')


if __name__ == "__main__":

    N = int(input())
    tree = {}

    for _ in range(N):
        node, left, right = map(str, input().split())
        tree[node] = Node(item=node, left=left, right=right)

    preorder(tree['A'])
    print()
    inorder(tree['A'])
    print()
    postorder(tree['A'])
