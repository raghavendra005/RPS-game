#basic digital clock



from tkinter import *
import time

def update():
    time_strng = time.strftime("%I:%M:%S")
    time_label.config(text=time_strng)

    day_strng = time.strftime("%B %d %Y")
    day_label.config(text=day_strng)

    window.after(1000,update)


window=Tk()

photo = PhotoImage(file='c1010ec3a4932de0663be16b37873f93.png')
time_label = Label(window,font=("Arial" , 50) ,
                   fg="black" ,
                   bg="black" ,
                   image=photo,
                   compound='center')

time_label.pack()
day_label = Label(window,font=("Ink free" , 50) ,
                   fg="#00FF00" ,
                   bg="white")
day_label.pack()

update()


window.mainloop()
