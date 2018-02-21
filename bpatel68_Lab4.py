#Bhavinkumar Patel - A20410380
#LAB4
#Date: 15-Feb-2018
#Course: ITMD 513

import time
import random

#Function to calculate winning Amount

def calculateWinningAmount(fLoopCounter, fFireBall, fgeneratedNumbers, fGeneratedFireBall, fNumber1List, fNumber2List, fNumber3List, fNumber4List):

    winamt = 0

    for j in range(len(fNumber1List)):
        if fLoopCounter == 3:
            if fNumber1List[j] == fgeneratedNumbers[0] and fNumber2List[j] == fgeneratedNumbers[1] \
                    and fNumber3List[j] == fgeneratedNumbers[2]:
                winamt = winamt + 250

            if fFireBall and fNumber1List[j] == fGeneratedFireBall[0] and fNumber2List[j] == fgeneratedNumbers[1] \
                    and fNumber3List[j] == fgeneratedNumbers[2]:
                winamt = winamt + 125

            if fFireBall and fNumber1List[j] == fgeneratedNumbers[0] and fNumber2List[j] == fGeneratedFireBall[0] \
                    and fNumber3List[j] == fgeneratedNumbers[2]:
                winamt = winamt + 125

            if fFireBall and fNumber1List[j] == fgeneratedNumbers[0] and fNumber2List[j] == fgeneratedNumbers[1] \
                    and fNumber3List[j] == fGeneratedFireBall[0]:
                winamt = winamt + 125

        elif fLoopCounter == 4:
            if fNumber1List[j] == fgeneratedNumbers[0] and fNumber2List[j] == fgeneratedNumbers[1] \
                    and fNumber3List[j] == fgeneratedNumbers[2] and fNumber4List[j] == fgeneratedNumbers[3]:
                winamt = winamt + 250

            if fFireBall and fNumber1List[j] == fGeneratedFireBall[0] and fNumber2List[j] == fgeneratedNumbers[1] \
                    and fNumber3List[j] == fgeneratedNumbers[2] and fNumber4List[j] == fgeneratedNumbers[3]:
                winamt = winamt + 125

            if fFireBall and fNumber1List[j] == fgeneratedNumbers[0] and fNumber2List[j] == fGeneratedFireBall[0] \
                    and fNumber3List[j] == fgeneratedNumbers[2] and fNumber4List[j] == fgeneratedNumbers[3]:
                winamt = winamt + 125

            if fFireBall and fNumber1List[j] == fgeneratedNumbers[0] and fNumber2List[j] == fgeneratedNumbers[1] \
                    and fNumber3List[j] == fGeneratedFireBall[0] and fNumber4List[j] == fgeneratedNumbers[3]:
                winamt = winamt + 125

            if fFireBall and fNumber1List[j] == fgeneratedNumbers[0] and fNumber2List[j] == fgeneratedNumbers[1] \
                    and fNumber3List[j] == fgeneratedNumbers[2] and fNumber4List[j] == fGeneratedFireBall[0]:
                winamt = winamt + 125

    return winamt


######Variable declaration

userChoice = 0
mainLoopFlag = False
loopCounter = 0
fireBall = False
number1List = []
number2List = []
number3List = []
number4List = []
generatedNumbers = []
generatedFireBall = 0
winningAmount = 0
numberGeneration = 0;

startRange = 0
endRange = 10

print("\n*****Welcome to Lucky Lotto Game******")
print("1. Lotto Pick 3.")
print("2. Lotto Pick 3 with Fireball.")
print("3. Lotto Pick 4.")
print("4. Lotto Pick 4 with Fireball.")

while True:
    try:
        userChoice = input("\nPlease Enter your Choice: ")

        if userChoice != '1' and userChoice != '2' and userChoice != '3' and userChoice != '4':
            raise Exception
        else:
            if userChoice == '1' or userChoice == '2':
                loopCounter = 3
            else:
                loopCounter = 4

            if userChoice == '2' or userChoice == '4':
                fireBall = True

            mainLoopFlag = True
            break
    except:
        print("!!!Invalid Choice. Please try again.")

if mainLoopFlag:

    while True:

        try:
            print("\nHow do you want to generate ticket numbers?")
            print("1. Quick pick.")
            print("2. Enter Manually.")
            numberGeneration = input("\nEnter your Choice :")

            if numberGeneration != '1' and numberGeneration != '2':
                raise Exception
            else:
                if numberGeneration == '1':

                    quickPickNumbers = sorted(random.sample(range(startRange, endRange), loopCounter))
                    number1List.append(quickPickNumbers[0])
                    number2List.append(quickPickNumbers[1])
                    number3List.append(quickPickNumbers[2])

                    if loopCounter == 4:
                        number4List.append(quickPickNumbers[3])

                    quickPickNumbers = []

                elif numberGeneration == '2':
                    print("\n**Note: Please Enter your Numbers between 0 to 9")

                    inputCounter = 1
                    inputNumbers = []

                    while True:

                        try:
                            inputVal = int(input("Enter Number " + str(inputCounter) + ": "))

                            if inputVal < startRange or inputVal > endRange:
                                raise Exception

                            inputCounter = inputCounter + 1

                            inputNumbers.append(inputVal)

                            if inputCounter > loopCounter:
                                break

                        except:
                            print("Invalid input. Please provide again.")
                            continue

                    inputNumbers.sort()

                    number1List.append(inputNumbers[0])
                    number2List.append(inputNumbers[1])
                    number3List.append(inputNumbers[2])

                    if loopCounter == 4:
                        number4List.append(inputNumbers[3])



            loopFlag = input("\nDo you want to buy another Ticket? (y/n): ").lower()

            if loopFlag == 'y':
                pass
            else:
                break

        except:
            print("!!!Provide valid input. Please retry.")
            continue

    generatedNumbers = sorted(random.sample(range(startRange, endRange), loopCounter))

    if fireBall:
        generatedFireBall = random.sample(range(startRange, endRange), 1)

    winningAmount = calculateWinningAmount(loopCounter, fireBall, generatedNumbers, generatedFireBall, number1List, number2List, number3List, number4List)

    print("\nSystem Generated Winning Numbers: "+str(generatedNumbers))

    if fireBall:
        print("System Generated Fireball: " + str(generatedFireBall))

    for k in range(len(number1List)):

        if loopCounter == 3:
            print("Your Ticket "+str(k+1)+": ["+str(number1List[k])+", "+str(number2List[k])+", "+str(number3List[k])+"]")
        elif loopCounter == 4:
            print("Your Ticket " + str(k+1) + ": [" + str(number1List[k])+", "+str(number2List[k])+", "+str(number3List[k])+
                  ", "+str(number4List[k])+"]")


    if winningAmount == 0:
        print("\nSorry. You are not a winner. Please try again tomorrow. Good luck!")
    else:
        print("\nCongratulations. You are a winner. You won $"+str(winningAmount)+".")


#####Printing signature
print("\n\n===================================")
print("Bhavinkumar Patel - A20410380")
print("Date :"+time.asctime(time.localtime(time.time())))
print("Course :ITMD-513 LAB4")