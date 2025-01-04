def linear(arr, target):
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [a for a in range(1,4,1000)]

target = input('enter the target:')

res = linear(arr, target)