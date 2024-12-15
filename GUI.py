import tkinter as tk
from tkinter import *
from tkinter import ttk




def create_gui():
    window = tk.Tk()
    window.title("Pharm")
    style = ttk.Style(window)
    style.theme_use("clam")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry(f"{screen_width}x{screen_height}")
    window.configure(bg='#333333')

    def add():
        window.destroy()
        import Add_Stock
        Add_Stock.create_add_stock()

    def Edit():
        return

    def Discount():
        return

    def Sale():
        return

    def User():
        return

    def Log_out():
        window.destroy()
        import Login
        Login.create_login()

    def View():
        return

    def Change():
        return

    def Report():
        return

    # Define Buttons
    Add_Button = Button(window, text="Add Stock", padx=40, pady=20, command=add)
    View_Button = Button(window, text="View Stock", padx=40, pady=20, command=View)
    Edit_Button = Button(window, text="Edit Stock", padx=70, pady=20, command=Edit)
    Discount_Button = Button(window, text="Discount", padx=40, pady=20, command=Discount)
    Sale_Button = Button(window, text="Sale", padx=40, pady=20, command=Sale)
    User_Button = Button(window, text="Add user", padx=40, pady=20, command=User)
    Report_Button = Button(window, text="Report", padx=40, pady=20, command=Report)
    LogOut_Button = Button(window, text="Log out", padx=42, pady=20, command=Log_out)
    ChangePass_Button = Button(window, text="Change Password", padx=50, pady=20, command=Change)

    # Button Positioning
    Add_Button.grid(row=0, column=0)
    Edit_Button.grid(row=0, column=1)
    Discount_Button.grid(row=0, column=2)
    Sale_Button.grid(row=0, column=3)
    User_Button.grid(row=0, column=4)
    Report_Button.grid(row=0, column=6)
    View_Button.grid(row=0, column=5)
    LogOut_Button.grid(row=1, column=2)
    ChangePass_Button.grid(row=1, column=1)

    window.mainloop()
# create_gui()
