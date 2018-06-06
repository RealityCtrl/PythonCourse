class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        return self.hidden_name

    def set_name(self, name):
        self.hidden_name = name

    name = property(get_name, set_name)

fowl = Duck("Howard")
print(fowl.name)

fowl.name = "Don"
print(fowl.name)