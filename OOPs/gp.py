#Generic properties by class
'''
class Bank:
    bank_name='sbi'
    bank_ifsc=1245
    bank_roi=6
    bank_address='kizikistan'

jaya=Bank()
susma=Bank()
print(Bank.bank_ifsc)
print(Bank.bank_roi)
'''  

#generic properties by object
'''
class Bank:
    bank_name='sbi'
    bank_ifsc=1245
    bank_roi=6
    bank_address='kizikistan'
jaya=Bank()
sushma=Bank()
print(jaya.bank_name)
print(sushma.bank_address)
'''

#Modifying Generic properties by class
'''
class Bank:
    bank_name='sbi'
    bank_ifsc=1245
    bank_roi=6
    bank_address='kizikistan'
jaya=Bank()
susma=Bank()
Bank.bank_roi=5        #if we modify using class it will effect on all its objects
print(Bank.bank_roi)
print(jaya.bank_roi)
print(susma.bank_roi)
'''

#Modifying Generic properties by object
'''
class Bank:
    bank_name='sbi'
    bank_ifsc=1245
    bank_roi=6
    bank_address='kizikistan'
jaya=Bank()
susma=Bank()
jaya.bank_address='delhi'
print(jaya.bank_address)    #if we modify using object it will applicable for that only
print(susma.bank_address)
print(Bank.bank_address)
'''
#creating Generic properties by class
'''
class Bank:
    bank_name='sbi'
    bank_ifsc=1245
    bank_roi=6
    bank_address='kizikistan'
jaya=Bank()
susma=Bank()
Bank.bank_mabile=56789      #creating using class so creted in all
print(Bank.bank_mabile)
print(jaya.bank_mabile)
print(susma.bank_mabile)
'''
#creating Generic properties by object
'''we cannot able to create generic properties by using
object'''


    











































    
