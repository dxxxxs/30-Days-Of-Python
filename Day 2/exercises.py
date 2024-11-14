import math

# Level 1

# Day 2: 30 Days of python programming

firstname = "oscar"
lastname = "gonzalez"
fullname = "oscar gonzalez"
country = "spain"
city = "valladolid"
age = 24
year = 2024
is_married = False
is_true = True
is_light_on = True
first, second, thrid = 1,2,3

# Level 2

# 1
print(type(firstname))
print(type(lastname))
print(type(fullname))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(first))
print(type(second))
print(type(thrid))

# 2
firstnameLength = len(firstname)
print(firstnameLength)

# 3
lastnameLength = len(lastname)
if(firstnameLength > lastnameLength):
    print(firstname, "is longer than", lastname)
elif(firstnameLength < lastnameLength):
    print(firstname, "is shorter than", lastname)
else:
    print(firstname, "is the same length as", lastname)

# 4
num_one = 5
num_two = 4

# 5
total = num_one + num_two

# 6
diff = num_one - num_two

# 7
product = num_two * num_one

# 8
division = num_one / num_two

# 9
remainder = num_two % num_one

# 10
exp = num_one ** num_two

# 11
floor_division = num_one // num_two

# 12
radius = 30
    # i
area_of_circle = math.pi*(radius**2)
print("Area of the circle  which radius is",radius,":",area_of_circle)
    # ii
circum_of_circle = 2*math.pi*radius
print("Circumference of the circle  which radius is",radius,":",circum_of_circle)
    # iii
radius = int(input("Set circle radius:"))
area_of_circle = math.pi*(radius**2)
print("Area of the circle  which radius is",radius,":",area_of_circle)

# 13
firstname = input("Set firstname (string):")
lastname = input("Set lastname (string):")
country = input("Set country (string):")
age = int(input("Set age (number):"))

print(firstname,lastname,country,age)