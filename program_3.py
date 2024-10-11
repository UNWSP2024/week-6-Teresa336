# Programmer: Teresa Fischer
# Date: 10/11/24
# Program #3: Tax Rate

# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.
def tax_rate():
    total_sales = float(input('Enter the total sales for the month:'))
    print('Total sales for the month: $', total_sales)
# From this figure, the application should calculate and display the following:
# The amount of county sales tax.
    county_sales_tax = (total_sales * .025)
    print('County sales tax: $', county_sales_tax)
# The amount of state sales tax.
    state_sales_tax = (total_sales * .05)
    print('State sales tax: $', state_sales_tax)
# The total sales tax (county plus state)
    total_sales_tax = (county_sales_tax + state_sales_tax)
    print('Total sales tax: $', total_sales_tax)
# Use at least one function with input and output in this program

tax_rate()