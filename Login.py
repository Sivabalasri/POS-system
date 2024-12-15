import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

def create_login():
    window = tk.Tk()
    # style=ttk.Style(window)
    # style.theme_use("")

    window.title("Login form")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry(f"{screen_width}x{screen_height}")
    window.configure(bg='#333333')

    def clear():
        username_entry.delete(0,tk.END)
        password_entry.delete(0,tk.END)

    def login_C():
        if username_entry.get() == "" or password_entry.get() == "":
            messagebox.showerror("Error", "Please provide your credentials")
        else:
            try:
                con = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="199603",
                    database="test_1")
                mycursor = con.cursor()
            except:
                messagebox.showerror("Error", "Database is not connected")
                return
            query = "use test_1"
            mycursor.execute(query)
            query = "select * from user where name=%s and password=%s "
            mycursor.execute(query, (username_entry.get(), password_entry.get()))
            row = mycursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid credentials")
            else:
                clear()
                window.destroy()
                import GUI
                GUI.create_gui()

    frame = tk.Frame(bg='#333333')

    login_label = tk.Label(
        frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
    username_label = tk.Label(
        frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    username_entry = tk.Entry(frame, font=("Arial", 16))
    password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
    password_label = tk.Label(
        frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    login_button = tk.Button(
        frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login_C)

    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=20)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)

    frame.pack()

    window.mainloop()
create_login()
