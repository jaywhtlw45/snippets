class Person:
    default_name = "doug"
    def __init__(self, name: str, age: str | None = None):
        if (age): 
            print(name, age)
        else:
            print(name)
    
    # static method can be called from any instance without passing self
    @staticmethod
    def echo(statement: str):
        print (statement)

    # class method needs the cls (class) object to be based to get information
    @classmethod
    def get_default_name(cls):
        print(cls.default_name)

the_guy = Person ("jason")
a_guy = Person("matthew", 18)

Person.echo("hello")
a_guy.echo("im a guy")
Person.get_default_name()
a_guy.get_default_name()


