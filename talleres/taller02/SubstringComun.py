def lcs(i, j, x, y):
    if(x == y):
        return len(x)
    elif(i == len(x) or j == len(y) or x == "" or y == ""):
        return 0
    return max(lcs(i+1, j, x, y), lcs(i+1, j, x[0:i] + x[i+1:len(x)], y),
                lcs(i, j+1, x, y), lcs(i, j+1, x, y[0:i] + y[i+1:len(x)]))

print(lcs(0, 0, "ABCDGH", "AEDFHR"))