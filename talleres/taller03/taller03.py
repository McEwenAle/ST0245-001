def hanoi(topN, a = "principio", b = "auxiliar", c = "destino"):
    if(topN == 1):
        return "Move piece " + str(topN) + " to tower " + str(c)
    return hanoi(topN-1, a, c, b) + "\n" + "Move piece " + str(topN) + " to tower " + str(c) + "\n" + hanoi(topN-1, b, a, c)

# print(hanoi(5, 1, 2, 3))

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

def fila(board, i):
    for n in board:
        if(board[n] == i):
            return False
    return True

def diagonal(board, i, j):
    for n in range(len(board)):
        if(n == len(board) or n == len(board[0])):
            break
        if(board[n+i][n+j] == 1):
            return False
    return True





def checkBoard(board, i, j):
    return fila(board, i, j) and diagonal(board, i, j)

def nextAvailable(board, i, j):
    for n in range(board(len)):
        if(checkBoard(board, n, ))

def reinas(n, board):
    if():
        pass
    