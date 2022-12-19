from tkinter.filedialog import *
from tkinter import *

window = Tk()
window.title("성적입력")
window.geometry("500x200")
window.resizable(width= FALSE, height =FALSE)


def grade():
    py_score=float(entry3.get())
    py_grade= ''
    if py_score  >= 90:
        py_grade = 'A'    

    elif py_score  >= 80:
        py_grade = 'B'    

    elif py_score  >= 70:
        py_grade = 'C'    

    elif py_score  >= 60:
        py_grade = 'D'    
    else:
        py_grade = 'F'

    label7.configure(text=py_grade)
    
    c_score=float(entry4.get())
    c_grade= ''
    if c_score  >= 90:
        c_grade = 'A'    

    elif c_score  >= 80:
        c_grade = 'B'    

    elif c_score  >= 70:
        c_grade = 'C'    

    elif c_score  >= 60:
        c_grade = 'D'    
    else:
        c_grade = 'F'

    label8.configure(text=c_grade)

    html_score=float(entry5.get())
    html_grade= ''
    if html_score  >= 90:
        html_grade = 'A'    

    elif html_score  >= 80:
        html_grade = 'B'    

    elif html_score  >= 70:
        html_grade = 'C'    

    elif html_score  >= 60:
        html_grade = 'D'    
    else:
        html_grade = 'F'

    label9.configure(text=html_grade)

    DB_score=float(entry6.get())
    DB_grade= ''
    if DB_score  >= 90:
        DB_grade = 'A'    

    elif DB_score  >= 80:
        DB_grade = 'B'    

    elif DB_score  >= 70:
        DB_grade = 'C'    

    elif DB_score  >= 60:
        DB_grade = 'D'    
    else:
        DB_grade = 'F'

    label10.configure(text=DB_grade)

    f= open("c:\\Users\\com\\Desktop\\대학\\과제\\파이썬과제\\새 폴더\\sauce.txt", "w")
    f.write("%s," %entry1.get())
    f.write("%s," %entry2.get())
    f.write("%s," %entry3.get())
    f.write("%s," %entry4.get())
    f.write("%s," %entry5.get())
    f.write("%s" %entry6.get())
    f.close()

    with open("c:\\Users\\com\\Desktop\\대학\\과제\\파이썬과제\\새 폴더\\grade.txt", "w") as fs:
        fs.write("학번: %s" %entry1.get())
        fs.write(",이름: %s," %entry2.get())
        fs.write("PYTHON: ")
        fs.write(py_grade)
        fs.write(",c 언어:")
        fs.write(c_grade)
        fs.write(",HTML5:")
        fs.write(html_grade)
        fs.write(",D/B:")
        fs.write(DB_grade)
        fs.close()
    

def retry():  
    entry1.delete(0, len(entry1.get()))
    entry2.delete(0, len(entry2.get()))
    entry3.delete(0, len(entry3.get()))
    entry4.delete(0, len(entry4.get()))
    entry5.delete(0, len(entry5.get()))
    entry6.delete(0, len(entry6.get()))

    
label1=Label(window, width=10, text="학      번")
label2=Label(window, width=10, text="이      름")
label3=Label(window, width=10, text="파이썬성적")
label4=Label(window, width=10, text="C언어 성적")
label5=Label(window, width=10, text="HTML5 성적")
label6=Label(window, width=10, text="D/B   성적")
label7=Label(window, width=10)
label8=Label(window, width=10)
label9=Label(window, width=10)
label10=Label(window, width=10)
label11=Label(window, width=10, text="학      점")
             
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)
label4.grid(row=3, column=0)
label5.grid(row=4, column=0)
label6.grid(row=5, column=0)
label7.grid(row=2, column=2)
label8.grid(row=3, column=2)
label9.grid(row=4, column=2)
label10.grid(row=5, column=2)
label11.grid(row=1, column=2)





entry1= Entry(window, width=20)
entry2= Entry(window, width=20)
entry3= Entry(window, width=20)
entry4= Entry(window, width=20)
entry5= Entry(window, width=20)
entry6= Entry(window, width=20)


entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
entry4.grid(row=3, column=1)
entry5.grid(row=4, column=1)
entry6.grid(row=5, column=1)


button1= Button(window, width=10, text = "저장", command=grade)
button2= Button(window, width=10, text = "입력 취소", command = retry)

button1.grid(row=6, column=0)
button2.grid(row=6, column=1)

window.mainloop()
