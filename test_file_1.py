from selenium import webdriver
class Test_Cases_01:
    def test_1(self):
        a=8
        b=6
        mul=a*b
        print("Multiplication of a and b:",mul)
        if mul==48:
            assert True
        else:
            assert False

    def test_2(self):
        a=9
        b=2
        sub=a-b
        print("Substraction of a and b:",sub)
        if sub==7:
            assert True
        else:
            assert False

