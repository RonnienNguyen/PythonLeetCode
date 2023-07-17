# Given an array of integers, return indices of the two numbers such that they add
# up to a specific target.
# You may assume that each input would have exactly one solution, and you may not
# use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# FIRST METHOD
# def twoSum(nums, target):
#     m = {}
#     for i in range(len(nums)):
#         if target - nums[i] not in m:
#             m[nums[i]] = i
#         else:
#             return [m[target - nums[i]], i]
#     return [-1, -1]

# SECOND METHOD
# def twoSum(nums, target):
#     m = {}
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if (nums[i] + nums[j]) == target:
#                 return [i,j]
#     return [-1, -1]

# print(twoSum([2,7,11,15], 9))

#THIRD METHOD

def twoSum(nums, target):
    m = {}
    for i in range(len(nums)):
        for j in range(len(nums) - 1, i, -1):
            if (nums[i] + nums[j]) == target:
                return [i,j]
    return [-1, -1]

print(twoSum([2,0,9,7,15], 9))


    
# print(twoSum([2,7,11,15], 9))