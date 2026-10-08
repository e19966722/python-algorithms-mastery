# =============================================================================
# ԽՆԴԻՐ 19: Group Anagrams (Խմբավորել Անագրամները) - LeetCode #49
# =============================================================================
#
# ՊԱՅՄԱՆԸ:
# Տրված է բառերի ցուցակ strs:
# Խմբավորիր այն բոլոր բառերը, որոնք կազմված են ճիշտ նույն տառերից (անագրամներ են):
#
# ՕՐԻՆԱԿ 1:
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Ելք: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
#
# ՕՐԻՆԱԿ 2:
# strs = [""]
# Ելք: [[""]]
#
# ՕՐԻՆԱԿ 3:
# strs = ["a"]
# Ելք: [["a"]]
# =============================================================================

def group_anagrams(strs):
    d={}

    for word in strs:
        key="".join(sorted(word))
        if key not in d:
            d[key]=[word]
        else:
            d[key].append(word)
    return list(d.values())


# --- ՍՏՈՒԳՈՒՄ ---
test1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("Թեստ 1:", group_anagrams(test1))

test2 = [""]
print("Թեստ 2:", group_anagrams(test2))

test3 = ["a"]
print("Թեստ 3:", group_anagrams(test3))
