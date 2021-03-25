import queue



fila1 = queue.Queue()
fila2 = queue.Queue()
fila3 = queue.Queue()
fila4 = queue.Queue()

filas = [fila1, fila2, fila3, fila4]

cajero1 = []
cajero2 = []

cajeros = [cajero1, cajero2]

for i in range(1,10):
    fila1.put(i)
for i in range(10,15):
    fila2.put(i)
for i in range(15,21):
    fila3.put(i)
for i in range(21,40):
    fila4.put(i)

i = 0
while not fila1.empty() or not fila2.empty() or not fila3.empty() or not fila4.empty():
    for fila in filas:
        if not fila.empty():
            if i == 2:
                i = 0
            cajeros[i].append(fila.get())
            i += 1

# print(cajero1)
# print(cajero2)