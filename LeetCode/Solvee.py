# Reverse String 

# METHOD 1
# def solve(input):
#     result = ""
#     for i in input:
#         result = i + result
#     return result


# METHOD 2
def solve(input):
    input = input[::-1]
    return input

result = solve("ABC")

print(result)