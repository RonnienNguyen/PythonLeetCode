# https://leetcode.com/problems/multiply-strings/

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"

def multiplyString(num1, num2):
    value1 = int(num1)
    value2 = int(num2)
    
    return str(value1 * value2)
print(multiplyString("123", "345"))

