#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for y in my_list:
        if y == search:
            new_list.append(replace)  # append replacement value
        else:
            new_list.append(x)  # append original

    return new_list

# the list comprehension way:
# def search_replace(my_list, search, replace):
# return [replace if search == y else y for y in my_list]
