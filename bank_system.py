import tkinter as tk
from tkinter import messagebox, ttk

class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, username, initial_deposit):
        if username in self.accounts:
            return "Account already exists!"
        else:
            self.accounts[username] = float(initial_deposit)
            return "Account created successfully!"

    def deposit(self, username, amount):
        if username in self.accounts:
            self.accounts[username] += float(amount)
            return f"Deposited {amount}. New Balance: {self.accounts[username]:.2f}"
        else:
            return "Account not found!"

    def withdraw(self, username, amount):
        if username in self.accounts:
            if float(amount) > self.accounts[username]:
                return "Insufficient balance!"
            else:
                self.accounts[username] -= float(amount)
                return f"Withdrew {amount}. New Balance: {self.accounts[username]:.2f}"
        else:
            return "Account not found!"

    def check_balance(self, username):
        if username in self.accounts:
            return f"Current Balance: {self.accounts[username]:.2f}"
        else:
            return "Account not found!"

class BankApp:
    def __init__(self, root):
        self.bank = BankSystem()
        self.root = root
        self.root.title("BPI-Like Bank System")
        self.root.geometry("600x500")
        self.root.config(bg="#F2E8C9")  # BPI Light Beige Background
        self.style_widgets()
        self.main_menu()

    def style_widgets(self):
        # Create a style for buttons with a red background and white text
        self.style = ttk.Style()
        self.style.configure(
            "Red.TButton",
            font=("Arial", 12, "bold"),
            background="#8A1538",
            foreground="white",
            padding=10
        )
        self.style.map("Red.TButton",
                       background=[("active", "#6E122E")],  # Darker red on hover
                       foreground=[("active", "white")])

    def main_menu(self):
        self.clear_window()

        # Header with BPI-like color
        header = tk.Frame(self.root, bg="#8A1538", height=70)
        header.pack(fill="x")
        tk.Label(header, text="BPI Bank System", fg="white", bg="#8A1538",
                 font=("Helvetica", 20, "bold")).pack(pady=15)

        # Menu Content
        tk.Label(self.root, text="Welcome to BPI Bank System", bg="#F2E8C9",
                 font=("Arial", 16, "bold"), fg="#8A1538").pack(pady=20)

        ttk.Button(self.root, text="Create Account", command=self.create_account_screen, style="Red.TButton").pack(pady=10)
        ttk.Button(self.root, text="Deposit", command=self.deposit_screen, style="Red.TButton").pack(pady=10)
        ttk.Button(self.root, text="Withdraw", command=self.withdraw_screen, style="Red.TButton").pack(pady=10)
        ttk.Button(self.root, text="Check Balance", command=self.balance_screen, style="Red.TButton").pack(pady=10)
        ttk.Button(self.root, text="Exit", command=self.root.quit, style="Red.TButton").pack(pady=10)

        # Footer
        tk.Label(self.root, text="© 2024 BPI-Inspired System", bg="#F2E8C9", fg="#8A1538", font=("Arial", 10)).pack(side="bottom", pady=10)

    def create_account_screen(self):
        self.form_template("Create Account", "Enter Username:", "Initial Deposit:", self.bank.create_account)

    def deposit_screen(self):
        self.form_template("Deposit", "Enter Username:", "Deposit Amount:", self.bank.deposit)

    def withdraw_screen(self):
        self.form_template("Withdraw", "Enter Username:", "Withdraw Amount:", self.bank.withdraw)

    def balance_screen(self):
        self.clear_window()
        self.header("Check Balance")

        tk.Label(self.root, text="Enter Username:", bg="#F2E8C9", fg="#8A1538", font=("Arial", 12, "bold")).pack(pady=10)
        username_entry = ttk.Entry(self.root)
        username_entry.pack(pady=5)

        def submit():
            username = username_entry.get()
            if username:
                result = self.bank.check_balance(username)
                messagebox.showinfo("Balance Inquiry", result)
                self.main_menu()
            else:
                messagebox.showerror("Error", "Username is required!")

        ttk.Button(self.root, text="Submit", command=submit, style="Red.TButton").pack(pady=10)
        ttk.Button(self.root, text="Back", command=self.main_menu, style="Red.TButton").pack(pady=5)

    def form_template(self, title, label1, label2, action):
        self.clear_window()
        self.header(title)

        tk.Label(self.root, text=label1, bg="#F2E8C9", fg="#8A1538", font=("Arial", 12, "bold")).pack(pady=5)
        entry1 = ttk.Entry(self.root)
        entry1.pack(pady=5)

        tk.Label(self.root, text=label2, bg="#F2E8C9", fg="#8A1538", font=("Arial", 12, "bold")).pack(pady=5)
        entry2 = ttk.Entry(self.root)
        entry2.pack(pady=5)

        def submit():
            value1 = entry1.get()
            value2 = entry2.get()
            if value1 and value2:
                result = action(value1, value2)
                messagebox.showinfo(title, result)
                self.main_menu()
            else:
                messagebox.showerror("Error", "All fields are required!")

        ttk.Button(self.root, text="Submit", command=submit, style="Red.TButton").pack(pady=10)
        ttk.Button(self.root, text="Back", command=self.main_menu, style="Red.TButton").pack(pady=5)

    def header(self, text):
        header = tk.Frame(self.root, bg="#8A1538", height=70)
        header.pack(fill="x")
        tk.Label(header, text=text, fg="white", bg="#8A1538", font=("Helvetica", 20, "bold")).pack(pady=15)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
