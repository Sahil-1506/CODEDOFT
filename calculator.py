import  customtkinter
from tkinter import*
from tkinter import messagebox



app = customtkinter.CTk()
app.title("Calculator")
app.geometry("250x370")
app.config(bg="green")


font1=("Arial",30,"bold")


i=0
equation=""

def show(value):
    global i
    global equation
    if value=="%":
        value="/100"
    equation+=value
    result_entry.insert(i,value)
    i=i+1

def clear():
    global equation
    result_entry.delete(0,END)
    equation=""

def calculate():
    try:
        global equation
        result=""
        result=eval(equation)
        clear()
        result_entry.insert(0,result)
    except:
        messagebox.showerror(title="Error",message="Please Enter a Valid Number!!")
        clear()

 



result_entry=customtkinter.CTkEntry(app,font=font1,placeholder_text="Enter here",width=250,height=50,fg_color="#ffffff",border_color="#000000")
result_entry.place(x=0,y=10)
Button1=customtkinter.CTkButton(app,command=clear,text="C",font=font1,width=50,height=2,fg_color="#b5520b",hover_color="red")
Button1.place(x=10,y=80)

Button2=customtkinter.CTkButton(app,command=lambda:show("%"),text="%",font=font1,width=50,height=2,fg_color="#b5520b",hover_color="#78d220")
Button2.place(x=70,y=80)

Button3=customtkinter.CTkButton(app,command=lambda:show("/"),text="/",font=font1,width=50,height=2,fg_color="#b5520b",hover_color="#78d220")
Button3.place(x=130,y=80)

Button4=customtkinter.CTkButton(app,command=lambda:show("*"),text="x",font=font1,width=50,height=2,fg_color="#b5520b",hover_color="#78d220")
Button4.place(x=190,y=80)

Button5=customtkinter.CTkButton(app,command=lambda:show("7"),text="7",font=font1,width=50,height=2,fg_color="#2e2a27",hover_color="#2e2a27")
Button5.place(x=10,y=140)

Button6=customtkinter.CTkButton(app,command=lambda:show("8"),text="8",font=font1,width=50,height=2,fg_color="#2e2a27",hover_color="#2e2a27")
Button6.place(x=70,y=140)

Button7=customtkinter.CTkButton(app,command=lambda:show("9"),text="9",font=font1,width=50,height=2,fg_color="#2e2a27",hover_color="#2e2a27")
Button7.place(x=130,y=140)

Button8=customtkinter.CTkButton(app,command=lambda:show("+"),text="+",font=font1,width=50,height=2,fg_color="#b5520b",hover_color="#78d220")
Button8.place(x=190,y=140)

Button9=customtkinter.CTkButton(app,command=lambda:show("4"),text="4",font=font1,width=50,height=2,fg_color="#2e2a27",hover_color="#2e2a27")
Button9.place(x=10,y=200)

Button10=customtkinter.CTkButton(app,command=lambda:show("5"),text="5",font=font1,width=50,height=2,fg_color="#2e2a27",hover_color="#2e2a27")
Button10.place(x=70,y=200)

Button11=customtkinter.CTkButton(app,command=lambda:show("6"),text="6",font=font1,width=50,height=2,fg_color="#2e2a27",hover_color="#2e2a27")
Button11.place(x=130,y=200)

Button12=customtkinter.CTkButton(app,command=lambda:show("-"),text="-",font=font1,width=50,height=2,fg_color="#b5520b",hover_color="#78d220")
Button12.place(x=190,y=200)

Button13=customtkinter.CTkButton(app,command=lambda:show("0"),text="0",font=font1,width=50,height=2,fg_color="#2e2a27",hover_color="#2e2a27")
Button13.place(x=10,y=260)

Button14=customtkinter.CTkButton(app,command=lambda:show("1"),text="1",font=font1,width=50,height=2,fg_color="#2e2a27",hover_color="#2e2a27")
Button14.place(x=70,y=260)

Button15=customtkinter.CTkButton(app,command=lambda:show("2"),text="2",font=font1,width=50,height=2,fg_color="#2e2a27",hover_color="#2e2a27")
Button15.place(x=130,y=260)

Button16=customtkinter.CTkButton(app,command=lambda:show("3"),text="3",font=font1,width=50,height=2,fg_color="#2e2a27",hover_color="#2e2a27")
Button16.place(x=190,y=260)

Button17=customtkinter.CTkButton(app,command=lambda:show("."),text=".",font=font1,width=50,height=2,fg_color="#2e2a27",hover_color="#78d220")
Button17.place(x=10,y=320)

Button18=customtkinter.CTkButton(app,command=calculate,text="=",font=font1,width=170,height=2,fg_color="#b5520b",hover_color="#3df0fd")
Button18.place(x=70,y=320)


app.mainloop()
