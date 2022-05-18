a=3
b=9
c=1
d=2
e=6
if a>b:
    smallest=b
    secondsmallest=a
else:
    smallest=a
    secondsmallest=b
    
if secondsmallest>c:
    if smallest>c:
        secondsmallest=smallest
        smallest=c
    else:
        secondsmallest=c
if secondsmallest>d:
    if smallest>d:
        secondsmallest=smallest
        smallest=d
    else:
        secondsmallest=d
if secondsmallest>e:
    if smallest>e:
        secondsmallest=smallest
        smallest=e
    else:
        secondsmallest=e
print(secondsmallest)
    
