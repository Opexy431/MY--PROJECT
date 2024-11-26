import tkinter as tk

window = tk.Tk()        
window.title("SAPi-BANK")

# Create labels and entry fields 
tk.Label(window, text="Account Number").grid(row=0)
tk.Label(window, text="Amount").grid(row=1)
tk.Label(window,text='pin').grid(row=2)

account_entry = tk.Entry(window)
amount_entry = tk.Entry(window)

account_entry.grid(row=0, column=1)
amount_entry.grid(row=1, column=1)

class Bank:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def credit(self, amount):
        self.balance += amount

    def debit(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient Funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance
# A SubClass of the class Bank 
class Transaction(Bank):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def transfer(self, amount, target_account):
        if self.balance < amount:
            raise Exception("Insufficient Funds")
        self.debit(amount)
        target_account.credit(amount)
        
    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient FUnds")
        self.debit(amount)

# Create an instance of the Transaction class
account = Transaction("123456", 5000)

def deposit_amount():
    try:
        amount = float(amount_entry.get())
        account.credit(amount)
        result_label.config(text=f"New Balance: {account.get_balance()}")
    except ValueError as e:
        result_label.config(text=str(e))

def withdraw_amount():
    try:
        amount = float(amount_entry.get())
        account.withdraw(amount)
        result_label.config(text=f"New Balance: {account.get_balance()}")
    except ValueError as e:
        result_label.config(text=str(e))

tk.Button(window, text="Deposit", command=deposit_amount).grid(row=2, column=0)
tk.Button(window, text="Withdraw", command=withdraw_amount).grid(row=2, column=1)

result_label = tk.Label(window, text="")
result_label.grid(row=3, columnspan=2)
# 
window.mainloop()

