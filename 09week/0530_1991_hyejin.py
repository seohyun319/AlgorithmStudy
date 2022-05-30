import sys
put = sys.stdin.readline

no_child = '.'

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    #노드삽입
    def insert_recursive(self, node, data, left_data, right_data):
        if node is None:
            node = Node(data)

            if self.root is None:
                self.root = node
            else:
                if left_data == '.':
                    node.left = None
                else:
                    node.left = self.insert_recursive(node.left, left_data, no_child, no_child)
                
                if right_data == '.':
                    node.right = None
                else:
                    node.right = self.insert_recursive(node.right, right_data, no_child, no_child)
        return node

    #전위순회
    def preorder(self, node):
        if node != None:
            print(node.data)

            if node.left:
                self.preorder(node.left)
            if node.right:
                self.preorder(node.right)

    # 중위 순회
    def inorder(self, node):
        if node != None:
            if node.left:
                self.inorder(node.left)
            
            print(node.data)

            if node.right:
                self.inorder(node.right)

    #후위 순회
    def postorder(self, node):
        if node != None:
            if node.left:
                self.postorder(node.left)
            if node.right:
                self.postorder(node.right)
            
            print(node.data)

            
n = int(input())
bst = BinarySearchTree()

for i in range(n):
    myself, left, right = put().split()
    bst.insert_recursive(bst.root, myself, left, right)

bst.preorder(bst.root)
bst.inorder(bst.root)
bst.postorder(bst.root)
