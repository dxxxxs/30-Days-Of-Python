# import math
# # 1
# age = 24

# # 2
# height = 1.82

# # 3
# complex = 2 + 4j

# # 4
# triangle = {
#     'base': float(input("Enter base:")),
#     'height': float(input("Enter height:")),
#     'area': 0
# }

# triangle['area'] = 0.5 * triangfor number in range(le['base'] * triangle['height']

# print("The area of the triangle is:", triangle['area'])

# # 5
# triangle = {
#     'a': float(input("Enter side a:")),
#     'b': float(input("Enter side b:")),
#     'c': float(input("Enter side c:")),
#     'perimeter': 0
# }

# triangle['perimeter'] = triangle['a'] + triangle['b'] + triangle['c']

# print("The perimeter of the triangle is:", triangle['perimeter'])

# # 6
# rectangle = {
#     'length': float(input("Enter length:")),
#     'width': float(input("Enter width:")),
#     'perimeter': 0
# }

# rectangle['perimeter'] = 2*(rectangle['length']+rectangle['width'])

# print("The perimeter of the rectangle is:", rectangle['perimeter'])

# # 7
# PI = 3.14
# circle = {
#     'radius': float(input("Enter radius:")),
#     'area': 0,
#     'circumference': 0
# }

# circle['area'] = PI * (circle['radius'] ** 2)
# circle['circumference'] = 2 * PI * circle['radius']

# print("The area of the circle is:",
#       circle['area'], "and the circumference is:", circle['circumference'])

# # 8
# # y = 2x -2
# exercise_8 = {
#     'slope': 2,
#     'x_intercept': 1,
#     'y_intercept': -2
# }

# print("Slope:", exercise_8['slope'])
# print("X-intercept:", exercise_8['x_intercept'])
# print("Y-intercept:", exercise_8['y_intercept'])

# # 9
# X = (2, 2)
# Y = (6, 10)

# exercise_9 = {
#     'slope': 0,
#     'euclidian_distance': 0
# }
# exercise_9['slope'] = (Y[1]-Y[0]/X[1]-X[0])
# exercise_9['euclidian_distance'] = math.sqrt(
#     (X[0]-Y[0]) ** 2 + (X[1]-Y[1]) ** 2)


# print("The slope between", X, "and", Y, "is", exercise_9['slope'],
#       "and the euclidian distance is", exercise_9['euclidian_distance'])

# # 10
# if (exercise_8['slope'] > exercise_9['slope']):
#     print("The slope in exercise 8 is greater than sloper in exercise 9")
# elif (exercise_8['slope'] < exercise_9['slope']):
#     print("The slope in exercise 8 is smaller than sloper in exercise 9")
# else:
#     print("The slope in exercise 8 is equal to sloper in exercise 9")

# # 11
# X = -3
# Y = X**2 + 6*X + 9
# print(Y)

# # 12
# length_python = len("python")
# length_dragon = len("dragon")

# comparison = length_dragon != length_python
# print(comparison)

# # 13
# python = "python"
# dragon = "dragon"
# on = "on"

# if (on in python and on in dragon):
#     print(on, "is in", python, "and", dragon)
# else:
#     print(on, "is not in", python, "and", dragon)

# # 14
# sentence = "I hope this course is not full of jargon"
# jargon = "jargon"

# if (jargon in sentence):
#     print(jargon, "is in sentence:", sentence)
# else:
#     print(jargon, "is not in sentence:", sentence)

# # 15
# if (on in python and on in dragon):
#     print(on, "is in", python, "and", dragon)
# else:
#     print(on, "is not in", python, "and", dragon)

# # 16
# float_length_python = float(length_python)
# string_float_length_python = str(float_length_python)
# print(string_float_length_python)

# # 17
# num = int(input("Enter a number to check if is even or odd:"))

# if (num % 2 == 0):
#     print(num, "is even")
# else:
#     print(num, "is odd")

# # 18
# a = 7
# b = 3
# c = 2.7
# floor_division = a//b
# casted_float = int(c)
# print(floor_division == casted_float)

# # 19
# print(type('10') == type(10))

# # 20
# print(int('9.8' == 10))

# # 21
# hours = int(input("Enter hours:"))
# rate_per_hour = int(input("Enter rate per hour:"))
# weekly_earning = hours * rate_per_hour
# print("Your weekly earning is", weekly_earning)

# # 22
# years = int(input("Enter number of years you have lived:"))
# seconds_lived = years * 365 * 24 * 60 * 60
# print("You have lived for", seconds_lived, "seconds")

# 23
for number in range(1, 6):
    print(f'{number} {number**0} {number**1} {number**2} {number**3}')
