

# Setting up necessary variables and input from user
investmentAmount = eval(input("Enter investment amount: "))
annualInterestRate = eval(input("Enter annual interest rate: "))
monthlyInterestRate = annualInterestRate / 1200
numberOfYears = eval(input("Enter number of years: "))
numberOfMonths = numberOfYears * 12

# Using formula to calculate future investment value
futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate) ** numberOfMonths

# Rounding the outcome to two decimal places
futureInvestmentValue = int(futureInvestmentValue * 100) / 100.0

# Displaying outcome to user
print("Accumulated value is", futureInvestmentValue)