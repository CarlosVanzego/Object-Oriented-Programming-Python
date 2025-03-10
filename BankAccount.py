# I created a class called 'BankAccount'
class BankAccount:
    # Then I initialize the class using the "__init__" constructor and pass the attributes 'self' and 'balance' which I set equal to '10000'.
    def __init__(self, balance=10000):
        # then I instantiate the 'balance' attribute.
        self.balance = balance
    # I created another function called 'get_balance'.
    def get_balance(self):
        # then I am returning the balance variable.
        return self.balance
# I created another instance of the 'BankAccount' class called 'MyAccount' and set it equal to the 'BankAccount' class.
MyAccount = BankAccount()
# then I'm printing the get_balance method.
print(MyAccount.get_balance())     
