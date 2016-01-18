# -*- coding: utf-8 -*-

def parse_number(string):
    """return the parsed number if any, otherwise, the string as it"""
    try:
        return int(string)
    except ValueError:
        pass
    try:
        return float(string)
    except ValueError:
        pass
    return string


def get_sublist(list_, keys, key):
    """get the sublist of list_ between key, and the next that is also in keys
    >>> get_sublist(range(20),[1,2,4,6,8,12,14,17],8)
    [9, 10, 11]
    """
    sl = list_[list_.index(key) + 1:]
    l = []
    for el in sl:
        if el in keys:
            break
        l.append(el)
    return l


def info_parse(info_txt, info_dict):
    """parse the info string sent by an UCI engine according to info_dict dictionary"""

    split_text = info_txt.split(" ")

    dict_ = dict()
    for key in info_dict.keys():
        if key in split_text:
            value = get_sublist(split_text, info_dict.keys(), key)
            if type(info_dict[key]) == list:
                dict_[key] = value
            elif type(info_dict[key]) == dict:
                info_txt_a = " ".join(value)
                dict_[key] = info_parse(info_txt_a, info_dict[key])
            else:
                if len(value) == 0:
                    dict_[key] = True
                else:
                    n = parse_number(value[0])
                    if n:
                        dict_[key] = n
                    else:
                        dict_[key] = value[0]
    return dict_


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
