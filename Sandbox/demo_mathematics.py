
class Mathematics:

    # class-wide attribute
    PI = 3.14159

    def __init__(self):
        self.number = 88

    def method1(self, x, y):
        print(self.number)
        return x ** y

    @classmethod
    def method2(cls, x, y):
        print(cls.PI)
        return x ** y

    @staticmethod
    def method3(x, y):
        print(Mathematics.PI)
        return x ** y

# --------

print(Mathematics.power(2, 5))