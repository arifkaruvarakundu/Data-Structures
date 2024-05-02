def Heapify(arr,n,i):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left<n and arr[left]>arr[largest]:
        largest = left
    if right<n and arr[right]>arr[largest]:
        largest = right
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        Heapify(arr,n,largest)

def Heap_sort(arr):
    n= len(arr)

    for i in range(n//2-1,-1,-1): # Building heap
        Heapify(arr,n,i)

    for i in range(n-1,0,-1):       #Deleting and swapping
        arr[i],arr[0]=arr[0],arr[i]
        Heapify(arr,i,0)

    return arr
    
arr = [7,1,9,3,5,2,8,6,4]
sorted_arr = Heap_sort(arr)
print(sorted_arr)
