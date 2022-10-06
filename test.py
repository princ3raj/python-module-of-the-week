class Random:
    def first_name(self, firstName):
        self.firstName = firstName
        return self

    def last_name(self, lastName):
        self.lastName = lastName
        return self 

    def full_name(self):
        return f"{self.firstName} {self.lastName}"










class A:
    def fun(self):
        print("A")

class B:
    def fun(self):
        print("B")

class C:
    def fun(self):
        print("C")



class D:
    def __init__(self):
        A().fun()
        B().fun()
        C().fun()


if __name__ == "__main__":
    print(Random().first_name("Prince").last_name("Raj").full_name())
