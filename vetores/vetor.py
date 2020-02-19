class Vetor():
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = [None] * tamanho
        self.__posicao = 0

    def tamanho_vetor(self):
        return len(self.__elementos)

    def __str__(self):
        return ' ' .join([str (i) for i in self.__elementos]) #Retorna uma string que percorre o vetor

    def inserir_elemento_posicao(self, elemento, posicao):
        vetor_inicio = self.__elementos[:posicao] + [None] #Pegando valores antes da posição e criando mais uma posição
        vetor_final = self.__elementos[posicao:] #Pegando os valores depois da posição
        vetor_inicio[len(vetor_inicio) - 1] = elemento # Colocando o elemento na posição criada acima
        self.__elementos = vetor_inicio + vetor_final #Concatenando os dois vetores para criar um unico
        self.__posicao += 1 #Informar que modificou 1 posição

    def inserir_elemento_final(self, elemento):
        if self.__posicao >= self.tamanho_vetor(): #Se o vetor já estiver cheio
            self.__elementos = self.__elementos + [None] #Gera mais uma posição no Vetor,
        self.__elementos[self.__posicao] = elemento
        self.__posicao += 1

    def listar_elemento(self, posicao):
        return self.__elementos[posicao]