class A:
    def display(self):
        print('I am inside A class')


class B(A):
    def display1(self):
        print('I am inside B class')


class C(B):
    def display3(self):
        super().display()
        super().display1()
        print('I am inside C class')


D = C()
D.display3()
