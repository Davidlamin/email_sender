from tkinter import *
import smtplib
import re

def login():
    if validate_login():
        username = entry1.get()
        password = entry2.get()
        global server
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(username, password)
        f2.pack_forget()
        btn2.grid()
        label4['text'] = "Logged In!"
        f1.pack_forget()
        f3.pack()
        label9.grid_remove()

def send_mail():
    if validate_message():
        label9.grid_remove()
        receiver = enrty3.get()
        subject = entry4.get()
        msgbody = enrty5.get()
        msg = "From " + username + "\n" + "To:" + receiver + "\n" + "Subject:" + \
              subject + "\n" + msgbody
        try:
            server.sendmail(username, receiver, msg)
            label9.grid()
            label9['text'] = "Mail Sent!"
        except Exception as e:
            label9.grid()
            label9['text'] = "Error in Sending Your Email"

def logout():
    try:
        server.quit()
        f3.pack_forget()
        f2.pack()
        label4.grid()
        label4['text'] = "Logged Out succesfully"
        btn2.grid_remove()
        f1.pack()
        enrty2.delete(0, END)
    except Exception as e:
        label4['text'] = "Error in Logout"

def validate_login():
    email_text = entry1.get()
    pass_text = entry2.get()
    if(email_text == "") or (pass_text == ""):
        label4.grid()
        label4['text'] = "Fill all Fields"
        btn2.grid_remove()
        return False
    else:
        EMAIL_REGEX = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")
        if not EMAIL_REGEX.match(email_text):
            label4.grid()
            label4['text'] = "Enter a valid Email Address"
            btn2.grid_remove()
            return False
    return True

def validate_message():
    email_text = enrty3.get()
    sub_text = entry4.get()
    msg_text = enrty5.get()
    if (email_text == "") or (sub_text == "") or (msg_text == ""):
        label9.grid()
        label9['text'] = "Fill in all the Places"
        return False
    else:
        EMAIL_REGEX = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")
        if not EMAIL_REGEX.match(email_text):
            label9.grid()
            label9['text'] = "Enter a Valid Email Address"
            return False
        elif(len(sub_text) < 3) or (len(msg_text) < 3):
            label9.grid()
            label9['text'] = "Enter atleast 3 Characters"
            return False
    return True

root = Tk()
root.title('Email Application')

f1 = Frame(root, width=1000, height=800)
f1.pack(side=TOP)

label1 = Label(f1, width=25, text='Enter your Credentials', font=("Calibri 18 bold"))
label1.grid(row=0, columnspan=3, pady=10, padx=10)

label2 = Label(f1, text="Email").grid(row=1, sticky=E, pady=5, padx=10)
label3 = Label(f1, text="Password").grid(row=2, sticky=E, pady=5, padx=10)

entry1 = Entry(f1)
entry2 = Entry(f1, show="*")

entry1.grid(row=1, column=1, pady=5)
entry2.grid(row=2, column=1)

btn1 = Button(f1, text="Login", width=10, bg="black", fg="white", command=login)
btn1.grid(row=3, columnspan=3, pady=10)

f2 = Frame(root)
f2.pack(side=TOP, expand=NO, fill=NONE)

label4 = Label(f2, width=20, bg="cyan", fg="red", text="Log in Success", font=("Calibri 12 bold"))
label4.grid(row=0, column=0, columnspan=2, pady=5)

btn2 = Button(f2, text="Logout", bg="black", fg="white", command=logout)
btn2.grid(row=0, column=4, sticky=E, pady=10, padx=(5, 0))

f3 = Frame(master=root)
f3.pack(side=TOP, expand=NO, fill=NONE)

label5 = Label(f3, width=20, text="Compose Email", font=("Calibri 18 bold"))
label5.grid(row=0, columnspan=3, pady=10)

label6 = Label(f3, text="To").grid(row=1, sticky=E, pady=5)
label7 = Label(f3, text="Subject").grid(row=2, sticky=E, pady=5)
label8 = Label(f3, text="Message").grid(row=3, sticky=E)

enrty3 = Entry(f3)
entry4 = Entry(f3)
enrty5 = Entry(f3)

enrty3.grid(row=1, column=1, pady=5)
entry4.grid(row=2, column=1, pady=5)
enrty5.grid(row=3, column=1, pady=5, rowspan=3, ipady=10)

btn3 = Button(f3, text="Send Mail", width=10, bg="black", fg="white", command=send_mail)
btn3.grid(row=6, columnspan=3, pady=10)

label9 = Label(f3, width=20, fg="white", bg="black", font=("Calibri 18 bold"))
label9.grid(row=7, columnspan=3, pady=5)

root.mainloop()
