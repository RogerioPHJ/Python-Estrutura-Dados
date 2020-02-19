from array import array
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
    print(vetor_teste)
    print(60 * "-")
    print(vetor_teste.tamanho_vetor()) # Verificando quantos elementos tem no vetor, pois o tamanho está dinamico




