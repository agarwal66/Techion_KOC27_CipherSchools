is_quit = False
user = {'pin': 1234, 'balance': 3000}
print("Welcome to the PythonATM")

pin = int(input('Please enter your four digit pin: '))
if pin == user['pin']:
    print("Account authorized")
    while is_quit == False:
        print("Welcome Mr John your balance is", user['balance'])
        print("What do you want to do?")
        print(" Enter 1 to Widthdraw Cash \n Enter 2 to deposit Cash \n Enter 3 to Quit")

        query = int(
            input("Enter the number corresponding to the activity you want to do: "))

        if query == 1:
            amount = int(input("Enter the amount of money you want to widthdraw: "))
            if amount > user['balance']:
                print("Your account balance is too low! Please enter lower amount")
            else:
                user['balance'] = user['balance'] - amount
                print(f"{amount} Rupees successfully widthdrawn your remaining balance is {user['balance']} Money")
                print('')
                print("Thankyou for Choosing Python ATM")
        elif query == 2:
            amount = int(input("Enter the amount  of money you want to deposit:"))
            if amount == user['balance']:
                print(f"deposit money {user['balance']} Money")
            else:
                user['balance'] = user['balance'] + amount
                print(f"{amount}Money sucessfully deposited your remaining balance is {user['balance']} Money")
            print('')
            print("Thankyou for Choosing Python ATM")
        elif query == 3:
            print("Thankyou for choosing Python ATM")
            print("Please visit Again")
            break
        else:
            print("please enter a correct value to shown")
else:
    print("Entered wrong pin")