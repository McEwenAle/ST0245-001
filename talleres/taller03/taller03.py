def hanoi(topN, a = "principio", b = "auxiliar", c = "destino"):
    if(topN == 1):
        return "Move piece " + str(topN) + " to tower " + str(c)
    return hanoi(topN-1, a, c, b) + "\n" + "Move piece " + str(topN) + " to tower " + str(c) + "\n" + hanoi(topN-1, b, a, c)

print(hanoi(5, 1, 2, 3))

def subset(s, base = ""):
    return permutations(base,s)
    
def permutations(base, stri):
    if(len(stri)==0):
        return base + " "
    ans = ""
    for c in range(len(stri)):
        ans += permutations(base+stri[c:c+1], stri[0:c]+stri[c+1:len(stri)])
    return ans

print(subset("abc"))

def fila(board, j):
    for n in board:
        if(n == j):
            return False
    return True

def diagonal(board, i, j):
    i1 = max(0, i-j)
    j1 = max(0, j-i)
    i2 = min(len(board)-1, j+i)
    j2 = max(i-(len(board)-1-j), 0)
    for n in range(i1,len(board)):
        if(j1==board[n]):
            return False        
        j1+=1
    for n in range(j2, len(board)):
        if(n==board[i2]):
            return False        
        i2-=1
    return True


def checkBoard(board, i, j):
    return fila(board, j) and diagonal(board, i, j)

def reinas(n, board, i):
    if(n==i):
        return True
    for m in range(len(board)):
        if(checkBoard(board, i, m)):
            board[i] = m
            if(reinas(n, board, i+1)):
                return True
            board[i] = -1
    return False

board = [-1]*8
reinas(6, board, 0)
print(board)


def tarritoDePaint(canvas,x, y, color, inColor = -1):
    if(inColor == -1):
        inColor = canvas[x][y]
    if(inColor == color):
        return
    boaders = [[0,-1], [-1, 0], [1, 0], [0, 1]]
    for boarder in boaders:
        x1 = boarder[0] + x
        y1 = boarder[1] + y
        if(x1 > -1 and x1 < len(canvas) and
           y1 > -1 and y1 < len(canvas[x1]) and
           canvas[x1][y1] == inColor):
            canvas[x1][y1] = color
            tarritoDePaint(canvas, x1, y1, color, inColor)

canvas = [[0, 0, 0],[1,0, 1],[1,0,1]]
tarritoDePaint(canvas, 1, 0, 2)
print(canvas)
        
    
