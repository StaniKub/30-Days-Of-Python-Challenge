# Day 1 of 30 Days of Python Challenge

print(2+3)
print(3-2)
print(2*2)
print(3/2)
print(2**2)
print(3 % 2)
print(3//2)

# Checking Data Types

print(type(10))  # integer
print(type(3.14))  # float
print(type(3 + 2j))  # complex number
print(type('Stanislav'))  # string
print(type([1, 2, 3, 4]))  # list
print(type({'hello': 'world', 'type': 'negative'}))  # dictionary
print(type({1, 2, 3, 4}))  # set
print(type((1, 2, 3, 4)))  # tuple

# Calculate Euclidian Distance between 2 numbers


def euclidian_distance(num1, num2):
    result = num1 - num2
    if result < 0:
        result *= -1
    print(result)


euclidian_distance(2, 3)
euclidian_distance(10, 8)
