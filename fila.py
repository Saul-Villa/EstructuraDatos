import os

os.system('cls' if os.name == 'nt' else 'clear')
#En el uso cotidiano, una fila se refieree a una
#secuencia de personas u objetos dispuestos en una linea,
#esperando su trurno para se atendidos o procesados.

#Al igual que una cola en informatica, sigue el principio FIFO,
#donde la primera persona u objetos en la linea sera el primero
#ser atendido.

#Este termino es menos tecnico y mas utilizado en contextos
#cotidianos o en la modelizacion de sistemas de esperando
#en la teoria de las cosas
i = 0
fila = []

fila.append('cliente1')
fila.append('cliente2')
fila.append('cliente3')

print("Los elementos de la fila son : ", fila)

for Clientes in fila:
        clienteAtendido = Clientes
        i = i+1
        print("Cliente atendido fue: ", clienteAtendido)
        print("Fila despues de atender al cliente son: ", fila[i-1:])
