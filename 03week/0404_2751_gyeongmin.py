#2751

# pop 사용해서 푸는 법
n = int(input())
array = list()
for i in range(n):
    array.append(int(input()))
print("초기", array)

def merge_sort(array):

    if len(array)<=1:
        return array

    mid = len(array)//2

    a1 = merge_sort(array[:mid])
    a2 = merge_sort(array[mid:])

    result = []
    while a1 and a2:
        print('a1', a1)
        print('a2', a2)
        if a1[0] < a2[0]:
            print(a1[0])
            result.append(a1.pop(0))
        else:
            print(a2[0])
            result.append(a2.pop(0))

    result = result + a1 + a2
    #print('result',result)
    return result

print(merge_sort(array))



# 시간초과 안 되게 푸는 법
def merge_sort(array):

    if len(array)<=1:
        return array

    mid = len(array)//2

    a1 = merge_sort(array[:mid])
    a2 = merge_sort(array[mid:])

    result = []

    i1, i2 = 0, 0

    while len(a1) > i1 and len(a2) > i2 :
        if a1[i1] < a2[i2]:
            result.append(a1[i1])
            i1+=1
        else:
            result.append(a2[i2])
            i2+=1

    while len(a1) > i1 and len(a2) <= i2 :
        result.append(a1[i1])
        i1+=1

    while len(a2) > i2 and len(a1) <= i1 :
        result.append(a2[i2])
        i2 += 1

    return result

n = int(input())
array = list()
for i in range(n):
    array.append(int(input()))

sorted_array = merge_sort(array)

for i in range(n):
    print(sorted_array[i])
