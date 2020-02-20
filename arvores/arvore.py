class Arvore():
    def __init__(self, raiz=None):
        self.__raiz = raiz

    @property
    def raiz(self):
        return self.__raiz

    def inserir_elemento(self, no):
        no.no_direito = None
        no.no_esquerdo = None
        if(self.__raiz == None):
            self.__raiz = no
        else:
            if (self.__raiz.peso() > no.peso()):
                self.__raiz.no_esquerdo = no
            else:
                self.__raiz.no_direito = no

    def __inserir(self, referencia, novo_no):
        if referencia.peso() < novo_no.peso():
            if referencia.no_direito == None:
                referencia.no_direito = novo_no
            else:
                self.__inserir(referencia.no_direito, novo_no)
        else:
            if referencia.no_esquerdo == None:
                referencia.no_esquerdo = novo_no
            else:
                self.__inserir(referencia.no_esquerdo, novo_no)

    def __buscar(self, referencia, no_busca):
        if referencia.valor == no_busca.valor:
            return referencia
        else:
            # Direita do nó
            if referencia.peso() < no_busca.peso():
                if referencia.no_direito == None:
                    raise ValueError("Elemento não encontrado")
                else:
                    print("Navegando pela direita do nó", referencia.valor.__str__())
                    return self.__buscar(referencia.no_direito, no_busca)
            else:
                # Esquerda do nó
                if referencia.no_esquerdo == None:
                    raise ValueError("Elemento não encontrado")
                else:
                    print("Navegando pela esquerda do nó", referencia.valor.__str__())
                    return self.__buscar(referencia.no_esquerdo, no_busca)

    def __str__(self):
        return "[(X)]" if self.__raiz == None else self.__raiz.__str__()