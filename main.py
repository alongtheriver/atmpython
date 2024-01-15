print("Welcome to Sound Bank")

choice01 = input("Please select which item C Checking S Saving")

choice02 = input("Please select the following: D Deposit W Withdrawal B Check Balance E Exit")

checking = 1500
saving = 5000



if(choice01 == "C"):
    if(choice02 == "D"):
        checking + value01
        value01 = input("Enter your deposit amount:")
    elif(choice02 == "W"):
        checking - value02
        value02 = input("Enter your withdrawal amount:")
    elif(choice02 == "B"):
        print("Your total balance is: " + checking)
elif (choice01 == "S"):
    if (choice02 == "D"):
        saving + value03
        value03 = input("Enter your deposit amount:")
    elif(choice02 == "W"):
        saving - value04
        value04 = input("Enter your withdrawal amount:")
    elif(choice02 == "B"):
        print("Your total balance is " + saving)
else:
    print("Exit")



