## 그래프 (Graph)

- 현상이나 사물을 정점 vertex (노드 node)과 간선 edge으로 표현한 것
- Graph G = (V, E)
V : 정점 집합
E : 간선 집합
    
    > 정점: 사람.
    간선: 사람간의 친구 관계. 친밀도(촌수)
    직접 연결) 친구(일촌). 직접 아는 사이
    간접 연결) 친친(친척). 직간접적으로 아는 모든 사람
    > 
- 두 정점이 간선으로 연결됨 == 인접 adjacent하다, 이웃 관계에 있다
    
    ![image](https://user-images.githubusercontent.com/76686872/171328617-b9698839-53d7-4fca-9290-36e8119210b7.png)
    
- 경로 (Path)
    - 정점 A에서 C까지의 경로는 A-B-C, A-E-B-C, A-D-C 등이 있음
- 그래프의 종류
    - 무방향성 그래프 (Undirected Graph): 간선에 방향이 없는 그래프
    - 방향성 그래프 (Directed Graph): 간선에 방향이 있는 그래프
    - 가중치 그래프 (Weighted Graph): 간선마다 가중치가 다르게 부여된 그래프
        - 간선에 방향이 없는 그래프 (Weighted Undirected Graph)
        - 간선에 방향이 있는 그래프 (Weighted Directed Graph)

![image](https://user-images.githubusercontent.com/76686872/171328652-880dc82b-447f-4df8-84c4-99b6767d7a6a.png)

![image](https://user-images.githubusercontent.com/76686872/171328684-95e2a038-0b70-462e-b64c-c3ec993ae83b.png)

---

## 그래프 표현법

- 그래프는 정점의 집합과 간선의 집합의 결합
→ 그래프를 표현하는 문제는 “정점의 집합”과 “간선의 집합”의 표현 문제
→ 간선은 정점과 정점이 “인접” 관계에 있음을 나타내는 존재
→ 그래프의 표현 문제는 “**간선, 즉 정점과 정점의 인접 관계를 어떻게 나타내는가?**”의 문제로 귀결

### 인접 행렬(Adjacency Matrix)

: 정점끼리의 인접 관계를 나타내는 행렬

- 그래프의 정점의 수가 N → N x N 크기의 행렬
- 원소 (i, j)로 표현:
    - • 원소 (i, j) == 1 : 정점 i 와 정점 j 사이에 간선이 있음 (인접함)
    • 원소 (i, j) == 0 : 정점 i 와 정점 j 사이에 간선이 없음 (인접 X)
        
        ![image](https://user-images.githubusercontent.com/76686872/171328735-9c5d0515-3c9c-4177-b615-9a408eb6103e.png)
        
        가중치 없는 방향 그래프
        
    - 유향 그래프의 경우: 원소 (i, j)와 원소 (j, i)가 대칭적이지 않음
    - 무향 그래프의 경우: 원소 (i, j) == 원소 (j, i) 항상 대칭
    - 가중치가 있는 그래프의 경우: 원소 (i, j)는 1 대신에 가중치 값을 가짐
- 인접 행렬 (Adjacency Matrix) 장단점
    - 장점
        - 이해하기 쉽고, 간선 존재 여부를 즉각 알 수 있음
        - 간선의 밀도가 높은 그래프에서는 유리
    - 단점
        - $N^2$에 비례하는 공간 필요 (N은 정점 수)
        - 행렬의 모든 원소를 채우는 데에만 N2에 비례하는 시간 필요

### 인접 리스트(Adjacency List)

: 그래프 내의 각 정점의 인접 관계를 표현하는 리스트

- N 개의 리스트 (연결리스트 또는 배열)로 표현
- i번째 리스트는 정점 i에 인접한 정점들을 리스트로 연결
    - 무향 그래프에서 총 간선 수의 두 배의 항목으로 표현
        
        ![image](https://user-images.githubusercontent.com/76686872/171328888-2a360d09-138e-4173-90f8-50baad9c39bf.png)
        
    - 유향 그래프에서 간선 하나 당 항목 하나씩 필요
        
        ![image](https://user-images.githubusercontent.com/76686872/171328931-0e51ee5c-944c-4478-a72e-5bffc3e17282.png)
        
- 가중치 (Weighted) 있는 그래프의 경우: 리스트에 가중치 (Weight)도 보관
    
    ![image](https://user-images.githubusercontent.com/76686872/171328961-4a51c941-39e8-4ab9-b4e1-f54fb1db55ef.png)
    
- 인접 리스트 (Adjacency List) 장단점
    - 장점
        - 간선 총 수에 비례하는 양만큼만 필요
        - 모든 가능한 정점 쌍에 비해 간선 수가 적을 때 유리
    - 단점
        - 거의 모든 정점에 간선이 있는 경우 구조적 접근 (Indexing) 비 효율성
        (LinkedList 구현일 경우 메모리에서도 손해, 리스트 연산량 오버헤드)
        - 정점 i와 j 간에 간선이 있는지 알아볼 때 시간이 많이 걸림

---

## 그래프의 순회 (Graph Traversal)

- 그래프의 모든 정점을 방문하는 방법
    - 너비우선탐색 BFS (Breadth-First Search)
    - 깊이우선탐색 DFS (Depth-First Search)

### 너비우선탐색 BFS (Breadth-First Search)

→ "Queue (FIFO)" 자료 구조 이용

- 과정
    1. 시작 정점을 “방문했음”으로 표시하고, 큐에 삽입 (Enqueue) 
    2. 큐가 비지 않았으면, 큐로부터 정점을 제거(Dequeue)해서 정점을 확인
    3. 제거한 정점이 이웃하고 있는 인접 정점 중 아직 방문하지 않은 곳들을 “방문했음”으로 표시하고, 큐에 삽입 (Enqueue) 
    - 큐가 비게 되면 탐색이 끝. 큐가 빌 때까지 2의 과정 반복
    
    ```c
    BFS(G, s) { 
    // G = (V, E): 주어진 그래프
    // s: 시작 정점
    	for each v ∈ V – {s}
    		visited[v] = NO; // 시작 정점을 뺀 모든 정점들을 ‘방문하지 않았음’으로 표시
    	visited[s] = YES; // 시작 정점
    	enqueue(Q, s); // 이미 방문한 정점들을 큐 Q에 넣는다.
    	while (Q ≠ Ø) {
    		u = dequeue(Q);
    		for each v ∈ L(u) // L(u): 정점 u의 인접리스트
    			if (visited[v] == NO) then
    			visited[v] = YES; // 방문하였음 이라고 표시
    			enqueue(Q, v);
    			}
    		}
    }
    //수행시간: 𝑂(|V|+|E|)
    ```
    
- 친친 찾기 예제
    1. 앞으로 처리할 정점을 저장할 리스트 (Queue) todo를 만듦
    2. 이미 리스트 (Queue)에 추가한 정점을 저장할 리스트 done을 만듦
    3. 검색의 출발점이 될 정점을 리스트 (todo)와 리스트 (done)에 추가
    4. 리스트 (Queue)에 사람이 남아 있다면 리스트에서 처리할 사람을 꺼냄
    5. 꺼낸 사람을 출력 (정점 데이터 처리)
    6. 꺼낸 정점의 이웃들 중 리스트 done을 확인해서
    아직 추가된 적이 없는 정점을 골라 리스트 (todo) 와 리스트 (done)에 추가
    7. 리스트 todo 에 처리할 정점이 남아 있다면 4번 과정부터 다시 반복
    
    ```python
    def print_all_friends(graph, start):
    	todo = []
    	done = []
    
    	# 처리를 시작할 항목 지정
    	todo.append(start)
    	done.append(start)
    
    	# 리스트 todo에 처리할 항목이 남아있을 때까지 처리
    	while todo:
    		vertex = todo.pop(**0**) # 리스트 todo를 Queue로 이용 (FIFO)
    		print(vertex)
    		for x in graph[vertex]: # todo에서 뽑은 정점의 모든 이웃에 대해서
    			# 방문한 적이 없다면 다음에 처리할 수 있도록 리스트(Queue)에 넣어줌
    			if x not in done: 
    				todo.append(x)
    				done.append(x)
    
    # 딕셔너리로 그래프 생성
    graph = {
    1: [2, 3],
    2: [4, 5],
    3: [4, 6],
    4: [5, 7],
    5: [7],
    6: [7],
    7: []
    }
    
    print_all_friends(graph, 1)
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    ```
    

### 깊이우선탐색 DFS (Depth-First Search)

→ "Stack (FILO)" 자료 구조를 이용

- 과정
    1. 시작 정점을 “방문했음”으로 표시
    2. 이 정점과 이웃하고 있는 정점 (인접 정점) 중에 아직 방문하지 않은 곳을 선택하여
    이를 시작 정점으로 삼아 다시 깊이 우선 탐색을 시작
    즉, 단계 1)을 다시 하기
    3. 정점에 더 이상 방문하지 않은 인접 정점이 없으면 이전 정점으로 돌아가서 단계 2)를 수행
    4. 이전 정점으로 돌아가도 더 이상 방문할 이웃이 없다면 그래프의 모든 정점을 모두 방문했다는 뜻. 탐색 종료
    
    ```c
    DFS(G) {
    	visited[v] ← YES;
    	for each x ∈ L(v) // L(v): 정점 v의 인접 리스트
    		if (visited== NO) then aDFS(x);
    }
    // 수행시간: 𝑂(|V|+|E|)
    ```
    
- 친친 찾기 예제
    1. 앞으로 처리할 정점을 저장할 리스트 (Stack) todo를 만듦
    2. 이미 리스트 (Stack)에 추가한 정점을 저장할 리스트 done을 만듦
    3. 검색의 출발점이 될 정점을 리스트 (todo)와 리스트 (done)에 추가
    4. 리스트 (Stack)에 사람이 남아 있다면 리스트에서 처리할 사람을 꺼냄
    5. 꺼낸 사람을 출력 (정점 데이터 처리)
    6. 꺼낸 정점의 이웃들 중 리스트 done을 확인해서
    아직 추가된 적이 없는 정점을 골라 리스트 (todo) 와 리스트 (done)에 추가
    7. 리스트 todo 에 처리할 정점이 남아 있다면 4번 과정부터 다시 반복
