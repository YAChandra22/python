#print hello with its ip
# s='HELLO'
# for ip in range(len(s)): # dealing ip so taking loop with range and collection
#     print(ip,s[ip])      #it is printing its ip and element at every iteration
#Hello with slicing (multiple eliments extarcting)
# s='HELLO'
# for ip in range(len(s)):    # dealing ip so taking loop with range and collection
#     print(ip,s[ip::])       #in every iteration ip wiil update like 0,1,2... and taking it is sip and extracting from that to last
#print index positions of a vowels in given str
# str=input()
# v='aeiouAEIOU'
# for ip in range(len(str)):
#     if str[ip] in v:
#         print(ip,str[ip])
'''
Taking input from user
Taking vowels in caps and lower also because we dont know how user input willbe
deling with index positions so taking for loop with range cdt
input is bus
we r checking single element so going with ip where we ip is 0 we r changing ip to element 
s[ip] is b checking it is in v no so skipping
s[ip] is u checking it is in v yes printing itz ip and the element
s[ip] is s b checking it is in v no so skipping
u and its ip only is our o/p
'''
#index positions of consonents in a given string
# s=input()
# v='aeiouAEIOU'
# for ip in range(len(s)):
#     if s[ip].isalpha():
#         if s[ip] not in v:
#             print(ip,s[ip])
'''
Taking input from user
Taking vowels in caps and lower also because we dont know how user input willbe
deling with index positions so taking for loop with range cdt
input is bus
we r checking single element so going with ip where we ip is 0 we r changing ip to element 
iteration1:
s[ip] is b checking it is not in v true so printing its ip and the element
Iteration2
s[ip] is u checking it is in v false so skipping
Iteration3
s[ip] is s b checking it is not in v true so printing ip and the element
u and its ip only is our o/p
'''
#sum of integers present in given string
# s=input()
# sum=0
# for i in s:                   #we know this method
#     if i.isdigit():              #we can solve in any method is our choice
#         k=int(i)
#         sum+=k
# print(sum)
#                         (or)
# s=input()
# sum=0
# for ip in range(len(s)):
#     if s[ip].isdigit():
#         j=int(s[ip])
#         sum=sum+j
# print(sum)
'''
taking input from user
sum=0 if the user does not give any number or 0 is gived
we can solve this any method loop with range and IP in for loop with range it deals with elements b/w the range
now we r already seen the for loop with range so now we r going with for loop with range and cdt
ab12 is my input
iteration 1:ip is 0 we r taking the 0th element by indexing checking it is digit r not false so skipping
iteration 2:ip is 1 we r taking the 1st element by indexing checking it is digit r not false so skipping
iteration 3:ip is 2 we r taking the 2nd element by indexing checking it is digit r not true,converting into int and adding that value to sum
iteration 4:ip is 3 we r taking the 3rd element by indexing checking it is digit r not true,converting into int and adding that value to sum
finally printing at outside of loop .'.total sum
'''
#sum of index positions of digits in a  given string
# s=input()
# sum=0
# for ip in range(len(s)):
#     if s[ip].isdigit():
#         sum+=ip
# print(sum)
'''
taking input from user
sum=0 if the user does not give any number or 0 is gived
dealing with ip so going with for loop with range and cdt
my input is: ab12
Iteration1: ip is 0 taking its value cheking it is digit or not a it is flase so does not enering into loop
Iteration2: ip is 1 taking its value cheking it is digit or not a it is flase so does not enering into loop
Iteration3: ip is 2 taking its value 1 checking it is digit or not true so adding its index positoin to sum
Iteration3: ip is 3 taking its value 2 checking it is digit or not true so adding its index positoin to sum
finally printing output in outof loop it is giving its total
'''
#sum of even digits present in odd index positions
# s=input()                     #taking input
# sum=0                          #there is no even digits at odd ip 
# for ip in range(len(s)):          #delaing with ip so taking loop with range &cdt
#     if s[ip].isdigit():           #checking it is digit or not
#         k=int(s[ip])              #type casting into integer
#         if k%2==0:                 #checking its element even or not 
#             if ip%2!=0:              #checking its ip odd r not
#                 sum+=k               #adding to sum
# print(sum)                           #printing total sum
'''
taking input from user
sum=0 if there is no even digits at odd ip 
delaing with ip so taking loop with range &cdt
input is ab2468
iteration 1: ip is 0 taking its element a checking it is digit false so dont enterin into loop
iteration 2: ip is 1 taking its element b checking it is digit false so dont enterin into loop
Iteration 3: ip is 2 taking its element 2 checking it is digit true cking it is even true checking position 2 false so dont enterin into loop  
Iteration 4: ip is 3 taking its element 4 checking it is digit true cking it is even true checking position 3 true so adding 4 to sum is 4  
Iteration 5: ip is 4 taking its element 6 checking it is digit true cking it is even true checking position 4 false so dont enterin into loop  
Iteration 6: ip is 5 taking its element 8 checking it is digit true cking it is even true checking position 5 true so adding 8 to sum is 12
printing sum at outof loop i.e,12  
'''
#sum of even index positions of even numbers
# s=input()                     #taking input
# sum=0                          #there is no even digits at odd ip 
# for ip in range(len(s)):          #delaing with ip so taking loop with range &cdt
    # if s[ip].isdigit():           #checking it is digit or not
        # k=int(s[ip])              #type casting into integer
        # if k%2==0:                 #checking its element is even or not 
            # if ip%2==0:              #checking its ip even r not
                # sum+=ip               #adding to sum
# print(sum)                           #printing total sum
'''
taking input from user
sum=0 if there is no even digits at even ip 
delaing with ip so taking loop with range &cdt
input is ab2468
iteration 1: ip is 0 taking its element a checking it is digit false so dont enterin into loop
iteration 2: ip is 1 taking its element b checking it is digit false so dont enterin into loop
Iteration 3: ip is 2 taking its element 2 checking it is digit true cking it is even true checking position 2 true so adding 2 to sum is 2  
Iteration 4: ip is 3 taking its element 4 checking it is digit true cking it is even true checking position 3 false so dont enterin into loop
Iteration 5: ip is 4 taking its element 6 checking it is digit true cking it is even true checking position 4 true so adding 4 to sum is 6 
Iteration 6: ip is 5 taking its element 8 checking it is digit true cking it is even true checking position 5 false so dont enterin into loop
printing sum at outof loop i.e,6  
'''
#sum of odd digits in even ip
# s=input()                     #taking input
# sum=0                          #there is no odd digits at even ip 
# for ip in range(len(s)):          #delaing with ip so taking loop with range &cdt
    # if s[ip].isdigit():           #checking it is digit or not
        # k=int(s[ip])              #type casting into integer
        # if k%2!=0:                 #checking its element is odd or not 
            # if ip%2==0:              #checking its ip even r not
                # sum+=k               #adding to sum
# print(sum)                           #printing total sum
'''
taking input from user
sum=0 if there is no even digits at odd ip 
delaing with ip so taking loop with range &cdt
input is ab1357
iteration 1: ip is 0 taking its element a checking it is digit false so dont enterin into loop
iteration 2: ip is 1 taking its element b checking it is digit false so dont enterin into loop
Iteration 3: ip is 2 taking its element 1 checking it is digit true cheking it is odd true checking position 2 even true so adding 1 to sum is 1  
Iteration 4: ip is 3 taking its element 3 checking it is digit true checking it is odd true checking position 3 odd false so dont enterin into loop  
Iteration 5: ip is 4 taking its element 5 checking it is digit true checking it is odd true checking position 4 even true so adding 5 to sum is 5  
Iteration 6: ip is 5 taking its element 7 checking it is digit true checking it is odd true checking position 5 odd false so dont enterin into loop
printing sum at outof loop i.e,6
'''
#sum of even ip of odd digits
s=input()                     #taking input
sum=0                          #there is no even digits at odd ip 
for ip in range(len(s)):          #delaing with ip so taking loop with range &cdt
    if s[ip].isdigit():           #checking it is digit or not
        k=int(s[ip])              #type casting into integer
        if k%2!=0:                 #checking its element is even or not 
            if ip%2==0:              #checking its ip even r not
                sum+=ip               #adding to sum
print(sum)                           #printing total sum
'''
taking input from user
sum=0 if there is no even digits at even ip 
delaing with ip so taking loop with range &cdt
input is ab1357
iteration 1: ip is 0 taking its element a checking it is digit false so dont enterin into loop
iteration 2: ip is 1 taking its element b checking it is digit false so dont enterin into loop
Iteration 3: ip is 2 taking its element 1 checking it is digit true cking it is even true checking position 2 true so adding 2 to sum is 2  
Iteration 4: ip is 3 taking its element 3 checking it is digit true cking it is even true checking position 3 false so dont enterin into loop
Iteration 5: ip is 4 taking its element 5 checking it is digit true cking it is even true checking position 4 true so adding 4 to sum is 6 
Iteration 6: ip is 5 taking its element 7 checking it is digit true cking it is even true checking position 5 false so dont enterin into loop
printing sum at outof loop i.e,6  
'''
#how many times the given sub str present in given str
s=input()
ss=input()
c=0
for ip in range(len(s)):
    if s[ip:ip+len(ss):]==ss:
        c=c+1
print(c)
