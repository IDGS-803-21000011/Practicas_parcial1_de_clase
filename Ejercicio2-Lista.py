class Lista:
    listaRecibida = []

    def __init__(self, listaRecibida):
        self.listaRecibida = listaRecibida

    def ordenarLista(self):
        self.listaRecibida.sort()

    def mostrarParesImpares(self):
        listaPares = []
        listaImpares = []
        for i in self.listaRecibida:
            if i % 2 == 0:
                listaPares.append(i)
            else:
                listaImpares.append(i)
        return (listaPares, listaImpares)

    def buscarRepetidos(self):
        valoresRepetidos = []
        for i in self.listaRecibida:
            if i not in valoresRepetidos:
                repeticion = self.listaRecibida.count(i)
                if repeticion >= 2:
                    print("El número {} se repitió {} veces.".format(i, repeticion))
                valoresRepetidos.append(i)

def main():
    lista = [10, 20, 25, 10, 11, 8, 8, 9, 11, 12, 8]
    objLista = Lista(lista)

    objLista.ordenarLista()
    print("Lista ordenada es: {}".format(objLista.listaRecibida))

    tuplaListas = objLista.mostrarParesImpares()
    print("La lista de números pares es: {}".format(tuplaListas[0]))
    print("La lista de números impares es: {}".format(tuplaListas[1]))

    objLista.buscarRepetidos()

if __name__ == "__main__":
    main()
