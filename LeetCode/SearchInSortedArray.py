def searchInSortedArray(input, value):
    length = len(input)
    
    for i in range(length):
        if (input[i] == value):
            return i
    return -1

array = [4,5,6,7,0,1,2]
target = 2
print(searchInSortedArray(array, target))
