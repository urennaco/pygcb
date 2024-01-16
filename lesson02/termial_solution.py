def termial(n):
    # your code here
    result = n
    for i in range(n):
        result += i
    return result

values = [1, 2, 5, 10, 20]
for value in values:
    print('The termial of %s is %s.' % (value, termial(value)))
