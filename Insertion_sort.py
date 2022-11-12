arr=[]
n=int(input("Enter the length of the array:"))
for i in range(n):
    x=int(input("Enter the value:"))
    arr.append(x)
print(arr)

def insertion_sort(arr):
    for i in range(n):
        current=arr[i]
        pos=i
        while current<arr[pos-1] and pos>0:
            arr[pos]=arr[pos-1]
            pos=pos-1
        arr[pos]=current

insertion_sort(arr)
print(arr)

