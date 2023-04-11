my_list = [1,2,3]
def add_to_list(lst, x):
    nl = lst.copy()
    nl.append(x)
    return nl
new_list = add_to_list(my_list, 4)
print(my_list)
print(new_list)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(10))