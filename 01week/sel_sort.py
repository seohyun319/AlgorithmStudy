def sel_sort(a):
    n = len(a)
    for i in range(n - 1): # 0부터 n-2까지 반복
    # i번 위치부터 끝까지 자료 값 중 최솟값의 위치를 찾음
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
            # for 문이 끝났으면 min_idx 안에 최소값의 위치가 들어있다.
        a[i], a[min_idx] = a[min_idx], a[i]
        print(a)
        
d = [2, 4, 5, 1, 3]
sel_sort(d)
print(d)