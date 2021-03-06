#! Python3
#Chi-Min Chiu, July 2018 milochiou@gmail.com

import tkinter as tk
from tkinter import filedialog
import time
from pinyin_processing import pinyin_processing
from jyutping_processing import jyutping_processing
root = tk.Tk()
root.title("拼音/粵拼 Tool")

global entry1, entry2, lblexport, option


def clickGo():
    lblexport.configure(text="in progress")
    time.sleep(1)
    inp = entry1.get()
    out = entry2.get()
    optionVal = option.get()
    if optionVal == 'pinyin':
        lblexport.configure(text=pinyin_processing(inp, out))
    elif optionVal == 'jyutping':
        lblexport.configure(text=jyutping_processing(inp, out))


def clickfile1():
    name = filedialog.askopenfilename(
        initialdir="D:/",
        filetypes=(("All Files", "*.*"), ("All Files", "*.*")),
        title="Choose a file.")
    entry1.delete(0, len(entry1.get()))
    entry1.insert(0, name)


lbl = tk.Label(root, text="input file:")
lbl.grid(column=0, row=2)
entry1 = tk.Entry(root)
entry1.grid(column=3, row=2)
entry1.insert(0, "input.csv")
btn1 = tk.Button(root, text="..", command=clickfile1)
btn1.grid(column=5, row=2)

lbl2 = tk.Label(root, text="export file:")
lbl2.grid(column=0, row=3)
entry2 = tk.Entry(root)
entry2.grid(column=3, row=3)
entry2.insert(0, "export.csv")

option = tk.StringVar()
option.set("pinyin")  # initialize
radio1 = tk.Radiobutton(root, text="拼音(Pinyin)", value="pinyin", var=option)
radio2 = tk.Radiobutton(
    root, text="粵拼(Jyutping)", value="jyutping", var=option)
radio1.grid(column=0, row=1)
radio2.grid(column=2, row=1)

btngo = tk.Button(root, text="Go", command=clickGo)
btngo.grid(column=5, row=10)

lblexport = tk.Label(root, text="請輸入")
lblexport.grid(column=0, row=0)

root.mainloop()
