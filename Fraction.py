class Fraction:
    def __init__(self, x=0, y=1):
        self.num = x
        if y!=0:
            self.den=y
        else:
            self.den=1
    def convert_decimal(self):
        return self.num/self.den
    def __str__(self):
        return f"{self.num}/{self.den}"
    def __add__(self, other):
        n = self.num * other.den + other.num * self.den
        d = self.den * other.den
        return Fraction(n, d)
    def __gt__(self, other):
        return self.num * other.den > other.num * self.den
    # def simplify(self):
    #     self.com_factor=self.common_factor(self.num, self.den)
    #     self.num = int(self.num/self.com_factor)
    #     self.den = int(self.den/self.com_factor)
    #     return f"{self.num}/{self.den}"
    # @staticmethod
    # def common_factor(x, y):
    #     if x > y:
    #         count = 0
    #         for i in range(1, x):
    #             if x % i == 0 and y % i == 0:
    #                 count = i
    #     else:
    #         count = 0
    #         for i in range(1, y):
    #             if x % i == 0 and y % i == 0:
    #                 count = i
    #     return count
    def simplify(self):
        self.all_factors = self.factors(self.num, self.den)
        self.com_factor = self.common_factor(self.all_factors[0], self.all_factors[1])
        self.num = int(self.num / self.com_factor)
        self.den = int(self.den/self.com_factor)
        return f"{self.num}/{self.den}"
    @staticmethod
    def factors(x, y):
        a=[]
        b=[]
        for i in range(1, x+1):
            if x % i == 0:
                a.append(i)
        for j in range(1, y+1):
            if y % j == 0:
                b.append(j)
        return a, b

    @staticmethod
    def common_factor(x, y):
        count=0
        for i in x:
            if i in y:
                count=i
        return count


f1=Fraction(80, 2)
print(f1.convert_decimal())
print("************************")
print(str(f1))
print("************************")
f2=Fraction(2, 4)
f3 = (f1.__add__(f2))
print(f3)
print(f3.convert_decimal())
print("************************")
print(f1>f2)
print("************************")
print(f1.simplify())



# try:
#     amount=int(input("Enter the amount:"))
#     if amount<100:
#         raise ValueError("Amount must be greater than 100")
#     sharer=int(input("Enter the number of sharers:"))
#     print("The total is", amount/sharer)
# except ValueError as e1:
#     print(e1)
#     print(TypeError,":",e1)
#
# except ZeroDivisionError as e2:
#     print(e2)
#     print(ZeroDivisionError,":",e2)
#
# except:
#     print("SOMETHING IS WRONG")

# from logging import *
# basicConfig(level=DEBUG,filename='Value.log', filemode="w",\
#             format="%(asctime)s - %(levelname)s:%(name)s:%(message)s")
# try:
#   value=int(input('Enter a value to be logged:'))
#   l=getLogger("Hellow")
#   l.debug(value)
# except Exception as e1:
#   l=getLogger("Mellow")
#   l.error(f"Error \n {e1}")
#
# class Vehicle:
#     def __init__(self, nw, c, mn):
#         self.__noOfWheels = nw
#         self.__color = c
#         self.__modelNo=mn
#     def set_nw(self, nw):
#         self.__noOfWheels = nw
#     def get_nw(self):
#         return self.__noOfWheels
#     def set_c(self, c):
#         self.__color = c
#     def get_c(self):
#         return self.__color
#     def set_mn(self, mn):
#         self.__modelNo = mn
#     def get_mn(self):
#         return self.__modelNo
# v = Vehicle(3, "red", "42")
# print(v.get_mn())


