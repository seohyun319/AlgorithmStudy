# 2750

def ins_sort(A):
    n = len(A)
    for i in range(1, n):
        j = i - 1
        key = A[i]

        while (j >= 0 and A[j] > key):
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key

n = int(input())
A = list()
for i in range(n):
    A.append(int(input()))

ins_sort(A)
print(A)


