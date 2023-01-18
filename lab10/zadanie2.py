class Wektor3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, Wektor3D):
            self.x = self.x + other.x
            self.y = self.y + other.y
            self.z = self.z + other.z
            return self
        else:
            print('Dodaj wektor!')        

    def __sub__(self, other):
        if isinstance(other, Wektor3D):
            self.x = self.x - other.x
            self.y = self.y - other.y
            self.z = self.z - other.z
            return self           
        else:
            print('Odejmij wektor!')

    def __mul__(self, value):
        self.x = self.x * value
        self.y = self.y * value
        self.z = self.z * value
        return self

    def mnozenie_skalarnie(self, other):
        return (self.x * other.x + self.y * other.y + self.z * other.z)

    def mnozenie_wektorowe(self, other):
        x = self.x
        y = self.y
        z = self.z

        self.x = y*other.z - z*other.y
        self.y = z*other.x - x*other.z
        self.z = x*other.y - y*other.x

        return self

    
    def dlugosc_wektora(self):
        import math
        return math.sqrt(mnozenie_skalarnie(self, self))

    def mnozenie_mieszane(self, other, other1):
        return self.mnozenie_wektorowe(other).mnozenie_skalarnie(other1)


    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'

def fun1(w1,w2):
    return w1.mnozenie_skalarnie(w2)

def fun2(w1, w2, w3, q):
    return (w2.mnozenie_wektorowe(w3) + w1) * q

def fun3(w1, w2, q):
    return (w1*q).mnozenie_skalarnie(w2)