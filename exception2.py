class NonPositiveError(ArithmeticError):
    pass


class PositiveList(list):
    def append(self, x):
        if x > 0:
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError()
x = PositiveList()
x.append(1)
print(x)
x.append(3)
print(x)
x.append(-3)
print(x)
