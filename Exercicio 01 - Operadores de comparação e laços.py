import time

print("BEM VINDO :D")
time.sleep(2)
print("Por favor, digite quanto você tirou na primeira prova (0 a 10): ")
nota_prova_um = float(input())
print("Perfeito, agora me diga quanto você tirou na segunda prova (0 a 10): ")
nota_prova_dois = float(input())
media_provas = (nota_prova_um + nota_prova_dois)/2
print("Calculando...")
time.sleep(3)
if media_provas >= 7:
    if media_provas == 10:
        print("Aprovado com Distinção")
    else:
        print("Aprovado")
elif media_provas < 7:
    print("Reprovado")
else:
    print("ERRO")
    print("Favor consultar o responsável")
