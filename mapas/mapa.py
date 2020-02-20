from listas import lista_ligada

class Mapa():
    def __init__(self):
        self.__elementos = lista_ligada.ListaLigada()
        self.__numero_categorias = 10

        for i in range(self.__numero_categorias):
            self.__elementos.inserir(lista_ligada.ListaLigada())

    def gerar_numero_espalhamento(self, chave):
        return hash(chave) % self.__numero_categorias