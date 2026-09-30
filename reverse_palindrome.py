# =============================================================================
# ԽՆԴԻՐ 2: Թվի Շրջում և Պալինդրոմ (Reverse Number & Palindrome)
# Կարգավիճակ: ԼՈՒԾՎԱԾ Է ✅ (Լիովին ինքնուրույն)
# Ճշգրտություն: 100%
# Բարդություն: Միջին (Medium)
# =============================================================================

number = 12321
reversed_number = 0
new_number = number

while new_number > 0:
    mod = new_number % 10
    new_number = new_number // 10
    reversed_number = reversed_number * 10 + mod

if reversed_number == number:
    print(f"Սկզբնական: {number} | Շրջված: {reversed_number} (Պալինդրոմ է ✅)")
else:
    print(f"Սկզբնական: {number} | Շրջված: {reversed_number} (Պալինդրոմ չէ ❌)")
