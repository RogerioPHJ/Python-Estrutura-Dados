from array import array

from listas import lista_ligada
from vetores import vetor

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
