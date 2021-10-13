"""
    Laboratory 1 - Python Programming
"""


def ex_1():
    """
        Find The greatest common divisor of multiple numbers read from the console.
    :return:
    """

    def gcd(a, b):
        """
            Calculates the greatest common divisor of two numbers
        :param a:   after all operations, greatest common divisor
        :param b:
        :return:
        """
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

    numbers = input("Insert numbers separated by space: ")
    numbers = [int(i) for i in numbers.split(" ")]  # functional programming course 2
    curr_gcd = numbers[0]
    for i in numbers[1:]:
        curr_gcd = gcd(curr_gcd, i)
    return curr_gcd


def ex_2():
    """
    Write a script that calculates how many vowels are in a string.
    :return: how many vowels are in a string
    """
    input_string = input("Insert string to calculate how many vowels are in it: ")
    input_string = input_string.lower()
    count_vowels = 0
    for character in input_string:
        if character in "aeiou":
            count_vowels += 1
    return count_vowels


def ex_3():
    """
        Write a script that receives two strings and prints the number of occurrences of the first string in the second.
    :return:
    """
    first_string = input("Insert a string: ")
    second_string = input("Insert a string to calculate how many occurrences of the first string are in this one: ")
    occurrences = 0
    while True:
        index = second_string.find(first_string)
        if index == -1:
            break
        occurrences += 1
        second_string = second_string[index + 1:]
    return occurrences


def ex_4():
    """
    Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
    :return: string in format lowercase_with_underscores
    """
    string = input("Input string in UpperCamelCase to convert it in lowercase_with_underscores(ex: AbCDe -> ab_c_de): ")
    lowercase_with_underscores = ""
    for character in string:
        if character.isupper():
            lowercase_with_underscores = lowercase_with_underscores + "_" + character.lower()
        else:
            lowercase_with_underscores += character
    return lowercase_with_underscores[1:] if lowercase_with_underscores[0] == "_" else lowercase_with_underscores


def ex_5():
    """
    Given a square matrix of characters write a script that prints the string obtained by going through the matrix in
    spiral order (as in the example):

    firs      1  2  3  4    =>   first_python_lab
    n_lt      12 13 14 5
    oba_      11 16 15 6
    htyp      10 9  8  7
    :return: string obtained by going through the matrix in spiral order
    """
    matrix = [
              ['b', 'u', 'n', 'a', '_'],
              ['c', 'i', '_', 'o', 'z'],
              ['a', '_', '?', 'm', 'i'],
              ['f', 'e', 'l', 'u', 'u'],
              ['_', 'e', 'c', '_', 'a']
            ]
    string = ""
    while matrix:
        for el in matrix[0][:len(matrix)]:
            string += el
        matrix = matrix[1:]

        for j in range(0, len(matrix)):
            string += matrix[j][-1]
            matrix[j] = matrix[j][0:-1]

        if len(matrix) == 0:
            break
        for el in matrix[len(matrix)-1][::-1]:
            string += el
        matrix = matrix[0:len(matrix) - 1]

        if len(matrix) == 0:
            break
        for j in range(len(matrix)-1, -1, -1):
            string += matrix[j][0]
            matrix[j] = matrix[j][1:]

    print(string)







def ex_6():
    """
        Write a function that validates if a number is a palindrome.
    :return: True if palindrome, False otherwise
    """
    number = input("Input number: ")
    return "Is the number %d a palindrome? Answer: %s" % (int(number), number == number[::-1])


def ex_7():
    """
    Write a function that extract a number from a text (for example if the text is "An apple is 123 USD",
    this function will return 123, or if the text is "abc123abc" the function will extract 123). The function will
    extract only the first number that is found.
    :return: First number that is found
    """
    text = input("Insert text (separate words with space): ")
    first_number_found = ""
    for character in text:
        if character in "0123456789":
            first_number_found += character
            index = text.index(character) + 1
            while index < len(text) and '0' <= text[index] <= '9':
                first_number_found += text[index]
                index += 1
            break
    return int(first_number_found) if first_number_found != "" else "No number found in text"


def ex_8():
    """
    Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary
    format is 00011000, meaning 2 bits with value "1"
    :return: Number of bits of value 1
    """
    number = input("Input number: ")
    binary_format = bin(int(number))
    return binary_format[2:].count('1')


def ex_9():
    """
    Write a function that determines the most common letter in a string. For example if the string is "an apple is
    not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered.
    Casing should not be considered "A" and "a" represent the same character.
    :return: Most common letter in the string
    """
    text = input("Input text here and press ENTER to submit it: ")
    text = text.lower()
    letter_frequencies = dict()
    for character in text:
        if not character.isalpha():
            continue
        if character not in letter_frequencies:
            letter_frequencies[character] = 1
        else:
            letter_frequencies[character] += 1
    inverse_letter_frequencies = [(value, key) for (key, value) in letter_frequencies.items()]
    return max(inverse_letter_frequencies)[1]


def ex_10():
    """
    Write a function that counts how many words exists in a text. A text is considered to be form out of words that
    are separated by only ONE space. For example: "I have Python exam" has 4 words.
    :return: How many words are in a text
    """
    text = input("Input text (separate words with exactly ONE space): ")
    return len(text.split(" "))


