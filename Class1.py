# class abc():
#     def __init__(self, a):
#         self.__a = a  #Instance variable
#     stat=10 #Static variable

#     def add(self, s):
#         s=s+10
#         return s

# obj=abc('Buddy')
# print(obj._abc__a)
# print(obj.a)
# print(abc.stat)
# s_new = abc.stat
# b=obj.add(s_new)
# print(b)


#Inheritance
# class A:
#     def __init__(self):
#         print("In A")

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("In B") 

#     def buy(self):
#         print("Hello")
        
# class C(B):
#     def __init__(self):
#         super().__init__()
#         print("In C")

#a=A()
#b=B()
#c=C()

#Encapsulation
# class Customer:
#     def __init__(self, cust_id, name, age,wallet_balance):
#         self.cust_id = cust_id
#         self.name = name
#         self.age = age
#         self.__wallet_balance = wallet_balance

#     def update_balance(self, amount):
#         if amount < 1000 and amount> 0:
#             self.__wallet_balance += amount

#     def show_balance(self):
#         print ("The balance is ",self.__wallet_balance)

# c1=Customer(100, "Gopal", 24, 1000)
# c1._Customer__wallet_balance = 10000000000
# c1.show_balance()



























































