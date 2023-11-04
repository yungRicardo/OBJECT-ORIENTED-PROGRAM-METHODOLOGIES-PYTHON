"""
Assignment 5: Reverse a List using Recursion
Submitted by Ricky Espinoza
Submitted:  October 29, 2023
"""


def reverse_a_list(my_list):
    """ reverses the order of a list using recursion. """

    # get the length of the input list
    length = len(my_list)
    # print the length for debugging purposes
    print(length)

    # base case: if the list contains only one element, return it as is
    if length == 0:
        return []
    elif length == 1:
        return [my_list[0]]

    # recursive case:
    # 1. take the last element of the list (my_list[-1])
    # 2. recursively call reverse_a_list on the list without the last element (my_list[:-1])
    # 3. concatenate the last element with the result of the recursive call
    else:
        ret_value = [my_list[-1]] + reverse_a_list(my_list[:-1])
        return ret_value


def main():
    """ demonstrates the use of the 'reverse_a_list' function. It also prints the original list
    and the reversed list without the last element to showcase the functionality of the program.
    """

    # create a list of lowercase letters from 'a' to 'z'
    alphabet = [chr(letter) for letter in range(ord('a'), ord('z')+1)]

    print(alphabet)
    print(reverse_a_list(alphabet))
    print(alphabet)


if __name__ == "__main__":
    main()

"""
SAMPLE RUN

['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
26
25
24
23
22
21
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

"""
