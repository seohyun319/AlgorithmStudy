n = int(input())
def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, c)
        hanoi(n - 1, b, a, c)
count = 0
for i in range(n):
    count = count * 2 + 1
print(count) # 이동횟수
hanoi(n, 1, 2, 3) # 움직이는 과정