# if we have a sequence if we find the value in the sequence then we can use binary search,
# how its work is we have to find the middle element of the sequence and compare the value with the middle element


def binary_search(seq, val):
    left, right = 0, len(seq)-1
    
    while  left <= right:
        
        mid = (left + right ) // 2
        
        if seq[mid] == val:
            return mid
        
        elif seq[mid]<val:
            left = mid + 1
        else :
            right = mid - 1
    return -1

arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search(arr, target)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")