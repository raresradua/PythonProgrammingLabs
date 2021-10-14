"""
    Laboratory 2 - Python Programming
"""


def ex_1():
    """
        Write a function to return a list of the first n numbers in the Fibonacci string.
        :return: list of the first n Fibonacci numbers
    """
    n = int(input("How many numbers from the Fibonacci string you want? "))
    if n < 1:
        print("Invalid number n. n needs to be >= 1.")
        return
    if n == 1:
        return f'List of the first {n} Fibonacci numbers: {[0]}'
    if n == 2:
        return f'List of the first {n} Fibonacci numbers: {[0, 1]}'
    fibonacci_numbers = [0, 1]
    for i in range(2, n):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return f'List of the first {n} Fibonacci numbers: {fibonacci_numbers}'


def ex_2(*list_of_numbers):
    """
        Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
        :return: list of the numbers that are prime in the original list
    """
    prime_numbers = [nr for nr in list_of_numbers if len([i for i in range(2, nr // 2 + 1) if nr % i == 0]) == 0]
    return f'List of the prime numbers of the list {list_of_numbers}: {prime_numbers}'


def ex_3(a, b):
    """
        Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited
        with b, a - b, b - a)
        :return: a intersected with b, a reunited with b, a - b, b - a
    """

    a_interesct_b = [i for i in a if i in b]
    a_minus_b = [i for i in a if (i in a) and (i not in b)]
    b_minus_a = [i for i in b if (i in b) and (i not in a)]
    a_union_b = a_minus_b + a_interesct_b + b_minus_a

    return f"a intersected b: {a_interesct_b}       a union b: {a_union_b}       a minus b: {a_minus_b}     " \
           f"b minus a: {b_minus_a} "


def ex_4(list_of_notes, list_of_moves, start_position):
    """
        Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and
        a start position (integer). The function will return the song composed by going though the musical notes
        beginning with the start position and following the moves given as parameter.

        Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]
        :return: return the song composed from the rules above
    """
    song = [list_of_notes[start_position % len(list_of_notes)]]
    for move in list_of_moves:
        start_position += move
        song.append(list_of_notes[start_position % len(list_of_notes)])
    return song


def ex_5(matrix):
    """
        Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the
        elements under the main diagonal with 0 (zero).
        :return: return the matrix with 0 below the main diagonal
    """
    if len(matrix) != len(matrix[0]):
        return "No square matrix, so no main diagonal"
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = 0 if i > j else matrix[i][j]
    return matrix


def ex_6(x, *lists):
    """
        Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list
        containing the items that appear exactly x times in the incoming lists.

        Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2 lists [1,2,3 ] # 1 is in list 1 and 4, 2 is
                 in list 1 and 2, 3 is in lists 1 and 2.

        :return: list that contains only the elements that appear exactly x times in all the lists
    """
    all_elements = [el for l in lists for el in l]
    return list(set(filter(lambda el: all_elements.count(el) == x, all_elements)))


def ex_7(*list_of_numbers):
    """
        Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements
        The first element of the tuple will be the number of palindrome numbers found in the list and the second element
        will be the greatest palindrome number.
        :return: tuple( nr of palindromes, greatest palindrome)
    """
    palindromes = [palindrom for palindrom in list_of_numbers if str(palindrom) == str(palindrom)[::-1]]
    return tuple((len(palindromes), max(palindromes) if len(palindromes) else 0))


def ex_8(list_of_strings, flag=True, x=1):
    """
        Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set
        to True. For each string, generate a list containing the characters that have the ASCII code divisible by x if
        the flag is set to True, otherwise it should contain characters that have the ASCII code not divisible by x.

        Example: x = 2, ["test", "hello", "lab002"], flag = False will return (["e", "s"], ["e" . Note: The function
                 must return list of lists.
        :return: list of lists that contain characters that are divisible with x if flag is True or not divisible with x
                 if flag is False
    """
    elements_of_string = []
    for string in list_of_strings:
        els = list()
        for el in string:
            els += el
        elements_of_string.append(els)

    result = []
    for element in elements_of_string:
        res = list()
        for character in element:
            if (ord(character) % x == 0 and flag) or (ord(character) % x != 0 and not flag):
                res += character
        result.append(res)
    return result


def ex_9():
    """
    Write a function that receives as parameter a matrix which represents the heights of the spectators in a stadium
    and will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the
    game. A spectator can't see the game if there is at least one taller spectator standing in front of him. All the
    seats are occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with
    the closest row from the field.

	Example:    [
                [1, 2, 3, 2, 1, 1],
                [2, 4, 4, 3, 7, 2],
                [5, 5, 2, 5, 6, 4],
                [6, 6, 7, 6, 7, 5]
                ]

    Will return : [(2, 2), (2, 4)]
    :return:
    """
    matrix = [[1, 2, 3, 2, 1, 1],
              [2, 4, 4, 3, 7, 2],
              [5, 5, 2, 5, 6, 4],
              [6, 6, 7, 6, 7, 5]]

    output = []
    for index_j in range(len(matrix[0])):
        last_big = matrix[0][index_j]
        for index_i in range(1, len(matrix)):
            if last_big > matrix[index_i][index_j]:
                output.append((index_i, index_j))
            else:
                last_big = matrix[index_i][index_j]
    return output


def ex_10(*lists):
    """
        Write a function that receives a variable number of lists and returns a list of tuples as follows: the first
        tuple contains the first items in the lists, the second element contains the items on the position 2 in the
        lists, etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")].

        Note: If input lists do not have the same number of items, missing items will be replaced with None to be
        able to generate max ([len(x) for x in input_lists]) tuples.
        :param lists: input lists
        :return: list of tuples described in the problem
    """
    max_length = max([len(l) for l in lists])
    for l in lists:
        l.extend([None for x in range(0, max_length - len(l))])
    return list(zip(*lists))


def ex_11(*lists):
    """
        Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the
        tuple.

        Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
        :return: sorted list of tuples based on the criteria in the problem. We will assume that each tuple has at least
                 2 elements and that the second element has at least 3 letters
    """

    return sorted(lists, key=lambda i: ord(i[1][2]))


def ex_12(list_of_words):
    """
        Write a function that will receive a list of words  as parameter and will return a list of lists of words,
        grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.

	    Example: group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will
                 return [['ana', 'banana'], ['carte', 'parte'], ['arme']]

        :return: list of lists with words that rhyme with each other
    """

    rhyme = dict()
    for word in list_of_words:
        if word[-2:] not in rhyme:
            rhyme[word[-2:]] = [word]
        else:
            rhyme[word[-2:]].append(word)

    return list(rhyme.values())
