from GeometricObject import GeometricObject
class Circle(GeometricObject):
    def __init__(self, radius = 1.00, color = "green", filled = True):
        super().__init__(color = color, filled = filled)
        self.__radius = radius
    def getRadius(self):
        return self.__radius
    def setRadius(self,radius):
        self.__radius = radius
    def getArea(self):
        return 22/7 * self.__radius**2
    def getPerimeter(self):
        return 2 * 22/7 * self.__radius
    def getDiameter(self):
        return 2 * self.__radius
    def __str__(self):
        return "Circle[ color:{}, filled:{}, radius:{}, area:{}, circumference:{}, diameter:{}]".format(GeometricObject.getColor(self),GeometricObject.isFilled(self) ,self.__radius, self.getArea(),self.getPerimeter(),self.getDiameter())
