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
    pass  # TODO: replace this line with your code


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
