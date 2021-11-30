"""
    Laboratory 6 - Python Programming
"""
import re


def ex_1(my_text):
    """
    Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of
    alpha-numeric characters.
    :param my_text:
    :return:
    """
    list_of_words = re.findall("\w+'\w+|\w+", my_text)
    return list_of_words


def ex_2(regex_str, my_text, x):
    """
    Write a function that receives as a parameter a regex string, a text string and a whole number x, and returns
    those long-length x substrings that match the regular expression.
    :return:
    """
    substrings = re.findall(regex_str, my_text)
    print(substrings)
    substrings = list(filter(lambda i: len(i) == x, substrings))
    return substrings


def ex_3(my_string, regex_list):
    """
    Write a function that receives as a parameter a string of text characters and a list of regular expressions and
    returns a list of strings that match on at least one regular expression given as a parameter.
    :return:
    """
    list_of_matches = list()
    dict_matches = dict()
    for regex in regex_list:
        # dict_matches[regex] = re.findall(regex, my_string)
        list_of_matches += re.findall(regex, my_string)
    # list_of_matches = set(list_of_matches)
    # return dict_matches
    return list_of_matches


def ex_4(path_to_xml, attrs):
    """
    Write a function that receives as a parameter the path to an xml document and an attrs dictionary and returns
    those elements that have as attributes all the keys in the dictionary and values the corresponding values. For
    example, if attrs={"class": "url", "name": "url-form", "data-id": "item"} the items selected will be those tags
    whose attributes are class="url" si name="url-form" si data-id="item".

    Ex: <img border="0" alt="W3Schools" src="logo_w3s.gif" width="100" height="100">
    :return:
    """
    with open(path_to_xml, "r") as f:
        content = f.read()

    # generam string urile cu atribute
    list_strings = ['{}="{}"'.format(k, v) for k, v in attrs.items()]
    print(list_strings)
    # identificam toate tag urile img, a, etc <ceva atribute>value</ceva>
    tags_attr = re.findall("(<.*>)", content)
    print(tags_attr)
    # cautam string urile in tag uri
    result = list()

    for tag in tags_attr:
        in_tag = 1
        for string in list_strings:
            if string not in tag:
                in_tag = 0
                break
        if in_tag:
            result += tag
    return result


def ex_5():
    """
    Write another variant of the function from the previous exercise that returns those elements that have at least
    one attribute that corresponds to a key-value pair in the dictionary.
    :return:
    """
    pass


def ex_6():
    """
    Write a function that, for a text given as a parameter, censures words that begin and end with vowels. Censorship
    means replacing characters from odd positions with *. :return:
    """
    pass


def ex_7():
    """
    Verify using a regular expression whether a string is a valid CNP.
    :return:
    """
    pass


def ex_8():
    """
    Write a function that recursively scrolls a directory and displays those files whose name matches a regular
    expression given as a parameter or contains a string that matches the same expression. Files that satisfy both
    conditions will be prefixed with ">>"
    :return:
    """
    pass