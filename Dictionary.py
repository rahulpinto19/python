dict1 = {
    "apple":1,
    "ball":2,
    "cat":3
}

for keys in dict1.keys():
    print(dict1.get(keys))


ep1 = {"1":1,"2":2,"3":3}
ep2 = {"4":4,"5":5}


ep1.update(ep2)
print(ep1)

ep1.pop("1") #removes 1 key and element
ep1.popitem() #removes last item form the dictionary