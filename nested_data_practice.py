# =============================================================================
# ԹԵՄԱ: ՆԵՐԴՐՎԱԾ ՏՎՅԱԼՆԵՐԻ ՄՇԱԿՈՒՄ (NESTED DICTS & LISTS / JSON-STYLE DATA)
# =============================================================================

# Տվյալներ՝ Պատվերների ցուցակ (List of Dictionaries)
orders = [
    {
        "order_id": 101,
        "user": "Aram",
        "items": [
            {"name": "Laptop", "price": 1200, "qty": 1},
            {"name": "Mouse", "price": 25, "qty": 2}
        ]
    },
    {
        "order_id": 102,
        "user": "Ani",
        "items": [
            {"name": "Phone", "price": 800, "qty": 1},
            {"name": "Headphones", "price": 150, "qty": 1},
            {"name": "Case", "price": 20, "qty": 3}
        ]
    },
    {
        "order_id": 103,
        "user": "Aram",
        "items": [
            {"name": "Keyboard", "price": 100, "qty": 1}
        ]
    }
]
user_spending={}
for l in orders:
    print("Պատվեր:", l["order_id"], l["user"])
    total=0
  
    # l["items"]-ը ցուցակ է, որի մեջ ամեն տարր մի ապրանք է (item)
    for item in l["items"]:
        
        total += item["price"] * item["qty"]
    if l["user"] in user_spending:
        user_spending[l["user"]]+=total
    else:
        user_spending[l["user"]]=total
        # item-ն արդեն բառարան է!
        # item-ը սա է՝ {"name": "Laptop", "price": 1200, "qty": 1}
user=None
max_total=0
for key,value in user_spending.items():
    if value>max_total:
        max_total=value
        user=key
print(f"Top Spender: {user} with {max_total}$")
# ՔԱՅԼ 1: Հաշվե յուրաքանչյուր us ընդհանուր արժեքը (order total):
# 
# Օրինակ՝
# Order 101 (Aram): 1200 * 1 + 25 * 2 = 1250$
# Order 102 (Ani): 800 * 1 + 150 * 1 + 20 * 3 = 1010$
# Order 103 (Aram): 100 * 1 = 100$



