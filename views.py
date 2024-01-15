class TelaMain():
    def __init__(self):
        pass

    def menu(self):
        print("____________________________")
        print("| Bem-vindo!               |")
        print("| Qual opção deseja?       |")
        print("| 1 -> create form         |")
        print("| 2 -> read form           |")
        print("| 3 -> update form         |")
        print("| 4 -> delete form         |")
        print("| 5 -> Sair                |")
        print("|__________________________|")

    def pedir_comando(self):
         return int(input(" - Digite o comando: "))

class TelaCreateForms():
    def __init__(self):
        pass

    def menu(self):
        print("____________________________")
        print("| Bem-vindo!               |")
        print("| Qual opção deseja?       |")
        print("| 1 -> Ponto               |")
        print("| 2 -> Linha               |")
        print("| 3 -> Circulo             |")
        print("| 4 -> Triangulo           |")
        print("| 5 -> Poligono            |")
        print("| 6 -> Sair                |")
        print("|__________________________|")

    def pedir_comando(self):
        return int(input("esolha uma opção : "))