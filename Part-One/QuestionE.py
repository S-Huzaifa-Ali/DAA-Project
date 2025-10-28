def closest_pair_1d(arr, low, high):
    if high - low == 1:
        return abs(arr[high] - arr[low])
    elif low == high:
        return float('inf')
    else:
        mid = (low + high) // 2
        d1 = closest_pair_1d(arr, low, mid)
        d2 = closest_pair_1d(arr, mid + 1, high)
        d3 = abs(arr[mid + 1] - arr[mid])
        return min(d1, d2, d3)



arr = [7.2, 3.1, 9.8, 5.5, 4.9, 2.3]
arr.sort()
print("Sorted array:", arr)

min_diff = closest_pair_1d(arr, 0, len(arr) - 1)
print("Smallest distance (closest pair difference):", min_diff)


#Time Complexity: O(n log n)
