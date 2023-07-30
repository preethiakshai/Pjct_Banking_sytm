class BankAccount:
    def __init__(self, User_name, pwd):
        self.User_name = User_name
        self.pwd = pwd
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}")
        print(f"Transaction Completed Successfully. Current Balance is Rupees: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn: ${amount}")
            print(f" Transaction Completed Successfully. Current Balance is Rupees: {self.balance}")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print(f"Account Balance: ${self.balance}")


def create_account():
    print("Welcome to the Bank Account Creation!")
    User_name = input("Enter your desired user name: ")


    while True:
        pwd = input("Set a password for your account(5 digit): ")
        if len(pwd) == 5:
            break
        print("Invalid Password")

    return BankAccount(User_name, pwd)


def login(accounts):
    print("Login to your Bank Account.")
    User_name = input("Enter your user name: ")
    pwd = input("Password: ")


    for account in accounts:
        if account.User_name == User_name and account.pwd == pwd:
            return account

    print("Invalid account number or Password.")
    return None


def main():
    accounts = []
    while True:
        print("\n Welcome To Banking System ")
        print("1. Create a New Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            account = create_account()
            accounts.append(account)
            print("Account created successfully!")

        elif choice == '2':
            if not accounts:
                print("No accounts created yet. Please create an account first.")
                continue

            account = login(accounts)
            if account:
                while True:
                    print("\n WELCOME TO THE HOME PAGE ")
                    print("1. Deposit Amount")
                    print("2. Withdraw Amount")
                    print("3. Check Account Balance")
                    print("4. Logout")
                    option = input("Enter your option: ")

                    if option == '1':
                        amount = float(input("Enter the amount to deposit: "))
                        account.deposit(amount)

                    elif option == '2':
                        amount = float(input("Enter the amount to withdraw: "))
                        account.withdraw(amount)

                    elif option == '3':
                        account.check_balance()

                    elif option == '4':
                        print("Logged out successfully.")
                        break

                    else:
                        print("Invalid option. Please try again.")

        elif choice == '3':
            print("Thank you for using our Banking System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()