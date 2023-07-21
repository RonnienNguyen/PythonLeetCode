# Write a function to find the longest common prefix string amongst an array of
# strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
# All given inputs are in lowercase letters a-z.

def longestCommonPrefix(input):
    if not input:
        return ""
    
    result = input[0]
    for string in input[1:]:
        while not string.startswith(result):
            result = result[:-1]
    return result
    
array = ["flower","flow","flight"]
array2 = ["dog","racecar","car"]
print(longestCommonPrefix(array2))