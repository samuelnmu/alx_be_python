#Finance Calclator
class financeCalculation:
    income = float(input("Enter your monthly income: "))
    expenses = float(input("Enter your total monthly expenses: "))
    
    monthlySavings = income - expenses
    interestRate = 0.05
    
    #(Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))
    projectedSavings = monthlySavings * 12 + (monthlySavings * 12 * interestRate)
    
    print("Your monthly savings are: ", "$",monthlySavings)
    print("Projected savings after one year, with interest, is: ", "$",projectedSavings)
    