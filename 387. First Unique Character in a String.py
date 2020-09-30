from collections import Counter

def firstUniqChar( s):
    char_occ_dict = Counter(s)

    for index, it in enumerate(s):
        if char_occ_dict[it] == 1:
            return index

    # for index, it in enumerate(s):
    #     if s.count(it) == 1:
    #         return index

    return -1



result = firstUniqChar("loveleetcode")
print(result)