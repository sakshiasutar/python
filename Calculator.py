def cal(a,b,op):
      if op=="+":
          print("Addition",a+b)
      if op=="-":
          print("subtraction",a-b)
      if op=="*":
          print("multiplication",a*b)
      if op=="/":
          print("division",a/b)
status="yes"
while status=='yes':
          n1=int(input("Enter any no."))
          n2=int(input("Enter any no."))
          print("which operator u want to select(+,-,*,/)")
          op=(input("enter a no."))
          cal(n1,n2,op)
          print("Do u want to continue(yes/no)")
          status=input()
