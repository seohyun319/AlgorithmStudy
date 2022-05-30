# silver1. 트리 순회
# 그래프 어떻게 입력할지...

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    node, left, right = map(int, input().split())     


class BinarySearchTree(object):
    # 전위 순회
    def preorder(self, node):
        if node != None:
            print(node.data, end = ' ')

            if node.left:
                self.preorder(node.left)
            if node.right:
                self.preorder(node.right)
    
    # 중위 순회
    def inorder(self, node):
        if node != None:
            if node.left:
                self.inorder(node.left)
            
            print(node.data, end = ' ')

            if node.right:
                self.inorder(node.right)
    
    #후위 순회
    def postorder(self, node):
        if node != None:
            if node.left:
                self.postorder(node.left)
            if node.right:
                self.postorder(node.right)
            
            print(node.data, end = ' ')


bst = BinarySearchTree()

bst.preorder('A')