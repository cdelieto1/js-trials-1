"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(items)

def get_all_evens(nums):
    evens = [ ]

    for num in nums:
        if num % 2 == 0:
            evens.append(num)

    return num        

def get_odd_indices(items):
    """List of odd characters from a string"""

    odd_chars = [ ]

    for character in range(len(items)):
        if character % 2 != 0:
            odd_chars.append(items[character])

    return odd_chars 

#print(get_odd_indices("stringy"))

def print_as_numbered_list(items):
    """Given an array, output a numbered list."""
    i=1

    for item in items: 
        print(f'{i}, {item}')  

        i += 1           

#print_as_numbered_list(['h', 'i'])

def get_range(start, stop):
    result = []
    
    for items in range(start,stop):
        result.append(items)
    return result    


def censor_vowels(word):
    VOWELS = ['a','e','i','o','u']

    for letter in word:
        if letter in VOWELS:
            word = word.replace(letter, "*")

    return word


#print(censor_vowels("cassie"))    

def snake_to_camel(string):

    camelCase = []

    for word in string.split("_"):
        camelCase.append(f'{word[0].upper()}{word[1:]}')

    return ''.join(camelCase)

#print(snake_to_camel("hey_you"))


def longest_word_length(words):

    longest_word = max(words, key=len)
    return len(longest_word)

#print(longest_word_length(['hi', 'hiiiiii']))


def truncate(string):

    result = [] # result = "" didn't work

    for letter in string:
        if len(result) == 0 or letter != result[-1]:
            result.append(letter)

    return "".join(result)        

#print(truncate("aaahhbbeer"))

def has_balanced_parens(string):

    parens = 0

    for char in string:
        if char == "(":
            parens += 1
        if char == ")":
            parens -= 1

            # if parens < 0:
            #     return False 

    return parens == 0            

            
#print(has_balanced_parens("("))


def compress(string):
    pass
