# 이진 검색 트리 (Binary Search Trees)

### ⏩ 개념

모든 노드에 대해서
**왼쪽** 서브트리에 있는 데이터는 **모두 현재 노드의 값보다 작고**
**오른쪽** 서브트리에 있는 데이터는 **모두 현재 노드의 값보다 큰** 
성질을 만족하는 **이진트리**

(중복되는 원소는 없는 것으로 가정)

### ⏩ 시간 복잡도

평균적으로 노드의 개수, 즉 데이터 원소의 개수를 n이라고 할 때 log(n)에 비례

### ⏩ 이진 검색 트리에서 값의 검색

 ***루트보다 작을 경우 : 왼쪽부터 찾기***

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/403b45b2-9868-4c35-9147-ce5bc71c3a2c/Untitled.png)

***루트보다 클 경우 : 오른쪽부터 찾기***

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0409e3ee-04b9-4a7c-a270-5c140a8b42fa/Untitled.png)

### ⏩ 이진 검색 트리에서 값의 삽입

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/de0e209a-4625-44a3-ac39-a464c1077b0a/Untitled.png)

### ⏩ 이진 검색 트리 구현

```python
class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = self.right = None
```

- 우리가 원하는 숫자를 변수 data에 저장
- 왼쪽 노드와 오른쪽 노드를 가리킬 변수 left, right 지정
- 아직 아무것도 가리키지 않아서 None으로 지정

```python
class BinarySearchTree(object):
	def __init__(self):
		self.root = None
```

- root라는 노드부터 시작하는 걸로 정의

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/270714ae-1f24-4303-98d0-1872039518f2/Untitled.png)

### ⏩ 이진 검색 트리 값의 삽입 구현

```python
class Node(object):
    def __init__(self):
        self.root = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None
    
    def insert_recursive(self, node, data): #node는 초기에는 root, data는 삽입할 값
        if node is None:
            node = Node(data) # 비어있는 노드 찾으면 노드 생성

            if self.root is None:
                self.root = node # root가 None이면 새로 생긴 노드를 넣어줌 
            else:
                if data <= node.data:
                    node.left = self.insert_recursive(node.left, data)
										# 검색했을 때 값이 더 작으면 왼쪽 자식 노드로 재귀 순회
                else:
                    node.right = self.insert_recursive(node.right, data)
										# 검색했을 때 값이 더 크면 오른쪽 자식 노드로 재귀 순회
            return node

array = [11, 5, 4, 7, 1, 6, 9, 15, 13, 18, 12, 14]

bst = BinarySearchTree()
for x in array:
    bst.insert_recursive(bst.root, x)
```

즉, bst 객체의 멤버 변수 root를 트리의 뿌리로 하는 이진 검색 트리를 생성하는 코드

### ⏩ 이진 검색 트리 값의 검색 구현

```python
class BinarySearchTree(object):

    def search_recursive(self, node, data):
        if node is None or node.data == data:
            return node is not None # 값이 같으면 True, 다르면 False 반환
# 재귀적 호출
        elif data < node.data:
            return self.search_recursive(node.left, data)
        else:
            return self.search_recursive(node.right, data)

print(bst.search_recursive(bst.root, 14))
print(bst.search_recursive(bst.root, 17))
```

- return [node.data](http://node.data) == data 는 안될까?
    
    : 노드가 None이면 데이터 자체를 확인할 수 없기 때문에 재귀를 위해 node가 None이 아니라는 사실을 반환한다.
    

### ⏩ 이진 검색 트리 값의 삽입 구현 LOOP ver.

```python
class BinarySearchTree(object):
    def insert(self, data):
        new_node = Node(data)

        cur_node = self.root
        if cur_node is None:
            self.root = new_node
            return
        
        while True:
            parent_node = cur_node
            if data < cur_node.data:
                cur_node = cur_node.left
                if cur_node == None:
                    parent_node.left = new_node
                    return
            else:
                cur_node = cur_node.right
                if cur_node == None:
                    parent_node.right = new_node
                    return

array = [11, 5, 4, 7, 1, 6, 9, 15, 13, 18, 12, 14]

bst = BinarySearchTree()
for x in array:
    bst.insert(x)
```

- 재귀함수가 아니라 while문으로 구현한 코드
- 재귀는 함수 자체에 부모 노드가 있어야 호출이 가능하다.
- 하지만 while문은 insert의 인자에 root를 넣을 필요가 없다.
- 즉, while문은 함수 인자가 깔끔해지고 재귀는 코드 자체가 깔끔해진다. (하지만 상관없음!!)

### ⏩ 이진 검색 트리 값의 검색 구현 LOOP ver.

```python
class BinarySearchTree(object):

    def search(self, data):
        cur_node = self.root

        while True:
            if cur_node is None or cur_node.data == data:
                return cur_node is not None
            elif data < cur_node.data:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

print(bst.search(14)) #True
print(bst.search(17)) #False
```

---

### ⏩ 트리의 순회

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/42696ebe-0c9f-465b-9eaf-01018f8bf803/Untitled.png)

### ⏩ 트리 너비 우선 검색 구현 (Breadth-first Search)

```python
class BinarySearchTree(object):
    def breadthfirst(self, node):
        q = []
        q.append(node)
        while q:
            cur_node = q.pop(0)

            print(cur_node.data, end=' ') # Processing for data
            
            if cur_node.left != None:
                q.append(cur_node.left)
            if cur_node.right != None:
                q.append(cur_node.right)

array = [11, 5, 4, 7, 1, 6, 9, 15, 13, 18, 12, 14]

bst = BinarySearchTree()
for x in array:
    # bst.insert(x)
    bst.insert(x)
    
bst.breadthfirst(bst.root)
```

- 자식 넣고 루트를 지우는 방식
- 트리는 중복을 생각할 필요가 없다

### ⏩ 트리 깊이 우선 검색 (Depth-first Search

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9b30505d-ffbe-4f8d-b828-dc8ad2115852/Untitled.png)

```python
class BinarySearchTree(object):
    def everyorder(self, node):
        if node != None:
            print(node.data, end = ' ') #node를 지날 때마다 출력하는 코드

            if node.left:
                self.everyorder(node.left) 

            print(node.data, end = ' ') #node를 지날 때마다 출력하는 코드

            if node.right:
                self.everyorder(node.right)

            print(node.data, end = ' ') #node를 지날 때마다 출력하는 코드

array = [11, 5, 4, 7, 1, 6, 9, 15, 13, 18, 12, 14]

bst = BinarySearchTree()
for x in array:
    # bst.insert(x)
    bst.insert(x)

bst.everyorder(bst.root)
```

- 3번 패스 (자식이 2) - 떨어져서 3번
- 2번 패스 (자식이 1) - 연속 2번, 떨어져서 1번
- 1번 패스 (말단노드) - 연속 3번

가장 먼저 나온 숫자만 고르면 → 전위 순회

두 번째 나온 숫자만 고르면 → 중위 순회

마지막으로 나온 숫자만 고르면 → 후위 순회

### ⏩ 전위, 중위, 후위

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b8f9caa7-b465-4a70-9ff4-fd3504f6cde5/Untitled.png)

- 전위 순회 (pre-order) : 루트 먼저 방문하는 방식 : root -> left -> right
- 중위 순회 (in-order) : 왼쪽 하위 트리 방문 후 루트를 방문하는 방식 : left -> root -> right
- 후위 순회 (post-order) : 왼쪽 하위 트리부터 모두 방문 후 루트 방문하는 방식 : left -> right -> root

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/65620908-1a1a-479a-a3fe-e780c995e8fe/Untitled.png)

```python
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
```

---

### ⏩ 프로그래머스 입국심사

```python
def solution(n, times):
    answer = 0
    # right는 가장 비효율적으로 심사했을 때 걸리는 시간
    # 가장 긴 심사시간이 소요되는 심사관에게 n 명 모두 심사받는 경우이다.
    left = 1 
		right = max(times) * n
    while left <= right:
        mid = (left+ right) // 2
        people = 0
        for time in times:
            # people 은 모든 심사관들이 mid분 동안 심사한 사람의 수
            people += mid // time
            # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 반복문을 나간다.
            if people >= n:
                break
        
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
        if people >= n:
            answer = mid
            right = mid - 1
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우
        elif people < n:
            left = mid + 1
            
    return answer
```

이진 탐색을 할 때는 **‘이진 탐색의 범위는 무엇으로 할지’** 와 **‘이진 탐색의 기준을 무엇으로 할지’** 을 잡아야한다.

- 범위 : 심사를 하는데 총 걸리는 시간으로, 1분 부터 가장 비효율적으로 심사를 받았을 때 걸리는 시간(분)으로 하였다.
- mid : 모든 심사관들에게 주어진 시간이다. 따라서 people 은 모든 심사관들이 mid분 동안 심사한 사람의 수가 된다.
- 기준 : mid 동안 심사한 사람의 수(people)가
    1. 심사 받아야할 사람의 수(n)보다 **많거나 같을 경우**에는 시간이 충분했던 것이므로 **주어진 시간을** **줄이고** ( right = mid - 1 -> right 를 줄이면 left와 right의 중간 값인 mid 도 줄어드니까 주어진 시간이 줄어든다.)
    2. 심사 받아야할 사람의 수(n)보다 **적은 경우**에는 시간이 부족했던 것이므로 **주어진 시간을** **늘린다**. (left = mid + 1)