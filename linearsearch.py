def linear_search(arr,k):
    for i in range(len(arr)):
        if arr[i]==k:
            return i
arr=[5,3,6,4,8]
k=3
result=linear_search(arr,k)
if result ==-1:
    print(f"{k} was not found in the array ")
else:
    print(f"{k} was found at index {result} in the array")