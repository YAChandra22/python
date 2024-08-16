'''s=input('Enter a string:')               #taking input from user
substring=input(('enter sub string:'))      #taking input from user
c=0                         #Given substring might be not in Given string the 0 will exicutes
for i in s:
    if i==substring:        #checking given substring is peresent or not
        c+=1                #condition is True c increments by 1 evry time while condition is true
print(c)                    #were print in outside of loop, so it will gives output after completing the loop

execution process:-
~~~~~~~~~~~~~~~~~
1.Taking inputs i.e,string and substrings from user
2.Giving c value is zero bcoz if the Given sub string is not available the directly exicuting the c value as 0
3.For example given String is 'sitarama' and the substring is 'a'
4.IN FOR LOOP:
    ->In for loop i will iterates the over statement i.e,
    ->ITERATION:- I extracts first element and checks the element is equal or not to the given substring if it is equal then it will add 1 to c valuei.e,
  ->Iteration 1: It wiil extracts element from s and checks the s is equal to the a if it is true 1 will add to c other wise it will can't
  ->Iteration 2: It wiil extracts element from s and checks the i is equal to the a if it is true 1 will add to c other wise it will can't
  ->Iteration 3: It wiil extracts element from s and checks the t is equal to the a if it is true 1 will add to c other wise it will can't
  ->Iteration 4: It wiil extracts element from s and checks the a is equal to the a if it is true 1 will add to c other wise it will can't
  ->Iteration 5: It wiil extracts element from s and checks the r is equal to the a if it is true 1 will add to c other wise it will can't
  ->Iteration 6: It wiil extracts element from s and checks the a is equal to the a if it is true 1 will add to c other wise it will can't
  ->Iteration 7: It wiil extracts element from s and checks the m is equal to the a if it is true 1 will add to c other wise it will can't
  ->Iteration 8: It wiil extracts element from s and checks the a is equal to the a if it is true 1 will add to c other wise it will can't

    Were output is 3 based on True conditions


name = input('Enter name:')
letter = input('enter sub string:')
count=0                     #Given substring is might not in the given string it will return 0
for k in name:              #iterating every elements by using for loop
    if k==letter:           #comparing elements r equal to given letter r not
        count+=1            #adding 1 to count if given condition is true
print(count)                #Taking at outerof loop to print total value r after completion of process

Hints about my code:
-------------------
1.Taking the inputs from the user i.e name and specific letter
2.Taking count value as 0 bcoz if the given specified letter is not available then it will exucutes 0 as directly without entering into the for loop
3.Now we r entering nto the for loop it will iterates each and every elements one by one or one after onethr untill the over the statement
4.Were iterated evry element compared with given condition if it is True then it will add  1 to  the count value otherwise not
    For example my sting is 'CHANDRA YA' & my substring is 'A' then it exicutes below
PROCESS:
```````
->Iteration1: It takes 1st element i.e, 'C' then compare with letter 'A' if it is True ,count is increment by 1 otherwise not
->Iteration2: It takes 2nd element i.e, 'H' then compare with letter 'A' if it is True ,count is increment by 1 otherwise not
->Iteration3: It takes 3rd element i.e, 'A' then compare with letter 'A' if it is True ,count is increment by 1 otherwise not
->Iteration4: It takes 4th element i.e, 'N' then compare with letter 'A' if it is True ,count is increment by 1 otherwise not
->Iteration5: It takes 5th element i.e, 'D' then compare with letter 'A' if it is True ,count is increment by 1 otherwise not
->Iteration6: It takes 6th element i.e, 'R' then compare with letter 'A' if it is True ,count is increment by 1 otherwise not
->Iteration7: It takes 7th element i.e, 'A' then compare with letter 'A' if it is True ,count is increment by 1 otherwise not
->Iteration8: It takes 8th element i.e, ' ' then compare with letter 'A' if it is True ,count is increment by 1 otherwise not
->Iteration9: It takes 9th element i.e, 'Y' then compare with letter 'A' if it is True ,count is increment by 1 otherwise not
->Iteration10: It takes 10th element i.e, 'A' then compare with letter 'A' if it is True ,count is increment by 1 otherwise not

    Were output is 3 based on True conditions


string=input('Give me a string:')           #taking input from user as str
num_of_elements=0                           #if the given string is empty it will gives 0
for i in string:
    num_of_elements+=1                      #for each iteration 1 will add
print(num_of_elements)                      #taking at outerside of loop to get total number of elements present in given string

EXECUTION OF PROCESS:
--------------------
* Takings the inputs from user
* If the i will assinged to the 1st elemnt and enter into the loop block and add 1 to num of elements and it will became 1 after this process again i assign to 2nd value
* If the i will assinged to the 2nd elemnt and enter into the loop block and add 1 to num of elements and it will became 2 after this process again i assign to 3rd value
* If the i will assinged to the 3rd elemnt and enter into the loop block and add 1 to num of elements and it will became 3 after this process again i assign to 4th value
.......
....
* If the i will assinged to the last elemnt and enter into the loop block and add 1 to num of elements and it will became n (i.e,len of collection) loop is end
'''


