'''s=input('enter str: ')
n=int(input('entr number '))
count=0
for i in s:
    if ord(i)==n:
      count+=1
print(count)

s=input('entr str: ')
list=[]
for i in s:
    list.append(sorted(i))
print(min(list))
print(list)

s=input()
for i in s:
    if i.isupper():
        print(ord(i))
        break

m=int(input('entr st.no.: '))
n=int(input('entr end no.: '))
for i in range(m,n+1):
    print(f'{i}: ',chr(i),end='\n')
    
 '''
n=int(input('entr n: '))
l=[]
for i in range(n):
    m=int(input())
    l.append(chr(m))
print(''.join(str(l)))










































