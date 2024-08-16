class Bank:
    bank_name='SBI'
    bank_ifsc=1234
    bank_roi=6
    bank_address='kizikistan'
    def __init__(self,n,ac,bl,ad):
        self.name=n
        self.account=ac
        self.balance=bl
        self.address=ad
    def customer_Details(self):
        print(f'name of the customer is {self.name}')
        print(f'account of the customer is {self.account}')
        print(f'balance of the customer is {self.balance}')
        print(f'address of the customer is {self.address}')
    def withdrawal(self):
        amount=int(input())
        self.balance>=amount:
            
        
