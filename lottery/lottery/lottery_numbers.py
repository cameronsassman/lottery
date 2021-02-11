from random import sample
from tkinter import *
from tkinter import messagebox
from datetime import *
from PIL import Image


window = Tk()
window.geometry("550x200")
window.title("Ithuba National Lottery")
window.configure(background='yellow')

def get_numbers():
    try:
        num1 = int(txt1.get())
        num2 = int(txt2.get())
        num3 = int(txt3.get())
        num4 = int(txt4.get())
        num5 = int(txt5.get())
        num6 = int(txt6.get())
        my_nums = [num1, num2, num3, num4, num5, num6]
        return my_nums
    except ValueError:
        messagebox.showerror("error", "please enter digits")



def win():
    random = sample(range(1, 49), 7)
    random.sort()
    lb.config(text=random[0])
    lb2.config(text=random[1])
    lb3.config(text=random[2])
    lb4.config(text=random[3])
    lb5.config(text=random[4])
    lb6.config(text=random[5])

    if get_numbers():
        btn1.config(state='normal')
    else:
        btn1.config(state='disabled')

#comparing get_numbers entries to random nuber generator
    matches = 0
    for i in get_numbers():
        if i in random:
            matches += 1

    if int(matches) == 6:
        messagebox.showinfo("result", "R10 000 000.00")
        f = open(r"/lottery/lottery.txt", "a+")
        f.write("amount recieved: R10 000 000.00" + "\n")
        f.close()
    if int(matches) == 5:
        messagebox.showinfo("result", "R8 584.00")
        f = open(r"/lottery/lottery.txt", "a+")
        f.write("amount recieved: R8 584.00" + "\n")
        f.close()
    if int(matches) == 4:
        messagebox.showinfo("result", "R2 384.00")
        f = open(r"/lottery/lottery.txt", "a+")
        f.write("amount recieved: R2 384.00" + "\n")
        f.close()
    if int(matches) == 3:
        messagebox.showinfo("result", "R100.50")
        f = open(r"/lottery/lottery.txt", "a+")
        f.write("amount recieved: R100.50" + "\n")
        f.close()
    if int(matches) == 2:
        messagebox.showinfo("result", "R20.00")
        f = open(r"/lottery/lottery.txt", "a+")
        f.write("amount recieved: R20.00" + "\n")
        f.close()
    if int(matches) == 1:
        messagebox.showinfo("result", "R0")
        f = open(r"/lottery/lottery.txt", "a+")
        f.write("amount recieved: R0" + "\n")
        f.close()
    if int(matches) == 0:
        messagebox.showinfo("result", "R0")
        f = open(r"/lottery/lottery.txt", "a+")
        f.write("amount recieved: R0" + "\n")
        f.close()


number1 = StringVar()
number2 = StringVar()
number3 = StringVar()
number4 = StringVar()
number5 = StringVar()
number6 = StringVar()

frame = Frame(window)

txt1 = Entry(frame, textvariable=number1, bd=5, insertwidth=1, justify='center', width=5)
txt1.pack(side=LEFT)
txt2 = Entry(frame, textvariable=number2, bd=5, insertwidth=1, justify='center', width=5)
txt2.pack(side=LEFT)
txt3 = Entry(frame, textvariable=number3, bd=5, insertwidth=1, justify='center', width=5)
txt3.pack(side=LEFT)
txt4 = Entry(frame, textvariable=number4, bd=5, insertwidth=1, justify='center', width=5)
txt4.pack(side=LEFT)
txt5 = Entry(frame, textvariable=number5, bd=5, insertwidth=1, justify='center', width=5)
txt5.pack(side=LEFT)
txt6 = Entry(frame, textvariable=number6, bd=5, insertwidth=1, justify='center', width=5)
txt6.pack(side=LEFT)


btn1 = Button(window, text="check winnings", width=20, fg="black", bg="white", command=win)


frame2 = Frame(window)

lb = Label(frame2, bd=5, width=4, bg="white", relief="sunken")
lb.pack(side=LEFT)
lb2 = Label(frame2, bd=5, width=5, bg="white", relief="sunken")
lb2.pack(side=LEFT)
lb3 = Label(frame2, bd=5, width=5, bg="white", relief="sunken")
lb3.pack(side=LEFT)
lb4 = Label(frame2, bd=5, width=5, bg="white", relief="sunken")
lb4.pack(side=LEFT)
lb5 = Label(frame2, bd=5, width=5, bg="white", relief="sunken")
lb5.pack(side=LEFT)
lb6 = Label(frame2, bd=5, width=5, bg="white", relief="sunken")
lb6.pack(side=LEFT)


canvas = Canvas(window, width=120, height=100, background='yellow')
canvas.pack(side=TOP)
img = ImageTk.PhotoImage(Image.open("ithuba_national_lottery.png"))
canvas.create_image(20, 20, anchor=NW, image=img)
date = datetime.now()
dlb = Label(window)
dlb.pack(side=TOP)
dlb.config(text="Date: " + date.strftime("%d/%m/%y %H:%M"), background='yellow')


frame.pack(side=TOP)
btn1.pack(side=TOP)

frame2.pack(side=BOTTOM)
window.mainloop()
