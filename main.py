from array import array
from vetores import vetor

#vetor_inteiros = array('b', [1,2,3])
#print(vetor_inteiros)
#vetor_inteiros.insert(3,4)
#print(vetor_inteiros)
#print(vetor_inteiros.index(2))

print(30 * "-", "MENU", 30 * "-")
print("1. vetores")
print("2. Listas Ligadas")
print("3. Listas Duplamente Ligadas")
print("4. Pilhas")
print("5. Filas")

menu = int(input("Digite a opção desejada: "))

if menu == 1:
    vetor_teste = vetor.Vetor(3)
    #vetor_teste.inserir_elemento_posicao(1, 0)
    #vetor_teste.inserir_elemento_posicao(3, 1)
    vetor_teste.inserir_elemento_final(1)
    vetor_teste.inserir_elemento_final(2)
    vetor_teste.inserir_elemento_final(3)
    vetor_teste.inserir_elemento_final(4) #Teste se gerou mais uma posição
    vetor_teste.inserir_elemento_final(5) #Teste se gerou mais uma posição x2
    print(vetor_teste.listar_elemento(0))
    print(vetor_teste.listar_elemento(1))
    print(vetor_teste.listar_elemento(2))
    print(vetor_teste.listar_elemento(3)) #Impressão do teste
    print(vetor_teste.listar_elemento(4)) #impressão do teste

