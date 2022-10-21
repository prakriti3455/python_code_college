def prime(n):
    for i in (2,n+1):
        if n%i==0:
            return False
    return True


n=int(input())
if(prime(n)):
    print(n,"is prime")
else:
    print(n,"is not prime")







