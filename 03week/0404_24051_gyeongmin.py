#24051
def insert_sort(array, n, k):
    count = 0

    for i in range(1, n):
        loc = i-1
        new_item = array[i] #미리 i번째 값 저장

        while (0 <=loc and new_item < array[loc]): # i번째 수가 i-1번째 수보다 작으면
            array[loc+1] = array[loc] # [i]에 [i-1] 값 넣기(원래 i번째 값 날아감)
            loc-=1 # i-2, i-3 ... 이랑 i번째 수 계속 비교
            count+=1
            print(count, '번째:', array)
            if (count == k):
                result = array[loc+1]
                print(result)

        if (loc+1 != i):
            array[loc+1] = new_item # 값이 변했으면 저장해놨던 값 맞는 자리에 넣기
            count += 1
            print(count, '번째:', array)
            if (count == k):
                result = array[loc+1]
                print(result)

    if (count < k):
        return -1
    else:
        return result

n, k = list(map(int, input().split()))
array = list(map(int, input().split()))


print(insert_sort(array, n, k))
