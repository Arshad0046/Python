#a num pos or neg
num=10
if num>0:
    print('positive')
elif num<0:
    print('negative')
else:
    print('zero')

#a num even or odd
num=3
if num%2==0:
    print('even number')
else:
    print('odd')

#sum of n natural numbers
n=6
sum=0
for i in range(n+1):
    sum+=i
print(sum)

# sum of numbers in given intervel
num1,num2=3,6
sum=0
for i in range(num1,num2+1):
    sum=sum+i
print(sum)

#greatest of two numbers
a,b=20,40
if a>b:
    print(f'{a} is grater than b')
else:
    print(f'{b} is greater than a')

#greatest of three numbers
a,b,c=20,30,10
if a>b and b>c:
    print(f'{a} is greater than b,c')
elif b>c and b>a:
    print(f'{b} is greater than a,c')
else:
    print(f'{c} is greater than b,a')

#leap year or not
y=int(input('enter a year:'))
if (y%4==0 and y%100!=0) or y%400==0:
    print('leap year')
else:
    print('not a leap year')

#check a num is prime number or not
num=11
for i in range(2,num):
    if num%i==0:
       break
else:
    print('prime',num)
    
num=11
flag=0
for i in range(2,num):
    if num%i==0:
        flag=1
if flag==1:
    print('not prime')
else:
    print('prime')

#print prime numbers in a given range
low=2
high=10
prime=[]
for i in range(low,high+1):
    flag=0
    if i==1:
        continue
    for x in range(2,i):
        if i%x==0:
            flag=1
    if flag==0:
        prime.append(i)
print(prime)

#sum of digits
s=input('enter the number:')
sum=0
for i in s:
    sum=sum+int(i)
print(sum)

# reverse a string
num=input()
reverse=""
for i in num:
    reverse=i+reverse
print(reverse)

num=1234
reversed=0
while num>0:
    remainder=num%10
    reversed=(reversed*10)+remainder
    num=num//10
print(reversed)

#print prime numbers
n=10
for i in range(n):
    if i==0:
        continue
    if i==1:
        continue
    for j in range(2,i):
        if i %j==0:
            break
    else:
        print(i)

#check a num palindrome or not
n=1221
t=n
reversed=0
while t>0:
    remainder=t%10
    reversed=(reversed*10)+remainder
    t=t//10
if n==reversed:
    print('palindrome')
else:
    print('not prime')

#check arm strong or not
n=input()
n1=input()
sum=0
num=int(n)
num1=int(n)
for i in str(num,num1):
    sum+=int(i)**len(str(num))
print(sum)


#print arm strong specific range
low=10
high=1000
for i in range(low,high+1):
    order=len(str(i))
    sum=0
    temp=i
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
    if i==sum:
        print(i)

#fibonacci number upto n
n=10
n1,n2=0,1
print(n1,n2)
for i in range(2,n):
    n3=n1+n2
    print(n3)
    n1,n2=n2,n3


n=10
n1,n2=0,1
i=2
while i<n:
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
    i+=1

#using fibnoacci series nth term
def fib(n):
    if n<2:
        return n
    return fib(n-1)+fib(n-2)
n=6
print(fib(n-1))

#factorial of a number 
n=6
fact=1
if n<0:
    print('not possible')
else:
    for i in range(1,n+1):
        fact=fact*i
print('factorial of',n,'is',fact)


def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
a=fact(6)
print(a)

num = int(input('enter numbers:'))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is", factorial)

#power of number
n=2
p=3
print(pow(n,p))
print(n**p)
  
#factors of number
n=10
l=[]
for i in range(1,n):
    if n%i==0:
       l.append(i)
print(f'factors of 10 is {l}')


#factor of a number
def factor(n):
    i=1
    while i<=n:
        if n%i==0:
            print(i,end=' ')
        i+=1
print('factors are')
factor(28)



#perfect number
def perfect_num(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
        #print(i,end=' ')
            sum=sum+i
    if sum==n:
        return "perfect"
print(perfect_num(6))



#check perfect square or not
import math
def perfect_square(n):
    if(math.ceil(math.sqrt(n))==math.floor(math.sqrt(n))):
        print(True)
    else:
        print(False)
perfect_square(49)


#Automorphic number using python
num=int(input("enter the number:"))
sqrt=num*num
if num%10!=sqrt%10:
    print('not 2automorphic')
else:
    print('automorphic')

#Harshad or not 
n=21
p=n
sum=0
while(n>0):
    sum+=n%10
    n=n//10
if(p%sum==0):
    print('Harshad number')
else:
    print('not Harshad number')

#check abundant number
n=12
sum=1
for i in range(2,n):
    if n%i==0:
        sum+=i
if (sum>n):
    print(n,'is abundant number')
else:
    print(n,'is not abundant number')

#friendly pairs
def sum_proper_divisors(n):
    """Calculate the sum of proper divisors of a number (excluding itself)."""
    return sum(i for i in range(1, n) if n % i == 0)

def is_friendly_pair(a, b):
    """Check if (a, b) is a friendly pair."""
    return (sum_proper_divisors(a) == b and 
            sum_proper_divisors(b) == a)

# Example usage
num1 = 220
num2 = 284

if is_friendly_pair(num1, num2):
    print(f"({num1}, {num2}) are friendly pairs!")
else:
    print(f"({num1}, {num2}) are NOT friendly pairs.")


#friendly number
n1=int(input('enter number1'))
n2=int(input('enter number2'))
sum1=0
sum2=0
for i in range(1,n1):
    if n1%i==0:
        sum1=sum1+i
sum1=sum1//n1
for j in range(1,n2):
    if n2%j==0:
        sum2=sum2+j
sum2=sum2//n2
if(sum1==sum2):
    print('it is a friendly number')
else:
    print('not a friendly number')