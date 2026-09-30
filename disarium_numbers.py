# =============================================================================
# ԽՆԴԻՐ 4: Դիզարիում թվեր (Disarium Numbers)
# Ամսաթիվ: 30/09/2026 (Session 2)
# Բարդություն: Միջին (Medium)
# 
# ՊԱՀԱՆՋԸ:
# Գտնել և տպել [1, 1000] միջակայքում գտնվող բոլոր Disarium թվերը:
# Թիվը կոչվում է Disarium, եթե նրա թվանշանների գումարը՝ բարձրացված
# իրենց դիրքի աստիճանին (ձախից աջ՝ 1-ից սկսած), հավասար է հենց այդ թվին:
#
# Օրինակներ:
#   89  -> 8^1 + 9^2 = 8 + 81 = 89 (Disarium է)
#   135 -> 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135 (Disarium է)
#   518 -> 5^1 + 1^2 + 8^3 = 5 + 1 + 512 = 518 (Disarium է)

for number in range(1,1001):
    sum_number=0
    new_number=number
    l=0
    while new_number>0:
        new_number=new_number//10
        l=l+1
    new_number=number
    
    while l>0:
        angle=(new_number%10)**l
        new_number=new_number//10
        sum_number=sum_number+angle
        l=l-1

    if sum_number==number:
        print("Disarium է",sum_number)
