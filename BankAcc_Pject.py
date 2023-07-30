class Bnk_Account:
    def __init__(self,account_type,Cash):
        self.account_type=account_type
        self.Cash=Cash
    def withdrw(self,Cash_withdraw): #Function for cash withdrawal
        if self.Cash>=Cash_withdraw:
            self.Cash -=Cash_withdraw
            print("Transaction completed. \n Your Current Balance Is:", self.Cash)
        else:
            print("Insufficient Balance")
    def Cash_deposit(self,Cash_Deposit):# Function for Cash Deposit
        self.Cash+=Cash_Deposit
        print("Available Balance is:",self.Cash)
#Creating new bank account
def New_Accnt():
    Name=input("Enter You Name with Surname:")
    Number=int(input("Enter valid Mobile Number:"))
    Address=input("Enter Your Contact Address:")
    account_type=input("Select Type of Account You wish to start SA, NRI, CA,NRE")
    Cash = float(input("Enter the initial amount that you want to deposit: "))
    return Name,Number, Address,Bnk_Account(account_type,Cash)
def login():
    accounts = {}  # to store name of account

    while True:
        choice = int(input("Press 1 for Login\nPress 2 for Creating a new account\n"))
        if choice == 1:
            user_name = input("Enter your User Name: ")
            if user_name in accounts:
                number, address, account = accounts[user_name]
                print(f"Welcome, {user_name}!")
                while True:
                    Activity = int(input("1. Balance\n2. Withdraw\n3. Deposit\n4. Account Details\n5. Logout\n"))
                    if Activity == 1:
                        print("Your Account Balance Is:", account.Cash)
                    elif Activity == 2:
                        with_amnt = float(input("Enter the amount to be withdrawn: "))
                        account.withdrw(with_amnt)


                    elif Activity == 3:
                        dep_amunt = float(input("Enter the amount to be deposited: "))
                        account.Cash_deposit(dep_amunt)

                    elif Activity == 4:
                        print("Account Details:")
                        print(f"Name: {user_name}")
                        print(f"Account Type: {account.account_type}")
                        print(f"Amount: {account.Cash}")
                    elif Activity == 5:
                        break
                    else:
                        print("Invalid Input")
            else:
                print("Account Not Found")
                choice = int(input("Do you want to Create An Account Here?\n Press 2"))


        elif choice == 2:
            name, number, address, type = New_Accnt()
            accounts[name] = (number, address, type)
            print("Your Account Is Created Successfully")
        else:
            print("Invalid option")


login()