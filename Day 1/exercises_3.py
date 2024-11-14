import math
# Question 1

# Number
print(2)
# Float
print(7.43)
# Complex
print(2 + 4j)
# String
print("String")
# Boolean
print(True)
# List
print([1, "string", True])
# Tuple
print(('Earth', 'Jupiter', 'Mercury'))
# Set
print({3.14, 9.81, 2.7})
# Dictionary
print({
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'skills': ['JS', 'React', 'Node', 'Python']
})

# Question 2

# d(p,q) = (q1-p1)^2+(q2-p2)^2
# P = (2,3), Q = (10,8)
print("Euclidian distance between (2,3) and (10,8) is",
      math.sqrt((10-2)**2+(8-3)**2))
