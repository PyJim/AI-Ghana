class BankAccount:
    def __init__(self, account_name, initial_amount):
        self.account_name = account_name
        self.initial_amount = initial_amount
        self.current_balance = self.initial_amount
    
    def Deposit(self, amount):
        """This function takes in an amount and adds it to the account balance.

        Args:
            amount (float): the amount of money to be deposited
        """
        self.current_balance += amount
    
    def CachWithdrawal(self, amount):
        """This function takes in an amount and subtracts it from the account balance.

        Args:
            amount (float): the amount of money to be withdrawn
        """
        self.current_balance -= amount
    
    def Balance(self):
        """This function returns the current balance of any instance of the BankAccount class.

        Returns:
            float: current balance
        """
        return f'The balance of {self.account_name} is {self.current_balance} Euros.'


account1 = BankAccount("Jimmy", 3000)
account1.Deposit(300)
account1.CachWithdrawal(1500)
print(account1.Balance())