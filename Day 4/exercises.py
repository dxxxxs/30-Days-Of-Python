# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
sentence = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(sentence)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
a = 'Coding'
b = 'For'
c = 'All'
sentence = a + ' ' + b + ' ' + c
print(sentence)

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

# 4. Print the variable company using print().
print(company)

# 5. Print the length of the company string using len() method and print().
print(len(company))

# 6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cut(slice) out the first word of Coding For All string.
print(company[0:1])

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))
print(company.find('Coding'))
print(company.rindex('Coding'))
print(company.rfind('Coding'))


# 11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
print('Python for Everyone'.replace('Everyone', 'All'))

# 13. Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(' '))

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))

# 15. What is the character at index 0 in the string Coding For All.
print(company[0])

# 16. What is the last index of the string Coding For All.
print(company[-1])

# 17. What character is at index 10 in "Coding For All" string.
print(company[10])

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
sentence = 'Python For Everyone'
sentence_array = sentence.split(' ')
acronym = ''

for n in sentence_array:
    acronym += n[0]

print(acronym)

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
company_array = company.split(' ')
acronym = ''

for n in company_array:
    acronym += n[0]

print(acronym)

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
first_index = sentence.find('because')
last_index = sentence.rfind('because')
because_length = len('because')

print(sentence[first_index:last_index+because_length])

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
first_index = sentence.find('because')
last_index = sentence.rfind('because')
because_length = len('because')

# 28. Does ''Coding For All' start with a substring Coding?
print(company.startswith('Coding'))

# 29. Does 'Coding For All' end with a substring coding?
print(company.endswith('coding'))

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
sentence = '   Coding For All      '
print(sentence.strip())

# 31. Which one of the following variables return True when we use the method isidentifier():
#       - 30DaysOfPython
#       - thirty_days_of_python
a = '30DaysOfPython'
b = 'thirty_days_of_python'
print(a.isidentifier())
print(b.isidentifier())

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(list))

# 33. Use the new line escape sequence to separate the following sentences.
sentence_one = 'I am enjoying this challenge.'
sentence_two = 'I just wonder what is next.'
print(sentence_one + '\n' + sentence_two)

# 34. Use a tab escape sequence to write the following lines.
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

# 35. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")


# 36. Make the following using string formatting methods:
a = 8
b = 6
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')
