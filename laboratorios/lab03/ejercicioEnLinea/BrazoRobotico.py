from collections import deque

n = int(input())
l = []
pos = []
for i in range(n):
    l.append(deque([i]))
    pos.append(i)
s = input()
while s != 'quit':
    command, a, direction, b = s.split()
    a = int(a)
    b = int(b)
    if command == 'move':
        if direction == 'onto':
            c = l[pos[b]].pop()
            while c != b:
                l[c].append(c)
                pos[c] = c
                c = l[pos[b]].pop()
            l[pos[b]].append(b)
            c = l[pos[a]].pop()
            while c != a:
                l[c].append(c)
                pos[c] = c
                c = l[pos[a]].pop()
            l[pos[b]].append(a)
            pos[a] = pos[b]
        if direction == 'over':
            c = l[pos[a]].pop()
            while c != a:
                l[c].append(c)
                pos[c] = c
                c = l[pos[a]].pop()
            l[pos[b]].append(a)
            pos[a] = pos[b]
    if command == 'pile':
        if direction == 'onto':
            c = l[pos[a]].pop()
            while c != a:
                l[pos[b]].append(c)
                pos[c] = pos[b]
                c = l[pos[a]].pop()
            l[pos[b]].append(a)
            pos[a] = pos[b]
        if direction == 'over':
            stk = deque()
            while c != a:
                c = l[pos[a]].pop()
                stk.append(c)
            while len(stk) > 0:
                c = stk.pop()
                l[pos[b]].append(c)
                pos[c] = pos[b]
    
    s = input()
for i in range(len(l)):
    s = ""
    for e in l[i]:
        s = s + str(e) + " "
    print(str(i) + ":", s)
