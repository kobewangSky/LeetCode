import collections


def fourSumCount( A, B, C, D):
    # AB = collections.Counter(a + b for a in A for b in B)
    # return sum(AB[-c - d] for c in C for d in D)

    temp = [-a - b for a in A for b in B]
    AB = collections.Counter(temp)
    temp = [c + d for c in C for d in D]
    result = sum(AB[i] for i in temp)
    return result




A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

result = fourSumCount(A, B, C, D)
print(result)