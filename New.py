from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="199603",
    database="test_1"

)

mycursor=mydb.cursor()

def table(rows):
    trv.delete(*trv.get_children())

    for i in rows:
        trv.insert("","end",values=i)
# Function to get the row count
def get_stock_count():
    mycursor.execute("SELECT COUNT(*) FROM stock_medicine")
    stock_count = mycursor.fetchone()[0]

    return stock_count
# Function to update stock count in StringVar
def update_stock_count(stock_var):
    stock_count = get_stock_count()
    stock_var.set(f"Stock Count: {stock_count}")
def Search():
    q2 = q.get()
    if q2=="":
        messagebox.showinfo("Empty","Search box is empty")
    else:

        try:

            query = "select * from stock_medicine where barcode like '%"+q2+"%' or name like '%"+q2+"%'"
            mycursor.execute(query)
            rows = mycursor.fetchall()
            table(rows)
        except Exception as e:
            messagebox.showerror("Not Found",f"Stock not found :{e}")
def add():
    if t1.get()=="" or t2.get()=="" or t3.get()=="" or t4.get()=="" or t5.get()=="" or t6.get()=="" or t7.get()=="" or t9.get()=="" or t10.get()==""or t11.get()==""or t12.get()==""or t13.get()==""or t14.get()==""or t15.get()=="":
        messagebox.showerror("Error","Please provide all details")
    else:
        query = "SELECT * FROM stock_medicine WHERE barcode=%s or name=%s"
        mycursor.execute(query, (
            t1.get(), t2.get()))
        row = mycursor.fetchall()
        if not row:


            try:
                query="insert into stock_medicine(barcode,name,expdate,quantity,free,totalcost,cost,mincost,sell,profit,minsell,maxsell,reminderquantity,reminderdate) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(query,(t1.get(),t2.get(),t3.get(),t4.get(),t5.get(),t6.get(),t14.get(),t15.get(),t13.get(),t7.get(),t9.get(),t10.get(),t11.get(),t12.get()))
                mydb.commit()
                query = "set @autoid:=0"
                mycursor.execute(query)
                query = "update stock_medicine set id=@autoid:=(@autoid+1)"
                mycursor.execute(query)
                query = "alter table stock_medicine auto_increment=1"
                mycursor.execute(query)

                query = "select id,barcode,name,expdate,quantity,free,totalcost,cost,mincost,sell,profit,minsell,maxsell,reminderquantity,reminderdate from stock_medicine"
                mycursor.execute(query)
                rows = mycursor.fetchall()
                table(rows)
                update_stock_count(stock_var)

                messagebox.showinfo("Success", "Stock added successfully")
                Clear()

            except Exception as e:
                messagebox.showerror("Error",f"Something went wrong : {e}")
        else:
            messagebox.showerror("Error","Recheck your Barcode and Name")
def update():
    if t1.get() == "" or t2.get() == "" or t3.get() == "" or t4.get() == "" or t5.get() == "" or t6.get() == "" or t7.get() == "" or t9.get() == "" or t10.get() == "" or t11.get() == "" or t12.get() == "" or t13.get() == "" or t14.get() == "" or t15.get() == "":
        messagebox.showerror("Error", "Please provide all details")
    else:
        try:
            query = "SELECT * FROM stock_medicine WHERE barcode=%s"
            mycursor.execute(query, (t1.get(),))
            row = mycursor.fetchone()

            if not row:
                messagebox.showerror("Error", "Stock not found")
            else:
                # Check if the data to be updated is the same as the current data
                current_data_query = "SELECT * FROM stock_medicine WHERE barcode=%s AND name=%s AND expdate=%s AND quantity=%s AND free=%s AND totalcost=%s AND profit=%s AND minsell=%s AND maxsell=%s"
                mycursor.execute(current_data_query, (t1.get(), t2.get(), t3.get(), t4.get(), t5.get(), t6.get(), t7.get(), t9.get(), t10.get()))
                current_data = mycursor.fetchone()

                if current_data:
                    messagebox.showinfo("Same data", "Trying to update with the same data")
                else:
                    if messagebox.askyesno("Confirm", "Do you really want to update the stock?"):
                        try:
                            # Update the stock with new data
                            update_query = """
                            UPDATE stock_medicine 
                            SET name=%s, expdate=%s, quantity=%s, free=%s, totalcost=%s, cost=%s, mincost=%s, sell=%s, profit=%s, minsell=%s, maxsell=%s, reminderquantity=%s, reminderdate=%s 
                            WHERE barcode=%s
                            """
                            mycursor.execute(update_query, (
                                t2.get(), t3.get(), t4.get(), t5.get(), t6.get(), t14.get(), t15.get(), t13.get(), t7.get(), t9.get(), t10.get(), t11.get(), t12.get(), t1.get()
                            ))
                            mydb.commit()

                            # Refresh the table
                            refresh_query = "SELECT id, barcode, name, expdate, quantity, free, totalcost, cost, mincost, sell, profit, minsell, maxsell, reminderquantity, reminderdate FROM stock_medicine"
                            mycursor.execute(refresh_query)
                            rows = mycursor.fetchall()
                            table(rows)

                            messagebox.showinfo("Success", "Stock updated successfully")
                            Clear()
                        except Exception as e:
                            messagebox.showerror("Error", f"Error updating stock: {e}")

        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")
def delete():
    bar=t1.get()
    if t1.get()==""or t2.get()=="":
        messagebox.showinfo("Empty","Fields are empty")
    elif messagebox.askyesno("Confirm","Do you really want to delete this stock?"):
        try:
            query="delete from stock_medicine where barcode= %s"
            mycursor.execute(query,(bar,))
            query="set @autoid:=0"
            mycursor.execute(query)
            query="update stock_medicine set id=@autoid:=(@autoid+1)"
            mycursor.execute(query)
            query="alter table stock_medicine auto_increment=1"
            mycursor.execute(query)
            query = "select id,barcode,name,expdate,quantity,free,totalcost,cost,mincost,sell,profit,minsell,maxsell,reminderquantity,reminderdate from stock_medicine"
            mycursor.execute(query)
            rows = mycursor.fetchall()
            table(rows)
            update_stock_count(stock_var)
            Clear()
        except EXCEPTION as e:
            messagebox.showerror("Error",f"Couldn't delete the stock:{e}")
def ok():
    t8 = var.get()
    qty = t4.get()
    fre = t5.get()
    buy = t6.get()
    pro = t7.get()
    cost = t14.get()

    if t8 == 1:
        if qty == "" or fre == "" or (buy == "" and cost == "") or pro == "":
            messagebox.showerror("Error", "Please re-check the entries")
        else:
            try:
                qty = float(qty)
                fre = float(fre)
                pro = float(pro)

                if buy != "":
                    buy = float(buy)
                if cost != "":
                    cost = float(cost)

                if buy != "" and cost == "":
                    max_price = (buy / qty) * (1 + pro / 100)
                    min_price = (buy / (qty + fre)) * (1 + pro / 100)
                    ent9.delete(0, END)
                    ent9.insert(0, round(float(min_price),2))
                    ent10.delete(0, END)
                    ent10.insert(0, round(float(max_price),2))

                    cost_per_unit = buy / qty
                    min_cost=buy/(qty+fre)
                    ent14.delete(0, END)
                    ent14.insert(0, round(float(cost_per_unit),2))
                    ent15.delete(0, END)
                    ent15.insert(0, round(float(min_cost),2))

                elif buy == "" and cost != "":
                    total_buy = qty * cost
                    max_price = (total_buy / qty) * (1 + pro / 100)
                    min_price = (total_buy / (qty + fre)) * (1 + pro / 100)
                    ent9.delete(0, END)
                    ent9.insert(0, round(float(min_price),2))
                    ent10.delete(0, END)
                    ent10.insert(0, round(float(max_price),2))
                    min_cost = total_buy / (qty + fre)
                    ent6.delete(0, END)
                    ent6.insert(0, round(float(total_buy),2))
                    ent15.delete(0, END)
                    ent15.insert(0, round(float(min_cost),2))

                else:
                    max_price = (buy / qty) * (1 + pro / 100)
                    min_price = (buy / (qty + fre)) * (1 + pro / 100)
                    ent9.delete(0, END)
                    ent9.insert(0, round(float(min_price),2))
                    ent10.delete(0, END)
                    ent10.insert(0, round(float(max_price),2))



            except ValueError:
                messagebox.showerror("Error", "Invalid input for quantity, buy price, or profit")
def getrow(event):
    rowid=trv.identify_row(event.y)
    item=trv.item(trv.focus())
    t1.set(item["values"][1])
    t2.set(item["values"][2])
    t3.set(item["values"][3])
    t4.set(item["values"][4])
    t5.set(item["values"][5])
    t6.set(item["values"][6])
    t7.set(item["values"][10])
    t9.set(item["values"][11])
    t10.set(item["values"][12])
    t11.set(item["values"][13])
    t12.set(item["values"][14])
    t13.set(item["values"][9])
    t14.set(item["values"][7])
    t15.set(item["values"][8])
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"
def Clear():
    ent1.delete(0,END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)
    ent5.delete(0, END)
    ent6.delete(0, END)
    ent7.delete(0, END)
    ent9.delete(0, END)
    ent10.delete(0, END)
    ent11.delete(0, END)
    ent12.delete(0, END)
    ent13.delete(0, END)
    ent14.delete(0, END)
    ent15.delete(0, END)
    e.deselect()
def Clear_Stock():

    query = "select id,barcode,name,expdate,quantity,free,totalcost,cost,mincost,sell,profit,minsell,maxsell from stock_medicine"
    mycursor.execute(query)
    rows = mycursor.fetchall()
    table(rows)
def Back():
    root.destroy()
def validate_Quantity(event):
    quantity=ent4.get()
    free=ent5.get()
    profit=ent7.get()
    if quantity.isdigit() or quantity=="":
        ent4.delete(0,tk.END)
        ent4.insert(0,quantity)
    else:
        messagebox.showerror("Error","Quantity should be a number")
        ent4.delete(0,tk.END)
    if free.isdigit() or free=="":
        ent5.delete(0,tk.END)
        ent5.insert(0,free)
    else:
        messagebox.showerror("Error","Free should be a number")
        ent5.delete(0,tk.END)
    try:
        if float(profit)<100 or profit=="":
            ent7.delete(0,tk.END)
            ent7.insert(0,profit)
        else:
            messagebox.showerror("Error","Check profit again")
            ent7.delete(0,tk.END)
    except ValueError:
        messagebox.showerror("Error","Invalid values")
        ent7.delete(0,tk.END)

root = Tk()
style = ttk.Style(root)
style.theme_use("default")
var = IntVar()

q = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()
t7 = StringVar()
t9 = StringVar()
t10 = StringVar()
t11 = StringVar()
t12 = StringVar()
t13 = StringVar()
t14 = StringVar()
t15 = StringVar()
stock_var=StringVar()

wrapper1 = LabelFrame(root, text="Stock details")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="Manage stock")

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

# Stock Details
trv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13), show="headings", height="10")
trv.grid(row=0, column=0, sticky='nsew')
trv.heading(1, text="No")
trv.heading(2, text="Barcode")
trv.heading(3, text="Name")
trv.heading(4, text="Exp_date")
trv.heading(5, text="Quantity")
trv.heading(6, text="Free")
trv.heading(7, text="TotalCost")
trv.heading(8, text="Cost")
trv.heading(9, text="Min.cost")
trv.heading(10, text="Sell.price")
trv.heading(11, text="Profit")
trv.heading(12, text="Min.price")
trv.heading(13, text="Max.price")

trv.column(1, width=50, minwidth=50, stretch=tk.NO,anchor="center")
trv.column(2, width=150, minwidth=150, stretch=tk.NO,anchor="center")
trv.column(3, width=300, minwidth=300, stretch=tk.NO,anchor="center")
trv.column(4, width=100, minwidth=100, stretch=tk.NO,anchor="center")
trv.column(5, width=75, minwidth=75, stretch=tk.NO,anchor="center")
trv.column(6, width=100, minwidth=100, stretch=tk.NO,anchor="center")
trv.column(7, width=100, minwidth=100, stretch=tk.NO,anchor="center")
trv.column(8, width=100, minwidth=100, stretch=tk.NO,anchor="center")
trv.column(9, width=100, minwidth=100, stretch=tk.NO,anchor="center")
trv.column(10, width=100, minwidth=100, stretch=tk.NO,anchor="center")
trv.column(11, width=100, minwidth=100, stretch=tk.NO,anchor="center")
trv.column(12, width=100, minwidth=100, stretch=tk.NO,anchor="center")
trv.column(13, width=100, minwidth=100, stretch=tk.NO,anchor="center")
trv.bind("<Double 1>",getrow)

query = "select id,barcode,name,expdate,quantity,free,totalcost,cost,mincost,sell,profit,minsell,maxsell,reminderquantity,reminderdate from stock_medicine"
mycursor.execute(query)
rows = mycursor.fetchall()
table(rows)
# Create Scrollbars
scroll_y = tk.Scrollbar(wrapper1, orient=tk.VERTICAL, command=trv.yview)
scroll_x = tk.Scrollbar(wrapper1, orient=tk.HORIZONTAL, command=trv.xview)
trv.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

# Place Scrollbars
scroll_y.grid(row=0, column=1, sticky='ns')
scroll_x.grid(row=1, column=0, sticky='ew')

# Configure wrapper1 to resize with the window
wrapper1.grid_rowconfigure(0, weight=1)
wrapper1.grid_columnconfigure(0, weight=1)

# Searching Option
lbl = Label(wrapper2, text="Search").pack(side=tk.LEFT, padx=10)
ent = tk.Entry(wrapper2, textvariable=q)
ent.pack(side=tk.LEFT, padx=10)
btn = Button(wrapper2, text="Search", command=Search).pack(side=tk.LEFT, padx=10)
btn = Button(wrapper2, text="Clear", command=Clear_Stock).pack(side=tk.LEFT, padx=10)
ent.bind("<Return>",lambda event:Search())

# Managing
lbl1 = tk.Label(wrapper3, text="Barcode")
lbl1.grid(row=1, column=0, padx=5, pady=3)
ent1 = tk.Entry(wrapper3, textvariable=t1)
ent1.grid(row=1, column=1, padx=5, pady=3)
ent1.bind("<Return>", lambda event:add())
ent1.bind("<Down>", focus_next_widget)
ent1.focus_set()

lbl2 = tk.Label(wrapper3, text="Name")
lbl2.grid(row=2, column=0, padx=5, pady=3)
ent2 = tk.Entry(wrapper3, textvariable=t2)
ent2.grid(row=2, column=1, padx=5, pady=3)
ent2.bind("<Return>", lambda event:add())
ent2.bind("<Down>", focus_next_widget)

lbl3 = tk.Label(wrapper3, text="Exp_date\n(yyyy-mm-dd)")
lbl3.grid(row=3, column=0, padx=5, pady=3)
ent3 = tk.Entry(wrapper3, textvariable=t3)
ent3.grid(row=3, column=1, padx=5, pady=3)
ent3.bind("<Return>", lambda event:add())
ent3.bind("<Down>", focus_next_widget)

lbl4 = tk.Label(wrapper3, text="Quantity")
lbl4.grid(row=4, column=0, padx=5, pady=3)
ent4 = tk.Entry(wrapper3, textvariable=t4)
ent4.grid(row=4, column=1, padx=5, pady=3)
ent4.bind("<Return>", lambda event:add())
ent4.bind("<Down>", focus_next_widget)
ent4.bind("<KeyRelease>",validate_Quantity)

lbl5 = tk.Label(wrapper3, text="Free")
lbl5.grid(row=5, column=0, padx=5, pady=3)
ent5 = tk.Entry(wrapper3, textvariable=t5)
ent5.grid(row=5, column=1, padx=5, pady=3)
ent5.bind("<Return>", lambda event:add())
ent5.bind("<Down>", focus_next_widget)
ent5.bind("<KeyRelease>",validate_Quantity)

lbl7 = tk.Label(wrapper3, text="Profit(%)")
lbl7.grid(row=1, column=2, padx=5, pady=3)
ent7 = tk.Entry(wrapper3, textvariable=t7)
ent7.grid(row=1, column=3, padx=5, pady=3)
ent7.bind("<Return>", lambda event:add())
ent7.bind("<Down>", focus_next_widget)
ent7.bind("<KeyRelease>",validate_Quantity)

lbl6 = tk.Label(wrapper3, text="Total Cost\nLKR")
lbl6.grid(row=2, column=2, padx=5, pady=3)
ent6 = tk.Entry(wrapper3, textvariable=t6)
ent6.grid(row=2, column=3, padx=5, pady=3)
ent6.bind("<Return>", lambda event:add())
ent6.bind("<Down>", focus_next_widget)

lbl14 = tk.Label(wrapper3, text="Cost\nLKR")
lbl14.grid(row=3, column=2, padx=5, pady=3)
ent14 = tk.Entry(wrapper3, textvariable=t14)
ent14.grid(row=3, column=3, padx=5, pady=3)
ent14.bind("<Return>", lambda event:add())
ent14.bind("<Down>", focus_next_widget)

lbl15 = tk.Label(wrapper3, text="Min.cost\nLKR")
lbl15.grid(row=4, column=2, padx=5, pady=3)
ent15 = tk.Entry(wrapper3, textvariable=t15)
ent15.grid(row=4, column=3, padx=5, pady=3)
ent15.bind("<Return>", lambda event:add())
ent15.bind("<Down>", focus_next_widget)

lbl9 = tk.Label(wrapper3, text="Min.Sell_pr\nLKR")
lbl9.grid(row=1, column=4, padx=5, pady=3)
ent9 = tk.Entry(wrapper3, textvariable=t9)
ent9.grid(row=1, column=5, padx=5, pady=3)
ent9.bind("<Return>", lambda event:add())
ent9.bind("<Down>", focus_next_widget)

lbl10 = tk.Label(wrapper3, text="Max.Sell_pr\nLKR")
lbl10.grid(row=2, column=4, padx=5, pady=3)
ent10 = tk.Entry(wrapper3, textvariable=t10)
ent10.grid(row=2, column=5, padx=5, pady=3)
ent10.bind("<Return>", lambda event:add())
ent10.bind("<Down>", focus_next_widget)

lbl13 = tk.Label(wrapper3, text="Sell_pr\nLKR")
lbl13.grid(row=3, column=4, padx=5, pady=3)
ent13 = tk.Entry(wrapper3, textvariable=t13)
ent13.grid(row=3, column=5, padx=5, pady=3)
ent13.bind("<Return>", lambda event:add())
ent13.bind("<Down>", focus_next_widget)

lbl11 = tk.Label(wrapper3, text="Set quantity\nReminder")
lbl11.grid(row=1, column=6, padx=5, pady=3)
ent11 = tk.Entry(wrapper3, textvariable=t11)
ent11.grid(row=1, column=7, padx=5, pady=3)
ent11.bind("<Return>", lambda event:add())
ent11.bind("<Down>", focus_next_widget)

lbl12 = tk.Label(wrapper3, text="Set Exp_date\nReminder\n(yyyy-mm-dd)")
lbl12.grid(row=2, column=6, padx=5, pady=3)
ent12 = tk.Entry(wrapper3, textvariable=t12)
ent12.grid(row=2, column=7, padx=5, pady=3)
ent12.bind("<Return>", lambda event:add())
ent12.bind("<Down>", focus_next_widget)

e = tk.Checkbutton(wrapper3, text="Auto Calculate", variable=var, onvalue=1, offvalue=0)
e.grid(row=5, column=2, padx=5, pady=3, columnspan=2)
e.select()

ok_btn = tk.Button(wrapper3, text="OK", command=ok)
ok_btn.grid(row=5, column=3, padx=15, pady=15, columnspan=2)

Add_btn = tk.Button(wrapper3, text="Add New", command=add)
Add_btn.grid(row=6, column=1, padx=25, pady=5)
up_btn = tk.Button(wrapper3, text="Update", command=update)
up_btn.grid(row=6, column=2, padx=25, pady=5)
del_btn = tk.Button(wrapper3, text="Delete", command=delete)
del_btn.grid(row=6, column=3, padx=25, pady=5)
clr1_btn = tk.Button(wrapper3, text="Clear", command=Clear)
clr1_btn.grid(row=6, column=4, padx=25, pady=5)
Back_btn = tk.Button(wrapper3, text="Back", command=Back)
Back_btn.grid(row=6, column=0, padx=25, pady=5)


update_stock_count(stock_var)
stock = tk.Label(root,textvariable=stock_var, bd=1, relief=SUNKEN, anchor=E)
stock.pack(fill=tk.X, expand="yes", padx=20, pady=5)


root.title("Stock")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.mainloop()
