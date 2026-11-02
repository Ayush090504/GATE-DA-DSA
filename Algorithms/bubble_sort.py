def bubble_sort(arr,n):
    for pos in range(n-1):
        flag=0
        for j in range(n-pos-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag=1
        if flag==0:
            return arr

n=int(input('Enter the size of the array: '))
arr=[0]*n
print('Enter the elements: ')
for i in range(n):
    arr[i]=int(input())

arr=bubble_sort(arr,n)
print(arr,end=' ')