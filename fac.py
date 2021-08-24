from tkinter import * 
import math

window = Tk()

def factorial():

    

    number = math.factorial(float(value_0.get()))
    

    

    t1.delete("1.0",END)
    t1.insert(END,number)

e1 = Label(window,text="Enter your number : ")

value_0 = StringVar()

e2 = Entry(window,textvariable=value_0)
e3 = Label(window,text='Factorial : ')

t1 = Text(window, height=1 , width=15)

b1 = Button(window, text='Convert' ,bg='red' , command=factorial)

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)

t1.grid(row=1 , column=1)

b1.grid(row=0, column=2)

l1 = Label(window,text="Dedicated to Virgil_H06", bd=1 , relief="solid", font="Arial" ,  anchor=S) #BRADHITC.TTF

txt = Label(window, text="Dedicated to Virgil_H06" , font="BRUSHSCI.TTF" , anchor=S  )

txt.grid(column=1)







window.title('Factorial Calculator')
window.iconbitmap("i.ico")

window.geometry('400x100')

window.resizable(0,0)

window.mainloop()


