class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        return self.hidden_name

    @name.setter
    def name(self, name):
        self.hidden_name = name


fowl = Duck("Howard")
print(fowl.name)

fowl.name = "Don"
print(fowl.name)