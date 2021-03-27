s = input()
m = int(input())
dp = [[-1 for item in range(len(s)+1)] for j in range(len(s)+1)]

def query(a, b):
    if a + 1 == b:
        if s[a-1] == s[b-1]:
            dp[a][b] = 1
            return 1
        else:
            dp[a][b] = 0
            return 0
    m = int((a+b)/2)
    return query(a, m) + query(m, b)

for i in range(m):
    a, b =  map(int, input().split())
    print(query(a, b))
