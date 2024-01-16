from models import Point, Line, Circle, Polygon, Triangle
import json


     
class CartesianBoard():



    def __init__(self, caminho_ponto, caminho_linha, caminho_circulo, caminho_triangulo, caminho_poligono):
        
        self.caminho_ponto = caminho_ponto
        self.caminho_linha = caminho_linha
        self.caminho_circulo = caminho_circulo
        self.caminho_triangulo = caminho_triangulo
        self.caminho_poligono = caminho_poligono
        pass

    
    def abrir_json(self,caminho):
        with open(caminho, 'r') as json_file:
            lista = json.load(json_file)
            return lista
        
        #caminho_do_arquivo = r'C:\Users\milen\OneDrive\Documentos\Monitoria (teórica)\Projeto 1\databasePolygon.json'

    def salvar_json(self,lista,caminho):
        with open(caminho,'w') as json_file:
            json.dump(lista, json_file, default=lambda obj: obj.to_json(), indent=2  )
    
    def criar_ponto(self):  
         x = Point.pedir_x()
         y = Point.pedir_y()
         ponto = Point(x,y)
         return ponto
    
    def inserir_ponto(self,ponto):
        lista_pontos = self.abrir_json(self.caminho_ponto)
        converter = vars(ponto)
        lista_pontos.append(converter)
        converter['id'] = len(lista_pontos) + 1  # Assume que os IDs começam de 1 e aumentam
        converter['_Point__nome'] = "ponto" + str(converter['id'])
        self.salvar_json(lista_pontos,self.caminho_ponto)
        
    def criar_inserir_ponto(self):
        ponto = self.criar_ponto()
        self.inserir_ponto(ponto)
        return ponto

    def criar_linha(self):
         ponto1 = self.criar_ponto()
         ponto2 = self.criar_ponto()
         linha = Line(ponto1, ponto2)
         return linha
    
    def inserir_linha(self,linha): 
        lista_linhas = self.abrir_json(self.caminho_linha)
        converter = vars(linha)
        lista_linhas.append(converter)
        converter['id'] = len(lista_linhas) + 1
        converter['_Line__nome'] = "linha" + str(converter['id'])
        self.salvar_json(lista_linhas,self.caminho_linha)

    def criar_inserir_linha(self):
        linha = self.criar_linha()
        self.inserir_linha(linha)
        return linha
    
    def criar_circulo(self):    
         ponto1 = self.criar_ponto()
         raio = Circle.pedir_raio()
         circulo = Circle(ponto1, raio)
         return circulo
    
    def inserir_circulo(self,circulo):
        lista_circulos = self.abrir_json(self.caminho_circulo)
        converter = vars(circulo)
        lista_circulos.append(converter)
        converter['id'] = len(lista_circulos) + 1
        converter['_Circle__nome'] = "circulo" + str(converter['id'])
        self.salvar_json(lista_circulos,self.caminho_circulo)

    def criar_inserir_circulo(self):
        circulo = self.criar_circulo()
        self.inserir_circulo(circulo)
        return circulo
    
    def criar_triangulo(self):
         ponto1 = self.criar_ponto()
         ponto2 = self.criar_ponto()
         ponto3 = self.criar_ponto()
         triangulo = Triangle(ponto1,ponto2,ponto3)
         return triangulo 
    
    def inserir_triangulo(self, triangulo):
         lista_triangulos = self.abrir_json(self.caminho_triangulo)
         converter = vars(triangulo)
         lista_triangulos.append(converter)
         converter['id']= len(lista_triangulos) +1 
         converter['_Triangle__nome'] = "triangulo" + str(converter['id'])
         self.salvar_json(lista_triangulos, self.caminho_triangulo)

    def criar_inserir_triangulo(self):
        triangulo = self.criar_triangulo()
        self.inserir_triangulo(triangulo)
        return triangulo 
                        
        

    def criar_Polygon(self):
        pontos =[]
        numero = int(input("Quantos lados tem o poligono?"))
        for i in range(numero):
            ponto =self.criar_ponto()
            pontos.append(ponto)
        poligono = Polygon(pontos)
        return poligono
    
    def inserir_poligono(self,poligono):
         
         lista_poligonos = self.abrir_json(self.caminho_poligono)
         converter = vars(poligono)
         lista_poligonos.append(converter)
         converter['id'] = len(lista_poligonos) +1
         converter['_Polygon__nome'] = "poligono" + str(converter['id'])
         self.salvar_json(lista_poligonos,self.caminho_poligono)

    def criar_inserir_poligono(self):
         
         poligono = self.criar_Polygon()
         self.inserir_poligono(poligono)
         return poligono


    
        
    
    def removePonto(self, nome):
        lista_pontos = self.abrir_json(self.caminho_ponto)
        nova_lista_pontos = [ponto for ponto in lista_pontos if ponto['_Point__nome'] != nome]
        self.salvar_json(nova_lista_pontos, self.caminho_ponto)

    def removeLine(self, nome):
        # Remove a linha do JSON de linhas
        lista_linhas = self.abrir_json(self.caminho_linha)
        for i in range(len(lista_linhas)):
            if lista_linhas[i]['_Line__nome'] == nome:
                del lista_linhas[i]

                break
        self.salvar_json(lista_linhas,self.caminho_linha)

    
    def removeCircle(self, nome):
        
        lista_circulos = self.abrir_json(self.caminho_circulo)
        for i in range(len(lista_circulos)):
             if lista_circulos[i]['_Circle__nome'] == nome:
                  del lista_circulos[i]

                  break
        self.salvar_json(lista_circulos,self.caminho_circulo)

    def removeTriangle(self, nome):
            
            lista_triangulos = self.abrir_json(self.caminho_triangulo)
            for i in range(len(lista_triangulos)):
                 if lista_triangulos[i]['_Triangle__nome'] == nome:
                      del lista_triangulos[i]
                      break
            self.salvar_json(lista_triangulos,self.caminho_triangulo)

    
    def removePolygon(self, nome):
        
        lista_poligonos = self.abrir_json(self.caminho_poligono)
        for i in range(len(lista_poligonos)):
             if lista_poligonos[i]['_Polygon__nome'] == nome:
                  del lista_poligonos[i]     
                  break
        self.salvar_json(lista_poligonos,self.caminho_poligono)
        
        
   

    def show_form(self, caminho, classe_forma):
        lista_formas = self.abrir_json(caminho)
        for forma in lista_formas:
            print(forma[f'_{classe_forma}__nome'])


  