from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error!"

        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root = Tk()
root.title("My_Calculator")
root.geometry("544x600")
root.wm_iconbitmap("favicon.ico")

# =============================================================================
# add your custom icon in place of "favicon.ico"
# =============================================================================

scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue,font="Helvetica 40 bold",bd=10,bg="lightgreen",fg="maroon",relief=RIDGE)
screen.pack(fill=X,ipadx=10,padx=20,pady=20)

frame1 = Frame(root, bg="darkblue",relief=SUNKEN,bd=3)
for i in range(9,6,-1):
    button1 = Button(frame1,bg="maroon",fg="gold",text=f"{i}",font="lucida 20 bold",padx=18,pady=3,bd=2)
    button1.pack(side=LEFT,padx=10,pady=3)
    button1.bind("<Button-1>",click)
frame1.pack()

frame1 = Frame(root, bg="darkblue",relief=SUNKEN,bd=3)
for i in range(6,3,-1):
    button1 = Button(frame1,bg="maroon",fg="gold",text=f"{i}",font="lucida 20 bold",padx=18,pady=3,bd=2)
    button1.pack(side=LEFT,padx=10,pady=3)
    button1.bind("<Button-1>",click)
frame1.pack()

frame1 = Frame(root, bg="darkblue",relief=SUNKEN,bd=3)
for i in range(3,0,-1):
    button1 = Button(frame1,bg="maroon",fg="gold",text=f"{i}",font="lucida 20 bold",padx=18,pady=3,bd=2)
    button1.pack(side=LEFT,padx=10,pady=3)
    button1.bind("<Button-1>",click)
frame1.pack()

frame1 = Frame(root, bg="darkblue",relief=SUNKEN,bd=3)
button1 = Button(frame1, bg="maroon", fg="gold", text="+", font="lucida 20 bold", padx=17, pady=3, bd=2)
button1.pack(side=LEFT, padx=12, pady=3)
button1.bind("<Button-1>", click)
button1 = Button(frame1, bg="maroon", fg="gold", text="0", font="lucida 20 bold", padx=17, pady=3, bd=2)
button1.pack(side=LEFT, padx=12, pady=3)
button1.bind("<Button-1>", click)
button1 = Button(frame1, bg="maroon", fg="gold", text="-", font="lucida 20 bold", padx=17, pady=3, bd=2)
button1.pack(side=LEFT, padx=12, pady=3)
button1.bind("<Button-1>", click)
frame1.pack()

frame1 = Frame(root, bg="darkblue",relief=SUNKEN,bd=3)
button1 = Button(frame1, bg="maroon", fg="gold", text="%", font="lucida 20 bold", padx=17, pady=3, bd=2)
button1.pack(side=LEFT, padx=10, pady=3)
button1.bind("<Button-1>", click)
button1 = Button(frame1, bg="maroon", fg="gold", text="=", font="lucida 20 bold", padx=17, pady=3, bd=2)
button1.pack(side=LEFT, padx=10, pady=3)
button1.bind("<Button-1>", click)
button1 = Button(frame1, bg="maroon", fg="gold", text="*", font="lucida 20 bold", padx=17, pady=3, bd=2)
button1.pack(side=LEFT, padx=10, pady=3)
button1.bind("<Button-1>", click)
frame1.pack()

frame1 = Frame(root, bg="darkblue",relief=SUNKEN,bd=3)
button1 = Button(frame1, bg="maroon", fg="gold", text="C", font="lucida 20 bold", padx=18, pady=3, bd=2)
button1.pack(side=LEFT, padx=10, pady=3)
button1.bind("<Button-1>", click)
button1 = Button(frame1, bg="maroon", fg="gold", text="/", font="lucida 20 bold", padx=18, pady=3, bd=2)
button1.pack(side=LEFT, padx=10, pady=3)
button1.bind("<Button-1>", click)
frame1.pack()

root.mainloop()
