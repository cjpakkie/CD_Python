def multiply(a):
    for num in range(len(a)):
        a[num] = a[num] * 5
    return a

b = multiply([2,4,10,16])
print b
