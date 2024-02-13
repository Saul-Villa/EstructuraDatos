import os
os.system('cls' if os.name == 'nt' else 'clear')

class Cola:

    #En informatica
    elementos = []

    def _init_(self):
        self.elementos= []

    def encolar(self, item):
        self.elementos.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        else:
            raise IndexError("Desencolar de una cola vacía")
    def esta_vacia(self):
        return len(self.elementos) == 0
    def printfirst(self, index):
        print("Elemento colocado", elementos[index])
#Uso fuera de la investigacion
cola = Cola()
for i in range (15):
    cola.encolar("elemento "+ str(i))
    cola.printfirst(int(i))
for i in cola.elementos:
    print("Elemento desencolado", cola.desencolar())
