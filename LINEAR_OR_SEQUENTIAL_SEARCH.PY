def sequential_search(arr, target):
    idx = 0
    while idx < len(arr):
        if arr[idx] == target:
            return idx 
        idx += 1
    return -1 

