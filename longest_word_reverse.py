# =============================================================================
# ԽՆԴԻՐ 15: Տողի Ամենաերկար Բառի Շրջում (Reverse Longest Word in String)
# (DIGI.code Օլիմպիադա, Ավագ խումբ)
# =============================================================================
#
# ՊԱՀԱՆՋԸ:
# Տրված է տեքստ: Գտի՛ր այդ տեքստի ԱՄԵՆԱԵՐԿԱՐ բառը և տողի մեջ շրջի՛ր ՄԻԱՅՆ ԱՅԴ ԲԱՌԸ,
# իսկ մնացած բոլոր բառերը թո՛ղ ԱՆՓՈՓՈԽ (իրենց տեղերում):
#
# ՕՐԻՆԱԿ (DIGI.code տոմսից):
# Մուտք:  "Armath: The Algorithm of the Future"
#
# Քայլերի վերլուծություն:
#   - Բառերն են՝ "Armath:", "The", "Algorithm", "of", "the", "Future"
#   - Ամենաերկար բառը "Algorithm"-ն է (9 տառ):
#   - Շրջում ենք միայն "Algorithm"-ը -> "mhtiroglA":
#
# Ելք:    "Armath: The mhtiroglA of the Future"
# =============================================================================

text = "Armath: The Algorithm of the Future"
new_text=text.split(" ")
ml=0
mindex=0
for i,char in enumerate(new_text):
    if ml<len(char):
        ml=len(char)
        mindex=i
        print(ml,mindex,char)
new_text[mindex]=new_text[mindex][::-1]
new_text=" ".join(new_text)


print(new_text)
