#lists are an ordeed squence of values
#to create we use as follows 

prime_nums = [2, 3, 13, 5, 7, 11,]
#numbers

fruits = ['apple', 'mangoes', 'paw paw', 'watermelons']
#strings

#A list of lists
collection = [[1,2,3,4,5], ['mango', 'paw paw', 'udara'], ['man', 2, 25, 'man child']]#can even go as far as mixing the elements in the set 


#you can access list elements using square brackets ex: fruits[0] == 'apple'
#indexing for lists start from 0 to (n-1)


third = fruits[2]
print(third)


#elements at the end can be accessed with negative numbers 
#negative indexing starts from -1
print(fruits[-1]) #this outputs'watermelons'

#SLICING
#next is slicing, this is essentially using colons':' to pick a ange to select from
#this startes from the first signified index to the one before the tail, ex: bags[c:f]
#the above checks from index c to the element before f
print(fruits[0:3]) #this outputs ['apples', 'mangoes', 'pawpaw'] (index 0 to 2)

#we can pick elements in a list fom start/to finish by ommitting the beginning or ending
#as such test[:3], this lists from the beginning to the index 2(third element)
#or test[2:] this lists from elemnt with index 2 to the end of the list 

print(fruits[:2])
print(fruits[1:])
print(fruits[1:-1]) #this is essentially the same as starting from index 1 to the last index
#(only the last would be ignored), so this outputs every element in the list except the first and the last element 

#it's more convinient to print the last set of values in a list using negative indexing 

#CHANGING LISTS
print(fruits)
fruits[2] = 'guava' #this changes the value of the index 2 in fruits to guava 
print(fruits)

fruits[:2] =['tangerine']
print(fruits)
fruits[:2] = ['orange', 'peach', 'strawberry', 'blueberry']
print(fruits)

fruits[:4] = ['paw paw', 'mangoes', 'apple']
print(fruits)

#LISTS FUNCTIONS

#how many fruits are in the list, use len(list[])

print('the number of fruits in the list is ',len(fruits))

#to sort the elements in a list we use the sorted() function

print(prime_nums)
sorted_primes = sorted(prime_nums)
print(sorted_primes)

sorted_fruits = sorted(fruits)
print(sorted_fruits)

#to get the sum of values in a list we use the sum() function
print(sum(prime_nums))

print(sum([2, 3, 7]))

print(max(2, 6, 19))#this gives the maximum number in the group of nmbers listed

print(max(prime_nums))#this outputs the maximum number inthe list, and vice versa for the min() function


#OBJECTS
#everyting in python is an object, methods are things that let us use built in pipertoes of objects
#example would be python numbers that carry ana associated variable called imag which represents their imaginary part, an example below (.imag is a method) a method is a function attached to an object

x = 24

print(x)
print(x.imag) #outputs 0 because the imaginary part of the eal number 24 is 0

#to create a complex number we use as follows

c = 12 + 9j
print(c)
print(c.imag)#this outputs the imaginary part of the complex number 

#example is the method for checking the bit lemgth of a number 

print(x.bit_length())


#LIST METHODS
#list.append modifies a list by adding an item to the end 

print(fruits.pop())
print(fruits)
fruits.append('banana')
print(fruits)
print(fruits.pop())

#we can search for where a particular element is in a list using the .index() method

print(fruits)

print('the index of mangoes in the list of fruits is ',fruits.index('mangoes'))

print('watermelon' in fruits)

if 'watermelon' in fruits:
    print('watermelon is here')
else:
    print('watermelon is not here')

#there are multiple ways to remove an item from a list
#one is the del, this is used to delete full lists or specfied index, also works with slicing
#the other is the .remove() method, this removes the value specified in the brackets
#the last is the .pop() method, this will remove the last element in the list if the index isn't signified 

new_list = ['apple', 'mango', 'watermelon', 'guava', 'paw paw', 'tangerine']
print(new_list)
new_list = sorted(new_list)
print(new_list)
print(new_list.pop(2))#removes the element at index 2
print(new_list)
print(new_list.remove('guava'))#deletes the first guava found
del new_list[1:3]#this deletes from indes 1 to 2 
print(new_list[1])
print(new_list)

#TUPLES
#similar to lists but uses parenthesis and cannot be modified 

even_tuple = (2, 4, 6, 8, 10, 16, 12, 22, 18, 16, 0)


#cannot be modified in the sense that stuffs like even_tuple[2] = 11 can't work




