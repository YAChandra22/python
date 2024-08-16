n=int(input())
for i in range(1,n):
    for j in range(1,n):
        if i==2:
            print(i,j)
    break
    '''print('in if block')'''
    print('in inner loop')
print('in outer loop')
