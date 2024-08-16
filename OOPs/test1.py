class Bank:
    bank_name='SBI'
    bank_ifsc=1234
    bank_roi=6
    bank_address='kizikistan'
    def __init__(self,n,ac,b,ad):
        self.name=n
        self.account=ac
        self.balance=b
        self.address=ad
    def customer_Details(self):
        print(f'name of the customer is {self.name}')
        print(f'account of the customer is {self.name}')
        print(f'balance of the customer is {self.name}')
        print(f'address of the customer is {self.name}')
    def withdrawal(self):
        amount=int(input('enter amount: '))
        if self.balance>=amount:
            self.balance-=amount
            print(f'balance is {self.balance}')
        else:
            print('Insuficient balance')
            print(f'balance is {self.balance}')
        
        
        
