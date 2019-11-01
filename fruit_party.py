import tkinter as tk
import random

fruit = ['apple','banana','mango']
fruit_party =  [['' for i in range(5)] for j in range(5)]

root = tk.Tk()
root.title('フルーツパーティ')

for i in range(5):
    for j in range(5):
        cell = tk.Label(text='({},{}){}'.format(i,j,fruit[random.randint(0,len(fruit)-1)]))
        cell.grid(column=i, row=j)
tk.mainloop()
