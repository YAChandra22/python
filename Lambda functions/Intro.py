'''
Lambda functions:-
-----------------
r the single line anonymous f/n
created when we need some funtionality only at the point of time
Ex:'''
#with one arg
# add=lambda x:x+10
# print(add(10))

#with 2 args
# add=lambda x,y:x+y
# print(add(10,20))

# with 3 args
# multiply=lambda x,y,z:x*y*z
# print(multiply(10,20,30))

#       Map Function
'''     A f/n in a python takes in a f/n and iterable 
Returns a map object After performing operations on each & every element of iterable by using given function
Syntax:     map(f/n address,iterable)'''

#Map with normal f/n
# l=[10,20,30,40,50]
# def power(n):
#      return n**2
# print(tuple(map(power,l)))

#      Map with lambda f/n
# l=[10,20,30,40,50]
# print(tuple(map(lambda n:n**2,l)))

#   Converting string integers into list of integers
# l='10','20','30','40','50'
# print(list(map(int,l)))

# take space seperatyed values as input convert into list of integers
# l=list(map(int,input().split()))
# print(l)


#take comma seperatyed values as input convert into list of integers
# l=list(map(int,input().split(',')))
# print(l)