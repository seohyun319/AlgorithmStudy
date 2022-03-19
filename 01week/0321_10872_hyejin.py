def factorial(i):
    if i==0:
        return 1
    else:
        return i*factorial(i-1)

n = int(input())
print(factorial(n))
