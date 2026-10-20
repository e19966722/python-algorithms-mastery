# =============================================================================
# ԹԵՄԱ: PYTHONIC COMPREHENSIONS, ZIP(), ENUMERATE()
# =============================================================================

# Սկզբնական տվյալներ
products = ["Laptop", "Mouse", "Broken_Screen", "Keyboard", "Old_Cable"]
prices = [1200, 25, -50, -100, 0]
valid={prod: price for prod, price in zip(products,prices) if price > 0}

print(valid)



