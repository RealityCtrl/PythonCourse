class Person():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class EmailPerson(Person):
    def __init__(self, name, email):
        Person.__init__(self, name)
        self.email = email

    def __str__(self):
        return "name: %s \nemail: %s"%(self.name, self.email)



ada = Person("Ada Lovelace")
print(ada)

name2 = EmailPerson("Ada Lovelace", "ada@lovelace.com")
print(name2)
