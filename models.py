class Point():

    def __init__(self, x: int, y: int, n: int):
        self.__x = x
        self.__y = y
        self.__n = n
        

    @property
    def coordinates(self):
        return (self.__x, self.__y)

    @coordinates.setter
    def coordinates(self, coordinates):
        self.__x, self.__y = coordinates

    @property
    def n(self):
        return self.__n
    
    @n.setter
    def n(self, n):
        self.__n = n

    @classmethod
    def pedir_x(self):
        return int(input("Digite o x do ponto: "))
    
    @classmethod
    def pedir_y(self):
        return int(input("Digite o y do ponto:"))
    
    @classmethod #nao preciso do ponto instanciado
    def pedir_n(self):
        return int(input("Digite o n do ponto: "))

    def distance(self):
        return (self.__x**2 + self.__y**2)**0.5
    
    #print(ponto) -> Point(1,2,1)
    def __str__(self):
        return f'Point-{self.__n} has ({self.__x},{self.__y})'
    
    #como colocar que o otherpoint é um point?
    def distance_to(self, other_point: 'Point'):
        return ((self.__x - other_point.__x)**2 + (self.__y - other_point.__y)**2)**0.5
    
    def distance_from_origin(self):
        origin = Point(0,0,0)
        return self.distance_to(origin)
    
    def equal_another(self, other_point: 'Point'):
        return self.__x == other_point.__x and self.__y == other_point.__y
    
class Line():
    def __init__(self, point1: 'Point', point2: 'Point',n: int):
        self.__point1 = point1
        self.__point2 = point2
        self.__n = n
        self.linhas = {}

    @property
    def points(self):
        return (self.__point1, self.__point2)
    
    @points.setter
    def points(self, points):
        self.__point1, self.__point2 = points

    @property
    def n(self):
        return self.__n
    
    @n.setter
    def n(self, n):
        self.__n = n

    @classmethod
    def pedir_ponto_X_1(self):
        return int(input("Digite o x primeiro ponto: "))
    
    @classmethod
    def pedir_ponto_Y_1(self):
        return int(input("Digite o y primeiro ponto: "))
    
    @classmethod
    def pedir_ponto_X_2(self):
        return int(input("Digite o x segundo ponto: "))
    
    @classmethod
    def pedir_ponto_Y_2(self):
        return int(input("Digite o y segundo ponto: "))
    
    @classmethod
    def pedir_ponto2(self):
        return int(input("Digite o segundo ponto: "))
    
    @classmethod #nao preciso do ponto instanciado
    def pedir_n(self):
        return int(input("Digite o n da linha: "))



    def length(self):
        return round(self.__point1.distance_to(self.__point2), 2)
    
    #usa o str do ponto para printar
    def __str__(self):
        return f'Line-{self.__n} has ({self.__point1},{self.__point2})'
    
    def equation(self):
        a = round((self.__point1.coordinates[1] - self.__point2.coordinates[1]) /
                  (self.__point1.coordinates[0] - self.__point2.coordinates[0]), 2)
        b = round(self.__point1.coordinates[1] - a * self.__point1.coordinates[0], 2)
        return f'y = {a}x + {b}'

class Circle():
    def __init__(self, center: 'Point', radius: int, n: int):
        self.__center = center
        self.__radius = radius
        self.__n = n
        self.circulos = {}

    @property
    def center(self):
        return f' O circulo tem o seu centro  {self.__center}'

    @center.setter
    def center(self, center):
        self.__center = center

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    @property
    def n(self):
        return self.__n
    
    @n.setter
    def n(self, n):
        self.__n = n

    @classmethod
    def pedir_ponto(self):
        return int(input("Digite o ponto: "))
    
    @classmethod
    def pedir_raio(self):
        return int(input("Digite o raio: "))
    
    @classmethod #nao preciso do ponto instanciado
    def pedir_n(self):
        return int(input("Digite o n do circulo: "))


    def area(self):
        return round(3.14 * self.__radius ** 2, 2)

    def length(self):
        return round(2 * 3.14 * self.__radius, 2)

    def __str__(self):
        return f'Circle has ({self.__center},{self.__radius})'

    def is_inside(self, point: 'Point'):
        return self.__center.distance_to(point) <= self.__radius
    
# lista de linhas
from typing import List

class Polygon():
    def __init__(self, lines: List['Line'], n: int):
        self.__lines = lines
        self.__n = n
        self.poligonos = {}

    @property
    def lines(self) -> List['Line']:
        return self.__lines

    @lines.setter
    def lines(self, lines: List['Line']):
        self.__lines = lines

    @property
    def n(self) -> int:
        return self.__n

    @n.setter
    def n(self, n: int):
        self.__n = n

    @classmethod
    def pedir_lista_linhas(self):
        return int(input("Digite o x do ponto: "))
    
    @classmethod #nao preciso do ponto instanciado
    def pedir_n(self):
        return int(input("Digite o n do poligono: "))


    def length(self) -> float:
        total_length = 0
        for line in self.__lines:
            total_length += line.length()
        return round(total_length, 2)

    def __str__(self) -> str:
        return f'Polygon-{self.__n} has {len(self.__lines)} lines'