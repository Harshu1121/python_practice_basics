class BankAccount:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.pin = pin
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


# Dictionary to store accounts
accounts = {}

# Main system loop
while True:
    print("\n🏦 Python Bank Secure System")
    print("1. Create New Account")
    print("2. Login to Account")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        name = input("Enter new user name: ").strip()
        if name in accounts:
            print("⚠️ Account already exists!")
        else:
            pin = input("Set a 4-digit PIN: ").strip()
            if len(pin) == 4 and pin.isdigit():
                accounts[name] = BankAccount(name, pin)
                print(f"✅ Account created for {name} with secure PIN.")
            else:
                print("❌ PIN must be exactly 4 digits.")

    elif choice == "2":
        name = input("Enter your username: ").strip()
        if name not in accounts:
            print("❌ Account not found.")
        else:
            pin = input("Enter your 4-digit PIN: ").strip()
            if accounts[name].pin == pin:
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
                        print("🔒 Logged out.")
                        break
                    else:
                        print("❌ Invalid choice.")
            else:
                print("❌ Incorrect PIN!")

    elif choice == "3":
        print("👋 Thank you for using Python Bank. Bye!")
        break
    else:
        print("❌ Invalid input.")
