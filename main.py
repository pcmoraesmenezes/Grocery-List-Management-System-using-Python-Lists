"""
Faça uma lista de compras usando listas
O usuario deve ter a opção de inserir, apagar e listar os dados da lista
Não permita que o programa quebre com indices não existentes na lista
"""
import os
lista = []
i = 0
j = 0
adicionar = ''
aux = ''
while i != 4:
    print("Bem vindo a sua lista de compras!")
    print("Caso deseje adicionar algo a sua lista de compras digite 1")
    print("Caso deseje remover algo da sua lista digite 2")
    print("Caso deseje listar os indices digite 3")
    print("Caso deseje encerrar o programa digite 4!")
    i = int(input())
    while i != 1 and i != 2 and i != 3 and i != 4:
        print("Você não forneceu uma opção valida! Tente novamente")
        i = int(input())
    if i == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Digite o que deseja inserir abaixo")
        adicionar = input()
        lista.append(adicionar)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Você adicionou {adicionar.upper()}!')  
    if i == 2:
        if len(lista) == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Você não possuí nenhum elemento nessa lista voltando para a central! ")
            continue
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Você optou por remover, recomendamos que liste os indices antes de prosseguir!")
        print("Deseja listar os elementos antes de remover? Digite 's' para 'Sim' e 'n' para 'Não'")
        aux = input()
        aux = aux.lower()
        while aux != 's' and aux != 'sim'  and aux != 'n' and aux != 'nao':
            print("Você não forneceu dados corretos! ")
            aux = input()
            aux = aux.lower()
        if aux == 'sim' or aux == 's':
            for i in enumerate(list(lista)):
                print(i)
        print("Informe o indice que deseja remover abaixo!")
        j = int(input())
        while j >= len(lista):
            print("Você não forneceu um índice válido! tente novamente")
            j = int(input())
        valor_removido = lista[j]
        lista.pop(j)
        print(f'Você removeu {valor_removido}')
        print("Deseja ver a sua lista? 's' para sim e 'n' para não")
        aux = input()
        aux = aux.lower()
        if len(lista) == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Não há nenhum elemento nessa lista!")
            continue
        while aux != 's' and aux != 'sim'  and aux != 'n' and aux != 'nao':
            print("Você não forneceu dados corretos! ")
            aux = input()
            aux.lower()
        if aux == 'sim' or aux == 's':
            os.system('cls' if os.name == 'nt' else 'clear')
            for i in enumerate(list(lista)):
                print(i)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
    if i == 3:
        if len(lista) == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Não há nenhum elemento nessa lista!")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Você escolheu a opção de listar os elementos da lista!")
        if len(lista) == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Ainda não há nenhum elemento nessa lista! ")
            continue
        for i in enumerate(list(lista)):
            print(i)
    if i == 4:
        break
os.system('cls' if os.name == 'nt' else 'clear')
