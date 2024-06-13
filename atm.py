def check_balance(balance):
    print("Your Current Balance is:", balance, "Rupees only")

def deposit(balance):
    damount = int(input("Enter your Deposit amount: "))
    balance += damount
    print("Successfully Deposited")
    return balance

def withdraw(balance):
    amount = int(input("Enter the Withdrawal amount: "))
    if amount <= balance:
        balance -= amount
        print("Transaction Successful")
    else:
        print("Insufficient Balance")
    return balance

def main():
    pin = 1234
    balance = 1000000
    
    print('Insert your Card')
    confirm_pin = int(input("Enter Your Pin: "))

    if pin == confirm_pin:
        while True:
            print("\nEnter 1 for Balance Inquiry")
            print("Enter 2 for Money Withdrawal")
            print("Enter 3 for Money Deposit")
            print("Enter 4 to Exit")
            
            try:
                option = int(input("Select an option (1/2/3/4): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
                continue

            if option == 1:
                check_balance(balance)
            elif option == 2:
                balance = withdraw(balance)
            elif option == 3:
                balance = deposit(balance)
            elif option == 4:
                print("Thank You, Visit Again")
                break
            else:
                print("Invalid Option")
    else:
        print("Invalid PIN")

if __name__ == "__main__":
    main()
