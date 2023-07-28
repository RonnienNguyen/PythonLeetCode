# METHOD 1
# def singleNumber(input):
#     length = len(input)
#     sum = 0
#     arrayR = []
#     result = []
#     for i in range(length):
#         for j in range(i+1, length):
#             if (input[i] == input[j]):
#                 arrayR.append(input[i])
    
#     for i in range(length):
#         for j in range(len(arrayR)):
#             if (input[i] == arrayR[j]):
#                 input[i] = None
                
#     result = [num for num in input if num is not None]
#     return result


# METHOD 2
def singleNumber(input):
    result = 0
    for i in range(len(input)):
        result ^= input[i]
    return result

input1 = [2,2,1]
input3 = [2,3,4,5,6,7,2,3,6,7,1,2,3,2,1,1,9,11,14,22,44]
input2 = [4,1,2,1,2]

print(singleNumber(input1))  # Output: 1
print(singleNumber(input3))  # Output: 4
print(singleNumber(input2))  # Output: 4
