# Isaiah Lugo - SFTE 307 - 09/08/2024
# This program contains a fixed hourly and commission rate that will be used throughout.
# The user will be prompted to eter hours worked and weekly sales in dollars.
# Some calculations will be made to find total pay of worker. 
# Finally, a list of information will be displayed at the end.

#Fixed rates
hourly_rate = 20.00 #hourly rate is $20
commission_rate = 0.8 #commission percentage set at 8%

#User input for hours worked and weekly sales
hours_worked = float(input("Number of hours worked in the week: "))
weekly_sales = float(input("Total weekly sales in USD: "))

#Calculate the total pay 
weekly_salary = hours_worked * hourly_rate  # Pay from hours worked
commission = weekly_sales * commission_rate  # Commission from sales

total_pay = weekly_salary + commission #total pay calculated

#Info display
print("\n--- Weekly Pay Summary ---")
print(f"Total hours worked for the week: {hours_worked} hours")
print(f"Weekly salary based on hourly rate: ${weekly_salary:.2f}") #The use of ':.2f' ensures that there are 2 decimal places used to represent full amount
print(f"Commission for the week based on sales: ${commission:.2f}")
print(f"Total pay for the week: ${total_pay:.2f}")