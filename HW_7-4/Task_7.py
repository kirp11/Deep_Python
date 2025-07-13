from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Home Work 7-4 Task-7")
root.geometry("600x300")
root.resizable(False, False)
value_sort = 0

def buble_sort(liist, widget, lable):
    global root
    global value_sort
    for i in range(0, len(liist)):
        for j in range(0, len(liist) - i-1):
            if liist[j] < liist[j+1]:
                liist[j], liist[j+1] = liist[j+1], liist[j]
        value_sort = i
        widget['value'] = value_sort
        lable.config(text = f"{value_sort} / {len(liist)}")
        root.update_idletasks()






def input_data():
    global value_sort
    if (int(entry_value.get()) > 0):
        val = int(entry_value.get())
        lst = [(random.randint(1, val)) for i in range(val)]
        progressbar = ttk.Progressbar(orient="horizontal", length=150, value=value_sort, maximum=val)
        progressbar.pack()
        label_progress = ttk.Label(text = f"0 / {val}")
        label_progress.pack()
        buble_sort(lst, progressbar, label_progress)
    else:
        print(entry_value.get())
        label_result = ttk.Label(text="поле не заполнено",  background="#FF033E", font=("Arial", 15))
        label_result.pack()


label_value = ttk.Label(text="Введите число", font = ("Arial", 18))
label_value.pack()
entry_value = ttk.Entry(width=50)
entry_value.pack()

btn_sort = ttk.Button(text="Начать сортировку / добавить помощи", command = input_data)
btn_sort.pack()

root.mainloop()