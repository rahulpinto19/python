#tuples are unchangable
#tuples are immutable

tup = (1,4,5)
print(type(tup),tup)
tup = (1) #python assumes this as integer

print(type(tup),tup)


#methods in tuples

country1 = ("India","afghanistan","Europe")
country2 = ("pakistan","banglades","saudi")
countries = country1 + country2

print(countries)
print(countries.index(3))