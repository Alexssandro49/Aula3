#encoding: latin-1
#Todas as questões das lista estão implementadas neste mesmo arquivo
num1={'n0':0,'n1':1,'n2':2,'n3':3,'n3':4,'n4':5}
num2={'n0':6,'n1':7,'n2':8,'n3':9,'n3':10,'n4':11}

resultado = {}

for chave, valor in num1.items():
    if chave in num2:
            resultado[chave] = valor + num2[chave]
    else:
            resultado[chave] = valor
print("Dicionário num1: \n"+str(num1)+"\n\nDicionário num2: \n"+str(num2)+"\n")
print("Fusão dos dicionários num1 e num2: \n"+ str(resultado)+"\n")
MaiorValor=max(resultado.items(), key=lambda k: k[1])
print("Maior valor do Dicionário fusão: "+str(MaiorValor)+"\n")

dicionario = {
    'lista1': ['maçã', 'banana', 'arroz','feijão','macarrão'],
    'lista2': ['banana', 'macaco', 'arroz','feijão','melão'],
    'lista3': ['uva', 'maçã', 'kiwi','figo','melão'],
}
resultado = {}

conjuntos = {chave: set(lista) for chave, lista in dicionario.items()}

for chave, ConjuntoAtual in conjuntos.items():
    ConjuntosB = set().union(*(conj for k, conj in conjuntos.items() if k != chave))
    resultado[chave] = list(ConjuntoAtual - ConjuntosB)

print("Dicionário de palavras únicas:")
for lista, palavras in resultado.items():
     print(lista, palavras)

nivel4={'nivel4':''}
nivel3={'nivel3':nivel4}
nivel2={'nivel2':nivel3}
nivel1={'nivel1':nivel2}
print("\nDicionário aninhado: "+str(nivel1)+"\n")

dicionario = {
    'nivel1': 'chave1',
    'nivel2': 'chave2',
    'nivel3': 'chave3',
    'nivel4': 'chave4'
}

dicionario['nivel5'] = dicionario

print("Dicionário Circular: "+str(dicionario['nivel5']['nivel1'])+"\n")

dicionario = {
    'a': 5,
    'b': 12,
    'c': 3,
    'd': 8,
}
