import tkinter as tk
from tkinter import ttk, messagebox
from typing import Self
import pymysql
from PIL import Image, ImageTk


class DoctorAppointment:
    def __init__(self, main):
        self.root = main
        self.play_icon = Image.open(r"C:\Users\DELL\Downloads\signupicon.png")
        self.play_icon = self.play_icon.resize((100, 40))
        self.play_icon_tk = ImageTk.PhotoImage(self.play_icon)
        self.login_screen()

    def clear(self):
        self.userentry.delete(0, tk.tk.END)
        self.passentry.delete(0, tk.tk.END)

    def close(self):
        win.destroy()

    def login(self):
        if self.user_name.get() == "" or self.password.get() == "":
            messagebox.showerror(
                "Error", "Enter User Name And Password", parent=win)
        else:
            con = pymysql.connect(
                host="localhost", user="root", password="", database="docterapp")
            cur = con.cursor()

            cur.execute("select * from user_information where username=%s and password = %s",
                        (self.user_name.get(), self.password.get()))
            row = cur.fetchone()

            if row == None:
                messagebox.showerror(
                    "Error", "Invalid User Name And Password", parent=win)

            else:
                messagebox.showinfo(
                    "Success", "Successfully Login", parent=win)
                self.close()
                self.deshboard()
            con.close()

    def login_screen(self):
        self.user_name = tk.StringVar()
        self.password = tk.StringVar()

        self.userentry = tk.Entry(win, width=40, textvariable=self.user_name)
        self.userentry.focus()
        self.userentry.place(x=200, y=223)

        self.passentry = tk.Entry(win, width=40, show="*",
                                  textvariable=self.password)
        self.passentry.place(x=200, y=260)

        # heading label
        heading = tk.Label(win, text="Login",
                           font='Verdana 25 bold', bg="#303030", fg="white")
        heading.place(x=80, y=150)

        username = tk.Label(win, text="User Name :",
                            font='Verdana 10 bold', bg="#303030", fg="white")
        username.place(x=80, y=220)

        userpass = tk.Label(win, text="Password :",
                            font='Verdana 10 bold', bg="#303030", fg="white")
        userpass.place(x=80, y=260)

        # button login and clear

        btn_login = tk.Button(
            win, text="Login", font='Verdana 10 bold', command=self.login, bg="green", fg="white", relief="groove", overrelief='groove')
        btn_login.place(x=200, y=293)

        btn_login = tk.Button(
            win, text="Clear", font='Verdana 10 bold', command=self.clear, bg="red", fg="white", relief="groove", overrelief='groove')
        btn_login.place(x=260, y=293)

        sign_up_btn = tk.Button(win, image=self.play_icon_tk, bg="skyblue",
                                fg="#303030", relief="groove", overrelief='groove', command=self.signup)
        sign_up_btn.place(x=350, y=20)

    def signup(self):
        # signup database connect
        def action():
            if first_name.get() == "" or last_name.get() == "" or age.get() == "" or city.get() == "" or add.get() == "" or user_name.get() == "" or password.get() == "" or very_pass.get() == "":
                messagebox.showerror(
                    "Error", "All Fields Are Required", parent=winsignup)
            elif password.get() != very_pass.get():
                messagebox.showerror(
                    "Error", "Password & Confirm Password Should Be Same", parent=winsignup)
            else:
                try:
                    con = pymysql.connect(
                        host="localhost", user="root", password="", database="docterapp")
                    cur = con.cursor()
                    cur.execute(
                        "select * from user_information where username=%s", user_name.get())
                    row = cur.fetchone()
                    if row != None:
                        messagebox.showerror(
                            "Error", "User Name Already Exits", parent=winsignup)
                    else:
                        cur.execute(
                            "insert into user_information(first_name,last_name,age,gtk.ender,city,address,username,password) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                            (
                                first_name.get(),
                                last_name.get(),
                                age.get(),
                                var.get(),
                                city.get(),
                                add.get(),
                                user_name.get(),
                                password.get()
                            ))
                        con.commit()
                        con.close()
                        messagebox.showinfo(
                            "Success", "Ragistration Successfull", parent=winsignup)
                        clear()
                        switch()

                except Exception as es:
                    messagebox.showerror(
                        "Error", f"Error Dui to : {str(es)}", parent=winsignup)

        # close signup function
        def switch():
            winsignup.destroy()

        # clear data function
        def clear():
            first_name.delete(0, tk.END)
            last_name.delete(0, tk.END)
            age.delete(0, tk.END)
            var.set("Male")
            city.delete(0, tk.END)
            add.delete(0, tk.END)
            user_name.delete(0, tk.END)
            password.delete(0, tk.END)
            very_pass.delete(0, tk.END)

        # start Signup Window
        winsignup = tk.Tk()
        winsignup.config(bg="#303030")
        winsignup.title("Docter Appointment App")
        winsignup.maxsize(width=500, height=600)
        winsignup.minsize(width=500, height=600)

        # heading label
        heading = tk.Label(winsignup, text="Signup",
                           font='Verdana 20 bold', bg='#303030', fg="white")
        heading.place(x=80, y=60)

        # form data label
        first_name = tk.Label(winsignup, text="First Name :",
                              font='Verdana 10 bold', bg='#303030', fg="white")
        first_name.place(x=80, y=130)

        last_name = tk.Label(winsignup, text="Last Name :",
                             font='Verdana 10 bold', bg='#303030', fg="white")
        last_name.place(x=80, y=160)

        age = tk.Label(winsignup, text="Age :",
                       font='Verdana 10 bold', bg='#303030', fg="white")
        age.place(x=80, y=190)

        gender = tk.Label(winsignup, text="Gender :",
                          font='Verdana 10 bold', bg='#303030', fg="white")
        gender.place(x=80, y=220)

        city = tk.Label(winsignup, text="City :",
                        font='Verdana 10 bold', bg='#303030', fg="white")
        city.place(x=80, y=260)

        add = tk.Label(winsignup, text="Address :",
                       font='Verdana 10 bold', bg='#303030', fg="white")
        add.place(x=80, y=290)

        user_name = tk.Label(winsignup, text="User Name :",
                             font='Verdana 10 bold', bg='#303030', fg="white")
        user_name.place(x=80, y=320)

        password = tk.Label(winsignup, text="Password :",
                            font='Verdana 10 bold', bg='#303030', fg="white")
        password.place(x=80, y=350)

        very_pass = tk.Label(winsignup, text="Verify Password:",
                             font='Verdana 10 bold', bg='#303030', fg="white")
        very_pass.place(x=80, y=380)

        first_name = tk.StringVar()
        last_name = tk.StringVar()
        age = tk.IntVar(winsignup, value='0')
        var = tk.StringVar()
        city = tk.StringVar()
        add = tk.StringVar()
        user_name = tk.StringVar()
        password = tk.StringVar()
        very_pass = tk.StringVar()

        first_name = tk.Entry(winsignup, width=40, textvariable=first_name)
        first_name.place(x=200, y=133)

        last_name = tk.Entry(winsignup, width=40, textvariable=last_name)
        last_name.place(x=200, y=163)

        age = tk.Entry(winsignup, width=40, textvariable=age)
        age.place(x=200, y=193)

        ttk.Radiobutton(
            winsignup, text='Male', value="Male", variable=var).place(x=200, y=220)
        ttk.Radiobutton(
            winsignup, text='Female', value="Female", variable=var).place(x=200, y=238)
        city = tk.Entry(winsignup, width=40, textvariable=city)
        city.place(x=200, y=263)

        add = tk.Entry(winsignup, width=40, textvariable=add)
        add.place(x=200, y=293)

        user_name = tk.Entry(winsignup, width=40, textvariable=user_name)
        user_name.place(x=200, y=323)

        password = tk.Entry(winsignup, width=40, textvariable=password)
        password.place(x=200, y=353)

        very_pass = tk.Entry(winsignup, width=40, show="*",
                             textvariable=very_pass)
        very_pass.place(x=200, y=383)

        # button login and clear

        btn_signup = tk.Button(winsignup, text="Signup",
                               font='Verdana 10 bold', command=action)
        btn_signup.place(x=200, y=413)

        btn_login = tk.Button(winsignup, text="Clear",
                              font='Verdana 10 bold', command=clear)
        btn_login.place(x=280, y=413)

        sign_up_btn = tk.Button(
            winsignup, text="Switch To Login", command=switch)
        sign_up_btn.place(x=350, y=20)

        winsignup.mainloop()

    def deshboard(self):
        def book():
            if docter_var.get() == "" or day.get() == "" or month.get() == "" or year.get() == "":
                messagebox.showerror(
                    "Error", "All Fields Are Required", parent=self.des)
            else:
                try:
                    con = pymysql.connect(
                        host="localhost", user="root", password="", database="docterapp")
                    cur = con.cursor()

                    query = "INSERT INTO appointment (docter, day, month, year, username) VALUES (%s, %s, %s, %s, %s)"

                    values = (docter_var.get(), day.get(),
                              month.get(), year.get(), self.user_name.get())

                    cur.execute(query, values)
                    con.commit()
                    con.close()

                    messagebox.showinfo(
                        "Success", "Booked Appointment", parent=self.des)
                except Exception as es:
                    messagebox.showerror(
                        "Error", f"Error Due to: {str(es)}", parent=self.des)

        def disp():
            doctor_name_var = tk.StringVar()

            def show_data():
                con = pymysql.connect(
                    host="localhost", user="root", password="", database="docterapp")
                cursor = con.cursor()
                cursor.execute(
                    f"SELECT * FROM appointment WHERE docter='{doctor_name_var.get()}'")

                show_all = cursor.fetchall()

                for row in show_all:
                    b = '\n'
                    display.insert(tk.END, f"{b}{[i for i in row]}")
                    

            def cls():
                display.delete("1.0", 'end')

            self.d = tk.Toplevel(self.des)
            self.d.title("Doctor's Appointment")
            self.d.config(bg="#303030")
            self.d.minsize(400, 400)
            f = tk.Frame(self.d, background="#303030", pady=20)
            f.pack()
            tk.Label(f, text="Enter Doctor name", font=("Helvetica 10 roman"),
                     bg="#303030", fg="white").grid(row=0, column=1, padx=10, pady=10)
            doctor_name = tk.Entry(f, width=33, textvariable=doctor_name_var)
            doctor_name.grid(row=0, column=2, padx=10, pady=10)

            self.text_frame = tk.Frame(self.d, background="#242424", borderwidth=5,
                                       relief=tk.RAISED, padx=30, pady=20)

            v = tk.Scrollbar(self.d, orient='vertical',
                             highlightbackground="#343434")
            v.pack(side=tk.RIGHT, fill='y')

            display = tk.Text(self.text_frame, pady=10, padx=10, height=17, width=30,
                              font="Serif 10 bold", yscrollcommand=v.set)
            display.pack()

            v.config(command=display.yview)

            tk.Button(self.text_frame, text="Display", font="Serif 12 ", relief=tk.RIDGE, overrelief=tk.GROOVE,
                      background="#002244", foreground='#e4d00a', command=show_data, padx=23).pack(pady=15, side=tk.LEFT)

            c = tk.Button(self.text_frame, text="Clear Screen", font="Serif 12 ", relief=tk.RIDGE, overrelief=tk.GROOVE,
                          background="#002244", foreground='#e4d00a', command=cls)
            c.pack(pady=15, side=tk.RIGHT)

            self.text_frame.pack()
            self.d.mainloop()

        self.des = tk.Tk()
        self.des.title("Admin Panel Docter App")
        self.des.config(bg="#303030")
        self.des.maxsize(width=800, height=500)
        self.des.minsize(width=800, height=500)

        self.menubar = tk.Menu(self.des)
        file = tk.Menu(self.menubar, tearoff=0)
        file.add_command(label='Display', command=disp)
        file.add_separator()
        self.menubar.add_cascade(label='File', menu=file)
        file.add_command(label='Exit', command=self.des.destroy)
        self.des.config(menu=self.menubar)

        # heading label
        heading = tk.Label(
            self.des, text=f"User Name : {self.user_name.get()}", font='Verdana 15 roman', bg='#303030', fg="red")
        heading.pack(side='top', anchor='nw', pady=30)

        f = tk.Frame(self.des, height=1, width=800, bg="green")
        f.place(x=0, y=95)

        con = pymysql.connect(host="localhost", user="root",
                              password="", database="docterapp")
        cur = con.cursor()

        cur.execute("select * from user_information where username ='" +
                    self.user_name.get() + "'")
        row = cur.fetchall()

        a = tk.Frame(self.des, height=1, width=400, bg="green")
        a.place(x=0, y=195)

        b = tk.Frame(self.des, height=100, width=1, bg="green")
        b.place(x=400, y=97)

        for data in row:
            first_name = tk.Label(
                self.des, text=f"First Name : {data[1]}", font='Verdana 10 bold', bg="#303030", fg="white")
            first_name.place(x=20, y=100)

            last_name = tk.Label(
                self.des, text=f"Last Name : {data[2]}", font='Verdana 10 bold', bg="#303030", fg="white")
            last_name.place(x=20, y=130)

            age = tk.Label(
                self.des, text=f"Age : {data[3]}", font='Verdana 10 bold', bg="#303030", fg="white")
            age.place(x=20, y=160)

            gender = tk. Label(
                self.des, text=f"ID : {data[0]}", font='Verdana 10 bold', bg="#303030", fg="white")
            gender.place(x=250, y=100)

            city = tk.Label(
                self.des, text=f"City : {data[5]}", font='Verdana 10 bold', bg="#303030", fg="white")
            city.place(x=250, y=130)

        add = tk.Label(
            self.des, text=f"Address : {data[6]}", font='Verdana 10 bold', bg="#303030", fg="white")
        add.place(x=250, y=160)

        # Book Docter Appointment App
        heading = tk.Label(self.des, text="Book Appointment",
                           font='Verdana 20 bold', bg="#303030", fg="white")
        heading.place(x=470, y=100)

        # Book DocterLabel
        Docter = tk. Label(self.des, text="Docter:",
                           font='Verdana 10 bold', bg="#303030", fg="white")
        Docter.place(x=480, y=145)

        Day = tk.Label(self.des, text="Day:", font='Verdana 10 bold',
                       bg="#303030", fg="white")
        Day.place(x=480, y=165)

        Month = tk.Label(self.des, text="Month:",
                         font='Verdana 10 bold', bg="#303030", fg="white")
        Month.place(x=480, y=185)

        Year = tk. Label(self.des, text="Year:",
                         font='Verdana 10 bold', bg="#303030", fg="white")
        Year.place(x=480, y=205)

        # Book Docter Entry Box

        docter_var = tk.StringVar()
        day = tk.StringVar()
        month = tk.StringVar()
        year = tk.StringVar()

        Docter_box = ttk.Combobox(
            self.des, width=30, textvariable=docter_var, state='readonly')
        Docter_box['values'] = ('Dr Raghottam', 'Dr Shreya',
                                'Dr Shetal', 'Dr riya', 'Dr Sunil')
        Docter_box.current(0)
        Docter_box.place(x=550, y=145)

        Day = tk.Entry(self.des, width=33, textvariable=day)
        Day.place(x=550, y=168)

        Month_Box = ttk.Combobox(
            self.des, width=30, textvariable=month, state='readonly')
        Month_Box['values'] = (
            'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
            'December')
        Month_Box.current(0)
        Month_Box.place(x=550, y=188)

        Year = tk.Entry(self.des, width=33, textvariable=year)
        Year.place(x=550, y=208)

        # buttonself.

        btn = tk.Button(self.des, text="Book", font='Verdana 10 bold',
                        width=20, command=book, bg='green', fg="white", padx=5)
        btn.place(x=553, y=250)

        con = pymysql.connect(host="localhost", user="root",
                              password="", database="docterapp")
        cur = con.cursor()

        # Fetch appointment data for the current user
        cur.execute("SELECT * FROM appointment WHERE username = %s",
                    (self.user_name.get,))
        appointment_rows = cur.fetchall()

        # Display appointment details
        x_coordinate = 20  # Adjust this value to place labels at different locations
        for appointment in appointment_rows:
            docter_label = tk.Label(
                self.des, text=f"Docter: {appointment[2]}", font='Verdana 10 bold')
            docter_label.place(x=x_coordinate, y=300)

            day_label = tk.Label(
                self.des, text=f"Day: {appointment[3]}", font='Verdana 10 bold')
            day_label.place(x=x_coordinate, y=320)

            month_label = tk.Label(
                self.des, text=f"Month: {appointment[4]}", font='Verdana 10 bold')
            month_label.place(x=x_coordinate, y=340)

            year_label = tk.Label(
                self.des, text=f"Year: {appointment[5]}", font='Verdana 10 bold')
            year_label.place(x=x_coordinate, y=360)

            x_coordinate += 150  # Increase x-coordinate for the next set of labels


if __name__ == '__main__':
    win = tk.Tk()
    # app title
    win.title("Docter Appointment App")
    win.config(bg="#303030")
    # window size
    win.maxsize(width=500, height=500)
    win.minsize(width=500, height=500)
    win.iconbitmap(r"C:\Users\DELL\Downloads\hospital.ico")
    app = DoctorAppointment(win)
    win.mainloop()
