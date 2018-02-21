#Bhavinkumar Patel - A20410380
#LAB1
#Date: 26-Jan-2018
#Course: ITMD 513

import time

######Variable declaration

appNameList = []
appCostList = []
appUseList = []

totalCost = avgCost = costVariance = costDeviation = 0.0
itemCount = 0

######Accepting user input for central air

while 1:

    appName1 = input("Please provide the appliance name           : ").capitalize()
    appCost1 = float(input("Please provide the cost per KW - hr         : "))
    appUse1  = int(input("Please provide approximate usage in KW - hr : "))

    appNameList.append(appName1)
    appCostList.append(appCost1)
    appUseList.append(appUse1)

    loopFlag = input("Do you want to add another appliance? (y/n) : ").lower()

    if loopFlag == 'y':
        pass
    else:
        break

######Deleting unnecessary variables
#del appName1, appCost1, appUse1, loopFlag

######Calculating total cost

for i in range(len(appNameList)):
    totalCost = totalCost + appCostList[i] * appUseList[i]
    itemCount = i+1

######Deleting unnecessary variables
del i;

print("Total Cost".ljust(25)+":"+"{:.2f}".format(totalCost))

######Calculating average cost

for i in range(len(appNameList)):
    avgCost = avgCost + appCostList[i]

avgCost = avgCost / itemCount


print("Average Cost".ljust(25)+":"+"{:.4f}".format(avgCost))
print("Item Count".ljust(25)+":"+str(itemCount))

######Deleting unnecessary variables
del i

#####Calculating cost variance

for i in range(len(appNameList)):
    costVariance = costVariance + (appCostList[i] - avgCost) ** 2


costVariance = costVariance/itemCount

print("Cost Variance".ljust(25)+":"+"{:.4f}".format(costVariance))

######Calculating cost deviation

costDeviation = costVariance ** 0.5

print("cost Deviation".ljust(25)+":"+"{:.4f}".format(costDeviation))

#####Printing signature
print("===================================")
print("Bhavinkumar Patel - A20410380")
print("Date :"+time.asctime(time.localtime(time.time())))
print("Course :ITMD-513 LAB1")