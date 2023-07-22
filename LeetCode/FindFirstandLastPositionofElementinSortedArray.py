# Given an array of integers nums sorted in ascending order, find the starting and
# ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]


# METHOD 1
# class Solution:
#     def searchRange(self, nums, target):
#         def binary_search_left(nums, target):
#             left, right = 0, len(nums) - 1
#             while left <= right:
#                 mid = left + (right - left) // 2
#                 if nums[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             return left

#         def binary_search_right(nums, target):
#             left, right = 0, len(nums) - 1
#             while left <= right:
#                 mid = left + (right - left) // 2
#                 if nums[mid] <= target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             return right

#         if target not in nums:
#             return [-1, -1]

#         left_index = binary_search_left(nums, target)
#         right_index = binary_search_right(nums, target)

#         if left_index <= right_index:
#             return [left_index, right_index]
#         else:
#             return [-1, -1]

#METHOD 2

# def searchRange(input, value):
#     array = []
#     resultNull = [-1, -1]
#     length = len(input)
#     for i in range(length):
#         if (input[i] == value):
#             array.append(i)
#     resultLength = len(array)
#     if resultLength != 0:
#         return array
#     else:
#         return resultNull

ArrayInit = [5, 7, 7, 8, 8, 10]
target = 5

print(searchRange(ArrayInit, target))
# Example usage:
# nums = [5, 7, 7, 8, 8, 10]
# target = 8

# numss = [5,7,7,8,8,10]
# targett = 6
# solution = Solution()
# result = solution.searchRange(nums, target)
# resultt = solution.searchRange(numss, targett)
# print(result)
# print(resultt)
