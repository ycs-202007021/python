from tkinter import *
from tkinter.filedialog import *
import os


def func_exit():
    window.quit()
    window.destroy()

def paint():
    os.startfile("C:\\Users\\com\\Desktop\\대학\\과제\\파이썬과제\\새 폴더\\그림판.py")


def txt():
    os.startfile("C:\\Users\\com\\Desktop\\대학\\과제\\파이썬과제\\새 폴더\\메모장.py")

def score():
    os.startfile("C:\\Users\\com\\Desktop\\대학\\과제\\파이썬과제\\새 폴더\\성적폼.py")

window=Tk()
window.title("기말평가-202007021 임정은")
window.geometry("400x400")

mainmenu= Menu(window)
window.config(menu=mainmenu)

               
filemenu = Menu(mainmenu)
submenu= Menu(filemenu)
mainmenu.add_cascade(label="Menu", menu=filemenu)
filemenu.add_cascade(label="작업선택", menu=submenu)
submenu.add_command(label="그림판", command = paint)
submenu.add_command(label="메모장", command = txt)
submenu.add_command(label="성적입력", command = score)
submenu.add_separator()
submenu.add_command(label="종료", command = func_exit)

window.mainloop()
