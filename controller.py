from models import Point, Line, Circle, Polygon, Triangle

class CartesianBoard():


    
    
    def __init__(self):
        
        self.pontos= {}
        self.lines= {}
        self.circles= {}
        self.triangles={}
        self.polygons= {}
        
    

    def inserPonto(self, ponto : Point):
        
        self.pontos["ponto" + str(ponto.n)]= ponto

    def criar_inserir_ponto(self):
        x = Point.pedir_x()
        y = Point.pedir_y()
        n = Point.pedir_n()
        ponto = Point(x, y, n)
        self.inserPonto(ponto)
        return ponto 

    def inserLine(self, line : Line):
            
        self.lines["line" + str(line.n)]= line
    
    def inserCircle(self, circle : Circle):
                
        self.circles["circle" + str(circle.n)]= circle

    def inserTriangle(self, triangle : Triangle):
                        
        self.triangles["triangle" + str(triangle.n)]= triangle  

    def inserPolygon(self, polygon : Polygon):
                    
        self.polygons["polygon" + str(polygon.n)]= polygon
        
        
    def removePonto(self, nome):
        
        del self.pontos[nome]

    def removeLine(self, nome):
            
        del self.lines[nome]
    
    def removeCircle(self, nome):
        
        del self.circles[nome]

    def removeTriangle(self, nome):
            
            del self.triangles[nome]
    
    def removePolygon(self, nome):
        
        del self.polygons[nome]
        
        
    def showPontos(self):
        
        print('\nEste plano cartesiano possui os seguintes pontos:\n')
        for ponto in self.pontos.keys():
            print(ponto)
    
    def showLines(self):
        
        print('\nEste plano cartesiano possui as seguintes linhas:\n')
        for line in self.lines.keys():
            print(line)

    def showCircles(self):
            
            print('\nEste plano cartesiano possui os seguintes circles:\n')
            for circle in self.circles.keys():
                print(circle)
    def showTriangles(self):
                
                print('\nEste plano cartesiano possui os seguintes triangles:\n')
                for triangle in self.triangles.keys():
                    print(triangle)

    def showPolygons(self):

            print('\nEste plano cartesiano possui os seguintes polygons:\n')
            for polygon in self.polygons.keys():
                print(polygon)

    # def printDetails(self):
        
    #     for key in self.pontos.keys():
    #         self.pontos[key].printCoord()
    
        
    # def getShape(self,key):
    #     return self.shapes[key]