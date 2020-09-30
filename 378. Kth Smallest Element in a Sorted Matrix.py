def kthSmallest( matrix, k):

    result = [ item for i in matrix for item in i]
    result = sorted(result)
    return result[k-1]

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
result = kthSmallest(matrix, 8)
print(result)