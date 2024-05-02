list=[1,2,3,4,5,6,7,8]
target=4
left=0
right=len(list)-1
while left<=right:
    mid=(left+right)//2
    if list[mid]==target:
        print("Target element found at:",mid)
        break
    elif list[mid]>target:
        right=mid-1
    else:
        left=mid+1


