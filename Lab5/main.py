"""
    Laboratory 5 - Python Programming
"""


def ex_2(*args, **kwargs):
    """
    2)  Create a function and an anonymous function that receive a variable number of arguments. Both will return the sum
        of the values of the keyword arguments.

        Example:

        For the call my_function(1, 2, c=3, d=4) the returned value will be 7.
    """
    anon_func = lambda *args, **kwargs: sum([value for value in kwargs.values()])
    print("anon_func called: ", anon_func(*args, **kwargs))

    def not_anon_func(*args, **kwargs):
        return sum([value for value in kwargs.values()])
    print("not_anon_func called: ", not_anon_func(*args, **kwargs))


def ex_3(my_string):
    """
    3)  Using functions, anonymous functions, list comprehensions and filter, implement three methods to generate a
        list with all the vowels in a given string.

        For the string "Programming in Python is fun" the list returned will be ['o', 'a', 'i', 'i', 'o', 'i', 'u'].
    """

    def my_func(my_string):
        vowels = list()
        for el in my_string:
            if el.lower() in "aeiou":
                vowels.append(el)
        return vowels

    print("Using a function called my_func: ", my_func(my_string))

    vowels = [el for el in my_string if el.lower() in "aeiou"]
    print("Using list comprehension: ", vowels)

    print("Using filter and anonymous functions: ", list(filter(lambda el: el.lower() in "aeiou", my_string)))


def ex_4(*args, **kwargs):
    """
    4)  Write a function that receives a variable number of arguments and keyword arguments. The function returns a
        list containing only the arguments which are dictionaries, containing minimum 2 keys and at least one string key
        with minimum 3 characters.

        Example:

        my_function(

        {1: 2, 3: 4, 5: 6},

        {'a': 5, 'b': 7, 'c': 'e'},

        {2: 3},

        [1, 2, 3],

        {'abc': 4, 'def': 5},

        3764,

        dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},

        test={1: 1, 'test': True}

        ) will return: [{'abc': 4, 'def': 5}, {1: 1, 'test': True}]

        ex_4({1:2, 3:4, 5:6}, {'a':5, 'b':7, 'c':'e'}, {2:3}, [1,2,3], {'abc':4, 'def': 5}, 3764, dictionar={'ab':4,
        'ac':'abcde', 'fg':'abc'}, test={1:1, 'test':True})

    :return:
    """

    result = list()
    for i in args:
        if isinstance(i, dict) and len(i.keys()) >= 2:
            for el in i.keys():
                if isinstance(el, str) and len(el) >= 3:
                    result.append(i)
                    break

    for j in kwargs.values():
        if isinstance(j, dict) and len(j.keys()) >= 2:
            for el in j.keys():
                if isinstance(el, str) and len(el) >= 3:
                    result.append(j)
                    break
    return result


def ex_5(my_list):
    """
    5)  Write a function with one parameter which represents a list. The function will return a new list containing all
        the numbers found in the given list.

        Example: my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]) will return [1, 5, 6, 3.0]
    """
    if not isinstance(my_list, list):
        return "Invalid parameter, not a list!"

    numbers_list = [el for el in my_list if isinstance(el, int) or isinstance(el, float)]
    return numbers_list


def ex_6(integers_list):
    """
    6)  Write a function that receives a list with integers as parameter that contains an equal number of even and odd
        numbers that are in no specific order. The function should return a list of pairs (tuples of 2 elements) of
        numbers (Xi, Yi) such that Xi is the i-th even number in the list and Yi is the i-th odd number

    Example:
        my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]) will return [(2, 1), (8, 3), (4, 5), (10, 7), (2, 9)]
    """
    even = list(filter(lambda i: i % 2 == 0, integers_list))
    if not len(integers_list) - len(even) == len(even):
        return "Invalid input. Make sure you have an equal amount of even and odd numbers"
    odd = list(filter(lambda i: i % 2 == 1, integers_list))
    return list(zip(even, odd))


def sum_digits(x):
    return sum(map(int, str(x)))


def ex_7(*args, **kwargs):
    """
    7) Write a function called process that receives a variable number of keyword arguments

        The function generates the first 1000 numbers of the Fibonacci sequence and then processes them in the following way:

        If the function receives a parameter called filters, this will be a list of predicates (function receiving an
        argument and returning True/False) and will retain from the generated numbers only those for which the predicates are True.
ex
        If the function receives a parameter called limit, it will return only that amount of numbers from the sequence.

        If the function receives a parameter called offset, it will skip that number of entries from the beginning of the result list.

        The function will return the processed numbers.

        Example:

        def sum_digits(x):

            return sum(map(int, str(x)))

        process(

            filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],

            limit=2,

            offset=2

        ) returns [34, 144]

        Explanation:

        # Fibonacci sequence will be: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...

        # Valid numbers are: 2, 8, 34, 144, 610, 2584, 10946, 832040

        # After offset: 34, 144, 610, 2584, 10946, 832040

        # After limit: 34, 144

    """
    filters = None
    limit = 1000
    offset = 0
    for i in kwargs.keys():
        if i == "filters":
            filters = kwargs[i]
        if i == "limit":
            limit = kwargs[i]
        if i == "offset":
            offset = kwargs[i]

    fib = list()
    for i in range(0, 1000):
        if i == 0:
            fib.append(0)
        elif i == 1:
            fib.append(1)
        else:
            fib.append(fib[i-2] + fib[i-1])

    if filters:
        for i in filters:
            fib = list(filter(i, fib))
    print(fib)
    fib = fib[offset:]
    print(fib)
    fib = fib[:limit]
    print(fib)


def ex_8():
    def multiply_by_two(x):
        return x * 2


    def print_arguments(func):
        print("Arguments are: ", func.__code__.co)
        return func

    augmented_multiply_by_two = print_arguments(multiply_by_two)
    x = augmented_multiply_by_two(10)
    print(x)

