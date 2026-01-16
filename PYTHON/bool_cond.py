#booleans[this gives true or false]

x = True #the first letter has to be in captal letter 

print(x)
print(type(x))


#instead of putting true or false in our code we use boolean operators

def can_run_for_pres(age):
    n_age = age >= 40
    if n_age == True:
        print(f"yes, {age} can run for president")
    else:
        print(f"no, {age} cannot run for president")
    return n_age

can_run_for_pres(50)
#print('is 50 enough to run for president? ', can_run_for_pres(50))
#print('can a 25 year old run for president? ', can_run_for_pres(25))


#to combine two bolean values we sue the and operator 


def run_for_pres(age , citizenxhip):
    iden = (age >= 35) and citizenxhip

    return iden


print(run_for_pres(33, False))
print(run_for_pres(44, False))
print(run_for_pres(34, True))
print(run_for_pres(37, True))
