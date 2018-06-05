#basic data handling

days = ["Monday", "Tuesday","Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
fruits = ["apples", "orange", "kiwi"]
deserts = ["sponge", "cake", "pannacotta"]

for day, fruit, desert in zip(days, fruits, deserts):
    print(day, fruit, desert)
    """
    Monday apples sponge
    Tuesday orange cake
    Wednesday kiwi pannacotta
    """

#range


def list_appender(x=0, y=10, z=1):
    list1 = []
    for x in range(x,y, z): #range is to 9
        list1.append(x)
    return list1

print(list_appender()) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_appender(10, 0, -1)) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list_appender(z=2)) #[0, 2, 4, 6, 8]

#generators
number_list = [number for number in range(1,10)]
print(number_list) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

word = "sjfnfsdkfnsdkfndfskdfn"

letter_count = {letter:word.count(letter) for letter in word}
print(letter_count)

def letter_counter(word):
    letters = {}
    for letter in word:
        letters[letter] = letters.get(letter,0) +1
    return letters

letter_count2 = letter_counter(word)
print(letter_count2)
print(type(letter_count2))
print(type(letter_count))
print(type(number_list))

