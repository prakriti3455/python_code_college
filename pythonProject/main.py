n=int(input())
while n!=6:
    if n<=5 and n>=1:
        a=int(input())
        b=int(input())
    if n==1:
        print(a+b)
    if n==2:
        print(a-b)
    if n==3:
        print(a*b)
    if n==4:
        print(a//b)
    if n==5:
        print(a%b)
    elif n<1 or n>6:
        print("Invalid Operation")
    n=int(input())

