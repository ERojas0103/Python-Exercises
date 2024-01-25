class bark:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f"{self.name} says alalala and her age is {self.age}")


dog1 = bark("rollie", 25)
dog1.shout()
