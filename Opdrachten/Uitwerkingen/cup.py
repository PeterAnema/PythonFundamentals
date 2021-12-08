class Cup:

    _slots_ = ('_color',
                 '_volume',
                 '_clean',
                 '_contents',
                 '_fluid')

    def __init__(self, color, volume):
        self._color = color
        self._volume = volume
        self._clean = True
        self._contents = 0
        self._fluid = None

    def __del__(self):
        print('Cleaning up broken cup')

    def __str__(self):
        return 'Cup info: ' + self.info()

    def fill(self, amount, fluid):
        self._contents += amount
        self._fluid = fluid

    def info(self):
        return f'A {self._color} cup of {self._volume}ml with {self._contents}ml of {self._fluid}'

    def drink(self, amount):
        if amount <= self._contents:
            self._contents -= amount
        elif self._contents == 0:
            print('The cup is empty')
        else:
            self._contents = 0
            print('Emptied the cup')

# ---------------------------------------

cup1 = Cup('black', 100)
cup2 = Cup('white', 200)

print(cup1.info())
print(cup2.info())

del cup2

cup1.drink(500)

print(cup1.info())

cup1.fill(100, 'coffee')

print(cup1.info())

cup1.drink(500)

print(cup1.info())

print(cup1)

print(dir(cup1))
