# interface in java is given like these
# interface:
# def xyz(a,b):
#     pass
# def abc(a):
#     pass


# #INTERFACE IN PYTHON
# from abc import ABC,abstractmethod
# class Shape(ABC): # ABSTRACT CLASS
#     @abstractmethod
#     def area(self):
#         pass   # ABSTRACT METHOD
#     def greet(self):
#         print("I am a shape")
# class Circle(Shape):  #Concrete class(normal class) inheriting abstrct class
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):  #This is like method overriding but not....here the resposibility of circle should define all the abstract function body also
#         return 3.14 * self.radius * self.radius
# class Rectangle(Shape):
#     def __init__(self,l,w):
#         self.length=l
#         self.width=w
#     def area(self):
#         return self.length*self.width
#
# # shape=Shape() ERROR: WE CANT INSTANTIATE ABSTRACT CLASS
# circle=Circle(5)
# circle.greet() # inherited concrete method
# print("Area:",circle.area())  #Overirdden abstract method
# Rect=Rectangle(5,6)
# print("Rectangle Area:",Rect.area())


