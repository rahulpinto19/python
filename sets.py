s = {2,3,4,2,2}
print(s)

temp1 = {}
temp2 = set()

print(type(temp1),type(temp2))



#methoda in sets
s1 = {2,3,4,5}
s2 = {5,3,6,7}

print(s1.intersection(s2))
print(s1.union(s2))
s1.update(s2)
print(s1,s2)