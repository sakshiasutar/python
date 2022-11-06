def main():
    r1=int(input("Enter the number of rows in Matrix 1:"))
    c1=int(input("Enter the number of rows in Matrix 1:"))

    A=[]
    print("Enter the data entries in the matrix A:")
    for i in range(r1):
        a=[]
        for j in range(c1):
            eleA=int(input("\tEnter the the element : "))
            a.append(eleA)
        A.append(a)
    print("Matrix 1:")
    for i in range(r1):
        print()
        for j in range(c1):
            print(A[i][j], end = " ")       
    print()

    r2=int(input("Enter the number of rows in Matrix 2:"))
    c2=int(input("Enter the number of rows in Matrix 2:"))
    
    B=[]
    print("Enter the data entries in the matrix B:")
    for i in range(r2):
        b=[]
        for j in range(c2):
            eleB=int(input("\tEnter the the element : "))
            b.append(eleB)
        B.append(b)
    print("Matrix 2:")
    for i in range(r2):
        print()
        for j in range(c2):
            print(B[i][j], end = " ")
    print()

    #Addition of matrix
    C=[]
    if r1==r2:
        if c1==c2:
            for i in range(r1):
                c=[]
                for j in range(c1):
                    res1=A[i][j]+B[i][j]
                    c.append(res1)
                C.append(c)
            print("The addition of matrix is :\n")
            for i in range(r1):
                print()
                for j in range(c1):
                    print(C[i][j],end=" ")
            print()
    else:
        print("The matrix dimensions are not equal")

    #Substraction of matirx
    D=[]
    if r1==r2:
        if c1==c2:
            for i in range(r1):
                d=[]
                for j in range(c1):
                    res2=A[i][j]-B[i][j]
                    d.append(res2)
                D.append(d)
            print("The substraction of matrix is :\n")
            for i in range(r1):
                print()
                for j in range(c2):
                    print(D[i][j],end=" ")
            print()
    else:
        print("The matrix dimensions are not equal")

    #Multiplication of matrix
    E=[]
    for i in range(r1): 
        E.append([])
        for j in range(c1):
            E[i].append(j)
            E[i][j]=0
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                E[i][j] += A[i][k] * B[k][j]

    print("The Multiplication of matrix is :\n")
    for i in range(r1):
        print()
        for j in range(c1):
            print(E[i][j],end=" ")
    print()

#Transpose of the matrix
    F = []
    import numpy
    print("The transpose of A is:")
    print(numpy.transpose(A))
    print("The transpose of B is:")
    print(numpy.transpose(B))
  
  
main()
