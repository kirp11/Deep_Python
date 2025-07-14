from tkinter import *
from tkinter import ttk
import random
import  threading
import time

root = Tk()
root.title("Home Work 7-4 Task-7")
root.geometry("600x800")
root.resizable(False, False)
global_value_sort = 0
labels = []

def buble_sort(liist, widget, lable, lable_prog, value_main, time_start):
    global root
    global global_value_sort
    global flag_label
    for i in range(len(liist)):
        for j in range(len(liist) - i-1):
            if liist[j] < liist[j+1]:
                liist[j], liist[j+1] = liist[j+1], liist[j]
        value_sort = i+1
        global_value_sort +=1
        widget['value'] = global_value_sort
        lable.config(text = f" Поток {threading.current_thread().name}: {value_sort} / {len(liist)}")
        lable_prog.config(text=f"{global_value_sort} / {value_main}")
        if global_value_sort == value_main:
            time_end = time.time()
            label_finish = ttk.Label(text=f"Время выполнения составляет: {time_end - time_start} сек")
            label_finish.pack()
        root.update_idletasks()


def input_data():
    time_start = time.time()


    global value_sort
    global global_value_sort
    num_threads = int(entry_thread.get())
    val = int(entry_value.get())
    main_lst = [(random.randint(1, val)) for i in range(val)]
    threads = []
    sub_lists= []
    progressbar = ttk.Progressbar(orient="horizontal", length=150, value=global_value_sort, maximum=val)
    progressbar.pack()
    main_label_progress = ttk.Label(text=f"0 / {val}")
    main_label_progress.pack()
    if num_threads == 1:
        label_progress = ttk.Label(text=f"0 / {len(main_lst)}")
        th = threading.Thread(target=buble_sort, args=(main_lst, progressbar, label_progress, main_label_progress, val, time_start))
        th.start()
        label_progress.pack()
    else:
        for i in range(1, num_threads+1):

            lst = main_lst[int(((i-1)/num_threads)*val):int((i/num_threads)*val)]
            sub_lists.insert(i-1, lst)
            print(len(sub_lists))
        for i in range(1, num_threads+1):
            label_progress = ttk.Label(text=f"0 / {len(sub_lists[i-1])}")
            # labels.insert(i, label_progress)
            th = threading.Thread(target=buble_sort, args=(sub_lists[i-1], progressbar, label_progress, main_label_progress, val, time_start))
            label_progress.pack()
            threads.append(th)

        for thread in threads:
            thread.start()


label_value = ttk.Label(text="Введите число", font = ("Arial", 18))
label_value.pack()
entry_value = ttk.Entry(width=50)
entry_value.pack()
thread_value = ttk.Label(text="Введите количество потоков (до 30)", font = ("Arial", 18))
thread_value.pack()
entry_thread = ttk.Entry(width=50)
entry_thread.pack()

btn_sort = ttk.Button(text="Начать сортировку", command = input_data)
btn_sort.pack()

root.mainloop()