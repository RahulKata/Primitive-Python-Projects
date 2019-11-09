from tkinter import *
import pandas  as pd


data =[]
def getvals():
    lst =0
    print("Submitting Form!")
    lst = [namevalue.get(),agevalue.get(),phonevalue.get(),gendervalue.get(),paymentvalue.get(), fitcheckval.get()]
    data.append(lst)
  #  with open("records.txt", "w") as f:
   #    f.write(f"{namevalue.get(), agevalue.get(), phonevalue.get(), gendervalue.get(),paymentvalue.get(), fitcheckval.get()}\n")


root = Tk()

root.geometry("300x233")

#heading
Label(root, text="Welcome to Rahul_Gym", pady="10", font="comicsansms 13",
      bg="black",fg="white").grid(column=3)

#text for our form
name = Label(root,text="Name").grid(row=2,column=2)
age = Label(root,text="Age").grid(row=3,column=2)
phone = Label(root,text="Phone").grid(row=4,column=2)
gender = Label(root,text="Gender").grid(row=5,column=2)
paymentmode = Label(root,text="Payment Mode").grid(row=6,column=2)

#tkinter variables for storing entries
namevalue = StringVar()
agevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
paymentvalue = StringVar()
fitcheckval = IntVar()

#entries for our form
nameentry = Entry(root, textvariable= namevalue)
ageentry = Entry(root, textvariable= agevalue)
phoneentry = Entry(root, textvariable= phonevalue)
genderentry = Entry(root, textvariable= gendervalue)
paymententry = Entry(root, textvariable= paymentvalue)

nameentry.grid(row=2,column=3)
ageentry.grid(row=3,column=3)
phoneentry.grid(row=4,column=3)
genderentry.grid(row=5,column=3)
paymententry.grid(row=6,column=3)

#checkbox
fitcheck = Checkbutton(text="Is your lifestyle a fit one?",variable=fitcheckval)
fitcheck.grid(row =7,column=3)


Button(text="Submit",command=getvals).grid(row=8,column=3)

root.mainloop()

csv_file = open('records.csv','w',newline='')
df = pd.DataFrame(data,columns=['Name','Age','Phone_Number','Gender','Payment_Mode','Fit lifestyle'])
df.to_csv("records.csv")