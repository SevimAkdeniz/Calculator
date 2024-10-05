from tkinter import * 


# Main

master = Tk()
master.title("Welcome to Sevim's Simple Calculator")


e = Entry(master,width=35,borderwidth=10,bg="light blue")
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


# functions

def button_select(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))

def button_c():
    e.delete(0,END)

def button_add(): 
    global f_num, operation
    f_num = float(e.get())
    e.delete(0,END)
    operation = "add"

def button_ex():
   global f_num,operation
   f_num = float(e.get())
   e.delete(0,END)
   operation = "ex"

def button_multi():
   global f_num,operation
   f_num = float(e.get())
   e.delete(0,END)
   operation = "multi"

def button_divi():
   global f_num,operation
   f_num = float(e.get())
   e.delete(0,END)
   operation = "divi"

def button_e():
    global f_num, operation
    if operation == "add":
     second_number =int(e.get())
     e.delete(0,END)
     e.insert(0,f_num + second_number)


    elif operation == "ex":
      second_number =e.get()
      e.delete(0,END)
      e.insert(0,float(f_num) - float(second_number))

    elif operation == "multi":
      second_number =e.get()
      e.delete(0,END)
      e.insert(0,float(f_num) * float(second_number))

    elif operation == "divi":
      second_number =e.get()
      e.delete(0,END)
      e.insert(0,float(f_num) / float(second_number))
   
# Buttons

button_1 = Button(master,text="1",padx=40,pady=20,command=lambda: button_select(1),bg="light blue")
button_2 = Button(master,text="2",padx=40,pady=20,command=lambda: button_select(2),bg="light blue")
button_3 = Button(master,text="3",padx=40,pady=20,command=lambda: button_select(3),bg="light blue")
button_4 = Button(master,text="4",padx=40,pady=20,command=lambda: button_select(4),bg="light blue")
button_5 = Button(master,text="5",padx=40,pady=20,command=lambda: button_select(5),bg="light blue")
button_6 = Button(master,text="6",padx=40,pady=20,command=lambda: button_select(6),bg="light blue")
button_7 = Button(master,text="7",padx=40,pady=20,command=lambda: button_select(7),bg="light blue")
button_8 = Button(master,text="8",padx=40,pady=20,command=lambda: button_select(8),bg="light blue")
button_9 = Button(master,text="9",padx=40,pady=20,command=lambda: button_select(9),bg="light blue")
button_0 = Button(master,text="0",padx=40,pady=20,command=lambda: button_select(0),bg="light blue")

button_ad = Button(master,text="+",padx=39,pady=20,command=lambda: button_add(),bg="light blue")
button_equal = Button(master,text="=",padx=91,pady=20,command=lambda:button_e(),bg="light blue")
button_clear = Button(master,text="clear",padx=79,pady=20,command= lambda:button_c(),bg="light blue")
button_extraction = Button(master,text="-",padx=40,pady=20,command= lambda:button_ex(),bg="light blue")
button_multiplication = Button(master,text="X",padx=40,pady=20,command= lambda:button_multi(),bg="light blue")
button_division = Button(master,text="/",padx=40,pady=20,command= lambda:button_divi(),bg="light blue")

# Grids

button_multiplication.grid(row=6,column=1)
button_division.grid(row=6,column=2)
button_extraction.grid(row=6,column=0)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)

button_ad.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)

# and done...

master.mainloop()