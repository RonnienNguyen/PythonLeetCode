# Given an unsorted integer array, find the smallest missing positive integer. 
# Example 1: 
# Input: [1,2,0] Output: 3 
# Example 2: 
 
# Input: [3,4,-1,1] Output: 2 
# Example 3: 
 
# Input: [7,8,9,11,12] Output: 1 Note: 
 
# Your algorithm should run in O(n) time and uses constant extra space. 
def firstMissingPositive(nums):
    seen = set()
    
    for i in nums:
        if i > 0:
            seen.add(i)
    
    i, n = 1, len(nums)
    while i <= n:
        if i not in seen:
            return i
        i += 1
    return i
# Your algorithm should run in O(n) time and uses constant extra space. 
# Example usage:
nums = [3, 4, -1, 1]
numss = [7,8,9,11,12] 
resultt = firstMissingPositive(numss)
result = firstMissingPositive(nums)
print(result)
print(resultt)
