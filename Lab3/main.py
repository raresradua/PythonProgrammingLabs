def ex_1(a, b):
    """
        Write a function that receives as parameters two lists a and b and
        returns a list of sets containing: (a intersected with b, a reunited with
        b, a - b, b - a)
        :return: x | y, x & y, x - y, y - x
    """
    x, y = set(a), set(b)
    return [x.union(y), x.intersection(y), x.difference(y), y.difference(x)]


def ex_2(string):
    """
        Write a function that receives a string as a parameter and returns a
        dictionary in which the keys are the characters in the character string
        and the values are the number of occurrences of that character in the
        given text.

        Example: For string "Ana has apples." given as a parameter the function
        will return the dictionary: {'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1,
        'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1} .
        :return: frequencies of letters in a string
    """
    return {char: string.count(char) for char in string}


def ex_3(elem1, elem2):
    """
        Compare two dictionaries without using the operator "==" and return a
        ist of differences as follows: (Attention, dictionaries must be
        recursively covered because they can contain other containers, such as
        dictionaries, lists, sets, etc.)
        :return:
    """

    if type(elem1) != type(elem2):
        return False

    if isinstance(elem1, (int, float, bool, type(None))):
        return elem1 == elem2

    # From this point, elem1 and elem2 are iterable objects (so they
    # implement the len method)
    if len(elem1) != len(elem2):
        return False

    if isinstance(elem1, (str, list, tuple, set, frozenset)):
        for item in elem1:
            if item not in elem2:
                return False

    if isinstance(elem1, dict):
        for key, value in elem1.items():
            if key not in elem2.keys():
                return False

            values_checker = ex_3(elem1[key], elem2[key])
            if not values_checker:
                return False

    return True


def ex_4(tag, content, kwargs):
    """
    The build_xml_element function receives the following parameters: tag,
    content, and key-value elements given as name-parameters. Build and
    return a string that represents the corresponding XML element. Example:
    build_xml_element ("a", "Hello there", href =" http://python.org ",
    _class =" my-link ", id= " someid ") returns  the string = "<a
    href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ ">
    Hello there </a>"
    :return: corresponding XML element
    """

    params = " ".join([f'{key}="{value}"' for key, value in kwargs.items()])
    return f"<{tag} {params}>{content}</{tag}>"


def ex_5(s, d):
    """
        The validate_dict function that receives as a parameter a set of tuples (
        that represents validation rules for a dictionary that has strings as
        keys and values) and a dictionary. A rule is defined as follows: (key,
        "prefix", "middle", "suffix"). A value is considered valid if it starts
        with "prefix", "middle" is inside the value (not at the beginning or end)
        and ends with "suffix". The function will return True if the given
        dictionary matches all the rules, False otherwise.

        Example: the rules  s={("key1", "", "inside", ""), ("key2", "start",
        "middle", "winter")}  and d= {"key1": "come inside, it's too cold out",
        "key3": "this is not valid"} => False because although the rules are
        respected for "key1" and "key2" "key3" that does not appear in the rules.
        :return:
    """

    for key, prefix, middle, suffix in s:
        value = d.get(key, "MISSING_VALUE")
        if value == "MISSING_VALUE":
            return False

        if not value.startswith(prefix) or value.startswith(middle):
            return False

        if not value.endswith(suffix) or value.endswith(middle):
            return False

        if middle not in value[len(suffix): len(middle) - len(prefix)]:
            return False

        return True


def ex_6(my_list):
    """
        Write a function that receives as a parameter a list and returns a tuple
        (a, b), representing the number of unique elements in the list,
        and b representing the number of duplicate elements in the list (use sets
        to achieve this objective).
        :return: (nr of unique elements in the list, nr of duplicate elements in the list)
    """
    freq = {item: my_list.count(item) for item in my_list}

    return \
        len([item for item in freq.values() if item == 1]), \
        len([item for item in freq.values() if item > 1])


def ex_7(*sets):
    """
    Write a function that receives a variable number of sets and returns a
    dictionary with the following operations from all sets two by two:
    reunion, intersection, a-b, b-a. The key will have the following form: "a
    op b", where a and b are two sets, and op is the applied operator: |, &, -.

    Ex: {1,2}, {2, 3} =>
    {
        "{1, 2} | {2, 3}": 3,
        "{1, 2} & {2, 3}": 1,
        "{1, 2} - {2, 3}": 1,
        ...
    }
    :return:
    """
    to_return = dict()
    combos = [(s1, s2) for s1 in sets for s2 in sets if s1 != s2]

    operations = {
        '|': lambda s1, s2: s1 | s2,
        '&': lambda s1, s2: s1 & s2,
        '-': lambda s1, s2: s1 - s2,
    }

    for s1, s2 in combos:
        for op in operations:
            to_return[f"{s1} {op} {s2}"] = operations[op](s1, s2)

    return to_return


def ex_8(mapping):
    """
    Write a function that receives a single dict parameter named mapping.
    This dictionary always contains a string key "start". Starting with the
    value of this key you must obtain a list of objects by iterating over
    mapping in the following way: the value of the current key is the key for
    the next value, until you find a loop (a key that was visited before).
    The function must return the list of objects obtained as previously
    described.

    Ex: loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2',
    '2': '2', 'y': 'start'}) will return ['a', '6', 'z', '2']
    :return:
    """

    to_return = list()
    value = mapping['start']

    while value not in to_return:
        to_return.append(value)
        value = mapping[value]

    return to_return


def ex_9(*args, **kvargs):
    """
    Write a function that receives a variable number of positional arguments
    and a variable number of keyword arguments adn will return the number of
    positional arguments whose values can be found among keyword arguments
    values.

    Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return returna 3
    :return: number of positional arguments whose values can be found among keyword arguments values
    """
    return len([1 for i in args if i in kvargs.values()])

