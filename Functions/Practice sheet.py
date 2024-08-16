'''n=int(input())
scores=set()
for i in range(n):
    score=int(input())
    scores.add(score)
li=list(scores)
sorted(li)
print(li[-2])


n = int(input("Enter the number of scores: "))
scores = []
for i in range(1, n+1):
    score = int(input(f"Enter score {i}: "))
    scores.append(score)
m = max(scores)
runner_up = None
for i in scores:
    if i < m and (runner_up is None or i > runner_up):
        runner_up = i
print("Runner-up score:", runner_up)


n = int(input())
t = tuple(map(int, input().split()))
print(hash(t))


# Step 1: Read the integer n
n = int(input())

# Step 2: Read the space-separated integers and store them in a list
elements = list(map(int, input().split()))

# Step 3: Convert the list to a tuple
t = tuple(elements)

# Step 4: Compute the hash of the tuple
result = hash(t)

# Step 5: Print the result
print(result)

def printing_Input(arg):
    return arg
s=input()
result='welcome '+printing_Input(s)
print(result)

def multiplyby_Three(arg):
    m=arg*3
    return m
s=int(input('entr number '))
print(multiplyby_Three(s))

first_name = input()
last_name = input()
def print_full_name(first, last):
    return f'Hello {first} {last}! You just delved into python.'
    # Write your code here
print(print_full_name(first_name, last_name))

string = input()
sub_string = input()
def count_substring(string, sub_string): 
string = input()
sub_string = input()
c=0
for i in range(len(string)):
    if string[i:i+len(sub_string)]==sub_string:
        c+=1
print(c)
return c
count = count_substring(string, sub_string)
print(count)'''
def count_substring(string, sub_string):
    c=0
    for i in range(len(string)):
        if string[i:i+len(sub_string)]==sub_string:
            c+=1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

    
    
    































































