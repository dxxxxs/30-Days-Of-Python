# Level 1
# 1. Write a function which generates a six digit/character random_user_id.
import random
import string


def random_user_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))


# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

def user_id_gen_by_user():
    num_char = int(input("Enter number of characters:"))
    num_id = int(input("Enter number of IDs:"))
    characters = string.ascii_letters + string.digits
    return [''.join(random.choice(characters) for _ in range(num_char)) for _ in range(num_id)]


# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).


def rgb_color_gen():
    rgb = f'rgb({random.randint(0, 255)},{
        random.randint(0, 255)},{random.randint(0, 255)})'
    return rgb


# Level 2
# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(n):
    characters = string.ascii_lowercase[0:6]+string.digits
    return ['#' + ''.join(random.choice(characters) for _ in range(6)) for _ in range(n)]


# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(n):
    return [f'{rgb_color_gen()}' for _ in range(n)]

# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.


def generate_colors(type, n):
    if type == 'hexa':
        print(list_of_hexa_colors(n))
    elif type == 'rgb':
        print(list_of_rgb_colors(n))
    else:
        return "Invalid type. Please enter 'hexa' or 'rgb'."


# Level 3
# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    return random.sample(lst, len(lst))

# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.


def array_seven_random_numbers():
    return random.sample(range(10), 7)
