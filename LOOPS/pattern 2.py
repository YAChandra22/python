# 
# n=int(input())
# for col in range(1,n+1):
#     for row in range(1,n+1):
#         if row==col:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# n=int(input())
# for col in range(1,n+1):
#     for row in range(1,n+1):
#         if row+col==n+1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# n=int(input())
# for col in range(1,n+1):
#     for row in range(1,n+1):
#         if row==col or row+col==n+1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# n=int(input())
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         if row+col>=n+1:
#             print('*',end=' ')
#         else:
#             print(" ",end=" ")
#     print()

# n=int(input())
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         if row+col<=n+1:
#             print('*',end=' ')
#         else:
#             print(" ",end=" ")
#     print()

# n=int(input())
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         if row<=col:
#             print('*',end=' ')
#         else:
#             print(" ",end=" ")
#     print()

# n=int(input())
# spaces=0
# stars=1
# for row in range(1,n+1):
#     for sp in range(1,spaces+1):
#         print(" ",end=" ")
#     for st in range(1,stars+1):
#         print('*',end=' ')
#     print()
#     spaces+=1

# n=int(input())
# spaces=n-1
# stars=1
# for row in range(1,n+1):
#     for sp in range(1,spaces+1):
#         print(" ",end=" ")
#     for st in range(1,stars+1):
#         print('*',end=' ')
#     print()
#     spaces-=1

# n=int(input())
# spaces=0
# stars=n
# for row in range(1,n+1):
#     for sp in range(1,spaces+1):
#         print(' ',end=' ')
#     for st in range(1,stars+1):
#         print('*',end=' ')
#     print()
#     spaces+=1
#     stars-=1

# n=int(input())
# spaces=n-1
# stars=1
# for row in range(1,n+1):
#     for sp in range(1,spaces+1):
#         print(' ',end=' ')
#     for st in range(1,stars+1):
#         print('*',end=' ')
#     print()
#     spaces-=1
#     stars+=1

# n=int(input())
# stars=1
# for row in range(1,n+1):
#     for st in range(1,stars+1):
#         print('*',end=' ')
#     print()
#     stars+=1

# n=int(input())
# stars=n
# for row in range(1,n+1):
#     for st in range(1,stars+1):
#         print('*',end=' ')
#     print()
#     stars-=1

# n=int(input())
# spaces=n-1
# stars=1
# for row in range(1,n+1):
#     for sp in range(1,spaces+1):
#         print(' ',end=' ')
#     for st in range(1,stars+1):
#         print('*',end=' ')
#     print()
#     spaces-=1
#     stars+=2

# n=int(input())
# spaces=0
# stars=2*n-1
# for row in range(1,n+1):
#     for sp in range(1,spaces+1):
#         print(' ',end=' ')
#     for st in range(1,stars+1):
#         print('*',end=' ')
#     print()
#     spaces+=1
#     stars-=2

n=int(input())
dummy=1
for row  in range(1,n+1):
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()
    