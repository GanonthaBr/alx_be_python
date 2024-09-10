monthly_incomes = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_incomes - monthly_expenses

#annual interest rate of 5%
annual_interest_rate = 0.05

#projection over one year
annual_savings = monthly_savings * 12
annual_interest = annual_savings * annual_interest_rate

#final output
projected_savings = annual_savings + annual_interest

print("Your monthly savings are $: ",monthly_savings)
print("Projected savings after one year, with interest, is: $", projected_savings)
