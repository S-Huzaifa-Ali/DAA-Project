def find_min_max(arr, low, high):

    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]


    mid = (low + high) // 2

    min1, max1 = find_min_max(arr, low, mid)
    min2, max2 = find_min_max(arr, mid + 1, high)

    overall_min = min(min1, min2)
    overall_max = max(max1, max2)

    return overall_min, overall_max


arr = [8, 3, 5, 9, 1, 7, 2, 6]
min_val, max_val = find_min_max(arr, 0, len(arr) - 1)
print("Divide & Conquer -> Minimum:", min_val)
print("Divide & Conquer -> Maximum:", max_val)


"""
------------------------------------------------------------
PART (3): Comparison with Brute Force Approach
------------------------------------------------------------

Brute Force Method:
-------------------
We simply iterate through the array once, comparing each element
to current min and max separately.

Comparisons:
------------
- Each iteration does 2 comparisons.
- Total = 2 * (n - 1) comparisons.

Divide & Conquer Method:
------------------------
- Recurrence: T(n) = 2T(n/2) + 2
- Solution:   T(n) = 2n - 2 comparisons (for n = 2^k)

Comparison Summary:
-------------------
| Method               | Comparisons     | Comment |
|----------------------|-----------------|----------|
| Brute Force          | 2n - 2          | Efficient |
| Divide & Conquer     | 2n - 2          | Same order, slightly more overhead |

"""