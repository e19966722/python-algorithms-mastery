import sys
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# =============================================================================
# ԽՆԴԻՐ 1: Ավտոմորֆիկ թվեր (ԼՈՒԾՎԱԾ Է ✅)
# =============================================================================
for i in range(1, 10001):
    k = 10
    while k <= i:
        k *= 10
    if (i ** 2) % k == i:
        print("Ավտոմորֆիկ թիվ:", i)


# =============================================================================
# ԽՆԴԻՐ 2 (Ամրապնդող): Թվի Մաթեմատիկական Շրջում (Reverse Number / Palindrome)
# =============================================================================
# ՊԱՀԱՆՋԸ:
# Տրված է կամայական դրական ամբողջ թիվ `number`:
# Շրջի՛ր այդ թիվը (աջից ձախ) և ստացի՛ր նոր շրջված թիվը `reversed_number`
# ՄԻՄԻԱՅՆ ՄԱԹԵՄԱՏԻԿՈՐԵՆ (օգտագործելով % 10 և // 10, առանց str() օգտագործելու):
#
# Օրինակներ:
#   number = 1234  -> reversed_number = 4321
#   number = 705   -> reversed_number = 507
#   number = 12321 -> reversed_number = 12321 (Պալինդրոմ է)
#
# ՈՒՇԱԴՐՈՒԹՅՈՒՆ:
# Չօգտագործե՛լ str(number): Աշխատի՛ր մաքուր `while` ցիկլով:
# =============================================================================

number = 12345
reversed_number = 0
new_number=number
while new_number>0:
    mod=new_number%10
    new_number=new_number//10
    reversed_number=reversed_number*10+mod

if reversed_number==number:
    print(f"Սկզբնական: {number} | Շրջված: {reversed_number} (Պալինդրոմ է)")
else:
    print(f"Սկզբնական: {number} | Շրջված: {reversed_number} ")
