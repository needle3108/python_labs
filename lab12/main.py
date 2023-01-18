print("ZADANIE 1")

class Wspolrzedne:
    def __init__(self):
        self.a = 0
        self.b = 0

    @property
    def a(self):
         return self._a

    @property
    def b(self):
        return self._b

    @a.setter
    def a(self, w):
        self._a = w 

    @b.setter
    def b(self, w):
        self._b = w 

    @a.getter
    def a(self):
        return self._a

    def b(self):
        return self._b

print("\nKlasa zostala utworzona :)")

print("\nZADANIE 2")

point1 = Wspolrzedne()
point1.b = 2

point2 = Wspolrzedne()
point2.a = 2
point2.b = 2

def range(a, b):
    def dec(pf):
        def fz(p1, p2):
            for i in (p1.a, p1.b, p2.a, p2.b):
                if i<a or b<i:
                    raise ValueError
                else:
                    return pf(p1,p2)
        return fz
    return dec

@range(0,7)
def add(p1, p2):
    wynik = Wspolrzedne()
    wynik.a = point1.a + point2.a
    wynik.b = point1.b + point2.b
    return wynik

@range(0,7)
def sub(p1, p2):
    wynik = Wspolrzedne()
    wynik.a = point1.a - point2.a
    wynik.b = point1.b - point2.b
    return wynik        

point_add = add(point1, point2)
point_sub = sub(point1, point2)

print("Punkt po dodaniu punktow = ", point_add.a, point_add.b)
print("Punkt po odjeciu punktow = ", point_sub.a, point_sub.b)


print("\nZADANIE 3")

from math import sqrt

class Oblicz:
    @staticmethod
    def Heron(p1, p2, p3):
        a = sqrt(pow(p1.a - p2.a, 2) + pow(p1.b - p2.b, 2))
        b = sqrt(pow(p2.a - p3.a, 2) + pow(p2.b - p3.b, 2))
        c = sqrt(pow(p1.a - p3.a, 2) + pow(p1.b - p3.b, 2))
        p = (a + b +c)/2
        return sqrt(p*(p-a)*(p-b)*(p-c))

    @staticmethod
    def Brah(p1, p2, p3, p4):
        a = sqrt(pow(p1.a - p2.a, 2) + pow(p1.b - p2.b, 2))
        b = sqrt(pow(p2.a - p3.a, 2) + pow(p2.b - p3.b, 2))
        c = sqrt(pow(p3.a - p4.a, 2) + pow(p3.b - p4.b, 2))    
        d = sqrt(pow(p1.a - p4.a, 2) + pow(p1.b - p4.b, 2))
        p = (a + b + c + d) / 2
        return sqrt((p-a)*(p-b)*(p-c)*(p-d))
    
    @staticmethod
    def obwod(*points):
        if len(points) == 3:
            a = sqrt(pow(points[0].a - points[1].a, 2) + pow(points[0].b - points[1].b, 2))
            b = sqrt(pow(points[1].a - points[2].a, 2) + pow(points[1].b - points[2].b, 2))
            c = sqrt(pow(points[0].a - points[2].a, 2) + pow(points[0].b - points[2].b, 2))
            return a + b + c
        elif len(points) == 4:
            a = sqrt(pow(points[0].a - points[1].a, 2) + pow(points[0].b - points[1].b, 2))
            b = sqrt(pow(points[1].a - points[2].a, 2) + pow(points[1].b - points[2].b, 2))
            c = sqrt(pow(points[2].a - points[3].a, 2) + pow(points[2].b - points[3].b, 2)) 
            d = sqrt(pow(points[0].a - points[3].a, 2) + pow(points[0].b - points[3].b, 2))
            return a + b + c + d 
        else:
            pass    

point3 = Wspolrzedne()
point3.a = 2

print("Pole trojkata = ", Oblicz.Heron(point1, point2, point3))
print("Obwod trojkata = ", Oblicz.obwod(point1, point2, point3))

point4 = Wspolrzedne()

print("\nPole czworokata = ", Oblicz.Brah(point1, point2, point3, point4))
print("Obwod czworokata = ", Oblicz.obwod(point1, point2, point3, point4))

print("\nZadanie 4")

class Count:
    value = {}

    def __init__(self, pf):
        self._pf = pf
        Count.value[pf.__name__] = 0 

    def __call__(self):
        Count.value[self._pf.__name__] += 1
        self._pf()

    def getValue():
        return Count.value

@Count
def func():
    print("d")

func() 

@Count
def fun():
    pass

fun()
fun()

print(Count.getValue())
