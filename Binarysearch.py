def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low <=high:
        mid=(low+high)//2
        if arr[mid]<target:
            low=mid+1
        elif arr[mid]>target:
            high=mid-1
        else:
            return mid
arr=[1,3,5,7,9]
target=7
result=binary_search(arr,target)
if result==-1:
    print(f"{target} was not found in the array")
else:
    print(f"{target} was found at index {result} in the array")
