# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should
# be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# The median is (2 + 3)/2 = 2.5


# FIRST METHOD
# def medianTwoSortedArray(arr1, arr2):
#     arr3 = []
#     for i in range(len(arr1)):
#         arr3.append(arr1[i])
#     for i in range(len(arr2)):
#         arr3.append(arr2[i])
        
#     print(arr3)
#     length = len(arr3)
#     arr3.sort()
#     if length % 2 == 0:
#         middle = (length - 1) // 2 + 1
#         next_middle = middle + 1
#         result = (arr3[middle-1] + arr3[next_middle-1]) / 2
#         return result
        
#     else:
#         middle = length // 2
#         result = arr3[middle]
#         return result
#     # return length

array1 = [-5, 3, 6, 12, 15 ]
array2 = [-12, -10, -6, -3, 4, 10]
print(medianTwoSortedArray(array1, array2))