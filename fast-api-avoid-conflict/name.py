def fullname(firstname: str, lastname:str):
    fullname = firstname.title() + " " + lastname.title()
    return fullname

def nameAndAge(name: str, age: int):
    return name + " is this many " + str(age)

def processList(items: list[str]):
    for item in items:
        print(item)

someItems = ["apple", "orange", "banana"]
print(processList(someItems))

def process(t_items: tuple[str, str, int], s_items: set[str]):
    return t_items, s_items
my_tuple = ("water", "fire", 4)
my_set = {"elephant", "giraffe", "giraffe"}
print(process(my_tuple, my_set))

print(nameAndAge("Jason", 34))
print(fullname("Jason", "Whitlow"))

