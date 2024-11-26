import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox

# Connect to MySQL database
try:
    conn = mysql.connector.connect(
        host='your_host',       
        database='your_database', 
        user='your_user',         
        password='your_password'  
    )
    if conn.is_connected():
        cursor = conn.cursor()
        print("Connected to MySQL database")
except Error as e:
    print(f"Error: {e}")
    messagebox.showerror("Database Connection Error", str(e))

class Bank:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = self.get_balance_from_db()

    def get_balance_from_db(self):
        cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (self.account_number,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            raise Exception("Account not found")

    def update_balance_in_db(self):
        cursor.execute("UPDATE accounts SET balance = %s WHERE account_number = %s", (self.balance, self.account_number))
        conn.commit()

    def credit(self, amount):
        self.balance += amount
        self.update_balance_in_db()

    def debit(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient Funds")
        self.balance -= amount
        self.update_balance_in_db()

    def get_balance(self):
        return self.balance

class Transaction(Bank):
    def __init__(self, account_number):
        super().__init__(account_number)

    def transfer(self, amount, target_account_number):
        target_account = Bank(target_account_number)
        if self.balance < amount:
            raise Exception("Insufficient Funds")
        self.debit(amount)
        target_account.credit(amount)

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient Funds")
        self.debit(amount)
# modification of the tkinter 
def deposit_amount():
    try:
        account_number = account_entry.get()
        amount = float(amount_entry.get())
        account = Transaction(account_number)
        account.credit(amount)
        result_label.config(text=f"New Balance: {account.get_balance()}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def withdraw_amount():
    try:
        account_number = account_entry.get()
        amount = float(amount_entry.get())
        account = Transaction(account_number)
        account.withdraw(amount)
        result_label.config(text=f"New Balance: {account.get_balance()}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def transfer_amount():
    try:
        sender_account_number = sender_entry.get()
        receiver_account_number = receiver_entry.get()
        amount = float(amount_entry.get())
        sender_account = Transaction(sender_account_number)
        sender_account.transfer(amount, receiver_account_number)
        result_label.config(text="Transfer successful")
    except Exception as e:
        messagebox.showerror("Error", str(e))

window = tk.Tk()        
window.title("SAPi-BANK")

# Create labels and entry fields
tk.Label(window, text="Sender Account Number").grid(row=0)
tk.Label(window, text="Receiver Account Number").grid(row=1)
tk.Label(window, text="Amount").grid(row=2)

sender_entry = tk.Entry(window)
receiver_entry = tk.Entry(window)
amount_entry = tk.Entry(window)

sender_entry.grid(row=0, column=1)
receiver_entry.grid(row=1, column=1)
amount_entry.grid(row=2, column=1)

tk.Button(window, text="Deposit", command=deposit_amount).grid(row=3, column=0)
tk.Button(window, text="Withdraw", command=withdraw_amount).grid(row=3, column=1)
tk.Button(window, text="Transfer", command=transfer_amount).grid(row=3, column=2)

result_label = tk.Label(window, text="")
result_label.grid(row=4, columnspan=3)

window.mainloop()
