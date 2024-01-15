from views import TelaMain, TelaCreateForms
from models import Point, Line, Circle, Polygon, Triangle
from controller import CartesianBoard

telaform = TelaCreateForms()
telamain = TelaMain()
carte=CartesianBoard()

comando = -1
while comando != 5:
    telamain.menu()
    comando = telamain.pedir_comando()


    match comando:
        case 1:
            telaform.menu()
            opcao = int(telaform.pedir_comando())
            
            match opcao :
                case 1:
                
                    carte.criar_inserir_ponto()
                

                case 2:
                    carte.criar_inserir_linha()
                
                    pass

                case 3:
                    carte.criar_inserir_circulo()
                    pass
                
                case 4:
                    carte.criar_inserir_triangulo()
                case 5:
                    carte.criar_inserir_poligono()

                    pass

                

        case 2:
            print("Qual opção deseja ler?")
            telaform.menu()
            opcao = int(telaform.pedir_comando())
            
            match opcao :
                case 1:
                    print("Pontos:")
                    carte.showPontos()
                    pass

                case 2:
                    print("Linhas:")
                    carte.showLines()
                    pass

                case 3:
                    print("Circulos:")
                    carte.showCircles()
                    pass
                
                case 4:
                    print("Triangulos:")
                    carte.showTriangles()
                    pass

                case 5:
                    print("Poligonos:")
                    carte.showPolygons()
                    pass

        case 3:
            print("Qual opção deseja atualizar?")
            telaform.menu()
            opcao = int(telaform.pedir_comando())
            
            match opcao :
                case 1:
                    #o que deseja atualizar
                    pass

                case 2:
                    #o que deseja atualizar
                    pass

        case 4:
            print("Qual opção deseja deletar?")
            telaform.menu()
            opcao = int(telaform.pedir_comando())
            
            match opcao :
                case 1:
                    ponto_deletar = input("Qual ponto deseja deletar?")
                    carte.removePonto(ponto_deletar)
                    print("Ponto deletado com sucesso!")
                    pass
                case 2: 
                    line_deletar = input("Qual linha deseja deletar?")
                    carte.removeLine(line_deletar)
                    print("Linha deletada com sucesso!")
                    pass

                case 3:
                    circulo_deletar = input("Qual circulo deseja deletar?")
                    carte.removeCircle(circulo_deletar)
                    print("Circulo deletado com sucesso!")
                    pass

                case 4:
                    triangulo_deletar = input("Qual triangulo deseja deletar?")
                    carte.removeTriangle(triangulo_deletar)
                    print("Triangulo deletado com sucesso!")
                    pass

                case 5:
                    poligono_deletar = input("Qual poligono deseja deletar?")
                    carte.removePolygon(poligono_deletar)
                    print("Poligono deletado com sucesso!")
                    pass
        case 5 :
            print("Saindo...")
            exit()
        case _:
            print("Comando inválido, digite outro número válido")
            
