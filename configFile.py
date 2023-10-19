from getpass import getuser
from os import system
from tkinter import *
from PIL import ImageTk,Image 
from tkinter import ttk
from tkinter import messagebox as mb
from shutil import copyfile



def add_startup():
    if var.get() == "Select file type":
        mb.showerror("what?!","please select file type or frequency you want !")

    else:
        button_1.config(bg="green")
        username = getuser()
        startup_path = r"C:\Users\%s\\AppData\Roaming\Microsoft\\Windows\\Start Menu\Programs\\Startup\ "%(username)
        if str(var.get()).lower() == 'exe':
            copyfile("run.exe",startup_path)
            system("copy run.exe %s"%(startup_path))
        else:
            copyfile("run.py",startup_path)
            system("copy run.py %s"%(startup_path))



def add_char_frequency():
    if var1.get() == "Select frequency":
        mb.showerror("what?!","please select file type or frequency you want !")

    else:
        button_2.config(bg="green")
        frequency_value = var1.get()
        print(frequency_value)
        with open("conf.cf","a") as file:
            file.writelines("char:%i\n"%(int(frequency_value)))
            file.close()


def add_key_frequency():
    if var2.get() == "Select frequency":
        mb.showerror("what?!","please select file type or frequency you want !")

    else:
        button_3.config(bg="green")
        frequency_value1 = var2.get()
        print(frequency_value1)
        with open("conf.cf","a") as file:
            file.writelines("key:%i\n"%(int(frequency_value1)))
            file.close()


config_status = []
def process_program_config():
    with open("conf.cf","a") as file:
        for txt in file.readlines():
            txt=txt.split(":")
            print(txt[1])
    
#
#
#
#
#
#
window = Tk()
window.title("-- Config File --")
window.geometry("420x516")


bg_image = Image.open("paint1.jpg") # add background image to program
bg_img = ImageTk.PhotoImage(bg_image)

label_bg = Label(window,image=bg_img)
label_bg.place(x=0,y=0)


var = StringVar(window,"Select file type") # default
var1 = StringVar(window,"Select frequency") # default
var2 = StringVar(window,"Select frequency") # default

button_1 = Button(window,text="Add startup",font=("tahoma",10),bd=1,bg="orange",command=add_startup)
button_1.grid(column=1,row=1,padx=20,pady=150)

comboBox = ttk.Combobox(window,textvariable=var,state='readonly')
comboBox['values']=("Python","Exe")
comboBox.grid(column=2,row=1,padx=20,pady=120)


# ***
button_2 = Button(window,text="Char sound",font=("tahoma",10),bd=1,bg="yellow",command=add_char_frequency)
button_2.grid(column=1,row=2) # change char keys signal 

comboBox1 = ttk.Combobox(window,textvariable=var1,state='readonly')
frequency_values = []
for value in range(37,32000):
    frequency_values.append(str(value))
comboBox1['values']=(frequency_values)
comboBox1.grid(column=2,row=2,padx=0,pady=0)


# ***
button_3 = Button(window,text="Key sound",font=("tahoma",10),bd=1,bg="yellow",command=add_key_frequency)
button_3.grid(column=1,row=3,pady=30)

comboBox2 = ttk.Combobox(window,textvariable=var2,state='readonly')
frequency_values = []
for value in range(37,32000):
    frequency_values.append(str(value))
comboBox2['values']=(frequency_values)
comboBox2.grid(column=2,row=3,padx=0,pady=0)

#
button_4 = Button(window,text="Process",font=("tahoma",20),bd=1,bg="blue",fg="white",command=process_program_config)
button_4.grid(column=1,row=4,padx=20)


# loop in program GUI
window.mainloop()
