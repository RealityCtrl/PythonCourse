#tuples
empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))
#unpacking tuples
marx = ('groucho', 'asdlasmd', 'name3')
a,b,c = marx
print(a) #groucho

#dictionaries
dict1 = {1:'one', 2:'two', 3:'three'}
print(dict1) #{1: 'one',  3: 'three', 2: 'two', 7:'seven'}
print(dict1[2]) #two
name = ["name", "david"]
email = ["email","a@b.com"]
dict_converted = dict([name,email])
print(dict_converted) #{'name': 'david', 'email': 'a@b.com'}
print(dict_converted["email"]) #a@b.com
dict_converted["email"] = "b@c.com"
print(dict_converted) #{'name': 'david', 'email': 'b@c.com'}
dict_converted.clear()
print(dict_converted) #{}

#sets
set_name = {"david", "david"}
set_name2 = {"alan", "emer", "david"}

print(set_name) #{'david'}
print(set_name2) #{'david', 'alan', 'emer'}
set1 = set_name & set_name2 #{'david'}
print(set1)
print(set_name | set_name2) #{'alan', 'emer', 'david'}

print(set_name ^ set_name2) #{'emer', 'alan'}