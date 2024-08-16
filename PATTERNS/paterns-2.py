'''n=int(input())
stars=1
spaces=n-1
for row in range(1,n+1):
    dummy=1
    for sp in range(1,spaces+1):
        print(' ',end='')
    for st in range(1,stars+1):
        print(dummy,end='')
        dummy+=1
    print()
    stars+=2
    spaces-=1'''
n=int(input())
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(dummy,end=' ')
        if n%2==0:
            dummy+=2
        else:
            dummy+=1 
    print()
    



    
