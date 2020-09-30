def reverseString( s):
    """
    Do not return anything, modify s in-place instead.
    """
    for i in range(len(s) // 2):
        s[i], s[len(s) - (i+1)] = s[len(s) - (i + 1)], s[i]

x = reverseString(["h","e","l","l","o"])