# # Level 1

# # 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# age = int(input("Enter your age:"))
# if age >= 18:
#     print("You are old enough to drive.")
# else:
#     print("You need to wait for", 18 - age, "years to drive.")

# # 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# my_age = 24
# your_age = int(input("Enter your age: "))
# if my_age > your_age:
#     if my_age-your_age == 1:
#         print(f'I am a year older than you.')
#     else:
#         print(f'I am {my_age-your_age} years older than you.')
# elif my_age < your_age:
#     if your_age-my_age == 1:
#         print(f'You are a year older than me.')
#     else:
#         print(f'You are {your_age-my_age} years older than me.')
# else:
#     print('We are the same age.')

# # 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# a = int(input("Enter number one:"))
# b = int(input("Enter number two:"))
# if a > b:
#     print(f'{a} is greater than {b}.')
# elif a < b:
#     print(f'{a} is smaller than {b}.')
# else:
#     print(f'{a} is equal to {b}.')


# # Level 2
# # 1. Write a code which gives grade to students according to theirs scores:
# score = 60
# if score >= 80:
#     print("A")
# elif score >= 70:
#     print("B")
# elif score >= 60:
#     print("C")
# elif score >= 50:
#     print("D")
# else:
#     print("F")

# # 2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
# season = input("Enter the month:")
# if season in ["September", "October", "November"]:
#     print("Autumn")
# elif season in ["December", "January", "February"]:
#     print("Winter")
# elif season in ["March", "April", "May"]:
#     print("Spring")
# elif season in ["June", "July", "August"]:
#     print("Summer")

# # 3. The following list contains some fruits, if a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruit = input("Enter a fruit")
# if fruit in fruits:
#     print('That fruit already exist in the list')
# else:
#     fruits.append(fruit)

# Level 3

# 1. Here we have a person dictionary. Feel free to modify it!

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if "skills" in person.keys():
    middle = len(person['skills'])//2
    print(person['skills'][middle])

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if "skills" in person.keys() and 'Python' in person['skills']:
    print("The person has ", person['skills']
          [person['skills'].index('Python')], " skill")

#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if ['JavaScript', 'React'] == person['skills']:
    print('He is a front end developer')
elif ['Node', 'Python', 'MongoDB'] == person['skills']:
    print('He is a backend developer')
elif ['React', 'Node', 'MongoDB'] == person['skills']:
    print('He is a fullstack developer')
else:
    print('unknown title')
#  * If the person is married and if he lives in Finland, print the information in the following format:
if person['country'] and person['is_marred']:
    print(f"{person['first_name']} {person['last_name']} lives in {
          person['country']}. He is married.")
