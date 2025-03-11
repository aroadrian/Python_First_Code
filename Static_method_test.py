# A Static method in Python is a method that belong to the class itself.
# To define a static method, use the @staticmethod decorator.

class Bank_account:
    Min_Balance = 100
    
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance
        
    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            self.__log_transcation("deposit", amount)
        else:
            print("Deposit must be higher than zero,")
            
    def _is_valid_amount(self, amount):
        return amount > 0
        
    def __log_transcation(self, transaction_type, amount):
        print(f"Logging {transaction_type} of ${amount}. New balance : ${self._balance}")
        
        
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5
        
        
account =Bank_account("Adrian", 400)
account.deposit(300)

print(Bank_account.is_valid_interest_rate(3))
print(Bank_account.is_valid_interest_rate(10))