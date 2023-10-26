# Modules - Import os and csv
import os
import csv

# Set path for file-using relative path
csvpath = "Resources/budget_data.csv"

# Define variables for PART 1 -> Total Months & Total Profit Loss
total_months = 0
total_profit_loss = 0

# Define variables for PART 2  -> Changes in Profit/Losses & last_profit_loss
changes_profit_losses = [] #use brackets to declare a list
last_profit_loss = 0

# Define variables for PART 3  -> Greatest Increase in profit (with date & amount) + Greatest Decrease in profit (with date & amount)
#After opening CSV file in Excel I know that the profit change range is between 1,862.002 and -1,825,558 so let's set the max and min change on a range that will cover these values
max_change = -2000000
min_change = 2000000
max_month = ""
min_month = ""

# Open the CSV file using the UTF-8 encoding (class example)
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first - should be: ['Date','Profit/Loss']
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

        # Calculate changes in profit/losses
            # if first row, no change, but assign last_profit_loss
                # else, calculate the change -> (Row-Last Profit Loss)
                

        if total_months != 0: # if total months is not equal to zero
            change = int(row[1]) - last_profit_loss #Need to start with Row 1 because row 0 is the header
            changes_profit_losses.append(change) #Append --> adds the item to the list and updates it

            # check max/min change
            if change > max_change:
                max_change = change
                max_month = row[0]
            elif change < min_change:
                min_change = change
                min_month = row[0]
            else:
                pass # If pass then there is not a max/min change

        # assign last month profit
        last_profit_loss = int(row[1])


        # To count total months --> need to add 1
        total_months = total_months + 1


        # Then --> Add the profit/loss to the variable
        total_profit_loss = total_profit_loss + int(row[1])


# Print Results PART 1 (Total number of months and total profit loss) 
print(total_months)
print(total_profit_loss)

# Print Results PART 2 (Changes in Profit Losses and Average changes) 
avg_change = sum(changes_profit_losses) / len(changes_profit_losses)
print(avg_change)

# Print Results part 3 (Greatest Increase in profit (with date & amount) + Greatest Decrease in profit (with date & amount)
print(max_change)
print(max_month)
print(min_change)
print(min_month)

# Create txt Output to show results 
with open("pybank_output.txt", "w") as txt_file:
    output = f"""
Financial Analysis
-------------------------------------------------------------
Total Months: {total_months}
Total: ${total_profit_loss}
Average Change: ${round(avg_change, 2)}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: {min_month} (${min_change})"""

    txt_file.write(output)

#End of PyBank Exercise :)