
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


    def inserir_forma(self, forma,caminho):
        lista_formas = self.abrir_json(caminho)
        converter = vars(forma)
        lista_formas.append(converter)
        converter['id'] = len(lista_formas) + 1
        converter[f'_{forma}__nome'] = f"{forma}" + str(converter['id'])
        self.salvar_json(lista_formas,caminho)
        return forma
    
    
    def criar_inserir_forma(self, classe,caminho):
            forma = classe.criar_forma()
            self.inserir_forma(forma,caminho)
            return forma
            
        
    def remove_forma(self, caminho, classe_forma,nome):
        lista_formas = self.abrir_json(caminho)
        for i in range(len(lista_formas)):
             if lista_formas[i][f'_{classe_forma}__nome'] == nome:
                  del lista_formas[i]     
                  break
        self.salvar_json(lista_formas,caminho)

    def show_form(self, caminho, classe_forma):
        lista_formas = self.abrir_json(caminho)
        for forma in lista_formas:
            print(forma[f'_{classe_forma}__nome'])


  