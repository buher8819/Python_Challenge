#1. The total number of months included in the dataset
#2. The net total amount of "Profit/Losses" over the entire period
#3. The average of the changes in "Profit/Losses" over the entire period
#4. The greatest increase in profits (date and amount) over the entire period
#5. The greatest decrease in losses (date and amount) over the entire period

#1. For the total number of months, we will need to tell the computer to count the number of rows 
#that we have

#2. For the net total of profit/losses, we will have to go through each row, locate the profit/loss
#value, and add it to the amount(declared variable) that is keeping track of the total

#3. Every time we go through a row, we will take the difference betwee the next day and the 
#last day. We will then average all these day-to-day changes.

#4. We will search through all the rows of the sheet and locate the row cntaining the highest
#value of profit (the date and the amount)

#5. We will search through all the rows of the sheet and locate the row cntaining the highest
#value of loss (the date and the amount)