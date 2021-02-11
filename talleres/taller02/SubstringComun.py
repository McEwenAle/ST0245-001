def lcs(i, j, x, y):    
    if(i<0 or j<0):
        return -1  
    if(x[i:i+1] == y[j:j+1]):
        return lcs(i-1, j-1, x, y) + 1
    return max(lcs(i-1, j, x, y), lcs(i, j-1, x, y))

x ="ABCD"
y ="ABCD"
print(lcs(len(x),len(y),x,y))