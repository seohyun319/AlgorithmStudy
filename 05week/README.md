# 중간고사 범위

## 알고리즘의 기초
- 1부터 n까지 연속한 정수의 합을 구하는 알고리즘

  ```python
  def sum_n(n):
    s = 0
    for i in range(1, n + 1):
      s = s + i
    return s
   
  print(sum_n(10))
  ```
  
  1부터 n까지의 합 = n x (n+1) / 2 (수식으로 정리)
  ```python
  def sum_n(n):
    return (n * (n + 1)) // 2 
  ```
  재귀함수 
  ```python
  def sum_n(n):
    if n == 0:
      return 0
    return sum_n(n - 1) + n
    
  print(sum_n(100))
  ```
  
- 주어진 숫자 n개 중 가장 큰 숫자를 찾는 알고리즘
  ```python
  def find_max(a):
    n = len(a) 
    max_v = a[0] 
    for i in range(1, n):
      if a[i] > max_v: 
      max_v = a[i]
    return max_v
    
  v = [17, 92, 18, 33, 58, 7, 33, 42]
  print(find_max(v)) 
  ```
  재귀
  ```python
  def find_max(a, n): # 리스트 a의 앞부분 n개 중 최댓값을 구하는 재귀 함수
    if n == 1:
      return a[0]
    max_n_1 = find_max(a, n - 1) # n-1개 중 최댓값을 구함
    if max_n_1 > a[n - 1]: # n-1개 중 최댓값과 n-1번 위치 값을 비교
      return max_n_1
    else:
      return a[n - 1]
   
  v = [17, 92, 18, 33, 58, 7, 33, 42]
  print(find_max(v, len(v)))
  ```

- 1부터 n까지 연속한 정수의 곱을 구하는 알고리즘

  ```python
  def fact(n):
    f = 1 
    for i in range(1, n + 1): 
      f = f * i
      return f
    ```
  재귀함수 이용
  ```python
  def fact(n):
    if n <= 1: #종료조건
      return 1
    return n * fact(n - 1)
  
  print(fact(10))
  ```
- 하노이의 탑
  ```python
  def Hanoi(N, from_pos, to_pos, via_pos):
    if N == 1:
      print( from_pos, "번 기둥에 있는 원반을 ", to_pos, "번 기둥으로 옮긴다." )
      return
    Hanoi(N - 1, from_pos, via_pos, to_pos)
    print( from_pos, " 번 기둥에 있는 원반을 ", to_pos, "번 기둥으로 옮긴다." )
    Hanoi(N - 1, via_pos, to_pos, from_pos)
  
  Hanoi(1, 1, 3, 2) # 원반 한 개를 1번 기둥에서 3번 기둥으로 이동 (2번을 경유 기둥으로)
  Hanoi(2, 1, 3, 2) # 원반 두 개를 1번 기둥에서 3번 기둥으로 이동 (2번을 경유 기둥으로)
  Hanoi(3, 1, 3, 2) # 원반 세 개를 1번 기둥에서 3번 기둥으로 이동 (2번을 경유 기둥으로)
  ```

- 미로찾기
- 거스름돈

<br/>

## 정렬 알고리즘

- 선택 정렬
  - 선택 정렬 개념

    배열에서 가장 작은 값을 뽑아 새로운 배열에 삽입
  - solution 1 (의미론적 이해를 돕기 위한 예제)
    ```python
    def find_min_idx(): #가장 작은 수의 인덱스값을 리턴하는 함수
      n = len(a)
      min_idx = 0 //첫번째 수를 가장 작은 수라고 가정
      for i in range(1, n):
        if a[i] < a[min_idx]:
          min_idx = i
      return min_idx
    
    def sel_sort(a): #새로운 배열에 선택 정렬 결과를 만드는 함수
      result = []
      while a:
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
      return result
      
    d = [2, 4, 5, 1, 3]
    print(ins_sort(d))
    ```
    
  - solution 2 (swap을 이용한 일반적인 알고리즘)
    ```python
    def sel_sort(a):
      n = len(a)
      for i in range(n-1): #i가 증가하면서 왼쪽 요소부터 비교에서 제외된다
        min_idx = i
        for j in range(i+1, n):
          if a[j] < a[min_idx]:
            min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        
    d = [2, 4, 5, 1, 3]
    ins_sort(d)
    print(d)
    ```
   - 시간복잡도
   
     (n-1)+(n-2)+···+2+1 = n(n-1)/2 = O(n^2)
     
- 버블 정렬
  - 버블 정렬 개념
  
    왼쪽부터 시작해 이웃한 쌍들을 비교하여 정렬되어 있지 않으면 순서를 바꾼다
    
    반복문을 돌 때마다 오른쪽 요소부터 비교에서 제외한다
    ```python
    def bubble_sort(a):
      n = len(a)
      for i in range(n):
        for j in range(n - i - 1): //오른쪽부터 범위가 줄어든다
          if a[j] > a[j + 1]:
          a[j], a[j + 1] = a[j + 1], a[j]
          
    d = [2, 4, 5, 1, 3]
    bubble_sort(d)
    print(d)
    ```
  - 시간복잡도
  
    (n-1)+(n-2)+···+2+1 = n(n-1)/2 = O(n^2)
    
- 삽입 정렬
  - 삽입 정렬 개념
    
    요소가 들어가야 할 위치를 찾아 삽입된다
    
  - solution 1 (의미론적 이해를 돕기 위한 예제)
    ```python
    def find_ins_idx(r, v):
      for i in range(len(r)):
        if v < r[i]: //v보다 큰 수가 있는 인덱스를 찾는다
          return i 
      return len(r)

    def ins_sort(a):
      result = [] 
      while a: 
        value = a.pop(0) 
        ins_idx = find_ins_idx(result, value) 
        result.insert(ins_idx, value) 
      return result

    d = [2, 4, 5, 1, 3]
    print(ins_sort(d))
    ```
  - solution 2 (삽입될 위치까지 리스트가 한 칸씩 이동)
    ```python
    def ins_sort(a):
      n = len(a)
      for i in range(1, n):
        key = a[i] #삽입할 요소의 값 저장, 2번째 값부터 비교 시작
        j = i - 1 #a[i]의 바로 왼쪽 요소부터 비교 시작
        while j >= 0 and a[j] > key: #j가 배열 범위 안에 있는 동안 비교
          a[j + 1] = a[j]
          j -= 1 #왼쪽으로 진행하며 비교
        a[j + 1] = key
        
    d = [2, 4, 5, 1, 3]
    ins_sort(d)
    print(d)
    ```
  - 시간복잡도
  
    (1+2+···+(n-2)+(n-1)) / 2 = n^2 / 2 = O(n^2)
    
- 병합 정렬
  - 병합 정렬 개념
  
    배열을 두 개로 나누어 정렬하고, 각 집단의 맨 앞 요소를 비교하여 새로운 배열에 삽입한다
    
    한 집단이 비게 되면 나머지 집단의 모든 요소를 새로운 배열에 이어붙인다
    
  - solution 1
    ```python
    def merge_sort(a):
      n = len(a)
      if n <= 1:
        return a
      mid = n // 2
      g1 = merge_sort(a[:mid])
      g2 = merge_sort(a[mid:])
      result = []
      while g1 and g2: 
        if g1[0] < g2[0]: 
          result.append(g1.pop(0))
        else:
          result.append(g2.pop(0))
      result = result + g1 + g2
      return result
      
    d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
    print(merge_sort(d))  
    ```
  
  - solution 2
    ```python
    def merge_sort(a):
      n = len(a)
      if n <= 1:
        return
      mid = n // 2
      g1 = a[:mid]
      g2 = a[mid:]
      merge_sort(g1) 
      merge_sort(g2)
      i1 = 0
      i2 = 0
      ia = 0
      while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
          a[ia] = g1[i1]
          i1 += 1
          ia += 1
        else:
          a[ia] = g2[i2]
          i2 += 1
          ia += 1
      while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
      while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1
        
    d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
    merge_sort(d)
    print(d)
    ```
  - 시간복잡도

    O(nlogn)
    
- 퀵 정렬
  - 퀵 정렬 개념
  
    병합 정렬과 기본 개념이 동일하지만, 배열을 둘로 나눌 때 pivot을 기준으로 나눈 뒤 각 그룹을 정렬한다
    
  - solution 1
    ```python
    def quick_sort(a):
      n = len(a)
      if n <= 1: # 재귀 종료 조건
      return a
      pivot = a[-1] #pivot = 마지막 값
      g1 = []
      g2 = []
      for i in range(n - 1): # 마지막 값은 기준 값이므로 제외
      if a[i] < pivot: # 기준 값과 비교
        g1.append(a[i]) # 작으면 g1에 추가
      else:
        g2.append(a[i]) # 크면 g2에 추가
      return quick_sort(g1) + [pivot] + quick_sort(g2)
      
    d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
    print(quick_sort(d))
    ```
  - solution 2 (swap 이용)
    ```python
    def partition(a, start, end):
      pivot = a[end] #pivot = 마지막 값
      i = start
      for j in range(start, end):
        if a[j] <= pivot: 
          a[i], a[j] = a[j], a[i]
          i += 1
        a[i], a[end] = a[end], a[i]
      return i
    def quick_sort_sub(a, start, end):
      if start < end:
        pos = partition(a, start, end)
        quick_sort_sub(a, start, pos - 1) # 기준 값보다 작은 그룹을 재귀 호출로 다시 정렬
        quick_sort_sub(a, pos + 1, end) # 기준 값보다 큰 그룹을 재귀 호출로 다시 정렬
    def quick_sort(a):
      quick_sort_sub(a, 0, len(a) - 1)
      
    d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
    quick_sort(d)
    print(d)
    ```
   - 시간복잡도
   
     O(nlogn)
     
   - pivot(기준 값) 선택 방식
     1. 랜덤
     2. 중간 위치
     3. Median : 앞, 뒤, 중간 위치 중 크기가 중간인 것을 선택
     4. Median of Medians : 배열을 세 구간으로 나누어 각 구간의 Median 중 중간값인 것을 선택
    
    
**생각해보아야 할 것 : 내림차순으로 정렬하기**
