class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited ₹{amount}. New Balance: ₹{self.balance}")
        else:
            print("❌ Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient funds.")
        elif amount <= 0:
            print("❌ Enter valid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"✅ Withdrew ₹{amount}. New Balance: ₹{self.balance}")

    def show_balance(self):
        print(f"💰 {self.name}, your current balance is ₹{self.balance}")


# Dictionary to store multiple accounts
accounts = {}

# Main loop
while True:
    print("\n🏦 Welcome to Python Bank System")
    print("1. Create New Account")
    print("2. Login to Account")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        name = input("Enter new user name: ").strip()
        if name in accounts:
            print("⚠️ Account already exists!")
        else:
            accounts[name] = BankAccount(name)
            print(f"✅ Account created for {name}!")

    elif choice == "2":
        name = input("Enter your username: ").strip()
        if name not in accounts:
            print("❌ Account not found.")
        else:
            account = accounts[name]
            while True:
                print(f"\n👋 Hello {name}!")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Show Balance")
                print("4. Logout")

                action = input("Choose an option (1-4): ")

                if action == "1":
                    amt = float(input("Enter amount to deposit: ₹"))
                    account.deposit(amt)
                elif action == "2":
                    amt = float(input("Enter amount to withdraw: ₹"))
                    account.withdraw(amt)
                elif action == "3":
                    account.show_balance()
                elif action == "4":
                    print("🔒 Logged out successfully.")
                    break
                else:
                    print("❌ Invalid choice.")

    elif choice == "3":
        print("👋 Thank you for using Python Bank. Goodbye!")
        break
    else:
        print("❌ Invalid input. Try again.")
