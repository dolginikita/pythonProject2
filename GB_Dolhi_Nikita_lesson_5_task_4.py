src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def src_bigger(my_list):
    """
    :param my_list: Taken list, with 'int' type of value
    :return: A list with values greater than the previous one
    """
    result = [i for n, i in enumerate(my_list) if i > src[n - 1] and n != 0]
    return result


print(src_bigger(src))