#booleans and conditionals

#conditional example
def run_for_pres(age):
    valid_age = age >= 35
    
    return valid_age


test_age = run_for_pres(44)

print('can the 44 yr old run for pres? ', test_age)
test_2_age = run_for_pres(16)
print('can a 15 year old run for pres? ', test_2_age)

#booleans and control flow

def inspect(num):

    if num == 0:
        print(num, ' is equal to zero')
    elif num > 0:
        print(num, ' is greater than zero')
    elif num < 0:
        print(num, ' is less than zero and negative')
    else: 
        print(num, ' is something i haven`t seen')

first_case = inspect(-5)
sec_case = inspect(19)
third_case = inspect(0)