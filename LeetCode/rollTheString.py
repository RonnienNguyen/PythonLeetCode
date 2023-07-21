# We define a single roll operation on a string to be the circular increment of each character by one. In other words, each character is rolled forward and overwritten with the next alphabetic character. Looking at the English alphabet, characters in the range ascii[a-z], a becomes b, b becomes c, and z becomes a. Given an array of integers named "roll", we want to perform a roller operation on the first roll[i] characters of s for each element in the array. Given a zero indexed string, an operation roll[i] affects characters at positions 0 through (roll[i]-1). For example, if string s = "abz", and roll = [3, 2, 1], we perform the following sequence of operations:

# roll[0] = 3: Roll all three characters so abz becomes bca.
# roll[1] = 2: Roll the first two characters so bca becomes cda.
# roll[2] = 1: Roll the first character so cda becomes dda.
# After performing all the operations, the final value of s is dda.

# Complete the function rollTheString in the editor below. The function must return the resulting string after all roll operations have been performed.

# Note that it is not sufficient for the answer to be correct. It must also be sufficiently computationally efficient to not timeout.

# def rollTheString(s, roll):
#     n = len(s)
#     result = list(s)

#     for r in roll:
#         for i in range(r):
#             result[i] = chr((ord(result[i]) - ord('a') + 1) % 26 + ord('a'))

#     return ''.join(result)

# # Example usage:
# s = "abz"
# roll = [3, 2, 1]
# result = rollTheString(s, roll)
# print(result)  # Output: "dda"

def increment_char(c):
    # Custom function to increment a lowercase character by one
    if c == 'z':
        return 'a'
    return chr(ord(c) + 1)

def rollTheString(s, roll):
    n = len(s)
    result = list(s)
    roll_sum = 0

    for r in roll:
        roll_sum += r
        idx = r if r < n else n
        for i in range(idx):
            result[i] = increment_char(result[i])

    return "".join(result)

# Example usage:
s = "abz"
roll = [3, 2, 1]
result = rollTheString(s, roll)
print(result)  # Output: "dda"
