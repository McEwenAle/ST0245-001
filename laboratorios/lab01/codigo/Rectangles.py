from tkinter.constants import INSERT
import tkinter as tk

def formas(n):
    if n == 0:
        return 1
    a = 0
    if n>1:
        a = formas(n-2)

    return  a + formas(n-1)

def shapes(n, top, arr):
    if n == 0:
        arr.append(top)
    else:
        if n>1:
            shapes(n - 2, top + "hh", arr)
        shapes(n - 1, top + "v", arr)


class Demo1:
    def __init__(self, master, n):
        self.master = master
        a = []
        shapes(n, "", a)
        self.text = tk.Text(self.master)
        self.text.insert(INSERT,"Main")
        self.text.pack()
        for s in a:
            self.new_window(n, s)
    def new_window(self, n, s):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow, n, s)

class Demo2:
    def __init__(self, master, n, s):
        self.master = master
        self.canvas = tk.Canvas(master, width=n*100 + 20, height=220)
        c = 0
        while c < len(s):
            if s[c] == 'h':
                self.canvas.create_rectangle(c*100+10, 10, (c+2)*100+10, 110, fill="red", width="4")
                self.canvas.create_rectangle(c*100+10, 110, (c+2)*100+10, 210, fill="red", width="4")
                c += 1
            else:
                self.canvas.create_rectangle(c*100+10, 10, (c+1)*100+10, 210, fill="blue", width="4")
            c += 1
        self.canvas.pack()

def main(): 
    root = tk.Tk()
    app = Demo1(root, 5)
    root.mainloop()

if __name__ == '__main__':
    main()

print(formas(4))