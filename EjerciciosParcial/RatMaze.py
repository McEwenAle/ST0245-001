maze = [[1,1,1,0], 
        [1,1,0,1],
        [1,1,1,1],
        [1,1,1,1]]
visited= []
for i in range(len(maze)):
    visited.append([])
    for m in range(len(maze[0])):
        visited[i].append(0)

def ratMaze(maze, results = [], x=0, y=0, path=''):
    if(x == len(maze)-1 and y == len(maze[0])-1):
        results.append(path)
        return results
    
    visited[x][y] = 1
    dir = [('U', 0,-1), ('D', 0, 1), ('L', -1, 0), ('R', 1, 0)]
    for d in dir:
        nx = x + d[1]  
        ny = y + d[2]
        if(nx > -1 and nx < len(maze) and
           ny > -1 and ny < len(maze[nx]) and
            maze[nx][ny] != 0 and visited[nx][ny] == 0):
            ratMaze(maze, results, nx, ny, path + d[0])
    visited[x][y] = 0
    return results


print(ratMaze(maze))
