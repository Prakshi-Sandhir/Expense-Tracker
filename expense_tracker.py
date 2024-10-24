import sqlite3
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

con=sqlite3.connect("expense_db.db")
def create_tables():
    con.execute("create table expenses(expense_id int , amount int , category varchar(50));")
# create_tables()

window=tk.Tk()
window.title("EXPENSE_TRACKER")
window.geometry("1000x700") 
window.configure(bg="#FCF7FF")

label = tk.Label(window, text="EXPENSE TRACKER", font=("Britannic Bold", 25), bg="#FCF7FF")
label.pack(padx=20, pady=20) 

frame = tk.Frame(window, padx=10, pady=10, bg="#FCF7FF")
frame.pack(padx=10, pady=10)  # Adjust padding

tk.Label(frame, text="Select category: ", font=("Britannic Bold", 18), bg="#FCF7FF").grid(row=0, column=0, padx=10, pady=10, sticky="w")

frame1 = tk.Frame(frame, padx=10, pady=10, bg="#FCF7FF")
frame1.grid(row=0, column=1, padx=10, pady=10)  # Consistent with grid manager

selected_value = tk.StringVar(value="")

checkbox1 = tk.Checkbutton(frame1, text="Food🍟", variable=selected_value, onvalue="Food", font=("Britannic Bold", 15)).grid(row=0, column=0)
checkbox2 = tk.Checkbutton(frame1, text="Study📓", variable=selected_value, onvalue="Study", font=("Britannic Bold", 15)).grid(row=0, column=1)
checkbox3 = tk.Checkbutton(frame1, text="Travel🚐", variable=selected_value, onvalue="Travel", font=("Britannic Bold", 15)).grid(row=0, column=2)
checkbox5 = tk.Checkbutton(frame1, text="Calls📞", variable=selected_value, onvalue="Calls", font=("Britannic Bold", 15)).grid(row=1, column=0)
checkbox6 = tk.Checkbutton(frame1, text="Savings🏦", variable=selected_value, onvalue="Savings", font=("Britannic Bold", 15)).grid(row=1, column=1)
checkbox7 = tk.Checkbutton(frame1, text="Health😷", variable=selected_value, onvalue="Health", font=("Britannic Bold", 15)).grid(row=1, column=2)

tk.Label(frame, text="Enter Amount: ", font=("Britannic Bold", 18), bg="#FCF7FF").grid(row=1, column=0, padx=10, pady=10, sticky="w")
amt = tk.Entry(frame, width=10,font=("Britannic Bold", 15))
amt.grid(row=1, column=1, padx=10, pady=10, sticky="w")

def add_exp():
    try:
        amount = int(amt.get())
        category = selected_value.get()
        print(category)
        if category != '0' and category != "":
            amount = amt.get()
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format current date and time

            con.execute("INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)", (amount, category, current_date))
            con.commit()
            messagebox.showinfo("Success", "Expense Added:)")
        else:
             messagebox.showerror("Error","Please select category!!🙂‍↕️")
    except ValueError:
        messagebox.showerror("Error","Enter Valid Amount!🥲")


add_button = tk.Button(frame, text="Add", command=add_exp,font=("Britannic Bold", 10))
add_button.grid(row=2, column=0, columnspan=2)

def open_transactions_window():
    # Check if the Treeview already exists and remove it before creating a new one
    if hasattr(open_transactions_window, 'tree'):
        open_transactions_window.tree.destroy()
    
    # Create a Treeview widget to display transactions
    open_transactions_window.tree = ttk.Treeview(window, columns=('Expense ID', 'Amount', 'Category', 'Date'), show='headings', height=8)
    open_transactions_window.tree.heading('Expense ID', text='Expense ID')
    open_transactions_window.tree.heading('Amount', text='Amount')
    open_transactions_window.tree.heading('Category', text='Category')
    open_transactions_window.tree.heading('Date', text='Date')

    # Format and place the Treeview below the button
    open_transactions_window.tree.pack(padx=20, pady=20, fill=tk.X)

    # Retrieve data from the database and insert it into the Treeview
    cursor = con.execute("SELECT * FROM expenses")
    for row in cursor:
        open_transactions_window.tree.insert('', tk.END, values=row)


transaction_button = tk.Button(window, text="Show Transactions", command=open_transactions_window, font=("Britannic Bold", 10))
transaction_button.pack(pady=20)


def show_pie_chart():
    cursor = con.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cursor.fetchall()
    
    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    fig = Figure(figsize=(6, 6))
    ax = fig.add_subplot(111)
    ax.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
    ax.set_title("Expenses by Category")
    
    chart_window = tk.Toplevel(window)
    chart_window.title("Pie Chart")
    chart_window.geometry("800x500")
    
    canvas = FigureCanvasTkAgg(fig, master=chart_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

def show_bar_chart():
    cursor = con.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cursor.fetchall()

    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    fig = Figure(figsize=(6, 4))
    ax = fig.add_subplot(111)

    # Set the width of the bars to make them thinner
    ax.bar(categories, amounts, width=0.5) 

    ax.bar(categories, amounts)
    ax.set_title("Expenses by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Amount")

    chart_window = tk.Toplevel(window)
    chart_window.title("Bar Chart")
    chart_window.geometry("800x600")

    canvas = FigureCanvasTkAgg(fig, master=chart_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

pie_chart_button = tk.Button(window, text="Show Pie Chart", command=show_pie_chart, font=("Britannic Bold", 10))
pie_chart_button.pack(pady=20)

bar_chart_button = tk.Button(window, text="Show Bar Chart", command=show_bar_chart, font=("Britannic Bold", 10))
bar_chart_button.pack(pady=20)

window.mainloop()




