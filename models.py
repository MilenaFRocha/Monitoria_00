from typing import List

class Point:
    

    def __init__(self, x: int, y: int):
        
        self.__x = x
        self.__y = y
        
    
 
    
    def to_json(self):
        return {'x': self.__x, 'y': self.__y}
    
    @classmethod
    def pedir_x(self):
        return int(input("Digite o x do ponto: "))
    
    @classmethod
    def pedir_y(self):
        return int(input("Digite o y do ponto:"))
    
    @classmethod
    def criar_forma(self):
        x = Point.pedir_x()
        y = Point.pedir_y()
        ponto = Point(x,y)
        return ponto
    
 

    @property
    def coordinates(self):
        return (self.__x, self.__y)

    @coordinates.setter
    def coordinates(self, coordinates):
        self.__x, self.__y = coordinates

    @property   
    def nome(self):
        return self.__nome
    
    @classmethod
    def type(self):
        return 'Point'
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    
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
    

    def __init__(self, point1: 'Point', point2: 'Point'):
        
        self.__point1 = point1
        self.__point2 = point2
        
        
    @classmethod
    def type(self):
        return 'Line'
    
    def to_json(self):
        return {
            'ponto1': self.__point1.to_json(),
            'ponto2': self.__point2.to_json(),
            'nome': self.__nome,  # Não chamamos to_json() aqui, pois presume-se que __nome seja uma string
        }
    
    def criar_forma(self):
         ponto1 = self.criar_ponto()
         ponto2 = self.criar_ponto()
         linha = Line(ponto1, ponto2)
         return linha
    
    @property
    def points(self):
        return (self.__point1, self.__point2)
    
    @points.setter
    def points(self, points):
        self.__point1, self.__point2 = points

    
    @classmethod
    def pedir_ponto2(self):
        return int(input("Digite o segundo ponto: "))
    
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
    

    def __init__(self, center: 'Point', radius: int):
        self.__center = center
        self.__radius = radius
        

    def criar_forma(self):
        ponto1 = self.criar_ponto()
        raio = Circle.pedir_raio()
        circulo = Circle(ponto1, raio)
        return circulo
    @classmethod
    def type(self):
        return 'Circle'
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

    # @property   
    # def id(self):
    #     return self.__id

    
    @classmethod
    def pedir_ponto(self):
        return int(input("Digite o ponto: "))
    
    @classmethod
    def pedir_raio(self):
        return int(input("Digite o raio: "))
    
    def area(self):
        return round(3.14 * self.__radius ** 2, 2)

    def length(self):
        return round(2 * 3.14 * self.__radius, 2)

    def __str__(self):
        return f'Circle has ({self.__center},{self.__radius})'

    def is_inside(self, point: 'Point'):
        return self.__center.distance_to(point) <= self.__radius
    

class Triangle():
        
    

    def __init__(self, point1: 'Point', point2: 'Point', point3: 'Point'):
        self.__point1 = point1
        self.__point2 = point2
        self.__point3 = point3
      
    @classmethod
    def type(self):
        return 'Triangle'
    
    def criar_forma(self):
        ponto1 = self.criar_ponto()
        ponto2 = self.criar_ponto()
        ponto3 = self.criar_ponto()
        triangulo = Triangle(ponto1,ponto2,ponto3)
        return triangulo   
    
    def __str__(self):
        return f'Triangle{self.__n} has ({self.__point1},{self.__point2},{self.__point3})'
    
    @property
    def points(self):
        return (self.__point1, self.__point2, self.__point3)
    
    @points.setter
    def points(self, points):
        self.__point1, self.__point2, self.__point3 = points

    # property   
    # def id(self):
    #     return self.__id

    
    
  
      

# triagulo = Triangle(Point(1,2,1), Point(2,3,2), Point(3,4,3), 1)
# print(triagulo)
# triagulo.points = Point(1,1,1), Point(2,2,2), Point(3,3,3)

# print(triagulo)

    
# lista de linhas

class Polygon:
    def __init__(self, pontos):
        if isinstance(pontos, dict):
            # Se pontos for um dicionário, convertemos seus valores em objetos Point
            self.__pontos = [Point(x, y) for x, y in pontos.items()]
        else:
            # Se não for um dicionário, assumimos que é um iterável de objetos Point
            self.__pontos = list(pontos)
    @classmethod
    def type(self):
        return 'Polygon'
    def criar_forms(self):
        pontos =[]
        numero = int(input("Quantos lados tem o poligono?"))
        for i in range(numero):
            ponto =self.criar_ponto()
            pontos.append(ponto)
        poligono = Polygon(pontos)
        return poligono
        
       
    @property
    def pontos(self) -> List['Point']:
        return self.__pontos

    @pontos.setter
    def pontos(self, pontos: List['Point']):
        self.__pontos = pontos

   

    
    @classmethod
    def pedir_lista_linhas(self):
        return int(input("Digite o x do ponto: "))

    def length(self) -> float:
        total_length = 0
        for line in self.__lines:
            total_length += line.length()
        return round(total_length, 2)

    def __str__(self) -> str:
        return f'Polygon-{self.__n} has {len(self.__lines)} lines'