# str=[start:stop:step]
trial = "HelloWorld"
new_trial = trial[::-1]
print(new_trial)


# new_way of reversing a string
def reverse_string(string):
    if len(string) == 0:
        return string
    return reverse_string(string[1:]) + string[0]
print(reverse_string("HelloWorld"))


# 1 more way to reverse a string
def reverse_string(string):
    if len(string) == 0:
        return string
    return string[::-1]
print(reverse_string("HelloWorld"))