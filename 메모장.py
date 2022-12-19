from tkinter.filedialog import *
from tkinter import *

def newfile():
    window.title("새로운 파일-메모장")
    txt.delete(1.0, END)

def openfile():
    filename = askopenfilename(parent=window, filetypes = (("텍스트 파일", "*.txt"),("모든 파일", "*.*")))
    txt.delete(1.0, END)
    file=open(filename, "r")
    txt.insert(1.0, file.read())
    file.close()

def savefile():
    filename = asksaveasfilename(parent=window, filetypes = (("텍스트 파일", "*.txt"),("모든 파일", "*.*")))
    file=open(filename, "w")
    file.write(txt.get(1.0, END))
    file.close()


def func_exit():
    window.quit()
    window.destroy()


window=Tk()
window.title("메모장")
window.geometry("400x400")
mainMenu= Menu(window)
txt=Text(window)
txt.pack()

window.config(menu=mainMenu)
fileMenu= Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="새 파일", command=newfile)
fileMenu.add_command(label="열기", command=openfile)
fileMenu.add_command(label="저장", command=savefile)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_exit)
window.mainloop()
