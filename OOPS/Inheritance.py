class Animal:
    def __init__(self):
        self.no_eyes = 2

    def breathe(self):
        print("Animal can breathe")


class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Underwater")

    def swim(self):
        print("I know to swim")


fish1 = Fish()
fish1.swim()
fish1.breathe()
print(fish1.no_eyes)
