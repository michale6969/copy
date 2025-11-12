def linear_search(arr, target):
    for elem in arr:
        if elem == target:
            return True
    return False

def binary_search(arr, target):
    arr.sort()
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

accounts = [int(acc) for acc in input("Enter account numbers separated by spaces: ").split(",")]
target = int(input("target:"))


print("Linear Search:", linear_search(accounts, target))
print("Binary Search:", binary_search(accounts, target))

    
