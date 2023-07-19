# Given a sorted array and a target value, return the index if the target is found. If not,
# return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:
# Input: [1,3,5,6], 5
# Output: 2

# Example 2:
# Input: [1,3,5,6] 7
# Output: 4

class Solution:
    def searchInsert(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

# Example usage:
nums = [1, 3, 5, 6]
target = 5
solution = Solution()
result = solution.searchInsert(nums, target)
print(result)
