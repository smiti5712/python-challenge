import os
import csv

#Opening the output file in append mode
with open("PyBankOutput.txt", 'a') as f:
#Creating Path for the Budget_data file which is in the same folder where the code is running
    Budget_csv = "budget_data.csv"

#printing the Header for Display
    print("Financial Analysis")
    f.write("Financial Analysis \n")
    #print >>f( "Financial Analysis")
    print("-----------------------------------------------")
    f.write("-----------------------------------------------\n")

#creating empty lists
    months = []
    profit_loss = []
    profit_loss_no_header = []
    Diff_profit_loss = []
    Diff_profit_loss_with_header = ["ProfitLossChange"]

#Opening the file in read mode
    with open(Budget_csv, "r", encoding='utf-8') as csvfile:
 
        csvreader = csv.reader(csvfile, delimiter=",")

    #Looping through the first column to count number of months
        for row in csvreader:
            months.append(row[0])
            profit_loss.append(row[1])
            profit_loss_no_header.append(row[1])
        print("Total Months: " + str(len(months)-1))
        writeTotalMonth = "Total Months: " + str(len(months)-1)
        f.write(writeTotalMonth + "\n")

#Removing the header for Profit Loss column
        profit_loss_no_header.pop(0)

#Creating a counter for the Total Value
        Total_ProfitLoss = 0
#Creating a counter for storing Prev Profit Loss value
        prev_profit_loss = 0

#looping through each value in profit loss column
        for i in profit_loss_no_header:
    #Calculating the Total by adding profit Loss value each time the loop progresses
            Total_ProfitLoss = Total_ProfitLoss+ int(i)
    #Assigning Current Profit Loss value
            current_Profit_loss = int(i)
    #Calculating the Difference between Current profit Loss and the Previous Profit Loss
            Difference_profit_loss = current_Profit_loss - prev_profit_loss
    #Appending the Diference in profit loss value to the list
            Diff_profit_loss.append(Difference_profit_loss )
            Diff_profit_loss_with_header.append(Difference_profit_loss )
    #Assigning  current profit loss as the Previous profit loss, for the next loop to start
            prev_profit_loss = current_Profit_loss

#displaying the Total profit Loss
    writeTotalprofitLoss = "Total: $" + str(Total_ProfitLoss )
    print (writeTotalprofitLoss)
    f.write(writeTotalprofitLoss + "\n")

#removing the first value from Difference profit Loss List
    Diff_profit_loss.pop(0) 
    Diff_profit_loss_with_header[1] = 0
#Creating a counter for the Total Change in profit Loss to use for Average calculation
    Total_Change_profit_loss = 0
#looping through the Difference in Profit Loss List
    for j in Diff_profit_loss:
        Total_Change_profit_loss = Total_Change_profit_loss + int(j)
#calculating the average change in profit loss and printing
    writeAverageChange = "Average Change: $" + str(round(Total_Change_profit_loss/len(Diff_profit_loss),2))
    print(writeAverageChange)
    f.write(writeAverageChange + "\n")

#Calculating Max Profit Increase and Max profit Decrease
    Max_profit_increase = max(Diff_profit_loss)
    Max_profit_decrease = min(Diff_profit_loss)

# Zip lists together
    new_budget_csv = zip(months,profit_loss,Diff_profit_loss_with_header)

#search in new list , the values for Max Profit Increase and Max profit Decrease and get respective Dates
    for eachrow in new_budget_csv:
#print (eachrow[2])
        if Max_profit_increase== eachrow[2]  :
            writeGreatestIncrease = "Greatest Increase in Profits: " + eachrow[0] + " ($" + str(Max_profit_increase) + ")"
            print (writeGreatestIncrease)
            f.write(writeGreatestIncrease + "\n")
        if Max_profit_decrease== eachrow[2]  :
            writeGreatestDecrease = "Greatest Decrease in Profits: " + eachrow[0] + " ($" + str(Max_profit_decrease) + ")"
            print (writeGreatestDecrease)
            f.write(writeGreatestDecrease + "\n")          