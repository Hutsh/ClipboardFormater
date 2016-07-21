#coding=utf-8
import win32clipboard
import win32con
import re
from tkinter import *

def get_clipboard():
	win32clipboard.OpenClipboard()
	data = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()
	return data

def set_clipboard(text):
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardText(text)
	win32clipboard.CloseClipboard()

# -----------可用----------------
# cb=get_clipboard()
# print(cb)
# print("\n\n")

# string =cb
# p = r'(\r\n)([ABCD])'
# pattern = re.compile(p)

# res = pattern.sub(r'\1\2. ',string)
# print(res)
# set_clipboard(res)
# -----------可用----------------


root=Tk()
root.title("Clipboard Formater")
root.geometry('400x300')






root.mainloop()