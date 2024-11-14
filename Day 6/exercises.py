# Level 1
# 1. Create an empty tuple
tpl = tuple()
tpl = ()
print(tpl)

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('David', 'Miguel')
sisters = ('Paula', 'Maria')
print(brothers, sisters)

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)

# 4. How many siblings do you have?
n = len(siblings)
print(n)

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings.append('Rocio')
siblings.append('Pedro')
family_members = tuple(siblings)
print(family_members)

# Level 2
# 1. Unpack siblings and parents from family_members
siblings = family_members[:-2]
parents = family_members[-2:]
print(siblings, parents)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'orange', 'grape')
vegetables = ('carrot', 'broccoli', 'spinach', 'potato')
animal_products = ('milk', 'eggs', 'cheese', 'butter')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
n = len(food_stuff_lt)

middle = n//2
if n % 2 == 1:
    print(food_stuff_tp[middle])
    print(food_stuff_lt[middle])
else:
    print(food_stuff_tp[middle-1:middle+1])
    print(food_stuff_lt[middle-1:middle+1])

# 5. Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[3:-3])

# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple:
#           - Check if 'Estonia' is a nordic country
#           - Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print(nordic_countries.count('Estonia'))
print(nordic_countries.count('Iceland'))
