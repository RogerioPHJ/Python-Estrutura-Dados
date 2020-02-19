class Vetor():
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = [None] * tamanho
        self.__posicao = 0

    def inserir_elemento_posicao(self, elemento, posicao):
        self.__elementos[posicao] = elemento

    def inserir_elemento_final(self, elemento):
        if self.__posicao >= len(self.__elementos): #Se o vetor já estiver cheio
            self.__elementos = self.__elementos + [None] #Gera mais uma posição no Vetor,
        self.__elementos[self.__posicao] = elemento
        self.__posicao += 1

    def listar_elemento(self, posicao):
        return self.__elementos[posicao]