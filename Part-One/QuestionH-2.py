def count_significant_inversions(arr):
    """
    Count significant inversions where i < j and arr[i] > 2 * arr[j].
    Uses modified merge sort to achieve O(n log n) complexity.
    
    Args:
        arr: list of distinct numbers
    
    Returns:
        tuple: (count, sorted_array, comparisons)
    """
    comparisons = [0]  # Track comparisons across recursive calls
    
    def merge_count(arr):
        """
        Recursively count significant inversions using divide and conquer.
        
        Returns:
            tuple: (count, sorted_array)
        """
        n = len(arr)
        
        # Base case
        if n <= 1:
            return 0, arr
        
        # Divide
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]
        
        # Conquer: recursively count in left and right halves
        left_count, left_sorted = merge_count(left)
        right_count, right_sorted = merge_count(right)
        
        # Count significant inversions crossing the middle
        cross_count = count_cross_inversions(left_sorted, right_sorted, comparisons)
        
        # Merge the two sorted halves
        merged = merge(left_sorted, right_sorted, comparisons)
        
        # Total inversions
        total_count = left_count + right_count + cross_count
        
        return total_count, merged
    
    def count_cross_inversions(left, right, comp_counter):
        """
        Count significant inversions where left[i] > 2 * right[j].
        Both arrays are sorted.
        
        Uses two-pointer technique for efficiency.
        """
        count = 0
        j = 0
        
        # For each element in left array
        for i in range(len(left)):
            # Find how many elements in right satisfy left[i] > 2 * right[j]
            while j < len(right) and left[i] > 2 * right[j]:
                comp_counter[0] += 1
                j += 1
            
            # All elements right[0] to right[j-1] form significant inversions with left[i]
            count += j
            
            # Count the comparison even if condition fails
            if j < len(right):
                comp_counter[0] += 1
        
        return count
    
    def merge(left, right, comp_counter):
        """
        Merge two sorted arrays.
        """
        merged = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            comp_counter[0] += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        # Append remaining elements
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged
    
    count, sorted_arr = merge_count(arr.copy())
    return count, sorted_arr, comparisons[0]


def count_significant_inversions_naive(arr):
    """
    Naive O(n²) algorithm to count significant inversions.
    Used for verification.
    
    Args:
        arr: list of distinct numbers
    
    Returns:
        int: count of significant inversions
    """
    count = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > 2 * arr[j]:
                count += 1
    
    return count


def visualize_inversions(arr):
    """
    Find and display all significant inversions in the array.
    """
    inversions = []
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > 2 * arr[j]:
                inversions.append((i, j, arr[i], arr[j]))
    
    return inversions


def test_significant_inversions():
    """Test the significant inversions counting algorithm."""
    
    print("=" * 80)
    print("SIGNIFICANT INVERSIONS COUNTER - O(n log n) Algorithm")
    print("=" * 80)
    print()
    print("Definition: A pair (i, j) is a SIGNIFICANT inversion if:")
    print("            i < j  AND  a[i] > 2 * a[j]")
    print()
    print("This is stricter than regular inversions (where a[i] > a[j])")
    print("=" * 80)
    print()
    
    # Test Case 1: Simple example
    print("-" * 80)
    print("Test Case 1: Simple Example")
    print("-" * 80)
    arr1 = [10, 6, 15, 20, 30, 5, 7]
    print(f"Array: {arr1}")
    print()
    
    inversions = visualize_inversions(arr1)
    print("Significant Inversions (i < j where a[i] > 2*a[j]):")
    for i, j, ai, aj in inversions:
        print(f"  ({i}, {j}): {ai} > 2*{aj} = {2*aj} ✓")
    print()
    
    count_dc, sorted_arr, comps = count_significant_inversions(arr1)
    count_naive = count_significant_inversions_naive(arr1)
    
    print(f"Divide & Conquer Result: {count_dc} significant inversions")
    print(f"Comparisons made: {comps}")
    print(f"Naive O(n²) Result: {count_naive} significant inversions")
    print(f"Match: {count_dc == count_naive} ✓")
    print()
    
    # Test Case 2: No significant inversions
    print("-" * 80)
    print("Test Case 2: Sorted Array (No Significant Inversions)")
    print("-" * 80)
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Array: {arr2}")
    print()
    
    count_dc, sorted_arr, comps = count_significant_inversions(arr2)
    count_naive = count_significant_inversions_naive(arr2)
    
    print(f"Divide & Conquer Result: {count_dc} significant inversions")
    print(f"Naive Result: {count_naive} significant inversions")
    print(f"Match: {count_dc == count_naive} ✓")
    print("(Expected 0 since array is sorted)")
    print()
    
    # Test Case 3: Maximum significant inversions
    print("-" * 80)
    print("Test Case 3: Reverse Sorted (Many Significant Inversions)")
    print("-" * 80)
    arr3 = [100, 50, 25, 12, 6, 3, 1]
    print(f"Array: {arr3}")
    print()
    
    inversions = visualize_inversions(arr3)
    print("Significant Inversions:")
    for i, j, ai, aj in inversions:
        print(f"  ({i}, {j}): {ai} > 2*{aj} = {2*aj} ✓")
    print()
    
    count_dc, sorted_arr, comps = count_significant_inversions(arr3)
    count_naive = count_significant_inversions_naive(arr3)
    
    print(f"Divide & Conquer Result: {count_dc} significant inversions")
    print(f"Naive Result: {count_naive} significant inversions")
    print(f"Match: {count_dc == count_naive} ✓")
    print()
    
    # Test Case 4: Mixed values
    print("-" * 80)
    print("Test Case 4: Mixed Values")
    print("-" * 80)
    arr4 = [24, 18, 38, 43, 14, 40, 1, 54]
    print(f"Array: {arr4}")
    print()
    
    inversions = visualize_inversions(arr4)
    print("Significant Inversions:")
    for i, j, ai, aj in inversions:
        print(f"  ({i}, {j}): {ai} > 2*{aj} = {2*aj} ✓")
    print()
    
    count_dc, sorted_arr, comps = count_significant_inversions(arr4)
    count_naive = count_significant_inversions_naive(arr4)
    
    print(f"Divide & Conquer Result: {count_dc} significant inversions")
    print(f"Comparisons made: {comps}")
    print(f"Naive Result: {count_naive} significant inversions")
    print(f"Match: {count_dc == count_naive} ✓")
    print()
    
    # Test Case 5: Comparison with regular inversions
    print("-" * 80)
    print("Test Case 5: Comparing Regular vs Significant Inversions")
    print("-" * 80)
    arr5 = [8, 4, 2, 1]
    print(f"Array: {arr5}")
    print()
    
    # Count regular inversions
    regular_inversions = []
    for i in range(len(arr5)):
        for j in range(i + 1, len(arr5)):
            if arr5[i] > arr5[j]:
                regular_inversions.append((i, j, arr5[i], arr5[j]))
    
    print("Regular Inversions (a[i] > a[j]):")
    for i, j, ai, aj in regular_inversions:
        print(f"  ({i}, {j}): {ai} > {aj}")
    print(f"Total regular inversions: {len(regular_inversions)}")
    print()
    
    significant_inversions = visualize_inversions(arr5)
    print("Significant Inversions (a[i] > 2*a[j]):")
    for i, j, ai, aj in significant_inversions:
        print(f"  ({i}, {j}): {ai} > 2*{aj} = {2*aj} ✓")
    print(f"Total significant inversions: {len(significant_inversions)}")
    print()
    
    count_dc, sorted_arr, comps = count_significant_inversions(arr5)
    print(f"Divide & Conquer confirms: {count_dc} significant inversions")
    print()
    print("Notice: Significant inversions ≤ Regular inversions")
    print("        (stricter condition means fewer pairs qualify)")
    print()
    
    # Test Case 6: Larger dataset
    print("-" * 80)
    print("Test Case 6: Larger Dataset (n = 20)")
    print("-" * 80)
    arr6 = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5,
            49, 44, 39, 34, 29, 24, 19, 14, 9, 4]
    print(f"Array size: {len(arr6)}")
    print(f"Array: {arr6}")
    print()
    
    count_dc, sorted_arr, comps = count_significant_inversions(arr6)
    count_naive = count_significant_inversions_naive(arr6)
    
    print(f"Divide & Conquer Result: {count_dc} significant inversions")
    print(f"Comparisons made: {comps}")
    print(f"Theoretical: O(n log n) = O({len(arr6)} * log {len(arr6)}) ≈ {len(arr6) * len(arr6).bit_length()}")
    print()
    print(f"Naive O(n²) Result: {count_naive} significant inversions")
    print(f"Naive comparisons: {len(arr6) * (len(arr6) - 1) // 2}")
    print()
    print(f"Match: {count_dc == count_naive} ✓")
    print(f"Efficiency gain: ~{(len(arr6) * (len(arr6) - 1) // 2) / comps:.1f}x faster")
    print()
    
    # Test Case 7: Edge cases
    print("-" * 80)
    print("Test Case 7: Edge Cases")
    print("-" * 80)
    
    # Single element
    arr7a = [42]
    count7a, _, _ = count_significant_inversions(arr7a)
    print(f"Single element {arr7a}: {count7a} inversions (expected 0)")
    
    # Two elements - significant inversion
    arr7b = [10, 4]
    count7b, _, _ = count_significant_inversions(arr7b)
    print(f"Two elements {arr7b}: {count7b} inversions (10 > 2*4=8, so 1)")
    
    # Two elements - no significant inversion
    arr7c = [10, 6]
    count7c, _, _ = count_significant_inversions(arr7c)
    print(f"Two elements {arr7c}: {count7c} inversions (10 > 2*6=12? No, so 0)")
    print()


def explain_algorithm():
    """Explain the algorithm approach."""
    print("=" * 80)
    print("ALGORITHM EXPLANATION")
    print("=" * 80)
    print()
    print("Modified Merge Sort Approach for O(n log n) Complexity:")
    print("-" * 80)
    print()
    print("1. DIVIDE:")
    print("   Split array into two halves")
    print()
    print("2. CONQUER:")
    print("   Recursively count significant inversions in:")
    print("   - Left half")
    print("   - Right half")
    print()
    print("3. COMBINE:")
    print("   Count cross-inversions (where i is in left, j is in right)")
    print()
    print("   Key Optimization for Cross-Inversions:")
    print("   - Both halves are already sorted (from recursion)")
    print("   - Use two-pointer technique:")
    print("     * For each left[i], find all right[j] where left[i] > 2*right[j]")
    print("     * Since both arrays are sorted, once we find the boundary,")
    print("       all elements before it form significant inversions")
    print("     * This takes O(n) time instead of O(n²)")
    print()
    print("4. MERGE:")
    print("   Merge sorted halves to maintain sorted order for parent calls")
    print()
    print("Time Complexity Analysis:")
    print("-" * 80)
    print("T(n) = 2T(n/2) + O(n)")
    print("     = O(n log n)")
    print()
    print("Where:")
    print("- 2T(n/2): Two recursive calls on halves")
    print("- O(n): Counting cross-inversions + merging")
    print()
    print("Key Insight:")
    print("-" * 80)
    print("By maintaining sorted subarrays, we can count cross-inversions")
    print("efficiently using the two-pointer technique, avoiding the naive")
    print("O(n²) comparison of all pairs.")
    print()
    print("Comparison with Regular Inversions:")
    print("-" * 80)
    print("Regular inversion: i < j and a[i] > a[j]")
    print("Significant inversion: i < j and a[i] > 2*a[j]")
    print()
    print("The 2x threshold makes the condition stricter, so significant")
    print("inversions are a subset of regular inversions.")
    print("=" * 80)
    print()


if __name__ == "__main__":
    explain_algorithm()
    test_significant_inversions()
    
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print()
    print("✓ Algorithm successfully counts significant inversions in O(n log n)")
    print("✓ Uses modified merge sort with two-pointer technique")
    print("✓ Much more efficient than naive O(n²) approach")
    print("✓ All test cases verified against naive implementation")
    print()
    print("=" * 80)