def merge_sort(arr):
    if len(arr)>1:  #base condition for recursion
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        merge(arr,left_half,right_half)
        return arr

def merge(arr,left_half,right_half):
    i=j=k=0
    while i<len(left_half) and j< len(right_half):
        if left_half[i]>right_half[j]:
            arr[k]=right_half[j]
            j+=1
        else:
            arr[k] = left_half[i]
            i+=1

        k+=1

    while j< len(right_half):
        arr[k] = right_half[j]
        j+=1
        k+=1

    while i<len(left_half):
        arr[k] = left_half[i]

        i+=1
        k+=1

    


arr= [2,23,1,56,32,45,65,27]

sorted_arr = merge_sort(arr)
print(sorted_arr)


