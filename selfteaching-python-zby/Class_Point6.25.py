#实现类Point
#使其满足
#1.二维空间
#2.实现方法reflect_x 和reflect_y, 分别返回按X/Y轴进行对称的点
#3.实现横纵坐标的 setter 和 getter


class Point():
    '''Create a new Point, at coordinates x and y.'''

    def __init__(self, x = 0, y = 0):
        '''Create a new point at x, y'''
        self.x = x
        self.y = y
#Add a method reflect_x to Point which returns a new Point, 
#one which is the reflection of the point about the x-axis. 
#For example, Point(3, 5).reflect_x() is (3, -5)
    def reflect_x(self):
        return -self.x
    def reflect_y(self):
        return -self.y


    def distance_from_origin(self):
        ''' Computer my distance from the origin '''
        return ((self.x **2) + (self.y **2)) **0.5

    
p = Point(3, 4)
print(p.x)
print(p.y)

z = p.distance_from_origin()
print(int(z))



import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distanceFromPoint(self, otherP):
        dx = (otherP.getX() - self.x)
        dy = (otherP.getY() - self.y)
        return math.sqrt(dy**2 + dx**2)

p = Point(3, 3)
q = Point(6, 7)
print(p.distanceFromPoint(q))






#实现类 Circle
#使其满足
#1.基于上述 Point类，记录圆心
#2.记录半径-为它实现area 方法，返回其面积
#3.实现方法 reflect_x 和 reflect_y, 分别返回按X/Y轴进行对称的圆







#写一个斐波那契数列迭代器