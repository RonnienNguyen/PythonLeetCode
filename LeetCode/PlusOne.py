# Given a non-empty array of digits representing a non-negative integer, plus one
# to the integer.
# The digits are stored such that the most significant digit is at the head of the
# list, and each element in the array contain a single digit.
# You may assume the integer does not contain any leading zero, except the number
# 0 itself.
# Example 1:
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# METHOD 1
# def plusOne(input):
#     length = len(input)
#     input[length-1] += 1
#     return input

# arrayInput = [1, 3, 5]
# print(plusOne(arrayInput))


#METHOD 2
# def plusOne(input):
#     length = len(input)
#     if not input:
#         return [1]
#     if input[length-1] != 9:
#         input[length-1] += 1
#         return input
#     else:
#         carry = 1
#         for i in range(length - 1, -1, -1):
#             carry += input[i]
#             input[i] = carry % 10
#             carry //= 10
#         if carry > 0:
#             input.insert(0, carry)
#         return input

#METHOD 3
# class Solution:
#     def plusOne(self, digits):
#         if not digits:
#             return [1]
        
#         carry = 1
#         n = len(digits)
#         for i in range(n - 1, -1, -1):
#             carry += digits[i]
#             digits[i] = carry % 10
#             carry //= 10
        
#         if carry > 0:
#             digits.insert(0, carry)
        
#         return digits

# METHOD 4

def plusOne(input):
    if not input:
        return [1]

    length = len(input)
    if input[length-1] != 9:
        input[length-1] + 1
        return input
    else:
        carry = 1
        for i in range(length -1, -1, -1):
            carry += input[i]
            input[i] = carry % 10
            carry //= 10
        if carry > 0:
            input.insert(0, carry)
        return input



# Example usage:
nums = [9, 9, 9, 9, 9, 9]
# solution = Solution()
result = plusOne(nums)
print(result)  # Output: [1, 0, 0, 0]


