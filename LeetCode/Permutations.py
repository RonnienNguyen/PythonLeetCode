# Given a collection of distinct integers, return all possible permutations.
# Example:
# Input: [1,2,3]
# Output:
# [
# [1,2,3],
# [1,3,2],
# [2,1,3],
# [2,3,1],
# [3,1,2],
# [3,2,1]
# ]

# METHOD 1
class Solution:
    def permute(self, nums):
        def backtrack(start, end):
            if start == end:
                result.append(nums[:])
                return
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1, end)
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack

        result = []
        backtrack(0, len(nums))
        return result

# # Example usage:
# nums = [1, 2, 3]
# solution = Solution()
# result = solution.permute(nums)
# print(result)


# METHOD 2

# class Solution:
#     def permute(self, nums):
#         def backtrack(chosen, permutation):
#             if len(permutation) == len(nums):
#                 result.append(permutation[:])
#                 return
            
#             for i in range(len(nums)):
#                 if not chosen[i]:
#                     chosen[i] = True
#                     permutation.append(nums[i])
#                     backtrack(chosen, permutation)
#                     chosen[i] = False
#                     permutation.pop()

#         result = []
#         chosen = [False] * len(nums)
#         backtrack(chosen, [])
#         return result


# METHOD 3

# Example usage:
nums = [1, 2, 3]
solution = Solution()
result = solution.permute(nums)
print(result)
