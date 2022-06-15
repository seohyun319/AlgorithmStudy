알고리즘입문 기말고사 대비 예상 문제

출제자: 김경민


1. 다음과 같이 max heap에 8을 새로 삽입하는 과정에서의 리스트의 변화 과정을 적으시오.

 <img width="245" alt="image" src="https://user-images.githubusercontent.com/66426083/173934580-91738bf9-9dd8-46ec-a57b-da1f10cc5bdc.png">


-> 

-> 


2. 다음은 이진 검색 트리에서 값을 검색하는 코드이다. 빈칸에 들어갈 코드를 작성하시오.

class BinarySearchTree(object):

    def search_recursive(self, node, data):
        if 		  :
            return node is not None 
	elif data < node.data:
            return self.search_recursive(node.left, data)
        else:
            return self.search_recursive(node.right, data)

print(bst.search_recursive(bst.root, 14))
print(bst.search_recursive(bst.root, 17))



정답: 







3. 다음은 DFS로 트리를 순회한 결과이다. 자식이 2개인 노드, 자식이 1개인 노드, 리프 노드에 해당되는 노드를 각각 적으시오.
A→B→D→H→H→H→D→D→B→E→I→I→I→E→ J→ J→ J→ E→B→A→C→F→K→K→K→F→L→L→L→F→C→ G→G→G→C→ A
- 자식이 2개인 노드: 
- 자식이 1개인 노드: 
- 리프 노드: 



4. 다음 트리의 후위 순회 과정을 적으시오.

 <img width="193" alt="image" src="https://user-images.githubusercontent.com/66426083/173934623-b22dfbc4-491d-4328-bda2-a400c8797281.png">


정답: 




5. 다음 코드를 바탕으로 28을 삭제한 후의 트리를 그리시오.

 <img width="279" alt="image" src="https://user-images.githubusercontent.com/66426083/173934634-72061fed-3e83-4df8-b5a3-064046c03a54.png">

<img width="162" alt="image" src="https://user-images.githubusercontent.com/66426083/173934705-71d62f6f-bbba-466e-bc57-bffa4f61e08b.png">

   ->   



6. 다음 중 balanceAVL(t,type)을 넣을 수 있는 위치를 모두 고르시오.

 
```python
class Node(object):
  def __init__(self, data):
    self.data = data
    self.left = self.right = None

class BinarySearchTree(object):
  def __init__(self):
    self.root = None
  ①
  def insert_recursive(self, node, data):
    if node is None:
      ②
      node = Node(data)
      if self.root is None:
        self.root = node
    else:
      ③
      if data <= node.data:
        node.left = self.insert_recursive(node.left, data)
      else:
        node.right = self.insert_recursive(node.right, data)
    ④
    return node
 ```
  

7. 아래 그림처럼 AVL Tree에 75를 삽입하고자 한다. 다음 문제에 답하시오.

 <img width="215" alt="image" src="https://user-images.githubusercontent.com/66426083/173934894-cea9f580-4941-4f2b-812b-cb2f741b44e0.png">



1) 노드 60의 균형인수: 
2) 불균형의 유형: 
3) 해결 방법(알파벳과 한글을 모두 적으시오):  (           )회전 후 (           )회전을 한다.
4) 1회전 후 트리의 모습

















5) 2회전 후 트리의 모습
















8. Red-Black 트리의 특징으로 옳지 않은 것은?  

① 모든 리프 노드는 블랙이다. <br>
② 레드 노드는 연속으로 출현하지 못 한다. <br>
③ 루트는 레드이다. <br>
④ 루트 노드에서 리프 노드 사이에 있는 블랙 노드의 수는 모두 같다. <br>
⑤ 레드 노드의 자식들은 모두 블랙이다. <br>




9. 다음 중 인접 행렬과 인접 리스트에 대한 설명으로 옳지 않은 것은?  

① 인접 행렬은 N^2에 비례하는 공간이 필요하다. <br>
② 무향 그래프인 경우 인접 행렬은 항상 대칭적이다. <br>
③ 인접 리스트는 간선 수에 비례하는 양만큼만 필요하다. <br>
④ 인접 리스트는 정점간 간선이 있는지 알아보는 데 시간이 오래 걸린다. <br>
⑤ 인접 리스트는 간선 수가 많을 때 사용하는 게 유리하다. <br>

