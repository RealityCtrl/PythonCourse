# simple functions
def overload(*args):
    for word in args:
        print(word)


overload("word1", "word2", "word3")


def keywords(**kwargs):
    print(kwargs)


keywords(key="words", name="david")


# default values
def fn(value, parameters_list = []):
    parameters_list.append(value)
    print(parameters_list)


fn("a") # ['a']
fn("b") # ['a', 'b']
fn("c", []) # ['c']

