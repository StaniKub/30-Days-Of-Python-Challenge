# Day 2: 30 Days of Python programming

first_name = 'Stanislav'
last_name = 'K'
full_name = first_name + ' ' + last_name
country = 'Slovakia'
city = 'Bratislava'
age = 29
year = 2023
is_maried = True
is_true = False
is_light_on = True
multiple, variables, declaration = 'string', 42, [5, 6, 7, 8]


print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_maried))
print(type(is_true))
print(type(is_light_on))
print(type(multiple))
print(type(variables))
print(type(declaration))

first_name_length = len(first_name)
last_name_length = len(last_name)


def is_bigger(one, another):
    if one > another:
        return 'first is bigger: ' + str(one)
    return 'second is bigger: ' + str(another)


print(is_bigger(first_name_length, last_name_length))

num_one, num_two = 5, 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# Circle
r = 30
area_of_circle = 3.14159 * (r ** 2)
print(area_of_circle)
circumference_of_circle = 2 * 3.14159 * r
print(circumference_of_circle)

radius = input('Set a radius of a circle: ')
area = 3.14159 * (int(radius) ** 2)
print(f'area of a circle with radius {radius}m is {area}m')

# Inputs

first_n = input('Enter your first name: ')
last_n = input('Enter your last name: ')
countr_y = input('Where are you from? ')
ag_e = input('What is your age? ')

print(
    f'Hi there! You are {first_n} {last_n}. You live in {country}. And you are {age} years old.')
