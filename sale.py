import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="199603",
    database="test_1"

)

mycursor=mydb.cursor()

def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
def Quantity_update(event):
    content=Qty_ent.get()
    if content.isdigit() or content=="":
        Qty_ent.delete(0,tk.END)
        Qty_ent.insert(0,content)
    else:
        messagebox.showerror("Error","Quantity should be number")
        Qty_ent.delete(0,tk.END)
def is_valid_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
def validate_discountp(event):
    percent = Dis_ent.get()
    amount = Disc_ent.get()
    unit = unit_ent.get()

    if unit == "":
        messagebox.showinfo("Unit Price", "Please enter the unit price first")
        unit_ent.focus_set()
    elif amount and float(amount) > 0:
        Dis_ent.delete(0, tk.END)
        Dis_ent.config(state='readonly')
        unit_ent.config(state='readonly')
        if percent == "" or is_valid_float(percent):
            if percent == "" or float(percent) < 100:
                Dis_ent.delete(0, tk.END)
                Dis_ent.insert(0, round(float(percent),2))
            else:
                messagebox.showerror("Error", "Discount should be less than 100%")
                Dis_ent.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Check your entries again")
            Dis_ent.delete(0, tk.END)
            Disc_ent.config(state='normal')
    else:
        Dis_ent.config(state='normal')
        if percent == "" or is_valid_float(percent):
            if percent == "" or float(percent) < 100:
                Dis_ent.delete(0, tk.END)
                Dis_ent.insert(0, round(float(percent),2))
            else:
                messagebox.showerror("Error", "Discount should be less than 100%")
                Dis_ent.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Check your entries again")
            Dis_ent.delete(0, tk.END)
def validate_discounta(event):
    percent = Dis_ent.get()
    amount = Disc_ent.get()
    unit = unit_ent.get()

    if unit == "":
        messagebox.showinfo("Unit Price", "Please enter the unit price first")
        unit_ent.focus_set()
    elif percent and float(percent) > 0:
        Disc_ent.delete(0, tk.END)
        Disc_ent.config(state='readonly')
        if amount == "" or is_valid_float(amount):
            if float(amount)<float(unit):
                Disc_ent.delete(0, tk.END)
                Disc_ent.insert(0,round(float(amount),2))
            else:
                messagebox.showerror("Error", "Discount should be less than unit price")
                Dis_ent.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Check your entries again")
            Dis_ent.delete(0, tk.END)
    else:
        Disc_ent.config(state='normal')
        if amount == "" or is_valid_float(amount):
            if amount == "" or float(amount) < float(unit):
                Disc_ent.delete(0, tk.END)
                Disc_ent.insert(0, round(float(amount),2))
            else:
                messagebox.showerror("Error", "Discount should be less than unit price")
                Disc_ent.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Check your entries again")
            Disc_ent.delete(0, tk.END)
def validate_unit(event):
    unit=unit_ent.get()
    if unit == "" or is_valid_float(unit):
        if unit == "" or float(unit)>0:
            unit_ent.delete(0, tk.END)
            unit_ent.insert(0, round(float(unit),2))
            Dis_ent.delete(0,tk.END)
            Disc_ent.delete(0,tk.END)
        else:
            messagebox.showerror("Error", "Check price")
            unit_ent.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Check price")
        unit_ent.delete(0, tk.END)
def Search_product():
    if Src_ent.get()=="":
        messagebox.showinfo("Empty","Search bar cannot be empty")
        Clear_single_product()
    else:
        try:

            query = "SELECT * FROM stock_medicine WHERE barcode=%s"
            mycursor.execute(query,(Src_ent.get(),))
            row=mycursor.fetchall()
            Name_ent.config(state='normal')  # Make the entry normal to insert text
            Name_ent.delete(0, tk.END)  # Clear any previous content
            Name_ent.insert(tk.END, row[0][2])  # Insert the product name
            Name_ent.config(state='readonly')

            unit_ent.config(state='normal')  # Make the entry normal to insert text
            unit_ent.delete(0, tk.END)  # Clear any previous content
            unit_ent.insert(tk.END, row[0][9])  # Insert the product name
            unit_ent.config(state='readonly')
            Qty_ent.focus_set()

        except Exception as e:
            messagebox.showerror("Error",f"No product found:{e}")
def Add_product():
    if Name_ent.get()=="" or Qty_ent.get()=="" or unit_ent.get()=="" or int(Qty_ent.get())==0:
        messagebox.showerror("Error","Name or Quanty can't be zero or empty")
    else:
        add_to_treeview()
        Clear_single_product()
        Src_ent.focus_set()
        show_count()
        show_time()
        show_total()
def Clear_single_product():
    Src_ent.delete(0,tk.END)
    Qty_ent.delete(0,tk.END)
    Name_ent.config(state='normal')
    Name_ent.delete(0,tk.END)
    unit_ent.config(state='normal')
    unit_ent.delete(0,tk.END)
    Dis_ent.delete(0,tk.END)
    Disc_ent.delete(0,tk.END)
def Delete_product():
    selected_item = bill.selection()  # Get the selected item
    if selected_item:
        bill.delete(selected_item)  # Delete the selected item
    else:
        messagebox.showerror("Error", "No item selected to delete")
    show_count()
    show_time()
    show_total()
def Deliver():
    return
def Clear_bill():
    if bill.get_children()=="":
        messagebox.showinfo("Clear","Nothing to clear")
    elif messagebox.askyesno("Warning","Do you want to clear the bill?"):
        bill.delete(*bill.get_children())
        show_time()
        show_count()
        show_total()
def Clear_details():
    detail.delete(*detail.get_children())
    Src1_ent.delete(0,tk.END)
def Add_Customer():
    return
def Print_bill():
    return
def Search1():
    x1 = Src1_ent.get()
    if x1 == "":
        messagebox.showinfo("Empty", "Search box is empty")
    else:
        try:
            query = "SELECT * FROM stock_medicine WHERE barcode LIKE '%" + x1 + "%' OR name LIKE '%" + x1 + "%'"
            mycursor.execute(query)
            rows = mycursor.fetchall()
            src_table(rows)
        except Exception as e:
            messagebox.showerror("Not Found", f"Stock not found: {e}")
def src_table(rows):
    detail.delete(*detail.get_children())
    if rows:
        for row in rows:
            item = row[2]
            cost = row[7]
            mincost = row[8]
            sell = row[9]
            qty = row[4]
            exp = row[3]
            detail.insert("", "end", values=(item, cost, mincost, sell, qty, exp))
    else:
        messagebox.showinfo("No Results", "No matching records found")
    Src1_ent.delete(0,tk.END)
def on_detail_click(event):
    rowid = detail.identify_row(event.y)
    item = detail.item(rowid)

    Name_ent.delete(0, tk.END)
    Name_ent.insert(0, item["values"][0])

    unit_ent.config(state='normal')
    unit_ent.delete(0, tk.END)
    unit_ent.insert(0, item["values"][3])
    unit_ent.config(state='readonly')

    Qty_ent.focus_set()
def log_out():
    return
def Back1():
    return
def on_treeview_click(event):
    # Identify the row that was clicked
    rowid = bill.identify_row(event.y)
    item = bill.item(rowid)

    # Set the values in the entry widgets
    Name_ent.delete(0, tk.END)
    Name_ent.insert(0, item["values"][0])

    Qty_ent.delete(0, tk.END)
    Qty_ent.insert(0, item["values"][1])

    unit_ent.config(state='normal')
    unit_ent.delete(0, tk.END)
    unit_ent.insert(0, item["values"][2])

    Disc_ent.delete(0, tk.END)
    Disc_ent.insert(0, item["values"][3])

    # Optionally set focus to the entry widget
    Qty_ent.focus_set()
def pop_updiscount():
    popup=tk.Toplevel(root)
    popup.title("Discout for total")
    Discount_for=tk.Label(popup,text="Enter Ammount\nLKR",font=(("Times New Roman"),10))
    Discount_for.grid(row=0,column=0,padx=2,pady=2)
    Discount_forent=tk.Entry(popup,textvariable=n1)
    Discount_forent.grid(row=0,column=1,padx=2,pady=2)
    Discount_forent.focus_set()
    Discount_forent.bind("<Down>",focus_next_widget)
    Discount_forent.bind("<Return>",lambda event:Discount_for_total(popup))
    Discount_for1 = tk.Label(popup, text="Enter Ammount\n(%)", font=(("Times New Roman"), 10))
    Discount_for1.grid(row=1, column=0, padx=2, pady=2)
    Discount_for1ent = tk.Entry(popup,textvariable=n2)
    Discount_for1ent.grid(row=1, column=1, padx=2, pady=2)
    Discount_for1ent.bind("<Down>", focus_next_widget)
    Discount_for1ent.bind("<Return>", lambda event: Discount_for_total(popup))
    Enterbtn=tk.Button(popup,text="Enter",padx=15,pady=5,borderwidth=2,command=lambda: Discount_for_total(popup))
    Enterbtn.grid(row=2,column=0)
    Cancelbtn = tk.Button(popup, text="Cancel", padx=15, pady=5, borderwidth=2,command=popup.destroy)
    Cancelbtn.grid(row=2, column=1)
    Discount_forent.delete(0,tk.END)
    Discount_for1ent.delete(0,tk.END)
def Discount_for_total(popup):
    try:
        if n1.get()!="" and n2.get()!="":
            messagebox.showerror("Error","Added Discount twice!!")
        elif n1.get()=="" and n2.get()=="":
            popup.destroy()
        elif n1.get()!="" and float(n1.get())<float(total_ent.get()):
            Discount_ent.config(state='normal')
            Discount_ent.delete(0,tk.END)
            Discount_ent.insert(0,round(float(n1.get()),2))
            Discount_ent.config(state='readonly')
        elif float(n2.get())>100:
            messagebox.showerror("Error","Discount should be less than 100%")
        elif float(n2.get())<100:
            m=float(total_ent.get())*float(n2.get())/100
            m1=round(m,2)
            Discount_ent.config(state='normal')
            Discount_ent.delete(0, tk.END)
            Discount_ent.insert(0, m1)
            Discount_ent.config(state='readonly')
        if Discount_ent.get()=="":
            y=0.00
            Discount_ent.config(state='normal')
            Discount_ent.delete(0, tk.END)
            Discount_ent.insert(0, y)
            Discount_ent.config(state='readonly')
        total_Dis_ent.config(state='normal')
        total_Dis_ent.delete(0, tk.END)
        total_Dis_ent.insert(0, float(total_ent.get()) - float(Discount_ent.get()))
        total_Dis_ent.config(state='readonly')
        popup.destroy()
    except ValueError:
        messagebox.showerror("Error","Invalid inputs")
    finally:
        popup.destroy()
def add_to_treeview():
    name = Name_ent.get()
    qty = int(Qty_ent.get())
    unit_price = float(unit_ent.get())
    unit_text = unit_ent.get()
    if unit_text == "":
        messagebox.showerror("Error", "Unit price cannot be empty")
        return
    discount_amount = float(Disc_ent.get() if Disc_ent.get() else 0)
    discount_percent = float(Dis_ent.get() if Dis_ent.get() else 0)
    if discount_amount==0 and discount_percent==0:
        act_discount=0
        discount_value=0
    elif discount_percent!=0 and discount_amount==0:
        act_discount=str(discount_percent)+"%"
        discount_value=((discount_percent / 100) * unit_price) * qty
    else:
        act_discount=discount_amount
        discount_value=(discount_amount*qty)
    subtotal = (unit_price * qty)-discount_value
    # Check for duplicate product in Treeview
    for item in bill.get_children():
        item_values = bill.item(item, 'values')
        if item_values[0] == name:
            messagebox.showerror("Error", "Product already exists in the bill")
            # Focus on the existing item
            bill.selection_set(item)
            bill.focus(item)
            bill.see(item)
            return
    bill.insert("", "end", values=(name, qty, unit_price, act_discount,discount_value, subtotal))
def show_count():
    item_ent.config(state='normal')
    item_ent.delete(0,tk.END)
    item_ent.insert(0,len(bill.get_children()))
    item_ent.config(state='readonly')
def show_time():
    if len(bill.get_children())==0:
        Date_ent.configure(state='normal')
        Date_ent.delete(0, tk.END)
    else:
        current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        Date_ent.configure(state='normal')
        Date_ent.delete(0,tk.END)
        Date_ent.insert(0,current_date_time)
        Date_ent.config(state='readonly')
def show_total():
    if len(bill.get_children())==0:
        total_ent.config(state='normal')
        total_ent.delete(0, tk.END)
        total_ent.config(state='readonly')
    else:
        total = 0
        for child in bill.get_children():
            amount = bill.item(child)["values"][5]  # Assuming the amount is in the second column
            total += float(amount)
            total_ent.config(state='normal')
            total_ent.delete(0,tk.END)
            total_ent.insert(0,round(float(total),2))
            total_ent.config(state='readonly')

root = tk.Tk()
style = ttk.Style(root)
style.theme_use("default")

n1 = tk.StringVar()
n2 = tk.StringVar()
# Configure the title frame
title_frame = tk.LabelFrame(root, bg="lightgrey", height=100)
title_frame.pack(fill=tk.X, padx=5, pady=2)
lbl = tk.Label(title_frame, text="\nPharmacy and Grocery", font=("Arial", 20), bg="lightgrey")
lbl.pack()

# Create a container frame to hold the left and right frames
container_frame = tk.Frame(root)
container_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Configure the main LabelFrame
main_labelframe = tk.LabelFrame(container_frame, highlightcolor="black", width=400, bg="white")
main_labelframe.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
main_labelframe.pack_propagate(False)

# Configure button frame
Btn_labelframe = tk.LabelFrame(container_frame, text="Buttons", font=("Times New Roman", 11), bg="lightgrey", width=200)
Btn_labelframe.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=1, pady=1)
Btn_labelframe.pack_propagate(False)

# Configure product frame inside main labelframe
Product_frame = tk.LabelFrame(main_labelframe, bg="lightgrey", height=100, font=("Arial", 11))
Product_frame.pack(side=tk.TOP, fill=tk.X, padx=1, pady=1)
Seaframe=tk.Frame(Product_frame,bg="lightgrey")
Seaframe.grid(row=0,column=0,columnspan=6,sticky="ew")
Src_ent = tk.Entry(Seaframe, font=("Arial", 9),width=30)
Src_ent.grid(row=0, column=0, padx=2, pady=2)
Src_ent.bind("<Return>", lambda event: Search_product())
Src_ent.focus_set()

# Product Entry and Labels
Name_lbl = tk.Label(Product_frame, text="Product", bg="lightgrey", font=("Arial", 9), anchor=tk.CENTER)
Name_lbl.grid(row=1, column=0, padx=2)
Name_ent = tk.Entry(Product_frame)
Name_ent.grid(row=2, column=0, padx=1, pady=1)

Qty_lbl = tk.Label(Product_frame, text="Quantity", bg="lightgrey", font=("Arial", 9), anchor=tk.CENTER)
Qty_lbl.grid(row=1, column=1, padx=2)
Qty_ent = tk.Entry(Product_frame)
Qty_ent.grid(row=2, column=1, padx=5, pady=1)
Qty_ent.bind("<Return>",lambda event: Add_product())
Qty_ent.bind("Tab",focus_next_widget)
Qty_ent.bind("<KeyRelease>",Quantity_update)
Qty_ent.bind("<Delete>",lambda event:Delete_product())

unit_lbl = tk.Label(Product_frame, text="Unit price\nLKR", bg="lightgrey", font=("Arial", 9), anchor=tk.CENTER)
unit_lbl.grid(row=1, column=2, padx=2)
unit_ent = tk.Entry(Product_frame)
unit_ent.grid(row=2, column=2, padx=5, pady=1)
unit_ent.bind("<Return>",lambda event:Add_product())
unit_ent.bind("<KeyRelease>",validate_unit)

Disc_lbl = tk.Label(Product_frame, text="Discount\nLKR", bg="lightgrey", font=("Arial", 9), anchor=tk.CENTER)
Disc_lbl.grid(row=1, column=3, padx=2)
Disc_ent = tk.Entry(Product_frame)
Disc_ent.grid(row=2, column=3, padx=5, pady=1)
Disc_ent.bind("Tab",focus_next_widget)
Disc_ent.bind("<Return>",lambda event:Add_product())
Disc_ent.bind("<KeyRelease>",validate_discounta)

Dis_lbl = tk.Label(Product_frame, text="Discount\n(%)", bg="lightgrey", font=("Arial", 9), anchor=tk.CENTER)
Dis_lbl.grid(row=1, column=4, padx=2)
Dis_ent = tk.Entry(Product_frame)
Dis_ent.grid(row=2, column=4, padx=5, pady=1)
Dis_ent.bind("<Return>",lambda event:Add_product())
Dis_ent.bind("<KeyRelease>",validate_discountp)

# Add, Delete, and Clear buttons
Add_btn = tk.Button(Product_frame, text="Add to Bill", command=Add_product)
Add_btn.grid(row=3, column=0, padx=2, pady=5)
Dlt_btn = tk.Button(Product_frame, text="Delete", command=Delete_product)
Dlt_btn.grid(row=3, column=2, padx=2, pady=5)
Clr_btn = tk.Button(Product_frame, text="Clear", command=Clear_single_product)
Clr_btn.grid(row=3, column=1, padx=2, pady=5)

# Configure bill frame with scrollbars
Bill_frame = tk.LabelFrame(main_labelframe)
Bill_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
Bill_frame.pack_propagate(False)  # Prevent the frame from resizing

bill = ttk.Treeview(Bill_frame, columns=(1, 2, 3, 4, 5,6), show="headings", height="10")
bill.grid(row=0, column=0, sticky="nsew")
bill.heading(1, text="Item")
bill.heading(2, text="Qty")
bill.heading(3, text="Unit price")
bill.heading(4, text="Discount")
bill.heading(5,text="Dis amount")
bill.heading(6, text="Sub total")
bill.bind("<Double 1>",on_treeview_click)
# Set column widths
bill.column(1, width=200, minwidth=200, stretch=tk.NO)  # Item column for 20 characters
bill.column(2, width=50, minwidth=50, stretch=tk.NO)    # Qty column
bill.column(3, width=100, minwidth=100, stretch=tk.NO)  # Unit price column
bill.column(4, width=50, minwidth=50, stretch=tk.NO)    # Discount column for 3 characters
bill.column(5, width=100, minwidth=100, stretch=tk.NO)
bill.column(6, width=100, minwidth=100, stretch=tk.YES) # Subtotal column

# Configure scrollbars for the Treeview
scroll_y = ttk.Scrollbar(Bill_frame, orient=tk.VERTICAL, command=bill.yview)
bill.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=0, column=1, sticky="ns")

# Label frame for total at the bottom
label_frame = tk.LabelFrame(Bill_frame, bg="lightgrey")
label_frame.grid(row=1, column=0, columnspan=2, sticky="ew")

# Left-aligned labels
ref = tk.Label(label_frame, text="Ref : ", font=("Times New Roman", 12), bg="lightgrey", anchor="w")
ref.grid(row=0, column=0, padx=5, pady=1, sticky="w")
ref_ent=tk.Entry(label_frame,font=("Times New Roman",12),bg="lightgrey",state="readonly")
ref_ent.grid(row=0,column=1,padx=5,pady=1,sticky="w")
Date = tk.Label(label_frame, text="Date : ", font=("Times New Roman", 12), bg="lightgrey", anchor="w")
Date.grid(row=1, column=0, padx=5, pady=1, sticky="w")
Date_ent=tk.Entry(label_frame,font=("Times New Roman",12),bg="lightgrey",state="readonly")
Date_ent.grid(row=1,column=1,padx=5,pady=1,sticky="w")
item = tk.Label(label_frame, text="No of items : ", font=("Times New Roman", 12), bg="lightgrey", anchor="w")
item.grid(row=2, column=0, padx=5, pady=1, sticky="w")
item_ent=tk.Entry(label_frame,font=("Times New Roman",12),bg="lightgrey",state="readonly")
item_ent.grid(row=2,column=1,padx=5,pady=1,sticky="w")

# Right-aligned labels
total = tk.Label(label_frame, text="Total : ", font=("Times New Roman", 12), bg="lightgrey", anchor="e")
total.grid(row=0, column=1, padx=5, pady=1, sticky="e")
total_ent=tk.Entry(label_frame,font=("Times New Roman",12),bg="lightgrey",state="readonly")
total_ent.grid(row=0,column=2,padx=5,pady=1,sticky="e")
Discount = tk.Label(label_frame, text="Discount for Total : ", font=("Times New Roman", 12), bg="lightgrey", anchor="e")
Discount.grid(row=1, column=1, padx=5, pady=1, sticky="e")
Discount_ent=tk.Entry(label_frame,font=("Times New Roman",12),bg="lightgrey",state="readonly")
Discount_ent.grid(row=1,column=2,padx=5,pady=1,sticky="e")
total_Dis = tk.Label(label_frame, text="Total after Discount : ", font=("Times New Roman", 12), bg="lightgrey", anchor="e")
total_Dis.grid(row=2, column=1, padx=5, pady=1, sticky="e")
total_Dis_ent=tk.Entry(label_frame,font=("Times New Roman",12),bg="lightgrey",state="readonly")
total_Dis_ent.grid(row=2,column=2,padx=5,pady=1,sticky="e")

# Make sure the right-aligned labels are properly aligned to the right
label_frame.grid_columnconfigure(1, weight=1)

Bill_frame.grid_rowconfigure(0, weight=1)
Bill_frame.grid_columnconfigure(0, weight=1)

# Option frame for Deliver button
option_frame = tk.LabelFrame(main_labelframe, bg="lightgrey")
option_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
Deliver_btn = tk.Button(option_frame, text="Deliver", padx=10, pady=10,command=Deliver)
Deliver_btn.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
tdisc_btn = tk.Button(option_frame, text="Discount", padx=10, pady=10,command=pop_updiscount)
tdisc_btn.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
print_btn = tk.Button(option_frame, text="Print Bill", padx=10, pady=10,command=Print_bill)
print_btn.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
Clear_btn = tk.Button(option_frame, text="Clear", padx=10, pady=10,command=Clear_bill)
Clear_btn.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
Customer_btn = tk.Button(option_frame, text="Add\nCustomer", padx=10, pady=10,command=Add_Customer)
Customer_btn.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

# Detail frame at the bottom
detail_frame = tk.LabelFrame(root, bg="lightgrey", height=100, font=("Arial", 11))
detail_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=2, pady=2, ipady=10)

# Configure the detail frame grid
detail_frame.grid_columnconfigure(0, weight=1)  # Make the first column expandable
detail_frame.grid_columnconfigure(1, weight=0)
detail_frame.grid_columnconfigure(2, weight=0)
detail_frame.grid_columnconfigure(3, weight=0)
detail_frame.grid_rowconfigure(0, weight=1)  # First row for search and buttons
detail_frame.grid_rowconfigure(1, weight=4)  # Second row for Treeview

# Search and buttons
searchframe=tk.Frame(detail_frame,bg="lightgrey")
searchframe.grid(row=0,column=0,padx=1,pady=1,sticky="ew")
Src1_ent = tk.Entry(searchframe, font=("Arial", 9),width=90)
Src1_ent.pack(side="left",padx=15)  # Make the entry expandable
Src1_ent.bind("<Return>", lambda event: Search1())
Src_btn = tk.Button(searchframe, text="Search", pady=3, padx=5, command=Search1)
Src_btn.pack(side="left",padx=2)
Srcclr_btn = tk.Button(searchframe, text="Clear", pady=3, padx=5, command=Clear_details)
Srcclr_btn.pack(side="left",padx=2)

# Treeview for details
detail = ttk.Treeview(detail_frame, columns=(1, 2, 3, 4, 5, 6), show="headings", height="3")
detail.grid(row=1, column=0, columnspan=6, sticky="nsew")
detail.heading(1, text="Item")
detail.heading(2, text="Cost")
detail.heading(3, text="Minimum Cost")
detail.heading(4, text="Sell_pr")
detail.heading(5, text="Quantity")
detail.heading(6, text="Exp date")

# Set column widths
detail.column(1, width=400, minwidth=200, stretch=tk.NO,anchor="center")  # Item column for 20 characters
detail.column(2, width=150, minwidth=150, stretch=tk.NO,anchor="center")  # Qty column
detail.column(3, width=150, minwidth=150, stretch=tk.NO,anchor="center")  # Unit price column
detail.column(4, width=150, minwidth=150, stretch=tk.NO,anchor="center")
detail.column(5, width=150, minwidth=150, stretch=tk.NO,anchor="center")  # Discount column for 3 characters
detail.column(6, width=250, minwidth=250, stretch=tk.YES,anchor="center")  # Subtotal column

scroll_y1 = ttk.Scrollbar(detail_frame, orient=tk.VERTICAL, command=detail.yview)
detail.configure(yscrollcommand=scroll_y1.set)
scroll_y1.grid(row=1, column=6, sticky="ns")
detail.bind("<Double-1>", on_detail_click)

# Create a new frame for the buttons
button_frame = tk.Frame(detail_frame,bg="lightgrey")
button_frame.grid(row=2, column=0, columnspan=7, sticky="e", padx=10, pady=10)

# Add buttons to the new frame
back = tk.Button(button_frame, text="Back", pady=5, padx=10, command=Back1)
back.pack(side="right", padx=5)
log = tk.Button(button_frame, text="Logout", pady=5, padx=10, command=log_out)
log.pack(side="right", padx=5)
day = tk.Button(button_frame, text="End Day", pady=5, padx=10, command=log_out)
day.pack(side="right", padx=5)

root.title("Sale")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

root.mainloop()
