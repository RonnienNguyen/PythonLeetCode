n = int(input("Input Number Please: "))
check = False

array = []
def function_compare(num1, num2, num3, num4):
    if (num1 > num2) and (num3 < num4):
        check = True
        array.append(check)
    if (num3 % 10 == 0) and (num4 % 20 != 0):
        array.append(num4)
    return array


def square(num):
    return num * num
def sum(num):
    return num + num
def minus(num1, num2):
    return num1 - num2
def div(num1, num2):
    return num1/num2


num2 = 10
num3 = 20
num4 = 30
print(square(n))
print(sum(n))
print(minus(n, num2))
print(div(n, num2))

print(function_compare(n, num2, num3, num4))