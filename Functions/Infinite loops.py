# N Prime Numbers
''' a number that can only be divided by itself and 1 without remainders
1 is not a prime number because it has only one factor, namely 1.
Prime numbers need to have exactly two factors.
'''
'''c=int(input('enter n '))
n=1
pc=0
while True:
      if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            print(n)
            pc+=1
    if c==pc:
        break
    n+=1
'''
# Nth Prime Number
'''
c=int(input('enter n '))
n=1
pc=0
while True:
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            pc+=1
    if c==pc:
        print(n)
        break
    n+=1
'''
# Prime Numbers in a range 8th TO 15th
'''
c=int(input('enter n '))
n=1
pc=0
while True:
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            pc+=1
            if pc>=8 and pc<=15:
                print(n)
    if pc==15:
        break
    n+=1
'''
# N Armstrong Numbers
'''c=int(input('enter n '))
n=1
ac=0
while True:
    dummy=n
    l=len(str(n))
    sum=0
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        sum+=rem**l
    if n==sum:
        print(n)
        ac+=1
    if c==ac:
        break
    n+=1
  '''
# Prime Numbers in a given range
'''ll=int(input())
ul=int(input())
for i in range(ll,ul+1):
    if i>1:
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            print(i)'''
# Print first n Prime Numbers
'''n=int(input())
pc=0
c=1
while True:
    if c>1:
        for i in range(2,c//2+1):
            if c%i==0:
                break
        else:
            print(c)
            pc+=1
    if n==pc:
        break
    c+=1         '''
#printing Nth prime
'''n=int(input())
c=1
pc=0
while True:
    if c>1:
        for i in range(2,c//2+1):
            if c%i==0:
                break
        else:
            pc+=1
    if n==pc:
        print(c)
        break
    c+=1'''
#6th to 10th primeno.

n = 1
pc = 0
while True:
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            break
    else:
        pc += 1
        if pc >= 6 and pc <= 10:
            print(n)
        if pc == 11:
            break
    n += 1















    






































    
