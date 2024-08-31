a = ["apple",1,2,434,"ball",8,3,2,3,21,12,1,2,]

print(a[0:len(a)])
print(a[1:8]) #slicing the list

print(a[1:9:3]) # slicing and jumping 3 is the parameter


#methods in list
l = [11,21,46,1,-93,64,23,88]
print(l)
l.append(5)
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
print(l.index(1))
print(l.count(64))


m = l # here m stores the reference and when changing in the m it willl reflect in the l instead we can do

m = l.copy()