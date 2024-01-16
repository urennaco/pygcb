numbers1 = [10, 20, 17, 12, 13, 6, 7, 18, 9, 15]
numbers2 = [15, 9, 17, 6, 16, 8, 19, 11, 19, 16]

overlapping = []

# your code here
for number in numbers1:
    if number in numbers2:
        overlapping.append(number)


print('The overlapping numbers are: ')
print(overlapping)
