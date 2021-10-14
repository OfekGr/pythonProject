class Person:
    def __init__(self, name, age, children):
        self.name=name
        self.age=age
        self.children=children

    def show(self):
        print(f"name: {self.name} age: {self.age} number of children: {self.children}")

    def hasChildren(self):
        if self.children > 0:
            print("has children")
        else:
            print("doesn't have children")

    def ageGroup(self):
        if 0 < self.age <=18:
            print("Child")
        else:
            if 19 <= self.age <= 60:
                print("adult")
            else:
                if 61 <= self.age <=120:
                    print("senior")
                else:
                    print("not valid age")

# Information:
my_name=Person("ofek", 22, 0)
# Show information
my_name.show()
# Show if has children
my_name.hasChildren()
# Show agegroup
my_name.ageGroup()