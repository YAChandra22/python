n=10
m=20
for i in range(n,m+1):
    s=str(i)
    se=set(s)
    if len(se)==len(s):
        print(i)
