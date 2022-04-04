#2751
# n = int(input())
# array = list()
# for i in range(n):
#     array.append(int(input()))
# print("초기", array)

# def merge_sort(array):

#     if len(array)<=1:
#         return

#     mid = len(array)//2

#     a1 = array[:mid]
#     a2 = array[mid:]

#     merge_sort(a1)
#     merge_sort(a2)

#     result = list()
#     while a1 and a2:
#         if a1[0] < a2[0]:
#             result.append(a1.pop(0))
#         else:
#             result.append(a2.pop(0))

#     result = result + a1 + a2
#     print(result)
#     return result

# # d = [1,3,5,2,4,6]
# print('최종결과', merge_sort(array))



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

# d = [1,3,5,2,4,6]
print(merge_sort(array))
