def withdraw(balance, pin):
    epin = int(input("Enter your pin: "))
    if epin == pin:
        amt = int(input("Enter the amount to withdraw: "))
        if amt <= balance:
            print("Transaction successful")
            balance -= amt
        else:
            print("Low balance")
    else:
        print("Wrong pin")
    return balance

def check_balance(balance, pin):
    epin = int(input("Enter your pin: "))
    if epin == pin:
        print("Balance:", balance)
    else:
        print("Wrong pin")

def change_pin(pin):
    epin = int(input("Enter your pin: "))
    if epin == pin:
        npin = int(input("Enter new pin: "))
        cpin = int(input("Confirm new pin: "))
        if npin == cpin:
            pin = npin
            print("Pin changed")
        else:
            print("Pin doesn't match")
    else:
        print("Wrong pin")
    return pin

def deposit(balance, pin):
    epin = int(input("Enter your pin: "))
    if epin == pin:
        amt = int(input("Enter amount to deposit: "))
        balance += amt
        print("Transaction successful")
    else:
        print("Wrong pin")
    return balance

def main():
    balance = float(input("Enter your initial balance: "))
    pin = int(input("Set your ATM PIN: "))
    while True:
        print("\nWelcome to the ATM service")
        print("1. Withdraw")
        print("2. Check balance")
        print("3. Change pin")
        print("4. Deposit")
        print("5. Exit")

        try:
            o = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        if o == 1:
            balance = withdraw(balance, pin)
        elif o == 2:
            check_balance(balance, pin)
        elif o == 3:
            pin = change_pin(pin)
        elif o == 4:
            balance = deposit(balance, pin)
        elif o == 5:
            print("Thanks for using our service")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
