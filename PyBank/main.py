import os
import csv

budget = os.path.join('Resources', 'budget_data.csv')

total_months = 0
net_total = 0
month_change = []
greatest_increase = 0
greatest_decrease = 0
# def financial_analysis(budget_data):
#     # For readability, it can help to assign your values to variables with descriptive names
#     dates = budget_data[0]
#     revenue = budget_data[1]
# for row in budget_data:
    
    # print(revenue)

with open(budget, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    for row in csv_reader:
        dates = row[0]
        revenue = int(row[1])

        total_months = total_months + 1
        net_total = net_total + revenue
        
        average_change = net_total/total_months
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: {average_change}")
#     #   print(row[1])
#     # financial_analysis(row)

# print(f"Total Months: {total_months}")
# print(f"Total: {net_total}")
# print(row[1])

