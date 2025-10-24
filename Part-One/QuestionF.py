def find_peak_unimodal(A):
    """
    Find the peak entry in a unimodal array using divide and conquer.
    Time Complexity: O(log n)
    
    Args:
        A: A unimodal array where values increase up to position p, then decrease
    
    Returns:
        tuple: (peak_value, peak_index, comparisons_made)
    """
    left = 0
    right = len(A) - 1
    comparisons = 0
    
    while left < right:
        mid = (left + right) // 2
        comparisons += 1
        
        # Compare mid with mid+1 to determine which side has the peak
        if A[mid] < A[mid + 1]:
            # Peak is in the right half (mid+1 to right)
            left = mid + 1
        else:
            # Peak is in the left half (left to mid, inclusive)
            right = mid
    
    # left == right, we've found the peak
    return A[left], left, comparisons


def create_unimodal_array(n, peak_position):
    """
    Create a unimodal array of size n with peak at peak_position.
    
    Args:
        n: size of the array
        peak_position: index where the peak should be (0 to n-1)
    
    Returns:
        list: unimodal array
    """
    A = []
    
    # Increasing part (up to peak)
    for i in range(peak_position + 1):
        A.append(i * 10 + 5)
    
    # Decreasing part (after peak)
    for i in range(peak_position + 1, n):
        A.append((2 * peak_position - i) * 10 + 5)
    
    return A


def test_algorithm():
    """Test the peak finding algorithm with various inputs."""
    
    # Test Case 1: Array of size 10
    print("=" * 60)
    print("Test Case 1: Array of size 10, peak at position 6")
    print("=" * 60)
    n1 = 10
    peak_pos1 = 6
    A1 = create_unimodal_array(n1, peak_pos1)
    print(f"Array: {A1}")
    peak_val, peak_idx, comps = find_peak_unimodal(A1)
    print(f"Peak found: {peak_val} at index {peak_idx}")
    print(f"Number of comparisons: {comps}")
    print(f"Theoretical maximum: O(log {n1}) ≈ {n1.bit_length() - 1} comparisons")
    print()
    
    # Test Case 2: Array of size 15
    print("=" * 60)
    print("Test Case 2: Array of size 15, peak at position 3")
    print("=" * 60)
    n2 = 15
    peak_pos2 = 3
    A2 = create_unimodal_array(n2, peak_pos2)
    print(f"Array: {A2}")
    peak_val, peak_idx, comps = find_peak_unimodal(A2)
    print(f"Peak found: {peak_val} at index {peak_idx}")
    print(f"Number of comparisons: {comps}")
    print(f"Theoretical maximum: O(log {n2}) ≈ {n2.bit_length() - 1} comparisons")
    print()
    
    # Test Case 3: Array of size 20
    print("=" * 60)
    print("Test Case 3: Array of size 20, peak at position 12")
    print("=" * 60)
    n3 = 20
    peak_pos3 = 12
    A3 = create_unimodal_array(n3, peak_pos3)
    print(f"Array: {A3}")
    peak_val, peak_idx, comps = find_peak_unimodal(A3)
    print(f"Peak found: {peak_val} at index {peak_idx}")
    print(f"Number of comparisons: {comps}")
    print(f"Theoretical maximum: O(log {n3}) ≈ {n3.bit_length() - 1} comparisons")
    print()
    
    # Test Case 4: Custom input
    print("=" * 60)
    print("Test Case 4: Custom unimodal array")
    print("=" * 60)
    custom_array = [1, 3, 5, 7, 9, 11, 13, 15, 12, 10, 8, 6, 4, 2]
    print(f"Array: {custom_array}")
    peak_val, peak_idx, comps = find_peak_unimodal(custom_array)
    print(f"Peak found: {peak_val} at index {peak_idx}")
    print(f"Number of comparisons: {comps}")
    print(f"Theoretical maximum: O(log {len(custom_array)}) ≈ {len(custom_array).bit_length() - 1} comparisons")
    print()
    
    # Test Case 5: Edge case - peak at beginning
    print("=" * 60)
    print("Test Case 5: Peak at the beginning (index 0)")
    print("=" * 60)
    A5 = create_unimodal_array(12, 0)
    print(f"Array: {A5}")
    peak_val, peak_idx, comps = find_peak_unimodal(A5)
    print(f"Peak found: {peak_val} at index {peak_idx}")
    print(f"Number of comparisons: {comps}")
    print()
    
    # Test Case 6: Edge case - peak at end
    print("=" * 60)
    print("Test Case 6: Peak at the end (index n-1)")
    print("=" * 60)
    n6 = 12
    A6 = create_unimodal_array(n6, n6-1)
    print(f"Array: {A6}")
    peak_val, peak_idx, comps = find_peak_unimodal(A6)
    print(f"Peak found: {peak_val} at index {peak_idx}")
    print(f"Number of comparisons: {comps}")
    print()


if __name__ == "__main__":
    print("\n" + "="*60)
    print("UNIMODAL ARRAY PEAK FINDER - O(log n) Algorithm")
    print("="*60 + "\n")
    
    print("Algorithm Explanation:")
    print("-" * 60)
    print("This divide-and-conquer algorithm finds the peak in O(log n) time by:")
    print("1. Examining the middle element and its right neighbor")
    print("2. If A[mid] < A[mid+1], the peak must be in the right half")
    print("3. Otherwise, the peak is in the left half (including mid)")
    print("4. Recursively narrow down the search space until found")
    print("-" * 60 + "\n")
    
    test_algorithm()
    
    print("\n" + "="*60)
    print("Algorithm successfully demonstrates O(log n) complexity!")
    print("="*60)