# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# - As an added requirement, withdrawals may not exceed the available balance.
# - Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.




class Account:
    def __init__(self, owner, balance) -> None:
        self.owner: str = owner
        self.balance: str = balance
    
    def deposit(self, amount: int) -> str:
        self.balance += amount
        return "Success"
    
    def withdraw(self, amount: int) -> str:
        if self.balance >= amount:
            self.balance -= amount
            return "Success"
        else:
            return "Not enough money"


# 3.1. Instantiate the class
acct1 = Account('Jose',100)


# 3.2. Print the object
print(acct1)




# 3.3. Show the account owner attribute
print(acct1.owner)




# 3.4. Show the account balance attribute
print(acct1.balance)




# 3.5. Make a series of deposits and withdrawals
print(acct1.deposit(50))
print(acct1.balance)
print(acct1.deposit(100))
print(acct1.balance)
print(acct1.withdraw(100))
print(acct1.balance)
acct1.withdraw(75)
print(acct1.balance)


# 3.6. Make a withdrawal that exceeds the available balance
print(acct1.withdraw(5000))
print(acct1.balance)



# ## Good job!
