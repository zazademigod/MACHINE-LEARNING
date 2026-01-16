#revision for functions learnt yesterday
def multi_types(name: str, age: int, bal: float)->str:
    details= f"my name is {name} , my age is {age}, and my balance is {bal}"
    return details
info = multi_types('zaza', 22, 0)
print(info)

#data types start 

phone_number = f'my phone number is  , {2349066127966}'
print(phone_number)
print(type(phone_number))

#representing a float can be done using a decimal or with a fraction as shown below 
almost_pi = 22/7
print(almost_pi)
print(type(almost_pi))

#there is a function that lets us round numbers, the function is called the round() fufnction 
pi_rounded = round(almost_pi, 3)
print(pi_rounded)
#this will still retain the same class as the pre-rounded value
print(type(pi_rounded))


sample_float = 44.
print(sample_float)
print(type(sample_float))



#boolean area
first_test = True
print(first_test)
print(type(first_test))
second_test = False
print(second_test)
print(type(second_test))

comp = 1<3
print(comp)
print(type(comp))

comp2 = 2>6
print(comp2)
print(type(comp2))

comp3 = not comp2
print(comp3)
print(type(comp3))


#to see the length of a string or argument we use the len() function

length_of = len(phone_number)
print(length_of)
print(type(length_of))
short_str =""
print(len(short_str))

#changing convertible string to numbers using the float() fuction

phone_num = "09023093318"
index_phn = float(phone_num)
print(index_phn)
print(type(index_phn))
print(type(phone_num))