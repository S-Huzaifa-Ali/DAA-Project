class Database:
    
    def __init__(self, values, name):
        self.values = sorted(values)
        self.name = name
        self.query_count = 0
    
    def query(self, k):
        self.query_count += 1
        if k < 1 or k > len(self.values):
            return None
        return self.values[k - 1]
    
    def size(self):
        return len(self.values)
    
    def reset_count(self):
        self.query_count = 0


def find_median_two_databases(db1, db2):
    n = db1.size()
    
    db1.reset_count()
    db2.reset_count()
    
    left = 0
    right = n
    
    while left <= right:
        i = (left + right) // 2
        j = n - i
        
        if i == 0:
            db1_left = float('-inf')
        else:
            db1_left = db1.query(i)
        
        if i == n:
            db1_right = float('inf')
        else:
            db1_right = db1.query(i + 1)
        
        if j == 0:
            db2_left = float('-inf')
        else:
            db2_left = db2.query(j)
        
        if j == n:
            db2_right = float('inf')
        else:
            db2_right = db2.query(j + 1)
        
        if db1_left <= db2_right and db2_left <= db1_right:
            median = max(db1_left, db2_left)
            total_queries = db1.query_count + db2.query_count
            return median, total_queries
        elif db1_left > db2_right:
            right = i - 1
        else:
            left = i + 1
    
    return None, db1.query_count + db2.query_count


def verify_median(db1, db2, median):
    all_values = sorted(db1.values + db2.values)
    n = len(db1.values)
    actual_median = all_values[n - 1]
    
    return median == actual_median


def test_median_algorithm():
    
    print("=" * 75)
    print("MEDIAN OF TWO DATABASES - O(log n) Algorithm")
    print("=" * 75)
    print()
    
    print("Algorithm Overview:")
    print("-" * 75)
    print("Goal: Find the nth smallest value among 2n values in two databases")
    print("Constraint: Can only query for kth smallest value in each database")
    print("Solution: Binary search on partition point + O(log n) queries")
    print("-" * 75)
    print()
    
    print("=" * 75)
    print("Test Case 1: Simple Example (n=5)")
    print("=" * 75)
    values1 = [1, 3, 5, 7, 9]
    values2 = [2, 4, 6, 8, 10]
    db1 = Database(values1, "DB1")
    db2 = Database(values2, "DB2")
    
    print(f"Database 1: {sorted(values1)}")
    print(f"Database 2: {sorted(values2)}")
    print(f"Combined sorted: {sorted(values1 + values2)}")
    print(f"Median (5th smallest): {sorted(values1 + values2)[4]}")
    print()
    
    median, queries = find_median_two_databases(db1, db2)
    is_correct = verify_median(db1, db2, median)
    
    print(f"Algorithm Result: {median}")
    print(f"Total Queries: {queries} (DB1: {db1.query_count}, DB2: {db2.query_count})")
    print(f"Theoretical Max: O(log n) = O(log {len(values1)}) ≈ {len(values1).bit_length()}")
    print(f"Verification: {'✓ CORRECT' if is_correct else '✗ INCORRECT'}")
    print()
    
    print("=" * 75)
    print("Test Case 2: Non-Interleaved (n=6)")
    print("=" * 75)
    values1 = [1, 2, 3, 4, 5, 6]
    values2 = [7, 8, 9, 10, 11, 12]
    db1 = Database(values1, "DB1")
    db2 = Database(values2, "DB2")
    
    print(f"Database 1: {sorted(values1)}")
    print(f"Database 2: {sorted(values2)}")
    print(f"Combined sorted: {sorted(values1 + values2)}")
    print(f"Median (6th smallest): {sorted(values1 + values2)[5]}")
    print()
    
    median, queries = find_median_two_databases(db1, db2)
    is_correct = verify_median(db1, db2, median)
    
    print(f"Algorithm Result: {median}")
    print(f"Total Queries: {queries} (DB1: {db1.query_count}, DB2: {db2.query_count})")
    print(f"Theoretical Max: O(log n) = O(log {len(values1)}) ≈ {len(values1).bit_length()}")
    print(f"Verification: {'✓ CORRECT' if is_correct else '✗ INCORRECT'}")
    print()
    
    print("=" * 75)
    print("Test Case 3: Reversed Order (n=7)")
    print("=" * 75)
    values1 = [2, 4, 6, 8, 10, 12, 14]
    values2 = [1, 3, 5, 7, 9, 11, 13]
    db1 = Database(values1, "DB1")
    db2 = Database(values2, "DB2")
    
    print(f"Database 1: {sorted(values1)}")
    print(f"Database 2: {sorted(values2)}")
    combined = sorted(values1 + values2)
    print(f"Combined sorted: {combined}")
    print(f"Median (7th smallest): {combined[6]}")
    print()
    
    median, queries = find_median_two_databases(db1, db2)
    is_correct = verify_median(db1, db2, median)
    
    print(f"Algorithm Result: {median}")
    print(f"Total Queries: {queries} (DB1: {db1.query_count}, DB2: {db2.query_count})")
    print(f"Theoretical Max: O(log n) = O(log {len(values1)}) ≈ {len(values1).bit_length()}")
    print(f"Verification: {'✓ CORRECT' if is_correct else '✗ INCORRECT'}")
    print()
    
    print("=" * 75)
    print("Test Case 4: Skewed Distribution (n=8)")
    print("=" * 75)
    values1 = [1, 2, 3, 4, 100, 101, 102, 103]
    values2 = [5, 6, 7, 8, 9, 10, 11, 12]
    db1 = Database(values1, "DB1")
    db2 = Database(values2, "DB2")
    
    print(f"Database 1: {sorted(values1)}")
    print(f"Database 2: {sorted(values2)}")
    combined = sorted(values1 + values2)
    print(f"Combined sorted: {combined}")
    print(f"Median (8th smallest): {combined[7]}")
    print()
    
    median, queries = find_median_two_databases(db1, db2)
    is_correct = verify_median(db1, db2, median)
    
    print(f"Algorithm Result: {median}")
    print(f"Total Queries: {queries} (DB1: {db1.query_count}, DB2: {db2.query_count})")
    print(f"Theoretical Max: O(log n) = O(log {len(values1)}) ≈ {len(values1).bit_length()}")
    print(f"Verification: {'✓ CORRECT' if is_correct else '✗ INCORRECT'}")
    print()
    
    print("=" * 75)
    print("Test Case 5: Larger Dataset (n=16)")
    print("=" * 75)
    values1 = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61]
    values2 = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62]
    db1 = Database(values1, "DB1")
    db2 = Database(values2, "DB2")
    
    print(f"Database 1: {sorted(values1)}")
    print(f"Database 2: {sorted(values2)}")
    combined = sorted(values1 + values2)
    print(f"Combined sorted (first 10): {combined[:10]}...")
    print(f"Median (16th smallest): {combined[15]}")
    print()
    
    median, queries = find_median_two_databases(db1, db2)
    is_correct = verify_median(db1, db2, median)
    
    print(f"Algorithm Result: {median}")
    print(f"Total Queries: {queries} (DB1: {db1.query_count}, DB2: {db2.query_count})")
    print(f"Theoretical Max: O(log n) = O(log {len(values1)}) ≈ {len(values1).bit_length()}")
    print(f"Verification: {'✓ CORRECT' if is_correct else '✗ INCORRECT'}")
    print()
    
    print("=" * 75)
    print("Test Case 6: Very Large Dataset (n=1000)")
    print("=" * 75)
    import random
    random.seed(42)
    
    all_vals = list(range(1, 2001))
    random.shuffle(all_vals)
    values1 = sorted(all_vals[:1000])
    values2 = sorted(all_vals[1000:])
    
    db1 = Database(values1, "DB1")
    db2 = Database(values2, "DB2")
    
    print(f"Database 1: {len(values1)} values")
    print(f"Database 2: {len(values2)} values")
    combined = sorted(values1 + values2)
    print(f"Median (1000th smallest): {combined[999]}")
    print()
    
    median, queries = find_median_two_databases(db1, db2)
    is_correct = verify_median(db1, db2, median)
    
    print(f"Algorithm Result: {median}")
    print(f"Total Queries: {queries} (DB1: {db1.query_count}, DB2: {db2.query_count})")
    print(f"Theoretical Max: O(log n) = O(log {len(values1)}) ≈ {len(values1).bit_length()}")
    print(f"Verification: {'✓ CORRECT' if is_correct else '✗ INCORRECT'}")
    print()


def explain_algorithm():
    print("=" * 75)
    print("DETAILED ALGORITHM EXPLANATION")
    print("=" * 75)
    print()
    print("Problem:")
    print("-" * 75)
    print("• Two databases, each with n sorted values (2n total)")
    print("• Find the median = nth smallest value")
    print("• Can only query: 'give me the kth smallest value'")
    print("• Goal: Use at most O(log n) queries")
    print()
    print("Key Insight:")
    print("-" * 75)
    print("• If we take i values from DB1, we must take (n-i) from DB2")
    print("• Use binary search on i to find the correct partition")
    print("• The median is the largest value in the first n elements")
    print()
    print("Algorithm Steps:")
    print("-" * 75)
    print("1. Binary search on i (number of elements from DB1)")
    print()
    print("2. For each candidate i:")
    print("   • Query DB1[i] and DB1[i+1]     (largest taken, smallest not taken)")
    print("   • Query DB2[j] and DB2[j+1]     where j = n - i")
    print()
    print("3. Check if partition is valid:")
    print("   • DB1[i] ≤ DB2[j+1]  (largest from DB1 ≤ smallest remaining in DB2)")
    print("   • DB2[j] ≤ DB1[i+1]  (largest from DB2 ≤ smallest remaining in DB1)")
    print()
    print("4. If valid: median = max(DB1[i], DB2[j])")
    print("   If DB1[i] > DB2[j+1]: took too many from DB1, search left")
    print("   Otherwise: took too few from DB1, search right")
    print()
    print("Complexity Analysis:")
    print("-" * 75)
    print("• Binary search iterations: O(log n)")
    print("• Queries per iteration: at most 4")
    print("• Total queries: O(log n)")
    print("=" * 75)
    print()


if __name__ == "__main__":
    explain_algorithm()
    test_median_algorithm()
    
    print("=" * 75)
    print("SUMMARY")
    print("=" * 75)
    print("✓ Algorithm successfully finds median in O(log n) queries")
    print("✓ Uses binary search on partition point")
    print("✓ Each iteration uses constant (≤4) queries")
    print("✓ Much better than naive O(n) approach")
    print("=" * 75)
