# 1. Create an empty dictionary called dog
dog = {}
# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Golden Retriever'
dog['legs'] = 4
dog['age'] = 3
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {}
student['first_name'] = 'John'
student['last_name'] = 'Doe'
student['gender'] = 'Male'
student['age'] = 20
student['marital_status'] = 'Single'
student['skills'] = ['Python', 'Java', 'C++']
student['country'] = 'USA'
student['city'] = 'New York'
student['address'] = '123 Main St'
print(student)

# 4. Get the length of the student dictionary
n = len(student)
print(n)

# 5. Get the value of skills and check the data type, it should be a list
print(type(student.get('skills')))

# 6. Modify the skills values by adding one or two skills
student.get('skills').append('JavaScript')
print(student.get('skills'))

# 7. Get the dictionary keys as a list
keys = student.keys()
print(keys)

# 8. Get the dictionary values as a list
values = student.values()
print(values)

# 9. Change the dictionary to a list of tuples using items() method
lst = student.items()
print(lst)

# 10. Delete one of the items in the dictionary
student.pop('gender')
student.popitem()
del student['age']

# 11. Delete one of the dictionaries
del student
