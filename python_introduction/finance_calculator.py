#Finance Calclator
class financeCalculation:
    income = int(input("Enter your monthly income: "))
    expenses = int(input("Enter your total monthly expenses: "))
    
    savings = income - expenses
    interest = 0.05
    
    #(Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))
    projectedSavings = savings * 12 + (savings * 12 * interest)
    
    print("Your monthly savings are: ", "$",savings)
    print("Projected savings after one year, with interest, is: ", "$",projectedSavings)
    