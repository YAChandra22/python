# Nested Loops
'''n=int(input())
for row in range(1,n+1):
    dm=1
    for col in range(1,n+1):
        if row>=col:
            print(dm,end=' ')
            dm+=1
    print()'''

'''m=int(input())
n=int(input())

for row in range(1,m+1):
    d=7
    for col in range(1,n+1):
        print(d,end=' ')
        d=d+1
    print()'''

'''num=int(input())
spaces=num-1
stars=1
dummy=1
for row in range(1,num+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
    dummy+=1
    stars+=2
    spaces-=1
    print()'''
'''
p = ["Python", "Java", "Ruby", "C", "C++", "Go", "R", 
"JavaScript", "Swift", "PHP", "Kotlin", "Perl"]
n=int(input())
for i in (p):
    m=int(input())
    print(p[m])
    '''
'''L = ["5", "eat", "9.80", "Water", "python", "-678", "7685.26", "-2.5", "sing"]
n=input()

for i in L:
    if n in L:
        print(True)
    else:
        print(False)
    break'''

# n=int(input())
# d=n
# l=len(str(n))
# s=0
# while d>0:
#     rem=d%10
#     d=d//10
#     s+=rem**l
# if n==s:
#     print('Armstrong Number')
# else:
#     print('Not an Armstrong Number')

# n=int(input())
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)
# else:
#     print('Invalid Number')

# n=int(input())
# s=0
# for i in range(1,n+1):
#     if n%i==0:
#         s+=i
# print(s)

# m=int(input())
# l=[]
# for  i in range(1,m+1):
#     n=int(input())
#     l.append(n)
# print(max(l))

# n=int(input())
# for num in range(1, n):
#     sum = 0
#     for i in range(1, num):
#         if num % i == 0:
#             sum += i
#     if sum == num:
#         print(num)



def find_runner_up_score():
    # Input the number of scores
    n = int(input())
    
    # Input the list of scores
    scores = list(map(int, input().split()))
    
    # Find the maximum score
    max_score = max(scores)
    
    # Remove all occurrences of the maximum score
    while max_score in scores:
        scores.remove(max_score)
    
    # Find the runner-up score which is now the maximum score in the modified list
    runner_up_score = max(scores)
    
    # Print the runner-up score
    print(runner_up_score)

# Example usage
find_runner_up_score()






































        



    

