# Given n non-negative integers a1, a2, ..., an , where each represents a point at
# coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
# line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
# forms a container, such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this
# case, the max area of water (blue section) the container can contain is 49.
# Example:
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49


def maxArea(height):
    left = 0
    right = len(height) - 1
    result = 0
    
    while left < right:
        min_between = min(height[left], height[right])
        h = right - left
        area = min_between * h
        result = max(result, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return result
# Example usage:
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = maxArea(height)
print(result)
