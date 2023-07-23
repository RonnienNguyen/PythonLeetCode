# Input:
# matrix = [
# [1, 3, 5, 7],
# [10, 11, 16, 20],
# [23, 30, 34, 50]
# ]
# target = 3

#METHOD 1

# def search2DMatrix(input, value):
#     nums_rows = len(input)
#     nums_cols = len(input[0])
    
#     for i in range(nums_rows):
#         for j in range(nums_cols):
#             if (input[i][j] == value):
#                 return True
#     return False


#METHOD 2
def search2DMatrix(input, value):
    nums_rows = len(input)
    nums_cols = len(input[0])
    
    total = nums_rows * nums_cols
    
    for i in range(total):
        row = i // nums_cols
        col = i % nums_rows
        if (input[row][col] == value):
            return True
    return False



matrix = [
[1, 3, 5, 7],
[10, 11, 16, 20],
[23, 30, 34, 50]
]

target = 3
print(search2DMatrix(matrix, target))
