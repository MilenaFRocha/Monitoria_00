from models import Point, Line, Circle, Polygon, Triangle
import json

     
class CartesianBoard():


    
    
    def __init__(self):
        
        self.pontos= {}
        self.lines= {}
        self.circles= {}
        self.triangles={}
        self.polygons= {}
        




    def inserPonto(self, ponto : Point):

        self.pontos[ponto.nome]= ponto
        

        lista_pontos = []

        # Abrir o arquivo JSON para leitura
        with open(r'C:\Users\milen\OneDrive\Documentos\Monitoria (teórica)\Projeto 1\database.json', 'r') as json_file:
            # Carregar os dados existentes do arquivo
           lista_pontos = json.load(json_file)

        


        # Criar um novo objeto Point
       

        # Adicionar um campo 'id' ao dicionário representando o número de identificação
        ver = vars(ponto)
        ver['id'] = len(lista_pontos) + 1  # Assume que os IDs começam de 1 e aumentam
        ver['_Point__nome'] = "ponto" + str(ver['id'])
        # Adicionar o dicionário à lista
        lista_pontos.append(ver)

        # Abrir o arquivo JSON para escrita
        with open('contagem.json', 'w') as count_file:
            json.dump(Point.count, count_file)

        with open(r'C:\Users\milen\OneDrive\Documentos\Monitoria (teórica)\Projeto 1\database.json', 'w') as json_file:
            # Escrever os dados atualizados de volta ao arquivo
            json.dump(lista_pontos, json_file, indent=2)
                

    def criar_inserir_ponto(self):
        x = Point.pedir_x()
        y = Point.pedir_y()
      
        ponto = Point(x, y)
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