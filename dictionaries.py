# js objects
# swift dictionaries
# Java hashmaps

d = {}

#one primary use-case is to associate keys with values
#Dicts provdie a very efficient fetching of keys
#Dicts provide a de-duplication functionality since they never stor dups of any keys

e = {'foo': 12, 11: 'bar'}

# print out the value 12 from dict
print(e['foo'])
print(e[11])

# iterate through dict keys pairs
for key on e:
    print(key, e[key])


# iterate through key-value pairs
for key, val in e.item():
    print(key, val)

# dictionaries have a very large use case 