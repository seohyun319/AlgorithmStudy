def dfs(y,x):
    if x < 0 or x >= w or y < 0 or y >= h:
        return False
    
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(y,x-1)
        dfs(y,x+1)
        dfs(y-1,x)
        dfs(y+1,x)
        dfs(y-1,x-1)
        dfs(y-1,x+1)
        dfs(y+1,x-1)
        dfs(y+1,x+1)
        return True
    return False
