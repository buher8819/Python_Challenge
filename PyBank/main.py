#import our dependencies
import os
import csv
#open the csv file
csvpath = os.path.join('budget_data_real.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    #we can store everything as a list. total rows can be converted to a number later with the len command?
    total_rows = []
    total_money = []
    total_money_change = []

    #loop through to count the rows and add up all the profits/losses as we go through
    for row in csvreader:
        total_rows.append(row[0])
        total_money.append(float(row[1]))
    print("Financial Analysis")
    print("-------------------")
    print("Total Months: " + str(len(total_rows)))
    print("Total: $" + str(sum(total_money)))
    #loop through again but now store the differences between each row and average them. use min and max to find most profit/loss
    for n in range(1, len(total_money)):
        total_money_change.append(total_money[n] - total_money[n-1])
        average_change = sum(total_money_change)/len(total_money_change)
        greatest_total_money_change = max(total_money_change)
        lossiest_total_money_change = min(total_money_change)
        #find the max and min, convert to strings with the date
        greatest_total_money_change_index = str(total_rows[total_money.index(max(total_money))])
        lossiest_total_money_change_index = str(total_rows[total_money.index(min(total_money))])

    print("Average Change: $" + str(round(average_change, 2)))
    print("Greatest Increase in Profits: " + str(greatest_total_money_change_index) + "($ " + str(greatest_total_money_change) + ")")
    print("Greatest Decrease in Profits: " + str(lossiest_total_money_change_index) + "($ " + str(lossiest_total_money_change) + ")")
#could use f strings here?

output_path = os.path.join("PyBank_output.csv")
#write the output to a file
with open(output_path, 'w', newline='') as new_csvfile:

    csvwriter = csv.writer(new_csvfile, delimiter=',')

    csvwriter.writerow(["Financial Analysis"])

    csvwriter.writerow(["Total Months", str(len(total_rows))])

    csvwriter.writerow(["Total: ", "$ " + str(sum(total_money))])

    csvwriter.writerow(["Average Change", "$ " + str(round(average_change, 2))])

    csvwriter.writerow(["Greatest Increase in Profits ", str(greatest_total_money_change_index), "$ " + str(greatest_total_money_change)])

    csvwriter.writerow(["Greatest Decrease in Profits ", str(lossiest_total_money_change_index), "$ " + str(lossiest_total_money_change)])
