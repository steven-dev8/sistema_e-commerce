class Teste:
    def metodo1(self):
        self.metodo2()
    
    def metodo2(self):
        print("Método 2 chamado")
    
    def metodo3(self):
        print("Método 3 chamado")

# Exemplo de uso:
obj = Teste()
obj.metodo1()
