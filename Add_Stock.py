import tkinter as tk
from tkinter import messagebox
import re
from tkcalendar import *


def create_add_stock():
    window = tk.Tk()
    window.title("Pharm")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry(f"{screen_width}x{screen_height}")
    window.configure(bg='#333333')

    def back_to_home():
        window.destroy()
        import GUI
        GUI.create_gui()
    def clear():
        barcode.delete(0,tk.END)
        name.delete(0,tk.END)
        buy_price.delete(0,tk.END)
        selling_price.delete(0,tk.END)
        quantity.delete(0,tk.END)
        exp_date.delete(0,tk.END)
        discount.delete(0,tk.END)
    # validating date


    # save stock
    def save():
        if barcode.get() == "" or name.get() == "" or buy_price.get() == "" or selling_price.get() == "" or quantity.get() == "" or exp_date.cget() == "" or discount.get() == "":
            messagebox.showerror("Error", "All fields should be filled")
        else:
            clear()
            # Save logic
            messagebox.showinfo("Success","Stock added successfully")





    barcode_label = tk.Label(window, text="Barcode", pady=5, padx=10, anchor=tk.W, borderwidth=5)
    name_label = tk.Label(window, text="Name", pady=5, padx=10, anchor=tk.W, borderwidth=5)
    buy_price_label = tk.Label(window, text="Buying Price", pady=5, padx=10, anchor=tk.W, borderwidth=5)
    selling_price_label = tk.Label(window, text="Selling Price", pady=5, padx=10, anchor=tk.W, borderwidth=5)
    quantity_label = tk.Label(window, text="Quantity", pady=5, padx=10, anchor=tk.W, borderwidth=5)
    exp_date_label = tk.Label(window, text="Exp.Date", pady=5, padx=10, anchor=tk.W, borderwidth=5)
    discount_label = tk.Label(window, text="Discount", pady=5, padx=10, anchor=tk.W, borderwidth=5)

    barcode = tk.Entry(window, width=60, borderwidth=5)
    name = tk.Entry(window, width=60, borderwidth=5)
    buy_price = tk.Entry(window, width=60, borderwidth=5)
    selling_price = tk.Entry(window, width=60, borderwidth=5)
    quantity = tk.Entry(window, width=60, borderwidth=5)
    # exp_date = tk.Entry(window, width=60, borderwidth=5)
    exp_date= Calendar(window,selectmode="day",year=2024,month=5,day=22)
    discount = tk.Entry(window, width=60, borderwidth=5)

    barcode_label.grid(row=0, column=0, pady=5, padx=5, sticky=tk.W)
    name_label.grid(row=1, column=0, pady=5, padx=5, sticky=tk.W)
    buy_price_label.grid(row=2, column=0, pady=5, padx=5, sticky=tk.W)
    selling_price_label.grid(row=3, column=0, pady=5, padx=5, sticky=tk.W)
    quantity_label.grid(row=4, column=0, pady=5, padx=5, sticky=tk.W)
    exp_date_label.grid(row=5, column=0, pady=5, padx=5, sticky=tk.W)
    discount_label.grid(row=6, column=0, pady=5, padx=5, sticky=tk.W)

    barcode.grid(row=0, column=1, pady=5)
    name.grid(row=1, column=1, pady=5)
    buy_price.grid(row=2, column=1, pady=5)
    selling_price.grid(row=3, column=1, pady=5)
    quantity.grid(row=4, column=1, pady=5)
    exp_date.grid(row=5, column=1, pady=5)
    discount.grid(row=6, column=1, pady=5)


    back_button = tk.Button(window, text="Back", padx=25, pady=10, command=back_to_home, anchor=tk.S)
    back_button.grid(row=7,column=0,sticky=tk.S)
    save_button = tk.Button(window,text="Save",pady=10,padx=25,command=save,anchor=tk.S )
    save_button.grid(row=7,column=1,sticky=tk.S)


    window.mainloop()
create_add_stock()