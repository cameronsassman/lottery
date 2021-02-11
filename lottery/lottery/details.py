from tkinter import *
from tkinter import messagebox
from datetime import *
from PIL import ImageTk

window = Tk()
window.geometry("550x200")
window.title("Ithuba national lottery")
window.configure(background='yellow')


canvas = Canvas(window, width=120, height=100, background='yellow')
canvas.grid(row=0, column=3)
img = ImageTk.PhotoImage(Image.open("ithuba_national_lottery.png"))
canvas.create_image(20, 20, anchor=NW, image=img)

label_1 = Label(window, text="name", width=20, font=10, background='yellow')
label_1.grid(row=1, column=0)

entry1 = Entry(window, width=10)
entry1.grid(row=2, column=0)

label_2 = Label(window, text="enter age.", width=20, font=10, background='yellow')
label_2.grid(row=1, column=2)

entry2 = Entry(window, width=10)
entry2.grid(row=2, column=2)

label_3 = Label(window, text="surname", width=20, font=10, background='yellow')
label_3.grid(row=1, column=3)


entry3 = Entry(window, width=10)
entry3.grid(row=2, column=3)

date = datetime.now()
dlb = Label(window)
dlb.grid(row=0, column=0)
dlb.config(text="Date: " + date.strftime("%d/%m/%y %H:%M"), background='yellow')

def ages():
    f = open(r"/lottery/lottery.txt", "w+")
    f.write("Name:"+str(entry1.get()) + "\n"+
            "Surname:"+str(entry3.get()+"\n"+
            "Age:"+str(entry2.get()+"\n")))
    f.close()
    try:
        age = int(entry2.get())
        if age >= 18:
            messagebox.showinfo("processing", "eligible to play the thuba National Lottery ")
            window.withdraw()
            import lottery_numbers
            lottery_numbers.status

        else:
            messagebox.showinfo("processing", "unable to play thuba National Lottery due to being underage")
    except ValueError:
        messagebox.showerror('error', "please enter details before moving forward")

btn = Button(window, text="Login", width=20, fg="black", bg="white", command=ages)
btn1 = Button(window, text="quit", width=20, fg="black", bg="white", command=window.quit)




btn.grid(row=5, column=2)
btn1.grid(row=15, column=2)
window.mainloop()