import numpy


def longestSubstring(s, k):
    unique_s = set(s)
    for it in unique_s:
        number = s.count(it)
        if number < k:
            return max(longestSubstring(t, k) for t in s.split(it))
    return len(s)



temp = longestSubstring("ababbc", 2)
print(temp)