def merge_and_count(arr, low, mid, high):
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]
    i = j = 0
    k = low
    inversions = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            inversions += (len(left) - i)
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return inversions


def count_inversions(arr, low, high):
    inv_count = 0
    if low < high:
        mid = (low + high) // 2
        inv_count += count_inversions(arr, low, mid)
        inv_count += count_inversions(arr, mid + 1, high)
        inv_count += merge_and_count(arr, low, mid, high)
    return inv_count



arr = [2, 4, 1, 3, 5]
arr_copy = arr.copy()
inversions = count_inversions(arr_copy, 0, len(arr_copy) - 1)
print("Array:", arr)
print("Number of inversions:", inversions)