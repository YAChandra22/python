#Sum of first n numbers
# n=int(input('enter number: '))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)
'''
Taking input from user
Assuming that if the given number is 0 then my sum is 0
In loop Intializing means i wiil assinged to first element of given numberand extracts that performs the operation
After completion of process traversing will happen means again go to given data and assing to next element and diong process
If n=11 then,
Iteration 1:i extracts 1 and adding to sum=1 
Iteration 2:i extracts 2 and adding to sum=3
Iteration 3:i extracts 3 and adding to sum=6
Iteration 4:i extracts 4 and adding to sum=10
Iteration 5:i extracts 5 and adding to sum=15
Iteration 6:i extracts 6 and adding to sum=21
Iteration 7:i extracts 7 and adding to sum=28
Iteration 8:i extracts 8 and adding to sum=36
Iteration 9:i extracts 9 and adding to sum=45
Iteration 10:i extracts 10 and adding to sum=55
after this ctrl will coming out from loop and do not extracts 11 bcoz always extracts before one element of that
printing statement is writed at outof loop so itz giving total out put as 55 
'''
#Factorial of a given number
# n=int(input())
# factorial=1
# for i in range(1,n+1):
#     factorial*=i
# print(factorial)
'''
Taking input from user
If the user give 0 then Taking factorial value as 1 b'coz 0 factrial value is 1
In range we take n+1 bcoz i extracts onts bofore one element of that
If given number is 5
Iteration 1: i intializes with 1 and extracts & multplying with factorial value after this i traversing i.e again i intilizes with next element
Iteration 2:i extracts 2 & multiplying with factorial value
Iteration 3:i extracts 3 & multiplying with factorial value
Iteration 4:i extracts 4 & multiplying with factorial value
Iteration 5:i extracts 5 & multiplying with factorial value
after completion of process ctrl comes out from loop giving total factorial value
'''
#checking given number is perfect or not
#Perfect Number :- A number is equals to sum of itz divisors which is Perfect Number
# n=int(input())
# d_sum=0
# for i in range (1,n):
#     if n%i==0:
#         d_sum+=i
# if d_sum==n:
#     print('Perfect Number')
# else:
#     print('Not Perfect Number')
'''
Taking input from a user 
Taking divisor sum as 0 assuming that there is no divisors for given number then directly exicute 0 as output
Dealing with numbers taking for loop with range and taking n only b'coz we dont want to check itself
if n value is 6 then
scenario1:-
---------
Iteration 1:i extracts 1 deviding with 6 its remainder is equals to 0 then 1 adding to sum othervise not
Iteration 2:i extracts 2 deviding with 6 its remainder is equals to 0 then 2 adding to sum othervise not
Iteration 3:i extracts 3 deviding with 6 its remainder is equals to 0 then 3 adding to sum othervise not
Iteration 4:i extracts 4 deviding with 6 its remainder is equals to 0 then 4 adding to sum othervise not
Iteration 5:i extracts 5 deviding with 6 its remainder is equals to 0 then 5 adding to sum othervise not
it was not checking the 6 and coming out side of loop
checking the sum is equls to given number if it is true then gives out put as perfect number
or else giving output as not perfect number
scenario2:-
`````````
we can take i values as half of given number b'cz ther is no number can devive after the half itz values
so we can take n//2+1 b'coz we dont want floating points so taking floor division and want divide itz half value also taking +1
for i in range(1,n//2+1): writing statements as it is
'''
# Even numbers in a given range
# n=int(input())
# m=int(input())
# for i in range(n,m+1):
#     if i%2==0:
#         print(i)
'''
Where we fetching the output in the range b/w 2 numbers 1 is starting and 2 is ending numbersi.e, where to where we r going to exicuting
Taking for loop with range
Giving the condition to check the even numbers
My 1st no.is 10 and i want to check 20 also includeded i.e,10 to 20
iteration 1: i extracts 10 checking it is even it is True printing 10 inside of loop b'coz we want every element
iteration 2: i extracts 11 checking it is even or not it is False so extracting another element without entering into loop 
iteration 3: i extracts 12 checking it is even or not it is True printing inside of loop 
iteration 4: i extracts 13 checking it is even or not False so extracting another element without entering into loop
iteration 5: i extracts 14 checking it is even or not it is True printing inside of loop
iteration 6: i extracts 15 checking it is even or not it is False so extracting another element without entering into loop
iteration 7: i extracts 16 checking it is even or not it is True printing inside of loop  
iteration 8: i extracts 17 checking it is even or not it is False so extracting another element without entering into loop
iteration 9: i extracts 18 checking it is even or not it is True printing inside of loop
iteration 10: i extracts 19 checking it is even or not it is False so extracting another element without entering into loop
iteration 11: i extracts 20 checking it is even or not it is True printing inside of loop
'''
#print alternative even numbers in a given range
# ll=int(input())
# ul=int(input())
# c=0
# for i in range(ll,ul+1):
#     if i%2==0:
#         c+=1
#         if c%2!=0:
#             print(i)
'''
we dealing with range so taking lower limit & upper limit
count=0 if there is no alternate or even numbers in given range
taking for loop with range with upperlimit+1
Where we r taking nested if if 1 cond. is satisfied then adding 1 to the c and checking this c is odd or not y means we r extracting from first alternative
so it will prints when c becames 1,3,5,7,9 where alternatevely it is printing ane after another i.e,1,3,5..
ex.my range is 1 to 10
iteration 1: i is 1 checking 1 is even false so skipping ang extracting anotherone  
iteration 2: i is 2 checking 2 is even True entering in loop c is 1 after checking c is odd then printing 2
iteration 3: i is 3 checking 3 is even false so skipping ang extracting anotherone  
iteration 4: i is 4 checking 4 is even True entering in loop c is 2 after checking c is not odd so skipping
iteration 5: i is 5 checking 5 is even false so skipping ang extracting anotherone  
iteration 6: i is 6 checking 6 is even True entering in loop c is 3 after checking c is odd then printing 6
iteration 7: i is 7 checking 7 is even false so skipping ang extracting anotherone  
iteration 8: i is 8 checking 8 is even True entering in loop c is 4 after checking c is not odd so skipping
iteration 9: i is 9 checking 9 is even false so skipping ang extracting anotherone  
iteration 10: i is 10 checking 10 is even True entering in loop c is 5 after checking c is odd then printing 10
'''
#printing every second number in a given range
# ll=int(input())
# ul=int(input())
# c=0
# for i in range(ll,ul+1):
#     if i%2==0:
#         c+=1
#         if c%2==0:
#             print(i)
'''
we dealing with range so taking lower limit & upper limit
count=0 if there is no alternate or even numbers in given range
taking for loop with range with upperlimit+1
Where we r taking nested if if 1 cond. is satisfied then adding 1 to the c and checking this c is even or not y means we r extracting from  second
so it will prints when c becames 2,4,6,8,10 where alternatevely it is printing ane after another i.e 4,8,12..
ex.my range is 1 to 10
iteration 1: i is 1 checking 1 is even false so skipping ang extracting anotherone  
iteration 2: i is 2 checking 2 is even True entering in loop c is 1 after checking c is odd so skipping
iteration 3: i is 3 checking 3 is even false so skipping ang extracting anotherone  
iteration 4: i is 4 checking 4 is even True entering in loop c is 2 after checking c is even then printing 2
iteration 5: i is 5 checking 5 is even false so skipping ang extracting anotherone  
iteration 6: i is 6 checking 6 is even True entering in loop c is 3 after checking c is odd so skipping
iteration 7: i is 7 checking 7 is even false so skipping ang extracting anotherone  
iteration 8: i is 8 checking 8 is even True entering in loop c is 4 after checking c c is even then printing 8
iteration 9: i is 9 checking 9 is even false so skipping ang extracting anotherone  
iteration 10: i is 10 checking 10 is even True entering in loop c is 1 after checking c is odd odd so skipping
'''
#print every 3rd even number
# ll=int(input())
# ul=int(input())
# l=[]
# # c=0
# for i in range(ll,ul+1):
#     if i%2==0:
#         # c+=1
#         # if c%3==0:
#         #     print(i)
#         l.append(i)
# print(l[2::3])
'''
we dealing with range so taking lower limit & upper limit
count=0 if there is no alternate or even numbers in given range
taking for loop with range with upperlimit+1
Where we r taking nested if if 1 cond. is satisfied then adding 1 to the c and checking this c is even or not y means we r extracting from  second
so it will prints when c becames 2,4,6,8,10 where alternatevely it is printing ane after another i.e 4,8,12..
ex.my range is 1 to 10
iteration 1: i is 1 checking 1 is even false so skipping ang extracting anotherone  
iteration 2: i is 2 checking 2 is even True entering in loop c is 1 after checking c is odd so skipping
iteration 3: i is 3 checking 3 is even false so skipping ang extracting anotherone  
iteration 4: i is 4 checking 4 is even True entering in loop c is 2 after checking c is even then printing 2
iteration 5: i is 5 checking 5 is even false so skipping ang extracting anotherone  
iteration 6: i is 6 checking 6 is even True entering in loop c is 3 after checking c is odd so skipping
iteration 7: i is 7 checking 7 is even false so skipping ang extracting anotherone  
iteration 8: i is 8 checking 8 is even True entering in loop c is 4 after checking c c is even then printing 8
iteration 9: i is 9 checking 9 is even false so skipping ang extracting anotherone  
iteration 10: i is 10 checking 10 is even True entering in loop c is 1 after checking c is odd odd so skipping
'''
