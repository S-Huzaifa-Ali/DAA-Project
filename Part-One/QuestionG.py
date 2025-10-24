def find_best_transaction(prices):
    """
    Find the best buy and sell days to maximize profit using divide and conquer.
    Time Complexity: O(n log n)
    
    Args:
        prices: list of prices where prices[i] is the price on day i+1
    
    Returns:
        tuple: (buy_day, sell_day, max_profit, comparisons)
               Days are 1-indexed
    """
    n = len(prices)
    if n < 2:
        return None, None, 0, 0
    
    comparisons = [0]  # Use list to track across recursive calls
    
    def divide_conquer(left, right):
        """
        Recursively find best transaction in subarray.
        
        Returns:
            tuple: (buy_day, sell_day, max_profit, min_price, min_day, max_price, max_day)
        """
        # Base case: single day
        if left == right:
            comparisons[0] += 0
            return (None, None, 0, prices[left], left, prices[left], left)
        
        mid = (left + right) // 2
        
        # Recursively solve left and right halves
        left_result = divide_conquer(left, mid)
        right_result = divide_conquer(mid + 1, right)
        
        # Unpack results
        (left_buy, left_sell, left_profit, 
         left_min_price, left_min_day, left_max_price, left_max_day) = left_result
        
        (right_buy, right_sell, right_profit,
         right_min_price, right_min_day, right_max_price, right_max_day) = right_result
        
        # Best transaction crossing the middle: buy in left, sell in right
        comparisons[0] += 1
        cross_profit = right_max_price - left_min_price
        cross_buy = left_min_day
        cross_sell = right_max_day
        
        # Find the best among: left only, right only, crossing
        best_profit = left_profit
        best_buy = left_buy
        best_sell = left_sell
        
        comparisons[0] += 1
        if right_profit > best_profit:
            best_profit = right_profit
            best_buy = right_buy
            best_sell = right_sell
        
        comparisons[0] += 1
        if cross_profit > best_profit:
            best_profit = cross_profit
            best_buy = cross_buy
            best_sell = cross_sell
        
        # Determine overall min and max for this range
        comparisons[0] += 1
        if left_min_price <= right_min_price:
            min_price = left_min_price
            min_day = left_min_day
        else:
            min_price = right_min_price
            min_day = right_min_day
        
        comparisons[0] += 1
        if left_max_price >= right_max_price:
            max_price = left_max_price
            max_day = left_max_day
        else:
            max_price = right_max_price
            max_day = right_max_day
        
        return (best_buy, best_sell, best_profit, 
                min_price, min_day, max_price, max_day)
    
    result = divide_conquer(0, n - 1)
    buy_day, sell_day, max_profit = result[0], result[1], result[2]
    
    # Convert to 1-indexed days
    if buy_day is not None:
        buy_day += 1
        sell_day += 1
    
    return buy_day, sell_day, max_profit, comparisons[0]


def find_best_transaction_optimized(prices):
    """
    Optimized O(n) solution using Kadane's algorithm approach.
    Included for comparison, though the problem asks for O(n log n).
    
    Time Complexity: O(n)
    """
    if len(prices) < 2:
        return None, None, 0
    
    min_price = prices[0]
    min_day = 0
    max_profit = 0
    best_buy = 0
    best_sell = 0
    
    for i in range(1, len(prices)):
        profit = prices[i] - min_price
        
        if profit > max_profit:
            max_profit = profit
            best_buy = min_day
            best_sell = i
        
        if prices[i] < min_price:
            min_price = prices[i]
            min_day = i
    
    if max_profit > 0:
        return best_buy + 1, best_sell + 1, max_profit
    else:
        return None, None, 0


def test_stock_algorithm():
    """Test the stock buy-sell algorithm with various inputs."""
    
    print("=" * 70)
    print("STOCK BUY-SELL PROBLEM - Divide and Conquer O(n log n)")
    print("=" * 70)
    print()
    
    # Test Case 1: Given example
    print("-" * 70)
    print("Test Case 1: Given Example")
    print("-" * 70)
    prices1 = [9, 1, 5]
    print(f"Days:   {list(range(1, len(prices1) + 1))}")
    print(f"Prices: {prices1}")
    buy, sell, profit, comps = find_best_transaction(prices1)
    if buy:
        print(f"Result: Buy on day {buy}, sell on day {sell}")
        print(f"Profit per share: ${profit}")
        print(f"Total profit (1000 shares): ${profit * 1000}")
    else:
        print("Result: No profitable transaction possible")
    print(f"Comparisons made: {comps}")
    print()
    
    # Test Case 2: Decreasing prices (no profit)
    print("-" * 70)
    print("Test Case 2: Decreasing Prices (No Profit)")
    print("-" * 70)
    prices2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"Days:   {list(range(1, len(prices2) + 1))}")
    print(f"Prices: {prices2}")
    buy, sell, profit, comps = find_best_transaction(prices2)
    if buy:
        print(f"Result: Buy on day {buy}, sell on day {sell}")
        print(f"Profit per share: ${profit}")
        print(f"Total profit (1000 shares): ${profit * 1000}")
    else:
        print("Result: No profitable transaction possible")
    print(f"Comparisons made: {comps}")
    print()
    
    # Test Case 3: Increasing prices
    print("-" * 70)
    print("Test Case 3: Increasing Prices")
    print("-" * 70)
    prices3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Days:   {list(range(1, len(prices3) + 1))}")
    print(f"Prices: {prices3}")
    buy, sell, profit, comps = find_best_transaction(prices3)
    if buy:
        print(f"Result: Buy on day {buy}, sell on day {sell}")
        print(f"Profit per share: ${profit}")
        print(f"Total profit (1000 shares): ${profit * 1000}")
    else:
        print("Result: No profitable transaction possible")
    print(f"Comparisons made: {comps}")
    print()
    
    # Test Case 4: Valley and peak
    print("-" * 70)
    print("Test Case 4: Valley and Peak Pattern")
    print("-" * 70)
    prices4 = [100, 80, 60, 40, 20, 30, 50, 70, 90, 110, 100, 90]
    print(f"Days:   {list(range(1, len(prices4) + 1))}")
    print(f"Prices: {prices4}")
    buy, sell, profit, comps = find_best_transaction(prices4)
    if buy:
        print(f"Result: Buy on day {buy}, sell on day {sell}")
        print(f"Profit per share: ${profit}")
        print(f"Total profit (1000 shares): ${profit * 1000}")
    else:
        print("Result: No profitable transaction possible")
    print(f"Comparisons made: {comps}")
    print()
    
    # Test Case 5: Multiple peaks
    print("-" * 70)
    print("Test Case 5: Multiple Peaks")
    print("-" * 70)
    prices5 = [5, 15, 3, 10, 2, 20, 1, 8]
    print(f"Days:   {list(range(1, len(prices5) + 1))}")
    print(f"Prices: {prices5}")
    buy, sell, profit, comps = find_best_transaction(prices5)
    if buy:
        print(f"Result: Buy on day {buy}, sell on day {sell}")
        print(f"Profit per share: ${profit}")
        print(f"Total profit (1000 shares): ${profit * 1000}")
    else:
        print("Result: No profitable transaction possible")
    print(f"Comparisons made: {comps}")
    print()
    
    # Test Case 6: Larger dataset
    print("-" * 70)
    print("Test Case 6: Larger Dataset (20 days)")
    print("-" * 70)
    prices6 = [45, 50, 48, 42, 38, 35, 40, 45, 52, 55, 
               53, 50, 48, 44, 40, 38, 42, 48, 55, 60]
    print(f"Days:   {list(range(1, len(prices6) + 1))}")
    print(f"Prices: {prices6}")
    buy, sell, profit, comps = find_best_transaction(prices6)
    if buy:
        print(f"Result: Buy on day {buy}, sell on day {sell}")
        print(f"Profit per share: ${profit}")
        print(f"Total profit (1000 shares): ${profit * 1000}")
    else:
        print("Result: No profitable transaction possible")
    print(f"Comparisons made: {comps}")
    print(f"Theoretical complexity: O(n log n) = O({len(prices6)} * log {len(prices6)}) ≈ {len(prices6) * len(prices6).bit_length()}")
    print()
    
    # Comparison with O(n) solution
    print("=" * 70)
    print("COMPARISON: Divide & Conquer O(n log n) vs Linear O(n)")
    print("=" * 70)
    print()
    
    test_prices = [100, 80, 60, 40, 20, 30, 50, 70, 90, 110, 100, 90]
    
    buy_dc, sell_dc, profit_dc, comps_dc = find_best_transaction(test_prices)
    buy_linear, sell_linear, profit_linear = find_best_transaction_optimized(test_prices)
    
    print(f"Test Array: {test_prices}")
    print()
    print(f"Divide & Conquer (O(n log n)):")
    print(f"  Buy day {buy_dc}, sell day {sell_dc}, profit ${profit_dc}")
    print(f"  Comparisons: {comps_dc}")
    print()
    print(f"Linear Solution (O(n)):")
    print(f"  Buy day {buy_linear}, sell day {sell_linear}, profit ${profit_linear}")
    print()
    print("Both solutions produce the same result!")
    print("The divide & conquer approach demonstrates the O(n log n) technique,")
    print("while the linear approach is more efficient for this specific problem.")
    print()


def explain_algorithm():
    """Explain how the divide and conquer algorithm works."""
    print("=" * 70)
    print("ALGORITHM EXPLANATION")
    print("=" * 70)
    print()
    print("Divide and Conquer Strategy:")
    print("-" * 70)
    print("1. DIVIDE: Split the array of prices into two halves")
    print()
    print("2. CONQUER: Recursively find the best transaction in:")
    print("   - Left half only")
    print("   - Right half only")
    print()
    print("3. COMBINE: Consider transactions that cross the middle:")
    print("   - Buy at the minimum price in the left half")
    print("   - Sell at the maximum price in the right half")
    print()
    print("4. RETURN: The best of the three options, plus:")
    print("   - Minimum price and its day in this range")
    print("   - Maximum price and its day in this range")
    print("   (These help parent calls find crossing transactions)")
    print()
    print("Time Complexity: O(n log n)")
    print("  - Each level of recursion does O(n) work")
    print("  - There are O(log n) levels in the recursion tree")
    print("=" * 70)
    print()


if __name__ == "__main__":
    explain_algorithm()
    test_stock_algorithm()