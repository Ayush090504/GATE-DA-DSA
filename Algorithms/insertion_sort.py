def insertion_sort(arr,n):
    for j in range(1,n):
        key=arr[j]
        i=j-1
        while(i>=0 and arr[i]>key):
            arr[i+1]=arr[i]
            i-=1
        arr[i+1]=key
    return arr

n=int(input('Enter the size of the array: '))
arr=[0]*n
print('Enter the inputs: ')
for i in range(n):
    arr[i]=int(input())

arr=insertion_sort(arr,n)
print(arr,end=' ')
