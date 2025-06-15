class BankAccount:    
    def __init__(self, initial_balance: float = 0.0):
        self.account_balance = initial_balance
        
    
    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self) -> None:
        print(f"Current Balance: ${self.account_balance:.2f}")