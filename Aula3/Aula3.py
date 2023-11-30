#encoding: latin-1
#Todas as quest�es das lista est�o implementadas neste mesmo arquivo

# Mesclar Dicion�rios
# Combine dois dicion�rios, substituindo valores comuns pela soma dos valores correspondentes.
num1={'n0':0,'n1':1,'n2':2,'n3':3,'n3':4,'n4':5}
num2={'n0':6,'n1':7,'n2':8,'n3':9,'n3':10,'n4':11}

resultado = {}

for chave, valor in num1.items():
    if chave in num2:
            resultado[chave] = valor + num2[chave]
    else:
            resultado[chave] = valor
print("Dicion�rio num1: \n"+str(num1)+"\n\nDicion�rio num2: \n"+str(num2)+"\n")
print("Fus�o dos dicion�rios num1 e num2: \n"+ str(resultado)+"\n")

# Maior Valor em Dicion�rio de Dicion�rios
# Encontre a chave e valor com o maior valor em um dicion�rio de dicion�rios.
MaiorValor=max(resultado.items(), key=lambda k: k[1])
print("Maior valor do Dicion�rio fus�o: "+str(MaiorValor)+"\n")

# Palavras �nicas por Chave
# Dado um dicion�rio de listas, encontre as palavras que s�o �nicas para cada chave.
dicionario = {
    'lista1': ['ma��', 'banana', 'arroz','feij�o','macarr�o'],
    'lista2': ['banana', 'macaco', 'arroz','feij�o','mel�o'],
    'lista3': ['uva', 'ma��', 'kiwi','figo','mel�o'],
}
resultado = {}

conjuntos = {chave: set(lista) for chave, lista in dicionario.items()}

for chave, ConjuntoAtual in conjuntos.items():
    ConjuntosB = set().union(*(conj for k, conj in conjuntos.items() if k != chave))
    resultado[chave] = list(ConjuntoAtual - ConjuntosB)

print("Dicion�rio de palavras �nicas:")

# Aninhamento de Chaves
# Crie um dicion�rio aninhado com n�veis de chaves fornecidos em uma lista.
for lista, palavras in resultado.items():
     print(lista, palavras)

nivel4={'nivel4':''}
nivel3={'nivel3':nivel4}
nivel2={'nivel2':nivel3}
nivel1={'nivel1':nivel2}
print("\nDicion�rio aninhado: "+str(nivel1)+"\n")

# Dicion�rio Circular
# Crie um dicion�rio em que a �ltima chave aponte para a primeira chave.
dicionario = {
    'nivel1': 'chave1',
    'nivel2': 'chave2',
    'nivel3': 'chave3',
    'nivel4': 'chave4'
}

dicionario['nivel5'] = dicionario

print("Dicion�rio Circular: "+str(dicionario['nivel5']['nivel1'])+"\n")

# Compress�o de Dicion�rio
# Comprima um dicion�rio removendo chaves com valores menores que um determinado limite.

dicionario = {
    'a': 5,
    'b': 12,
    'c': 3,
    'd': 8,
}
limite = 4
dicionario_comprimido = {chave: valor for chave, valor in dicionario.items() if valor >= limite}

print("Dicion�rio Comprimido: "+str(dicionario_comprimido)+"\n")

# Frequ�ncia de Palavras em Texto
# Conte a frequ�ncia de cada palavra em um texto usando um dicion�rio.

texto = """Conte a frequ�ncia de cada palavra em um texto usando um dicion�rio. Palavra no texto"""

texto = texto.lower()
texto = ''.join(caracter if caracter.isalnum() or caracter.isspace() else ' ' for caracter in texto)

# Dividir o texto em palavras
palavras = texto.split()

# Contar a frequ�ncia de cada palavra usando um dicion�rio
frequencia = {}
for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print("Contando Palavras:");
for palavra, frequencia in frequencia.items():
    print(f'{palavra}: {frequencia}')

# Ordena��o de Dicion�rio por Valor
# Ordene um dicion�rio com base nos valores, em ordem decrescente.
dicionario = {'banana': 3, 'ma��': 7, 'laranja': 5, 'uva': 2}

dicionarioOrden = dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=True))

print("\nDicion�rio ordenado:"+str(dicionarioOrden)+"\n")

# Dicion�rio de Matrizes
# Crie um dicion�rio de matrizes, onde as chaves s�o coordenadas e os valores s�o os elementos correspondentes.

matriz = {'(0,0)': 3, '(0,1)': 7, '(0,2)': 5, '(1,0)': 2,'(1,1)':3,'(1,2)':6}

print("Dicion�rio de Matriz:")
for coordenada, elemento in matriz.items():
    print(f'{coordenada}: {elemento}')

# Mapeamento de Palavras
# Crie um dicion�rio que mapeie palavras em um texto para palavras diferentes com base em um dicion�rio de substitui��o.

textoExemplo= "Este � um exemplo de texto em python. O exemplo mostra como mapear palavras."
dicionarioSubstituicao = {
    'python': 'Programa��o',
    'exemplo': 'ilustra��o',
    'texto': 'conte�do',
}


palavras = textoExemplo.split()
texto_mapeado = [dicionarioSubstituicao.get(palavra, palavra) for palavra in palavras]
print("\nNovo texto: "+' '.join(texto_mapeado))
