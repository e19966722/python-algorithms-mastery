# =============================================================================
# ԹԵՄԱ: ԱՌԱՋԻՆ ՉԿՐԿՆՎՈՂ ՍԻՄՎՈԼԸ (FIRST UNIQUE CHARACTER — LEETCODE #387)
# =============================================================================
#
# ԽՆԴՐԻ ՊԱՀԱՆՋԸ.
# Տրված է տեքստ (string): Գտնել և վերադարձնել ԱՌԱՋԻՆ տառը, որը հանդիպում է
# ընդամենը ՄԵԿ անգամ (չի կրկնվում):
# Եթե այդպիսի տառ չկա, վերադարձնել None (կամ "-1"):
#
# ՕՐԻՆԱԿՆԵՐ.
# 1. "leetcode"     -> 'l'
# 2. "loveleetcode" -> 'v'
# 3. "aabbcc"       -> None==

def first_unique_char2(s):
    # Գրիր քո կոդը այստեղ
    l=[]
    for i in s:
        l.append(i)
    for i in l:
        if l.count(i)==1:
            return i
    return 0

def first_unique_char(s):
    # Գրիր քո կոդը այստեղ
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in s:
        if d[i]==1:
            return i
    return 0




# Թեստեր
print("leetcode ->", first_unique_char("leetcode"))         # Պետք է տպի 'l'
print("loveleetcode ->", first_unique_char("loveleetcode")) # Պետք է տպի 'v'
print("aabbcc ->", first_unique_char("aabbcc"))             # Պետք է տպի None

