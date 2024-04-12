from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
#------------------password Generator--------------------#
def pd_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letter = [random.choice(letters) for i in range(random.randint(5,7)) ]
    password_symbol = [random.choice(symbols) for i in range(random.randint(2,4))]
    password_number = [random.choice(numbers) for i in range(random.randint(2,4))]

    password = password_letter + password_number + password_symbol
    #print(password)
    random.shuffle(password)
    #print(password)

    passd = "".join(password)
    pd_entry.insert(0,passd)
    pyperclip.copy(passd)
    



#------------------Save password--------------------#
def save():
    a = website_entry.get()
    b = email_entry.get()
    c = pd_entry.get()
    new_data = {
        a:{
            "email":b,
            "password":c
        }
    }
    if len(a)==0 or len(b)==0 or len(c)==0 :
        messagebox.showinfo(title="Empty", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("./data.json","r") as datafile:
                data = json.load(datafile)
                
        except FileNotFoundError:
            with open("./data.json","w") as datafile:
                json.dump(new_data,datafile,indent=4)
        else:
            is_ok = messagebox.askokcancel(title="Confirm", message=f"These are the details entered:\nWebsite:{a} \nEmail:{b}\nPassword:{c} \n Is it ok to save?")
            if is_ok:
                data.update(new_data)
                with open("./data.json","w") as datafile:
                    json.dump(data,datafile,indent=4)
            
        finally:
            website_entry.delete(0,END)
            email_entry.delete(0,END)
            pd_entry.delete(0,END)
#---------------------Find Password-----------------#
def find_password():
    website = website_entry.get()
    try:
        with open("./data.json","r") as datafile:
            data = json.load(datafile)      
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No details exists")
    else:
        if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title="Info", message=f"These are the details:\nWebsite:{website} \nEmail:{email}\nPassword:{password} \n")
        else:
            messagebox.showinfo(title="Not found", message=f"No details for '{website}' exists")
    







#---------------------UI setup-----------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=30,pady=30,bg="white")

#Adding the logo
canvas = Canvas(width=200,height=200,bg="white",highlightthickness=0)
pd_image = PhotoImage(file="./logo.png")
canvas.create_image(130,100,image=pd_image)
canvas.grid(row=0,column=1)

#Labels
label = Label(text="Website:",bg="white")
label.grid(row=1,column=0)

label = Label(text="Email: ",bg="white")
label.grid(row=2,column=0)

label = Label(text="Password:",bg="white")
label.grid(row=3,column=0)


#Entry
website_entry = Entry(width=33)
website_entry.grid(row=1,column=1)
website_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"Hari@gmail.com")

pd_entry = Entry(width=32)
pd_entry.grid(row=3,column=1)


#Buttons
search = Button(text="Search",width=14,command=find_password)
search.grid(row=1,column=2,columnspan=3)

Pd_generator = Button(text="Generator Password",width=15,command=pd_generator)
Pd_generator.grid(row=3,column=2,columnspan=2)

add = Button(text="Add",width=40,command=save)
add.grid(row=4,column=1,columnspan=2)

window.mainloop()




