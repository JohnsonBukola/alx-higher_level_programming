#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for lists in matrix:
        new_list = []
        for y in lists:
            new_list.append(y ** 2)
        new_matrix.append(new_list)

    return new_matrix

# the lambda and the map function would look something like this:
# def square_matrix_simple(matrix=[]):
# return [list(map(lambda n: n**2, sublist)) for sublist in matrix]
