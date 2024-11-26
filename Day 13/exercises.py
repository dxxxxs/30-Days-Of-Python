# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
lst = [i for i in numbers if i <= 0]

# 2. Flatten the following list of lists of lists to a one dimensional list :
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lst = [item for sublist1 in list_of_lists for sublist2 in sublist1 for item in sublist2]

# 3. Using list comprehension create the following list of tuples:
list_of_tuples = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(10)]

# 4. Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
lst = [[country.upper(), country[:3].upper(), city.upper()]
       for sublist1 in countries
       for country, city in sublist1]

# 5. Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
lst = [dict(country=country, city=city)
       for sublist1 in countries for country, city in sublist1]

# 6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]
lst = [(f'{firstname} {lastname}')
       for sublist1 in names for firstname, lastname in sublist1]

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.


def slope(x1, y1, x2, y2): return (y2 - y1) / (x2 - x1) if x1 != x2 else None
def y_intercept(m, x1, y1): return y1 - m * x1
