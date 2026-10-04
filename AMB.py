# =============================================================================
# ԹԵՄԱ: ԱՄԵՆԱՄԵԾ ԸՆԴՀԱՆՈՒՐ ԲԱԺԱՆԱՐԱՐ (ԱՄԵԲ / GCD) + ՌԵԿՈՒՐՍԻԱ
# =============================================================================
# ԻՆՉՊԵ՞Ս Է ԱՇԽԱՏՈՒՄ ԷՎԿԼԻԴԵՍԻ ԱԼԳՈՐԻԹՄԸ.
# 1. Վերցնում ենք երկու թիվ՝ a և b:
# 2. Հաշվում ենք a-ն b-ի բաժանելու մնացորդը (a % b):
# 3. Հաջորդ քայլում a-ի տեղը դնում ենք b-ն, իսկ b-ի տեղը՝ ստացված մնացորդը:
# 4. Կրկնում ենք այնքան, մինչև b-ն դառնա 0:
# 5. Երբ b == 0 է, այդ պահի a-ն հենց մեր փնտրած ԱՄԵՆԱՄԵԾ ԸՆԴՀԱՆՈՒՐ ԲԱԺԱՆԱՐԱՐՆ է:
# =============================================================================

def gcd(a, b):
    if b != 0:
        return gcd(b, a % b)
    else:
        return a

# Փորձարկում
print("amenamec endhanur bajanarar(24, 18) =", gcd(24, 18))
#բանաձև կա բազմապատկում ենք թվերը բաժանում ամենափոքր ընդհանուր բաժանառարի վռա
def lcm(a, b):
    print("amenapoqr endhanur bazmapatik",a*b/gcd(a,b))
lcm(2,7)
#առանց բանաձև
def lcm_logic(a,b):
    m=a
    p=b
    if m<b:
        m=b
        p=a
    lcm=m
    while(lcm%p!=0):
        lcm+=m
    print("amenapoqr endhanur bazmapatik",lcm)
lcm_logic(2,7)
#կրճատում ենք կոտորակները ամենամեծ ընսհանուր բաժանարարի օգնությամբ
def simplify_fraction(numerator, denominator):
    d=gcd(numerator,denominator)
    
    a,b=numerator//d,denominator//d
    return a,b
print(simplify_fraction(24, 36))
print(simplify_fraction(14, 21))
print(simplify_fraction(8, 20))
print(simplify_fraction(7, 13))