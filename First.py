random_string = "asfnsakdnaskdn"
x = random_string[::2] # take every second characters
print(x) #afsknsd

l1 = [1,2,3,4]
l2 = [5,6,7,7]
l3 = l1+l2
print(l3)
l1.extend(l2) #[1, 2, 3, 4, 5, 6, 7, 7]
print(l1)
x = l1.pop()
print(x) #7
print(l1) #[1, 2, 3, 4, 5, 6, 7]

index7 = l1.index(7)
print(index7) #6, position of 7 in list

l3 = [1,2,3]
l3.append(l2)
print(l3) #[1, 2, 3, [5, 6, 7, 7]]

print(7 in l3) #False
print(7 in l3[3]) #True