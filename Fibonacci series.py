def fib(n):
    n1=0
    n2=2
    for i in range(2,n+1):
        n3=n1+n2
        print(n3,end=" ")
        n1=n2
        n2=n3
n=int(input("Enter any value"))
fib(n)
