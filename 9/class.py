class C:
    s = 3.142
    def __init__(self, x = 0):
        self.x = x

    def __str__(self):
        return f"(x = {self.x}, s = {self.s})"


o1 = C(5)
o2 = C(9)

print(o1)
print(o2)

o1.s = 2.718

print(o1)
print(o2)
