#Local variable
'''
Created inside functions
Accessed ,Modified and deleted in that f/n space only
Wee cannot access Local vars in main space'''
#   Ex:-
# def function():
#     a=20
#     print(a)
# function()
# print(a)   #were we cannot access bcoz it is in main space

#   Global Variables
'''
Created outside f/n Accessed and Modified inside the f/n
To make normal var into Global we want to use Global Keyword'''
#   Ex:-
# a=20
# def function():
#     global a            #to make normal to global
#     print(a)
#     a-=10
#     print(a)
# function()
# print(a)

#  Nested Functions
# Defining F/n Inside another F/n
# def outer():
#     print('outer is started')
#     def inner():
#         print('inner is started')
#         print('inner is ended')
#     inner()
#     print('outer is ended')
# outer()

'''
Non local variables
Used in nested f/n
Defined in Outer F/n and Accessd and modified in inner f/n
To make normal vars to non local vars we want to use non local keyword
    Ex:-'''
# def Outer():
#     a=20
#     def Inner():
#         nonlocal a
#         print(a)
#         a-=5
#         print(a)
#     Inner()
#     print(a)
# Outer()


