from array import *

arr=array("i",[])
n=int(input("Enter the length of the array:"))
for i in range(n):
    x=int(input("Enter the number:"))
    arr.append(x)
print(arr)
ele=int(input("Enter the number to search for:"))
found=False
for i in range(len(arr)):
    if arr[i]==ele:
        print(ele,"found in the array")
        break
if found==False:
    print(ele,"not found in the array")
