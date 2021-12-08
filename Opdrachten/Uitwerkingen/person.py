class Person:

    def __init__(self, name, residence):
        self.name = name
        self.residence = residence

    def tell(self):
        print(f'My name is {self.name} and I live in {self.residence}')

    def move(self, new_residence):
        self.residence = new_residence

class Dog:

    def __init__(self, bread):
        self.bread = bread

    def bark(self):
        print("BLAF BLAF BLAF!!!")

    def tell(self):
        print("I'm a " + self.bread)

class Customer(Person, Dog):

    def __init__(self, name, residence, customer_number):
        Person.__init__(self, name, residence)
        Dog.__init__(self, "Terrier")
        self.customer_number = customer_number


# ---------

person = Person('Peter', 'Lhee')
person.tell()

customer = Customer('Jeroen', 'Eindhoven', 'VIP0001')
customer.tell()
customer.bark()