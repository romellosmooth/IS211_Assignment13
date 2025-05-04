def compareTo(s1, s2):
    if not s1 and not s2:
        return 0
    elif not s1:
        return -1
    elif not s2:
        return 1  # s2 is empty, so s1 is "greater"

    if s1[0] != s2[0]:  # Compare first character
        return ord(s1[0]) - ord(s2[0])

    return compareTo(s1[1:], s2[1:])



print(compareTo("apple", "banana"))  # Should return a negative number
print(compareTo("grape", "grape"))  # Should return 0
print(compareTo("zebra", "ant"))  # Should return a positive number
