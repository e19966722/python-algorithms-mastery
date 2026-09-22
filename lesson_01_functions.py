from typing import List, Optional


def two_sum(numbers: List[int], target: int) -> Optional[List[int]]:
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]


def max_profit(prices: List[int]) -> int:
    min_price = prices[0]
    best_profit = 0
    for price in prices:
        if min_price > price:
            min_price = price
        elif best_profit < price - min_price:
            best_profit = price - min_price

    return best_profit


def is_valid_parentheses(s: str) -> bool:
    memory = []
    for char in s:
        if char in ('[', '(', '{'):
            memory.append(char)
        elif char in (']', ')', '}'):
            if not memory:
                return False
            
            top = memory.pop()
            if char == ']' and top != '[':
                return False
            elif char == ')' and top != '(':
                return False
            elif char == '}' and top != '{':
                return False

    return memory == []


# =============================================================================
# Կանչերի արդյունքները
# =============================================================================
if __name__ == "__main__":
    print("1. Two Sum:", two_sum([2, 7, 11, 15], 9))
    print("2. Max Profit:", max_profit([7, 1, 5, 3, 6, 4]))
    print("3. Valid Parentheses:", is_valid_parentheses("{[()]}"))