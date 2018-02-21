#Bhavinkumar Patel - A20410380
#LAB3
#Date: 06-Feb-2018
#Course: ITMD 513

import time

######Variable declaration
balance = rateCode = monthlyDeposit = 0.0
pinCount = 0
mainLoopFlag = True

print("Hello! Welcome to annual interest balance calculation program.")

while mainLoopFlag:
    try:
        accPin = input("\nPlease enter your account pin to proceed :")
    except:
        accPin = ''

    pinCount = pinCount +1

    if accPin != 'ab12' and pinCount < 3:
        print("Invalid pin provided. Please retry. You have "+str(3-pinCount)+" attempts left")
        continue
    elif accPin != 'ab12' and pinCount >= 3:
        print("You have exceeded number of attempts. Please try next time. Good bye.")
        mainLoopFlag = False
        break
    else:

        mainLoopFlag = False

        while True:

            while 1:
                try:
                    balance = float(input("\nPlease enter beginning account balance :"))
                except:
                    print("***Invalid value provide for initial balance. Please enter again.")
                    continue
                else:
                    break

            while 1:
                try:
                    monthlyDeposit = float(input("\nPlease enter monthly deposit amount :"))
                except:
                    print("***Invalid value provide for monthly deposit amount. Please enter again.")
                    continue
                else:
                    break

            while 1:
                try:
                    rateCode = float(input("\nPlease enter annual interest rate (as a decimal) :"))
                except:
                    print("***Invalid value provide for interest rate. Please enter again.")
                    continue
                else:
                    break


            for i in range(1,13):
                if i ==1:
                    balance =  balance + (rateCode/12)*balance
                else:
                    balance = balance + monthlyDeposit + (rateCode/12) * (balance+monthlyDeposit)

                print(("Month "+str(i)).ljust(15)+"New monthly balance :"+"{:.2f}".format(balance))

            loopFlag = input("Do you want to calculate again? (y/n) : ").lower()

            if loopFlag == 'y':
                pass
            else:
                break
                mainLoopFlag = False


#####Printing signature
print("===================================")
print("Bhavinkumar Patel - A20410380")
print("Date :"+time.asctime(time.localtime(time.time())))
print("Course :ITMD-513 LAB3")