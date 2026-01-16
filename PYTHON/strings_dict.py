#STRINGS, single or double quatations '/"

#strings are sequences 

x = 'hello, world'

print(x[7]) #output: w

#slicing
print(x[3: ])#output: lo, world

print(len(x)) #output: 12

print([t + ' ' for t in x])

#strings differ from lists in the way that they're immutable, append and other mods don't work on them

#x.append('sd') doesn't work
#x[3] = 'am' doesn't work

#STRING METHODS


print(x.upper())
print(x.lower())

print(x.index('world'))# this takes the substring 'world' as a single index and returns 7

print(x.startswith('he'))#also treats the "he" as a substring and returns true as it starts the string

print(x.endswith('rld'))#returns true as it ends the string


#we can slice between strings in a different way apart from index,  we can use split()

print(x.split())#this splits the string with whitespace by default

#you can specify what you want to be used for splitting

print(x.split('o'))#this forms a list with the parts broken by 'o' as elements

#we can join a list of  by reversing using the .join() method

hi = ['h', 'e', 'l', 'l', 'o']

print(''.join(hi))#this outputs 'hello'


#DICTIONARIES

dictionary = {"key": 'value'}

print(dictionary["key"])#outputs: value

new_dict = {1:'one', 2:'two', 3:"three"}

print(new_dict)

new_dict[2] = "2s"

print(new_dict)
print(new_dict[2])


#dictionary comprehensions

a_list = ['apple', 'book', 'song', 'dance', 'joy']

#to form a dict with the initials as the value


a_dict = {i: i[0] for i in a_list}
print(a_dict)

#'in' keyword in a dict tells us if something is a key

print('apple' in a_dict)
print('table' in a_dict)


#a for loop over a dictionary will loop oevr its keys

for i in a_dict:
    print("{} = {}".format(a_dict[i], i))














	









