def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i!=0:
                return True
        else:
            return False
    else:
        return False
def Summofdigits(n):
    d=n
    s=0
    while d>0:
        rem=d%10
        d=d//10
        s=s+rem
        return s
def replaceVowels(s):
    new=' '
    for i in range(len(s)):
        if s[i] in 'aeiouAEIOU':
            k=i*100
            sum=0
            for i in range(1,k+1):
                if isPrime(i):
                    sum+=i
                    while sum>9:
                        sum=Summofdigits(sum)
                        new=str(sum)
        else:
            new+=s[i]
    print(new)
replaceVowels('Harshad')
                        
                    
    
