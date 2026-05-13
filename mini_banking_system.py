

total_amount= 0

def deposit_amount():
    global total_amount
    amount= float(input("Enter your deposite amount : "))
    if amount > 0:
        total_amount +=amount
        print("Your Balance is: ", total_amount, " Taka")
    else:
        print("Enter a valid amount") 

def Withdraw_amount():
    global total_amount
    Withdrawal_amount= float(input("Enter your Withdrawal amount : "))
    if Withdrawal_amount > 0:
        total_amount -=Withdrawal_amount
        print("Your current Balance is: ", total_amount, " Taka")
    else:
        print("Enter a valid amount") 

while True:
    option = int(input(
        "Press 1 to deposit\n"
        "Press 2 to withdraw\n"
        "Press 3 to check balance\n"
        "Press 0 to exit: "
    ))

    if option == 1:
        deposit_amount()

    elif option == 2:
        Withdraw_amount()

    elif option == 3:
        print("Current Balance:", total_amount, "Taka")

    elif option == 0:
        print("Exited")
        break

    else:
        print("Invalid option")
