#Bhavinkumar Patel - A20410380
#LAB2
#Date: 30-Jan-2018
#Course: ITMD 513

import time

######Variable declaration

name = ""
mass = length = 0.0
resultVal = 0.0


while 1:

    print("Hello..how do you want to calculate your BMI? Choose one of the below options. \n")
    print("Press 1 to calculate BMI in English Unit.")
    print("Press 2 to calculate BMI in Metric Unit.\n")
    selectedOption = input("Enter your choice : ")

    if selectedOption == '1':

        name = input("Please provide your name           			: ").capitalize()
        mass = float(input("Please provide your weight in U.S. pounds 	: "))
        length = float(input("Please provide your height in U.S. inches 	: "))

        resultVal = (mass * 703) / (length ** 2)

        print(resultVal)

        if resultVal < 18.5:
            print("Hey " + name + "! you are under weight.")
        elif resultVal >= 18.5 and resultVal <= 25:
            print("Hey " + name + "! your weight is normal.")
        else:
            print("Hey " + name + "! you are over weight.")

    elif selectedOption == '2':

        name = input("Please provide your name           			: ").capitalize()
        mass = float(input("Please provide your weight in kilogram 		: "))
        length = float(input("Please provide your height in centimeter 	: "))

        resultVal = mass * 10000 / (length ** 2)

        print(resultVal)

        if resultVal < 18.5:
            print("Hey " + name + "! you are under weight.")
        elif resultVal >= 18.5 and resultVal <= 25:
            print("Hey " + name + "! your weight is normal.")
        else:
            print("Hey " + name + "! you are over weight.")

    else:
        pass

    loopFlag = input("Do you want to calculate again? (y/n) : ").lower()

    if loopFlag == 'y':
        pass
    else:
        break

#####Printing signature
print("===================================")
print("Bhavinkumar Patel - A20410380")
print("Date :"+time.asctime(time.localtime(time.time())))
print("Course :ITMD-513 LAB2")