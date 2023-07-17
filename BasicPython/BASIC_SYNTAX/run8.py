class Person:
    name = "Person"
    
    def __init__(self, name = None):
        self.name = name


Phuc = Person("PHUC")

print("%s name is %s" % (Person.name, Phuc.name))

nick = Person()
nick.name = "Phuc"

print("%s name is %s" % (Person.name, nick.name))