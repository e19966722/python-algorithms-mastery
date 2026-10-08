import sys

# Ստուգենք, թե ինչպես է list-ը մեծանում RAM-ում
lst = []
print(f"Դատարկ list-ի չափը: {sys.getsizeof(lst)} բայթ")

current_size = sys.getsizeof(lst)

for i in range(50):
    lst.append(i)
    new_size = sys.getsizeof(lst)
    if new_size != current_size:
        print(f"Տարրերի քանակը՝ {len(lst):2d} | Զբաղեցրած չափը RAM-ում՝ {new_size} բայթ (+{new_size - current_size} բայթ նոր բուֆեր)")
        current_size = new_size
