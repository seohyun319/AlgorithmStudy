def append_star(n):
    if n==1:
        return ['*']
    
    stars = append_star(n//3)
    list_star = []

    for i in stars:
        list_star.append(i * 3)
    for i in stars:
        list_star.append(i + ' ' * (n//3) + i)
    for i in stars:
        list_star.append(i * 3)

    return list_star

N = int(input()) 
print('\n'.join(append_star(N)))

