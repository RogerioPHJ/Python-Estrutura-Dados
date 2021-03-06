from array import array

from conjuntos import conjunto
from filas import fila
from pilhas import pilha
from listas import lista_ligada, lista_duplamente_ligada
from vetores import vetor
from mapas import mapa
from arvores import arvore, no_arvore_inteiro

#vetor_inteiros = array('b', [1,2,3])
#print(vetor_inteiros)
#vetor_inteiros.insert(3,4)
#print(vetor_inteiros)
#print(vetor_inteiros.index(2))

print(30 * "-", "MENU", 30 * "-")
print("1. Vetores")
print("2. Listas Ligadas")
print("3. Listas Duplamente Ligadas")
print("4. Pilhas")
print("5. Filas")
print("6. Conjuntos")
print("7. Mapas")
print("8. Árvores")


menu = int(input("Digite a opção desejada: "))

if menu == 1:
    vetor_teste = vetor.Vetor(0)
    vetor_teste.inserir_elemento_posicao(1, 0)
    vetor_teste.inserir_elemento_posicao(2, 1)
    vetor_teste.inserir_elemento_posicao(3, 2)
    vetor_teste.inserir_elemento_posicao(4, 2) # Essa chamada aqui empurrou o 3 para o final do vetor
    vetor_teste.inserir_elemento_posicao(5, 2) # Essa chamada empurra o 4 e o 3
    vetor_teste.inserir_elemento_final(1)
    #vetor_teste.inserir_elemento_final(2)
    print(60 * "-")
    print(vetor_teste.tamanho_vetor()) # Verificando quantos elementos tem no vetor, pois o tamanho está dinamico
    print(vetor_teste)
    #print(vetor_teste.contem(8))
    print(vetor_teste.indice(4)) #Buscando em qual indice está o 3
    vetor_teste.remover_elemento_indice(3) #Removeu pelo indice
    print(vetor_teste)
    vetor_teste.remover_elemento(5) #Removeu pelo elemento (que por debaixo dos panos usa o indice)
    print(vetor_teste)

elif menu == 2:
    lista_teste = lista_ligada.ListaLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(4)
    lista_teste.inserir(5)
    lista_teste.inserir_posicao(1, 10)
    print(lista_teste)
    print(60 * "-")
    print(lista_teste.contem(5))
    print(lista_teste.indice(55))
    print(60 * "-")
    lista_teste.remover_elemento(4)
    print(lista_teste)
    #print(lista_teste.recuperar_elemento_no(2))

elif menu == 3:
    lista_teste = lista_duplamente_ligada.ListaDuplamenteLigada()
    lista_teste.inserir(1)
    lista_teste.inserir(4)
    lista_teste.inserir(5)
    lista_teste.inserir_posicao(2, 10)
    print(lista_teste)
    print(60 * "-")
    #print(lista_teste.contem(5))
    #print(lista_teste.indice(55))
    print(60 * "-")
    lista_teste.remover_posicao(1)
    print(lista_teste)

elif menu == 4:
    pilha_teste = pilha.Pilha()
    pilha_teste.empilhar(5)
    pilha_teste.empilhar(6)
    pilha_teste.empilhar(7)
    print(pilha_teste.desempilhar())

elif menu == 5:
    fila_teste = fila.Fila()
    fila_teste.enfileirar(1)
    fila_teste.enfileirar(2)
    fila_teste.enfileirar(3)
    fila_teste.enfileirar(4)
    print(fila_teste) #1 2 3 4
    print(fila_teste.desenfileirar())
    print(fila_teste)  # 2 3 4
    print(fila_teste.desenfileirar())
    print(fila_teste)  # 3 4
    fila_teste.enfileirar(6)
    print(fila_teste)

elif menu == 6:
    conjunto_teste = conjunto.Conjunto()
    conjunto_teste.inserir(1)
    conjunto_teste.inserir(2)
    conjunto_teste.inserir(3)
    print(conjunto_teste.inserir(3))
    #print(conjunto_teste.inserir_posicao(1, 4))
    print(conjunto_teste)
    print(conjunto_teste.remover_elemento(3))
    print(conjunto_teste.inserir(3))
    print(conjunto_teste.inserir("Python"))
    print(conjunto_teste.inserir("TreinaWeb"))
    print(conjunto_teste.inserir(4))
    print(conjunto_teste)

elif menu == 7:
    mapa_teste = mapa.Mapa()
    print(mapa_teste)
    mapa_teste.adicionar("par", 10)
    mapa_teste.adicionar("impar", 5)
    mapa_teste.adicionar("par", 2)
    print(mapa_teste)
    print(mapa_teste.contem_chave("par"))
    print(mapa_teste.recuperar("par"))

elif menu == 8:
    arvore_teste = arvore.Arvore()
    print(arvore_teste)
    arvore_teste.inserir_elemento(no_arvore_inteiro.NoArvoreInteiro(5))
    print(arvore_teste)
    arvore_teste.inserir_elemento(no_arvore_inteiro.NoArvoreInteiro(4))
    arvore_teste.inserir_elemento(no_arvore_inteiro.NoArvoreInteiro(6))
    print(arvore_teste)
    arvore_teste.inserir_elemento(no_arvore_inteiro.NoArvoreInteiro(8))
    arvore_teste.inserir_elemento(no_arvore_inteiro.NoArvoreInteiro(7))
    print("Em ordem")
    print(arvore_teste.em_ordem())
    print("Pré-ordem")
    print(arvore_teste.pre_ordem())
    print("Pós-ordem")
    print(arvore_teste.pos_ordem())
    print("Altura")
    print(arvore_teste.altura())


else:
    print("Opção inválida")