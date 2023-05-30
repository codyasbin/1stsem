def linearserch(arr,x):
    for i in range (len(arr)):
        if arr[i]==x:
         return i
    return-1
arr=["Hi","Hello","Set","Ss","C","ISMT","o","l"]
x="Hello"
indexofElement=linearserch(arr,x)
if indexofElement<0:
    print("Element not found"+str(indexofElement))
else:
    print("Element found at index"+str(indexofElement))


