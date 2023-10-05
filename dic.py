print("containers:Dictionaries")
d=dict()
d={"cat":"cute","dog":"furry"}
print("Is the dictionary has the key 'cat'?",'cat' in d)
d['fish']='wet'
print("After adding new entry to 'd':",d)
print("get an element monkey:",d.get('monkey','N/A'))
del d['fish']
