dictone ={"ginger": 1, "garlic": 2, "onion": 3}
print(dictone)

for key in dictone:
    print(key, dictone[key])

for key,value in dictone.items():
    print(key, value) 



print(dictone.pop("ginger"))
print(dictone.popitem())

squared_dict = {x: x**2 for x in range(10)}
print(squared_dict)


keys = ['a', 'b', 'c']
values = [1, 2, 3]
dicttwo = dict(zip(keys, values))
dictthree = dict.fromkeys(keys,values)
print(dicttwo)
print(dictthree)