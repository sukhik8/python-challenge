import os
import csv

# Set file path
file = os.path.join('/Users/sukhikaur/Desktop/UCI Class Analysis/Python HW/budget_data.csv', 'Resources', 'budget_data.csv')
with open('budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Read the header row
    header = next(csvreader)

    # Set variables
    month_count = []
    profit = []
    change_profit = []

    # Iterate through the values and add them to the empty list
    for row in csvreader:
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])

# Evaluate the greatest increase and decrease from the list made
increase = max(change_profit)
decrease = min(change_profit)
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1

# Generate analysis summary
print("Financial Analysis")
print("-"*30)
print(f"Total Months: {len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: ${round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")

# Generate output text file
output = (
    f"Financial Analysis\n"
    f"-----------------------------\n"
    f"Total Months: {len(month_count)}\n"
    f"Total: ${sum(profit)}\n"
    f"Average Change: ${round(sum(change_profit)/len(change_profit),2)}\n"
    f"Greatest Increase in Profit: {month_count[month_increase]} (${(str(increase))})\n"
    f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})\n")

print(output)
with open(output,"w") as txt_file:
    txt_file.write(output)
