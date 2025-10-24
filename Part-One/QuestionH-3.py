class BankCard:
    """Represents a bank card with an account number."""
    
    def __init__(self, card_id, account):
        self.card_id = card_id
        self.account = account
    
    def __repr__(self):
        return f"Card{self.card_id}(Acc:{self.account})"


class EquivalenceTester:
    """
    Simulates the equivalence tester device.
    Can compare two cards and determine if they're equivalent.
    """
    
    def __init__(self):
        self.comparison_count = 0
    
    def are_equivalent(self, card1, card2):
        """
        Check if two cards correspond to the same account.
        
        Args:
            card1, card2: BankCard objects
        
        Returns:
            bool: True if cards have same account
        """
        self.comparison_count += 1
        return card1.account == card2.account
    
    def reset_count(self):
        """Reset the comparison counter."""
        self.comparison_count = 0
    
    def get_count(self):
        """Get the number of comparisons made."""
        return self.comparison_count


def find_majority_card(cards, tester):
    """
    Find if there exists a set of more than n/2 cards that are equivalent.
    Uses divide-and-conquer to achieve O(n log n) comparisons.
    
    Algorithm:
    1. Divide cards into two halves
    2. Recursively find majority candidate in each half
    3. If both halves have same candidate, verify it
    4. If different candidates, test both to see which (if any) is global majority
    
    Args:
        cards: list of BankCard objects
        tester: EquivalenceTester object
    
    Returns:
        BankCard or None: A card representing the majority account, or None
    """
    
    def find_candidate(cards_subset):
        """
        Recursively find a majority candidate using divide and conquer.
        
        Returns:
            BankCard or None: candidate card
        """
        n = len(cards_subset)
        
        # Base cases
        if n == 0:
            return None
        if n == 1:
            return cards_subset[0]
        if n == 2:
            # Check if they're equivalent
            if tester.are_equivalent(cards_subset[0], cards_subset[1]):
                return cards_subset[0]
            else:
                return None
        
        # Divide
        mid = n // 2
        left_cards = cards_subset[:mid]
        right_cards = cards_subset[mid:]
        
        # Conquer: find candidates in each half
        left_candidate = find_candidate(left_cards)
        right_candidate = find_candidate(right_cards)
        
        # Combine
        # Case 1: One or both halves have no candidate
        if left_candidate is None and right_candidate is None:
            return None
        
        if left_candidate is None:
            # Check if right_candidate is majority in full subset
            count = count_equivalent(cards_subset, right_candidate, tester)
            return right_candidate if count > n // 2 else None
        
        if right_candidate is None:
            # Check if left_candidate is majority in full subset
            count = count_equivalent(cards_subset, left_candidate, tester)
            return left_candidate if count > n // 2 else None
        
        # Case 2: Both halves have candidates
        # Check if they're the same
        if tester.are_equivalent(left_candidate, right_candidate):
            # Same candidate in both halves - guaranteed to be majority
            return left_candidate
        
        # Different candidates - check both
        left_count = count_equivalent(cards_subset, left_candidate, tester)
        right_count = count_equivalent(cards_subset, right_candidate, tester)
        
        if left_count > n // 2:
            return left_candidate
        elif right_count > n // 2:
            return right_candidate
        else:
            return None
    
    def count_equivalent(cards_subset, candidate, tester):
        """Count how many cards in subset are equivalent to candidate."""
        if candidate is None:
            return 0
        
        count = 0
        for card in cards_subset:
            if tester.are_equivalent(card, candidate):
                count += 1
        return count
    
    # Find the candidate
    candidate = find_candidate(cards)
    
    if candidate is None:
        return None
    
    # Verify candidate is actually majority in full set
    # (This final check is already done in the recursion, but we can do it again)
    final_count = count_equivalent(cards, candidate, tester)
    
    if final_count > len(cards) // 2:
        return candidate
    else:
        return None


def find_majority_card_optimized(cards, tester):
    """
    Optimized O(n log n) algorithm using Boyer-Moore-like pairing.
    
    This is a cleaner implementation that pairs up cards and eliminates
    different pairs, similar to Boyer-Moore majority vote.
    
    Returns:
        BankCard or None: majority card or None
    """
    
    def find_candidate_optimized(cards_subset):
        """Find potential majority candidate."""
        n = len(cards_subset)
        
        if n == 0:
            return None
        if n == 1:
            return cards_subset[0]
        
        # Pair up cards and keep one from each equivalent pair
        survivors = []
        i = 0
        
        while i < n - 1:
            if tester.are_equivalent(cards_subset[i], cards_subset[i + 1]):
                # Equivalent pair - keep one
                survivors.append(cards_subset[i])
                i += 2
            else:
                # Different pair - eliminate both
                i += 2
        
        # If odd number of cards, last one survives
        if i == n - 1:
            survivors.append(cards_subset[-1])
        
        # Recursively find candidate among survivors
        if len(survivors) == 0:
            return None
        elif len(survivors) == 1:
            return survivors[0]
        else:
            return find_candidate_optimized(survivors)
    
    def count_equivalent(cards_subset, candidate):
        """Count equivalent cards."""
        if candidate is None:
            return 0
        count = 0
        for card in cards_subset:
            if tester.are_equivalent(card, candidate):
                count += 1
        return count
    
    # Find candidate
    candidate = find_candidate_optimized(cards)
    
    if candidate is None:
        return None
    
    # Verify candidate is majority
    count = count_equivalent(cards, candidate)
    
    return candidate if count > len(cards) // 2 else None


def test_fraud_detection():
    """Test the bank card fraud detection algorithm."""
    
    print("=" * 80)
    print("BANK CARD FRAUD DETECTION - O(n log n) Algorithm")
    print("=" * 80)
    print()
    print("Problem: Given n bank cards, determine if more than n/2 cards")
    print("         correspond to the same account (potential fraud).")
    print()
    print("Constraint: Can only use equivalence tester to compare pairs.")
    print("Goal: Use O(n log n) comparisons.")
    print("=" * 80)
    print()
    
    # Test Case 1: Clear majority
    print("-" * 80)
    print("Test Case 1: Clear Majority (7 out of 10 cards)")
    print("-" * 80)
    tester = EquivalenceTester()
    cards1 = [
        BankCard(1, "ACC_A"),
        BankCard(2, "ACC_A"),
        BankCard(3, "ACC_B"),
        BankCard(4, "ACC_A"),
        BankCard(5, "ACC_A"),
        BankCard(6, "ACC_C"),
        BankCard(7, "ACC_A"),
        BankCard(8, "ACC_A"),
        BankCard(9, "ACC_D"),
        BankCard(10, "ACC_A"),
    ]
    
    print(f"Cards: {cards1}")
    print(f"Account distribution:")
    from collections import Counter
    dist = Counter(c.account for c in cards1)
    for acc, count in sorted(dist.items()):
        print(f"  {acc}: {count} cards", "← MAJORITY!" if count > len(cards1)//2 else "")
    print()
    
    tester.reset_count()
    result = find_majority_card(cards1, tester)
    
    print(f"Result: {'FRAUD DETECTED!' if result else 'No fraud detected'}")
    if result:
        print(f"Majority account: {result.account}")
    print(f"Comparisons used: {tester.get_count()}")
    print(f"Theoretical max: O(n log n) ≈ {len(cards1) * len(cards1).bit_length()}")
    print()
    
    # Test Case 2: No majority
    print("-" * 80)
    print("Test Case 2: No Majority (evenly distributed)")
    print("-" * 80)
    tester2 = EquivalenceTester()
    cards2 = [
        BankCard(1, "ACC_A"),
        BankCard(2, "ACC_A"),
        BankCard(3, "ACC_B"),
        BankCard(4, "ACC_B"),
        BankCard(5, "ACC_C"),
        BankCard(6, "ACC_C"),
        BankCard(7, "ACC_D"),
        BankCard(8, "ACC_D"),
    ]
    
    print(f"Cards: {cards2}")
    print(f"Account distribution:")
    dist = Counter(c.account for c in cards2)
    for acc, count in sorted(dist.items()):
        print(f"  {acc}: {count} cards")
    print()
    
    tester2.reset_count()
    result = find_majority_card(cards2, tester2)
    
    print(f"Result: {'FRAUD DETECTED!' if result else 'No fraud detected'}")
    if result:
        print(f"Majority account: {result.account}")
    print(f"Comparisons used: {tester2.get_count()}")
    print()
    
    # Test Case 3: Exact threshold (n/2 + 1)
    print("-" * 80)
    print("Test Case 3: Exact Threshold (6 out of 11 cards = just over n/2)")
    print("-" * 80)
    tester3 = EquivalenceTester()
    cards3 = [
        BankCard(1, "ACC_X"),
        BankCard(2, "ACC_X"),
        BankCard(3, "ACC_Y"),
        BankCard(4, "ACC_X"),
        BankCard(5, "ACC_Z"),
        BankCard(6, "ACC_X"),
        BankCard(7, "ACC_X"),
        BankCard(8, "ACC_W"),
        BankCard(9, "ACC_X"),
        BankCard(10, "ACC_V"),
        BankCard(11, "ACC_U"),
    ]
    
    print(f"Cards: {cards3}")
    print(f"n = {len(cards3)}, n/2 = {len(cards3)//2}")
    print(f"Account distribution:")
    dist = Counter(c.account for c in cards3)
    for acc, count in sorted(dist.items()):
        print(f"  {acc}: {count} cards", "← MAJORITY!" if count > len(cards3)//2 else "")
    print()
    
    tester3.reset_count()
    result = find_majority_card(cards3, tester3)
    
    print(f"Result: {'FRAUD DETECTED!' if result else 'No fraud detected'}")
    if result:
        print(f"Majority account: {result.account}")
    print(f"Comparisons used: {tester3.get_count()}")
    print()
    
    # Test Case 4: Almost majority (exactly n/2)
    print("-" * 80)
    print("Test Case 4: Almost Majority (5 out of 10 = exactly n/2, NOT majority)")
    print("-" * 80)
    tester4 = EquivalenceTester()
    cards4 = [
        BankCard(1, "ACC_M"),
        BankCard(2, "ACC_M"),
        BankCard(3, "ACC_M"),
        BankCard(4, "ACC_M"),
        BankCard(5, "ACC_M"),
        BankCard(6, "ACC_N"),
        BankCard(7, "ACC_O"),
        BankCard(8, "ACC_P"),
        BankCard(9, "ACC_Q"),
        BankCard(10, "ACC_R"),
    ]
    
    print(f"Cards: {cards4}")
    print(f"n = {len(cards4)}, n/2 = {len(cards4)//2}")
    print(f"Account distribution:")
    dist = Counter(c.account for c in cards4)
    for acc, count in sorted(dist.items()):
        print(f"  {acc}: {count} cards", "← exactly n/2" if count == len(cards4)//2 else "")
    print()
    
    tester4.reset_count()
    result = find_majority_card(cards4, tester4)
    
    print(f"Result: {'FRAUD DETECTED!' if result else 'No fraud detected'}")
    if result:
        print(f"Majority account: {result.account}")
    print(f"Comparisons used: {tester4.get_count()}")
    print("Note: Exactly n/2 is NOT a majority (need STRICTLY more than n/2)")
    print()
    
    # Test Case 5: All same (extreme fraud)
    print("-" * 80)
    print("Test Case 5: All Same Account (Extreme Fraud!)")
    print("-" * 80)
    tester5 = EquivalenceTester()
    cards5 = [BankCard(i, "ACC_FRAUD") for i in range(1, 16)]
    
    print(f"Cards: 15 cards, all with account ACC_FRAUD")
    print()
    
    tester5.reset_count()
    result = find_majority_card(cards5, tester5)
    
    print(f"Result: {'FRAUD DETECTED!' if result else 'No fraud detected'}")
    if result:
        print(f"Majority account: {result.account}")
    print(f"Comparisons used: {tester5.get_count()}")
    print(f"Theoretical max: O(n log n) ≈ {len(cards5) * len(cards5).bit_length()}")
    print()
    
    # Test Case 6: Larger dataset
    print("-" * 80)
    print("Test Case 6: Larger Dataset (n = 50)")
    print("-" * 80)
    tester6 = EquivalenceTester()
    
    # Create 30 cards with ACC_FRAUD, 20 with other accounts
    cards6 = []
    for i in range(30):
        cards6.append(BankCard(i, "ACC_FRAUD"))
    for i in range(20):
        cards6.append(BankCard(30 + i, f"ACC_{i}"))
    
    # Shuffle to make it more realistic
    import random
    random.seed(42)
    random.shuffle(cards6)
    
    print(f"Total cards: {len(cards6)}")
    print(f"n/2 = {len(cards6)//2}")
    dist = Counter(c.account for c in cards6)
    print(f"Account distribution (top 5):")
    for acc, count in dist.most_common(5):
        print(f"  {acc}: {count} cards", "← MAJORITY!" if count > len(cards6)//2 else "")
    print()
    
    tester6.reset_count()
    result = find_majority_card(cards6, tester6)
    
    print(f"Result: {'FRAUD DETECTED!' if result else 'No fraud detected'}")
    if result:
        print(f"Majority account: {result.account}")
        actual_count = sum(1 for c in cards6 if c.account == result.account)
        print(f"Actual count: {actual_count} out of {len(cards6)}")
    print(f"Comparisons used: {tester6.get_count()}")
    print(f"Theoretical max: O(n log n) ≈ {len(cards6) * len(cards6).bit_length()}")
    print(f"Naive approach would need: O(n²) ≈ {len(cards6) * len(cards6)} comparisons")
    print()


def explain_algorithm():
    """Explain the algorithm."""
    print("=" * 80)
    print("ALGORITHM EXPLANATION")
    print("=" * 80)
    print()
    print("Divide-and-Conquer Strategy:")
    print("-" * 80)
    print()
    print("1. DIVIDE: Split cards into two equal halves")
    print()
    print("2. CONQUER: Recursively find majority candidate in each half")
    print()
    print("3. COMBINE: Analyze candidates from both halves")
    print()
    print("   Case A: Both halves have SAME candidate")
    print("           → This candidate is guaranteed to be global majority")
    print("           → Return it immediately")
    print()
    print("   Case B: Halves have DIFFERENT candidates (or one has none)")
    print("           → Test both candidates against full subset")
    print("           → Return whichever (if any) is majority")
    print()
    print("   Case C: Neither half has a candidate")
    print("           → No global majority possible")
    print()
    print("Key Insight:")
    print("-" * 80)
    print("If an account appears more than n/2 times overall, it MUST appear")
    print("more than n/4 times in at least ONE half (pigeonhole principle).")
    print()
    print("This means the true majority (if it exists) will be found as a")
    print("candidate in at least one recursive call.")
    print()
    print("Time Complexity:")
    print("-" * 80)
    print("T(n) = 2T(n/2) + O(n)")
    print()
    print("Where:")
    print("- 2T(n/2): Two recursive calls on halves")
    print("- O(n): Counting/verifying candidates in the combine step")
    print()
    print("Solution: T(n) = O(n log n)")
    print()
    print("This achieves the required O(n log n) comparisons!")
    print("=" * 80)
    print()


if __name__ == "__main__":
    explain_algorithm()
    test_fraud_detection()
    
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print()
    print("✓ Algorithm detects fraud in O(n log n) comparisons")
    print("✓ Uses divide-and-conquer with candidate verification")
    print("✓ Correctly identifies when more than n/2 cards share an account")
    print("✓ Handles edge cases (no majority, exact threshold, all same)")
    print()
    print("Real-world application: Detecting fraudulent card duplication")
    print("=" * 80)