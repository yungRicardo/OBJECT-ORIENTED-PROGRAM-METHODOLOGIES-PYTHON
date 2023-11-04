# def factorial(n):
#     """ Factorial calculation """
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)


# print(factorial(10))


# def fibonacci(n):
#     """ fibonacci sequence """

#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# print(fibonacci(14))


# def countdown(n):
#     """ Counts down to 1 with whatever number is passed in the params"""
#     if n == 0:
#         print("Countdown complete!!")
#     else:
#         print(n)
#         return countdown(n-1)


# countdown(10)

# def sum_of_natural_num(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return n + sum_of_natural_num(n-1)


# print(sum_of_natural_num(10))

# def print_a_pattern(n):else:        return lst[0] + sum_of_list(lst[1:])
#     """ print a right triangle """
#     if n > 0:
#         print_a_pattern(n-1)
#         print("*" * n)


# print_a_pattern(5)

# def sum_of_list(lst):
#     """ sums up all the elements in a list and return value"""
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_of_list(lst[1:])


# print(sum_of_list([1, 2, 3]))

# def print_numbers(n):
#     """ print numbers from 1 to n"""
#     if n > 0:
#         print_numbers(n-1)
#         print(n, end=" ")


# print_numbers(5)
