#Nested Functions
'''
def outer(arg):
    print('outer is started')
    print(arg)
    def inner():
        print('inner is started')
        arg()
        print('inner is ended')
    print('outer is ended')
    return inner

def wish():
    print('wish is started')
    print('wish is ended')
result=outer(wish)
print(result)
result()    
'''








































    
