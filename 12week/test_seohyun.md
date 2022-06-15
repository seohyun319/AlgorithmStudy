1. 다음의 시간 복잡도를 쓰시오
    
    
    |  | 배열 | 연결리스트 | 힙 |
    | --- | --- | --- | --- |
    | 삽입 |  |  |  |
    | 삭제 |  |  |  |
2. 다음 코드의 시간 복잡도와 어떠한 알고리즘에 대한 함수인지 쓰시오
    
    ```python
    def name(arr, findThis):
    	pos = -1
    	size = len(arr)
    
    	print(f'{findThis}와 비교한 데이터 : ', end='')
    
    	for i in range(size):
    		print(arr[i], end=' ')
    		if arr[i] == findThis:
    			pos = i
    			break
    	print()
    	return pos
    
    dataArr = [188, 150, 168, 162, 105, 120, 177, 50]
    pos = name(dataArr, 105) # 105와 비교한 데이터 : 188 150 168 162 105
    pos = name(dataArr, 110) # 110와 비교한 데이터 : 188 150 168 162 105 120 177 50
    ```
    
    → 
    
3. 다음 코드의 시간 복잡도와 어떠한 알고리즘에 대한 함수인지 쓰시오
    
    ```python
    def name(a, x):
    	start = 0
    	end = len(a) - 1
    	while start <= end:
    		mid = (start + end) // 2 
    		if x == a[mid]: 
    			return mid
    		elif x > a[mid]:
    			start = mid + 1
    		else: 
    			end = mid - 1
    	return -1 
    d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
    print(name(d, 36)) 
    print(name(d, 50)) 
    ```
    
    → 
    
4. AVL 트리에서 LR이 가장 깊을 때 어떤 회전을 해야 하는가?
    
    → 
    
5. 레드블랙트리가 균형을 맞추는 두 가지 방법을 쓰시오
    
    → 
    
6. 다음 코드는 깊이 우선 탐색의 코드이다. answer에 들어갈 값과 탐색 결과를 적으시오.
    
    ```python
    def print_all_friends(graph, start):
        todo = []
        done = []
    
        todo.append(start)
        done.append(start)
    
        while todo:
            vertex = todo.pop(**answer**)
            print(vertex)
            for x in graph[vertex]:
                if x not in done:
                    todo.append(x)
                    done.append(x)
    
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
    ```
    
    answer: 
    
    탐색 결과:
