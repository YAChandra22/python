'''n=int(input())
for i in range(n):
    for j in range(n):
        print('*',end='')
    print()

n=int(input())
for i in range(n):
    for j in range(n):
        if i==j:
            print('*',end='')
        else:
            print(' ',end='')
    print()

n=int(input())
for i in range(n):
    for j in range(n):
        if i+j==n:
            print('*',end='')
        else:
            print(' ',end='')
    print()

n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
    
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row>=col:
            print('*',end='')
        else:
            print(' ',end='')
    print()
    
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col>=n+1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
        
n=int(input())                         
for row in range(1,n+1):                   
    for col in range(1,n+1):                
        if row<=col:                         
            print('*',end='')                 
        else:
            print(' ',end='')
    print()
    
n=int(input())                         
for row in range(1,n+1):                   
    for col in range(1,n+1):                
        if row+col<=n+1:                         
            print('*',end='')                 
        else:
            print(' ',end='')
    print()
    
stars=1
spaces=0
n=int(input())
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end='')
    for st in range(1,stars+1):
        print('*',end='')
    print()
    spaces+=1
    
n=int(input())
stars=1
spaces=n-1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end='') 
    for st in range(1,stars+1):
        print('*',end='')
    print()
    spaces-=1
   
n=int(input())
stars=n
spaces=0
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end='')
    for st in range(1,stars+1):
        print('*',end='')
    print()
    spaces+=1
    stars-=1
    
n=int(input())
stars=1
spaces=n-1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end='')
    for st in range(1,stars+1):
        print('*',end='')
    print()
    spaces-=1
    stars+=1
    
n=int(input())
stars=1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print('*',end='')
    print()
    stars+=1

n=int(input())
stars=n
for row in range(1,n+1):
    for st in range(1,stars+1):
        print('*',end='')
    print()
    stars-=1
    
n=int(input())
stars=1
spaces=n-1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end='')
    for st in range(1,stars+1):
        print('*',end='')
    print()
    spaces-=1
    stars+=2
    
n=int(input())
stars=2*n-1
spaces=0
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end='')
    for st in range(1,stars+1):
        print('*',end='')
    print()
    spaces+=1
    stars-=2
    
n=int(input())
stars=1
spaces=n//2
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end='')
    for st in range(1,stars+1):
        print('*',end='')
    print()
    if row<=n//2:
        spaces-=1
        stars+=2
    else:
        spaces+=1
        stars-=2
       
n=int(input())
stars=1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print('*',end='')
    print()
    if row<=n//2:
        stars+=1
    else:
        stars-=1

n=int(input())
stars=1
spaces=n//2
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end='')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    if row<=n//2:
        spaces-=1
        stars+=1
    else:
        spaces+=1
        stars-=1

dummy=1
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        print(dummy,end='')
    print()
    dummy+=1

dummy=1
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()                

n=int(input())
for row in range(1,n+1):
    dummy=1
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print
            
    print()

n=int(input('entr no '))
stars=1
spaces=n//2
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end='')
    for st in range(1,stars+1):
        print('*',end='')
    print()
    if row<=n//2:
        stars+=2
        spaces-=1
    else:
        stars-=2
        spaces+=1
    '''
n=int(input())
stars=1
c=0
for row in range(1,n+1):
    for st in range(1,stars+1):
        print('*',end='')
    print()
    if row<=n//2:
        c+=1
        print(f'c is {c}, row={row},n is {n}')
        stars+=1
    else:
        
        print(f'c is {c}, row={row},n is {n}')
        stars-=1
    print(c)
print(n//2)







































