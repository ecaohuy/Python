usingrange = {x:x*2 for x in range(12)}
print("Using range(): ",usingrange)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)

# Using two input lists
months_dict = {key:value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dict)
months_dict2 = {months[i]:number[i] for i in range(len(months))}
print("Using two lists: ", months_dict2)

a = [[96], [69]]
print(''.join(list(map(str, a))))

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squares = map(square, numbers)

# Convert the iterator returned by map() to a list
squares_list = list(squares)

print(squares_list)  # Output: [1, 4, 9, 16, 25]

def sum(n):
   if n == 1:
       return 0
   return n + sum(n-1)

a = sum(5)
print(a)

some = ["aaa", "bbb"]

#1
def aa(some):
   return

#2
#def aa(some, 5):
#   return

#3
def aa():
   return

#4
def aa():
   return "aaa"

numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(map(lesser, numbers))
print(small)