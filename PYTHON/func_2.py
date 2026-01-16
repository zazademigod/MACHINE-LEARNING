#a docstring is using triple quatation to pass a message in code for help() to be able to return something meaningful when called 

def smallest_diff(a, b, c, d):

    """this returns the smalest difference from the provided numbers and computations

    >>>smallest_diff(4, 6, 12, 5)

    return 1
    """
    first_diff = abs(a-b)
    sec_diff = abs(b-c)
    third_diff = abs(c-d)
    four_diff =  abs(a-c)
    fifth_diff = abs(a-d)

    least = min(first_diff, sec_diff, third_diff, four_diff, fifth_diff)

    return least

find_smallest = smallest_diff(4, 6, 12, 5)
print (find_smallest)

help(smallest_diff)

#seperating values

print(12, 18, 99, sep='-')

print('a', 4, 19, 'd', sep='[')

#an interesting example using the max function sees us using the optional key argument that returns the argument x that maximizes key(x), the argmax


def mod_5(x):

    """this return the value of the remainder of 'x' divided by 5"""
    modulo_x = x % 5
    return modulo_x
#here we refer to the value of mod_5 as a key in the print function
print(
    "what's the biggest number?", 
    max(120, 12, 99),
    "which number is the biggest modulo 5?", 
    max(120, 12, 99, key=mod_5),
    sep= '\n',
)