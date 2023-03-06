class Animal:
    def legs(self):
        print("I have four lrgs")

    def fur(self):
        print("My body is covered with fur")


class Dog:
    def bark(self):
        print("The dog barks")

class Cat(Animal,Dog):
    def squick(self):
        print("The Cat jumps")

d = Cat()
d.bark()
d.legs()
d.fur()
d.squick()
