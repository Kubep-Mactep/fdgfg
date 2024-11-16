class IterableWithGenerator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self._generator()

    def _generator(self):
        for i in range(1, self.n + 1):
            yield i ** 2

iterable_object = IterableWithGenerator(45)

for value in iterable_object:
    print(value)