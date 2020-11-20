from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Logins")
root.geometry("500x330")
root.config(background='blue')

#Functions of buttons
def login():
    usp = {"cossie":"khumalo","prince":"moahlodi", "praise":"judah"}
    usr = us_entry.get()
    psw = p_entry.get()
    if (usr,psw)in usp.items():
        messagebox.showinfo("INFO", "12th of November")
        root.withdraw()
        import handling
        handling.verify()
    else:
        messagebox.showinfo("INFO", "Oops try again!!!")
        us_entry.delete(0, END)
        p_entry.delete(0, END)

#labels
instruction_label = Label(root, text = 'Please enter login details', font = 40)
username_label = Label(root, text = 'Username: ')
password_label = Label(root, text = 'Password: ')

#entry boxes
us_entry = Entry(root)
p_entry = Entry(root, show = '*')

#buttons
login_btn = Button(root, text = 'Login', command=login)

#Placements
instruction_label.place(x=90, y=5)
username_label.place(x=100, y=55)
password_label.place(x=100, y=105)
us_entry.place(x=100, y=75)
p_entry.place(x=100, y=125)
login_btn.place(x=150, y=160)


root.mainloop()
