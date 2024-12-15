import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Detail frame at the bottom
detail_frame = tk.LabelFrame(root, bg="lightgrey", height=100, font=("Arial", 11))
detail_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=2, ipady=10)

# Configure the detail frame grid
detail_frame.grid_columnconfigure(0, weight=1)  # Make the first column expandable
detail_frame.grid_columnconfigure(1, weight=0)
detail_frame.grid_columnconfigure(2, weight=0)
detail_frame.grid_columnconfigure(3, weight=0)
detail_frame.grid_rowconfigure(0, weight=1)  # First row for search and buttons
detail_frame.grid_rowconfigure(1, weight=4)  # Second row for Treeview

# Search and buttons
Src1_ent = tk.Entry(detail_frame, font=("Arial", 9))
Src1_ent.grid(row=0, column=0, padx=2, pady=2, sticky="ew")  # Make the entry expandable
Src1_ent.bind("<Return>", lambda event: Search1())
Src_btn = tk.Button(detail_frame, text="Search", pady=3, padx=5)
Src_btn.grid(row=0, column=1, padx=2, pady=2)
Srcclr_btn = tk.Button(detail_frame, text="Clear", pady=3, padx=5)
Srcclr_btn.grid(row=0, column=2, padx=2, pady=2)

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
detail.column(1, width=200, minwidth=200, stretch=tk.NO)  # Item column for 20 characters
detail.column(2, width=100, minwidth=100, stretch=tk.NO)  # Qty column
detail.column(3, width=100, minwidth=100, stretch=tk.NO)  # Unit price column
detail.column(4, width=100, minwidth=100, stretch=tk.NO)
detail.column(5, width=100, minwidth=100, stretch=tk.NO)  # Discount column for 3 characters
detail.column(6, width=150, minwidth=150, stretch=tk.YES)  # Subtotal column

scroll_y1 = ttk.Scrollbar(detail_frame, orient=tk.VERTICAL, command=detail.yview)
detail.configure(yscrollcommand=scroll_y1.set)
scroll_y1.grid(row=1, column=6, sticky="ns")


# Create a new frame for the buttons
button_frame = tk.Frame(detail_frame)
button_frame.grid(row=2, column=0, columnspan=7, sticky="e", padx=10, pady=10)

# Add buttons to the new frame
back = tk.Button(button_frame, text="Back", pady=5, padx=10)
back.pack(side="right", padx=5)
log = tk.Button(button_frame, text="Logout", pady=5, padx=10)
log.pack(side="right", padx=5)



root.mainloop()
