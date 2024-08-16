'''In Recursion we want to remember two points
1)How we need to call a function within itself
2)Till when you need to call(At which point u want to stop)
=>By default function will returns the None'''


#sum of individual digits
'''def sum_Digits(n):
    if n==0:
        return 0
    return n%10+sum_Digits(n//10)
print(sum_Digits(1234))'''
#Armstrong Number
def armstrong(n, original, length, sum):
    if n == 0:
        return sum == original
    else:
        digit = n % 10
        sum += digit ** length
        return armstrong(n // 10, original, length, sum)

def arm_Num(n):
    return armstrong(n, n, len(str(n)), 0)

print(arm_Num(153))

