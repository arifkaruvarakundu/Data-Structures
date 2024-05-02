def selection_sort(arr):
    n=len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index]>arr[j]:
                min_index = j

        arr[i],arr[min_index] = arr[min_index], arr[i]


my_list = [64,25,12,22,11]
selection_sort(my_list)
print("Sorted list" , my_list)