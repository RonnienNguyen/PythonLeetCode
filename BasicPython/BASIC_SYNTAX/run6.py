value = input("Input array: ")

res = value.split(",")

result = tuple(res)
print(result)

# print(result.index('66'))
element = "23"

indices = [index for index, value in enumerate(result) if value == element]
print(indices)

