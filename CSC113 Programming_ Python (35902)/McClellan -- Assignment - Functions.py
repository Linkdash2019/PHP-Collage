from logging import raiseExceptions
from operator import index

ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz "
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
DECIMAL_DIGITS = "0123456789"

def main():
    test_list = ['BANANA', 'happy', 'number1', 'Cameron', 'Happy and I know it', 'Are you number 1']
    for item in test_list:
        print(is_alpha(item))

    print('--------------------------------')

    test_list = ['12345', '1x5=99', 'No', '6867578587', '0', '123']
    for item in test_list:
        print(is_digit(item))

    print('--------------------------------')

    test_list = ['banana', 'happy', 'free', 'not found']
    test_list2 = ['a', 'no', 'f', 'm']
    test_index = 0
    for item in test_list:
        print(find_chr(item, test_list2[test_index]))
        test_index += 1

    print('--------------------------------')

    test_list = ['banana', 'happy', 'free', 'wii', 'become']
    test_list2 = ['a', 'pp', 'f', 'e', 'o']
    test_list3 = ['o','t', 't', 'i', 'am']
    test_index = 0
    for item in test_list:
        print(replace_chr(item, test_list2[test_index], test_list3[test_index]))
        test_index += 1

def is_alpha(str) -> bool:
    for var in str:
        if var in ASCII_LOWERCASE or var in ASCII_UPPERCASE:
            bool = True
        else:
            bool = False
            return bool
    return bool

def is_digit(str) -> bool:
    for var in str:
        if var in DECIMAL_DIGITS:
            bool = True
        else:
            bool = False
            return bool
    return bool

def find_chr(str, char_to_find) -> int:
    index = 1
    for var in char_to_find:
        if index > 1:
            return "Error: char_to_find is not a single character"
        index += 100000

    index = 1
    for var in str:
        if var == char_to_find:
            return index
        else:
            index += 1
    index = -1
    return index

def replace_chr(str, char_to_find, char_to_replace) -> str:
    index = 1
    for var in char_to_find:
        if index > 1:
            return "Error: char_to_find is not a single character"
        index += 100000

    index = 1
    for var in char_to_replace:
        if index > 1:
            return "Error: char_to_replace is not a single character"
        index += 100000

    word = []
    for var in str:
        if var == char_to_find:
            word.append(char_to_replace)
        else:
            word.append(var)
    word = ''.join(word)
    return word

