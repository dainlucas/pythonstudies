#Função que verifica validade da entrada
def obter_numero():
    while True:
        try:
            return float(input())
        except ValueError:
            print("Erro: por favor, digite um número válido.")

#Importação do Time para tornar mais dinãmica a operação
import time

#Mensagem de boas vindas
print("BEM VINDO AO COMPARADOR DE NÚMEROS :D")
time.sleep(1.5)

#Criação de lista aonde os números serão armazenados
lista_numeros = []

#Usuário digita os números que serão comparados
print("Digite um número: ")
lista_numeros.append(obter_numero())
print("Ótimo, digite outro número: ")
lista_numeros.append(obter_numero())
print("Perfeito, digite mais um número: ")
lista_numeros.append(obter_numero())

#Condição caso queira adicionar mais números ou não
while True:
    print('Gostaria de adicionar mais algum número? Digite "SIM" ou "NÃO: ')
    sim_nao = input().lower()

    if sim_nao == "sim":
        print("Digite outro número: ")
        lista_numeros.append(obter_numero())

    elif sim_nao == "nao" or sim_nao == "não":
        break

    else:
        print('Erro: Digite "Sim" ou "Não')
        continue

print("Calculando...")

#Comparação de maior e menor número
maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)
time.sleep(2.5)
print("Pronto :D")
print(f"Maior número da lista: {maior_numero}")
print(f"Menor número da lista: {menor_numero}")

input("Pressione Enter para finalizar o programa...")

