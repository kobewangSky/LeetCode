import numpy
from collections import Counter

def intersect(nums1, nums2):
    c1 = Counter(nums1)
    c2 = Counter(nums2)
    return list((c1 & c2).elements())

result = intersect([1,2,2,1], [2, 2])