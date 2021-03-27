from collections import deque

n = input()
l = []
pos = []
for i in range(n):
    l.append(deque(i))
    pos.append(i)
s = input()
a = int(a)
b = int(b)
while s != 'quit':
    command, a, direction, b = s.split()
    if command == 'move':
        if direction == 'onto':
            c = l[pos[b]].pop()
            while c != b:
                l[c].push(c)
                pos[c] = c
                c = l[pos[b]].pop()
            l[pos[b]].push(b)
            c = l[pos[a]].pop()
            while c != a:
                l[c].push(c)
                c = l[pos[a]].pop()
            l[pos[b]].push(a)
            pos[a] = pos[b]
        if direction == 'over':
            c = l[pos[a]].pop()
            while c != a:
                l[c].push(c)
                pos[c] = c
                c = l[pos[a]].pop()
            l[pos[b]].push(a)
            pos[a] = pos[b]
    if command == 'pile':
        if direction == 'onto':
            c = l[pos[a]].pop()
            while c != a:
                l[pos[b]].push(c)
                pos[c] = pos[b]
                c = l[pos[a]].pop()
            l[pos[b]].push(a)
            pos[a] = pos[b]
        if direction == 'over':
            stk = deque()
            while c != a:
                stk.push(c)
                c = l[pos[a]].pop()
            c = stk.pop()
            l[pos[b]].push(a)
            pos[a] = pos[b]
            while len(stk) > 0:
                c = stk.pop()
                l[pos[b]].push(c)
                pos[c] = pos[b]
                c = stk.pop()
    
    s = input()
for i in range(len(l)):
    print(i, ":", l[i])
