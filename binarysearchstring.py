def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = ["C", "Hi", "Hello", "ISMT", "Ss", "Set", "l", "o"]
x = "Hi"
index_of_element = binary_search(arr, x)

if index_of_element < 0:
    print("Element not found: " + str(index_of_element))
else:
    print("Element found at index: " + str(index_of_element))
