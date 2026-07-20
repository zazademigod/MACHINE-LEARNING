people = [
    {"name": 'david', 'school':'UI'},
    {'name': 'james', 'school': 'FUTO'},
    {'name': 'ebuka', "school": 'YABATECH'},
    {'name': 'favour', 'school': 'UI'}
]

#running some operations on this like sort, would fail and as such we need to define functions to tell what to use

def f(person):
    return person['name']

people.sort(key=f)
print(people)

#python provides us a shorter way to represent a very short function

people.sort(key=lambda person: person["school"])

print(people)