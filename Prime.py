def prime(n):
    x=0
    for i in range(1,n+1):
        if n%i==0:
            x=x+1
    if x==2:
        print("prime")
    else:
         print("not prime")
n=int(input("Enter any value"))
prime(n)
