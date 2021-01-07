import os
import csv
budget = os.path.join("Resources","budget_data.csv")
total_months = 0
net_total = 0
previous_month = 0
month_change = 0
total_change = 0
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0
with open(budget, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    for row in csv_reader:
        current_month = row[0]
        current_revenue = int(row[1])
        #empty variables to hold greatest increase and decrease


        # total month calculation
        total_months += 1

        # calculation for first row
        if previous_month == 0:
            net_total = current_revenue

        #calculation for remainder
        if previous_month != 0:
            net_total += current_revenue
            month_change = current_revenue - previous_month
            total_change += month_change
            if month_change > greatest_increase:
                greatest_increase = month_change
                greatest_increase_month = current_month
                print(greatest_increase)
            elif month_change < greatest_decrease:
                greatest_decrease = month_change
                greatest_decrease_month = current_month
        previous_month = current_revenue
        


        average_change = total_change/85
    print("Financial Analysis")
    print("--------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${round(average_change,2)}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")   
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")