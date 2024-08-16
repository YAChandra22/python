'''#Printing how mny vowels in given string\
s=input('enter a string:')       #taking input from user
vowels='aeiouAEIOU'             #to check both lower and upper case
count=0                         #assuming if the given string can'nt having vowels
for i in s:
    if i in vowels:
        count+=1
print(count)

Exicution process:if there is a string then i is assigned to first val of str after enter into loop checks the cond. i is vowels it will true adds 1 to count other wise count is 0 after completion this i wiil assigning to next element it will iterates over a loop by extracting each element from given string
    FOR Ex.my string is Sita Rama
Iteration 1: cond. checks i is in vowels or not i.e, extracts the element s and it checks it is present in vowels it is false so the count value is 0 and i extracts next element
Iteration 2: cond. checks i is in vowels or not i.e, extracts the element i and it checks it is present in vowels it is true so the count value is 1 and i extracts next element
Iteration 3: cond. checks i is in vowels or not i.e, extracts the element t and it checks it is present in vowels it is false so the count value is 1 and i extracts next element
Iteration 4: cond. checks i is in vowels or not i.e, extracts the element a and it checks it is present in vowels it is true so the count value is 2 and i extracts next element
Iteration 5: cond. checks i is in vowels or not i.e, extracts the element ' ' and it checks it is present in vowels it is false so the count value is 2 and i extracts next element
Iteration 6: cond. checks i is in vowels or not i.e, extracts the element R and it checks it is present in vowels it is false so the count value is 2 and i extracts next element
Iteration 7: cond. checks i is in vowels or not i.e, extracts the element a and it checks it is present in vowels it is true so the count value is 3 and i extracts next element
Iteration 8: cond. checks i is in vowels or not i.e, extracts the element m and it checks it is present in vowels it is false so the count value is 3 and i extracts next element
Iteration 9: cond. checks i is in vowels or not i.e, extracts the element a and it checks it is present in vowels it is true so the count value is 4 and i extracts next element
    so the i value is 4

#   Consonents present in given string
s= input('enter string: ')  #taking input from user
v='aeiouAEIOU'      #taking vowels
sum=0               #assuming that given string is not have consonents
for i in s:
    if i.isalpha() and i not in v:
        sum+=1
print(sum)

execution:
1.loop will extracts each element and iterates to end of the string
2.enters into lop black and checks the given cond. i.e, i is alphabet and it is not present in v
    for example my string is 'Hai Hello'
Iteration 1: Extracts H and it is alpha and it is not in v so sum will increment by 1 so its now it is 1
Iteration 2: Extracts a and it is alpha and it is in v so sum will not increment by 1 so its now it is 1
Iteration 3: Extracts i and it is alpha and it is in v so sum will not increment by 1 so its now it is 1
Iteration 4: Extracts ' ' and it is not alpha and it is not in v so sum will not increment by 1 other wise not
Iteration 5: Extracts H and it is alpha and it is not in v so sum will increment by 1 so its now it is 2
Iteration 6: Extracts e and it is alpha and it is in v so sum will increment by 1 so its now it is 2
Iteration 7: Extracts l and it is alpha and it is not in v so sum will increment by 1 so its now it is 3
Iteration 8: Extracts l and it is alpha and it is not in v so sum will increment by 1 so its now it is 3
Iteration 9: Extracts o and it is alpha and it is in v so sum will increment by 1 so its now it is 3
    so the sum value is 3 

# how many vowels and how many cosonents
s=input('enter string: ')
v='aeiouAEIOU'
vc=0        #assuming that vowels not present in given collection 
cc=0        #assuming that consonents not present in given collection
for i in s:
    if i.isalpha():
        if i in v:
            vc+=1
        else:
            cc+=1
print(f'vewels count is {vc}')
print(f'consonent count is {cc}')

1.i will exatracts every ingle element over the string
2.were we r taked nested if condition
3.i will checks it is alpha or not true then enters into block otherwise exatracts another elemnt
    for example my string is Ashu12
iteration 1 :checks A is abhabet it is true after checking A in vowels it is also True so adding vc to 1 i.e,1
iteration 2 :checks s is abhabet it is true after checking s in vowels it is false so adding i.e,1 to cc,i. e 1
iteration 3 :checks h is abhabet it is true after checking h in vowels it is false so adding 1 to cc,i.e 2
iteration 4 :checks u is abhabet it is true after checking u in vowels it is also True so adding vc to 1 1 i.e, 2
iteration 5 :checks 1 is abhabet it is false so block will not exicute
iteration 6 :checks 2 is abhabet it is false so block will not exicute 
were used format 
vc is 2     &&      cc is 2  

#printing how many intezers present in given string
s=input(('enter a string: '))
count=0
for i in s:
    if i.isdigit():
        count+=1
print (count)

iteration process:

1.Takisum of dng input from users
2.i am assuming if the string does not having numbers
my string is 12nikki34
execution
iteration 1: checking 1 isdigit it is true so count became as 1
iteration 2: checking 2 isdigit it is true so count became as 2
iteration 3: checking n isdigit it is false so cont is 2
iteration 4: checking i isdigit it is false so count is 2
iteration 5: checking k isdigit it is false so count is 2
iteration 6: checking k isdigit it is false so count is 2
iteration 7: checking i isdigit it is false so count is 2
iteration 8: checking 3 isdigit it is true so count became as 3
iteration 9: checking 4 isdigit it is true so count became as 4
so string ends and loop stops coming out of the loop
printing sum of count is 4

#Sum of integers presentb in given string
s=input()
sum=0
for i in s:
    if i.isdigit():
        j=int(i)
        sum+=j
print(sum)

1.Taking input from users
2.i am assuming if the string does not having numbers
my string is 12he lo34 5hi6 
execution
iteration 1: checking 1 isdigit it is true converting into int and adding to sum to 1 it is 1
iteration 2: checking 2 isdigit it is true converting into int and adding to sum to 2 it is 3
iteration 3: checking h isdigit it is false so not addig t sum is 3
iteration 4: checking e isdigit it is false so not ading to sum is 3
iteration 5: checking ' ' isdigit it is false so not ading to sum is 3
iteration 6: checking l isdigit it is false so not ading to sum is 3
iteration 7: checking o isdigit it is false so not ading to sum is 3
iteration 8: checking 3 isdigit it is true converting into int and adding to sum to 3 it is 6
iteration 9: checking 4 isdigit it is trueconverting into int and adding to sum to 4 it is 10
iteration 10: checking ' ' isdigit it is false so not ading to sum is 10
iteration 11: checking 5 isdigit it is true converting into int and adding to sum to 5 it is 15
iteration 12: checking h isdigit it is false so not ading to sum is 15
iteration 13: checking i isdigit it is false so not ading to sum is 15
iteration 14: checking 6 isdigit it is true converting into int and adding to sum to 6 it is 21
so string ends and loop stops coming out of the loop
printing sum of sum is 21
'''
#Printingsum of even numbers in a given string
# s=input()
# sum=0
# for i in s:
#     if i.isdigit():
#         j=int(i)
#         if j%2==0:
#             sum+=j
# print(sum)
'''iteration process:

1.Taking input from users
2.i am assuming if the string does not having numbers
my string is 12nikki34
execution
iteration 1: checking 1 isdigit it is true and converting into int so sum became as 1
iteration 2: checking 2 isdigit it is true and converting into int so sum became as 3
iteration 3: checking n isdigit it is false so sum is 2
iteration 4: checking i isdigit it is false so sum is 2
iteration 5: checking k isdigit it is false so sum is 2
iteration 6: checking k isdigit it is false so sum is 2
iteration 7: checking i isdigit it is false so sum is 2
iteration 8: checking 3 isdigit it is true and converting into int so sum became as 6
iteration 9: checking 4 isdigit it is true and converting into int so sum became as 10
so string ends and loop stops coming out of the loop
printing sum is 10
'''
#absolute difference between even digits and odd numbers
# s=input()
# e_sum=0
# o_sum=0
# for i in s:
#     k=int(i)
#     if k%2==0:
#         e_sum+=k
#     else:
#         o_sum+=k
# print(abs(e_sum-o_sum))
# s=input(): Takes the input string from the user.

# es=0 and os=0: Initialize es (sum of even digits) and os (sum of odd digits) as 0.

# for i in s:: Iterates over each character i in the input string s.

# if i.isdigit():: Checks if the character i is a digit.

# k=int(i): Converts the character i to an integer k.

# if k%2==0:: Checks if the integer k is even.

# If k is even, es=es+k adds k to es.
# else:: If k is odd,

# os=os+k adds k to os.
# print(abs(es-os)): Prints the absolute difference between es and os.

# Now, for the input 56chand78:

# es: Sum of even digits = 6 + 8 = 14
# os: Sum of odd digits = 5 + 7 = 12
# Absolute difference = |14 - 12| = 2
# So, the output of the code for the input 56chand78 would be: 2

#how many special charecters in given string
# s=input()
# count=0
# for i in s:
#     if not i.isalnum():
#        count+=1
# print(count)
'''
Exicution Process
1. Taking the input from user
2. Assuming that my string might be does not have any special characters
For example the input is '$ch@a#nd$' then
1. Iteration: i exatracts $ and cheking it is alpha or number it is True so count is 1
2. Iteration: i exatracts c and cheking it is alpha or number it is false so count is 1
3. Iteration: i exatracts h and cheking it is alpha or number it is false so count is 0
4. Iteration: i exatracts @ and cheking it is alpha or number it is True so count is 2
5. Iteration: i exatracts a and cheking it is alpha or number it is false so count is 2
6. Iteration: i exatracts # and cheking it is alpha or number it is True so count is 3
7. Iteration: i exatracts n and cheking it is alpha or number it is false so count is 3
8. Iteration: i exatracts d and cheking it is alpha or number it is false so count is 3
9. Iteration: i exatracts $ and cheking it is alpha or number it is True so count is 4
finally the ctrl exits from loop and gives total count 4
'''
#igits of a given list
# l=eval(input())
# sum=0
# for k in l:
#     if isinstance(k,int):        
#         sum+=k
# print(sum)
'''
isinstance() Function:
``````````````````````
    Syntax:
            isinstance(data,DATATYPE)
    It returns True when specified data is a Object of Specified DATATYPE else it returns False
1. eval
'''