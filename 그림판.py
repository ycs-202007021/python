from tkinter import *

mycolor = 'black'
wp=5

def paint(event):
    x1,y1=(event.x),(event.y)
    x2,y2=(event.x+2),(event.y+2)
    canvas.create_line(x1,y1,x2,y2, width=wp, fill = mycolor)

 
def change_color1():
    global mycolor
    mycolor ='red'
    changecolor.config(text=str(mycolor))


    
def change_color2():
    global mycolor
    mycolor='blue'
    changecolor.config(text=str(mycolor))
    
def change_color3():
    global mycolor
    mycolor='yellow'
    changecolor.config(text=str(mycolor))
    
def change_color4():
    global mycolor
    mycolor='green'
    changecolor.config(text=str(mycolor))
    
def change_color5():
    global mycolor
    mycolor='white'
    changecolor.config(text= str(mycolor))   


def pensize1():
    global wp
    wp+=2
    pensize.config(text= wp)
    
def pensize2():
    global wp
    wp-=2
    if wp<1:
            wp=1
    pensize.config(text= wp)
    
def func_exit():
    window.quit()
    window.destroy()

window=Tk()
frame= Frame(window)
frame.pack()

canvas=Canvas(window, width=300, height=300, bg='white')
canvas.pack()
canvas.bind('<B1-Motion>',paint)

label1= Label(frame, text= '펜 색:', bg="pink")
changecolor= Label(frame, text= mycolor, bg="pink")
label1.pack(side=LEFT)
changecolor.pack(side=LEFT)

label3= Label(frame, text= '펜 굵기:', bg="skyblue")
pensize= Label(frame, text= wp, bg="skyblue")
label3.pack(side=LEFT)
pensize.pack(side=LEFT)


button1=Button(window, text='빨 강', command= change_color1, bg="red")
button2=Button(window, text='파 랑', command= change_color2, bg="blue")
button3=Button(window, text='노 랑', command= change_color3, bg="yellow")
button4=Button(window, text='초록', command= change_color4, bg="green")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)

button5=Button(window, text='더 크게', command= pensize1)
button6=Button(window, text='더 작게', command= pensize2)
button5.pack(side=LEFT)
button6.pack(side=LEFT)

button7=Button(window, text='지우개', command= change_color5, bg="white")
button7.pack(side=LEFT)

mainMenu= Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="menu", menu=fileMenu)
fileMenu.add_command(label="종료", command = func_exit)

window.mainloop()
