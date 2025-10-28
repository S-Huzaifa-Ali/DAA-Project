def power_divide_conquer(a, n):

    if n == 0:
        return 1
    elif n % 2 == 0:
        half = power_divide_conquer(a, n // 2)
        return half * half
    else:
        half = power_divide_conquer(a, n // 2)
        return a * half * half


a = 3
n = 13
result = power_divide_conquer(a, n)
print(f"Divide & Conquer -> {a}^{n} = {result}")

"""
------------------------------------------------------------
PART (3): Comparison with Brute Force Approach
------------------------------------------------------------

Brute Force Method:
-------------------
We multiply 'a' by itself n times
And this results in exactly (n - 1) multiplications
Time complexity: O(n)

Divide & Conquer Method:
------------------------
Recurrence:
    T(n) = T(n/2) + O(1)
Solution:
    T(n) = O(log n)
→ Number of multiplications ~ 2 * log₂(n)

Comparison Summary:
-------------------
| Method               | Multiplications | Time Complexity | Comment |
|----------------------|-----------------|-----------------|----------|
| Brute Force          | n - 1           | O(n)            | Slower for large n |
| Divide & Conquer     | ~2 * log₂(n)    | O(log n)        | Much faster for large n |

"""
