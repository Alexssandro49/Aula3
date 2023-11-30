#encoding: latin-1
#Todas as questões das lista estão implementadas neste mesmo arquivo

# Mesclar Dicionários
# Combine dois dicionários, substituindo valores comuns pela soma dos valores correspondentes.
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

# Maior Valor em Dicionário de Dicionários
# Encontre a chave e valor com o maior valor em um dicionário de dicionários.
MaiorValor=max(resultado.items(), key=lambda k: k[1])
print("Maior valor do Dicionário fusão: "+str(MaiorValor)+"\n")

# Palavras Únicas por Chave
# Dado um dicionário de listas, encontre as palavras que são únicas para cada chave.
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

# Aninhamento de Chaves
# Crie um dicionário aninhado com níveis de chaves fornecidos em uma lista.
for lista, palavras in resultado.items():
     print(lista, palavras)

nivel4={'nivel4':''}
nivel3={'nivel3':nivel4}
nivel2={'nivel2':nivel3}
nivel1={'nivel1':nivel2}
print("\nDicionário aninhado: "+str(nivel1)+"\n")

# Dicionário Circular
# Crie um dicionário em que a última chave aponte para a primeira chave.
dicionario = {
    'nivel1': 'chave1',
    'nivel2': 'chave2',
    'nivel3': 'chave3',
    'nivel4': 'chave4'
}

dicionario['nivel5'] = dicionario

print("Dicionário Circular: "+str(dicionario['nivel5']['nivel1'])+"\n")

# Compressão de Dicionário
# Comprima um dicionário removendo chaves com valores menores que um determinado limite.

dicionario = {
    'a': 5,
    'b': 12,
    'c': 3,
    'd': 8,
}
limite = 4
dicionario_comprimido = {chave: valor for chave, valor in dicionario.items() if valor >= limite}

print("Dicionário Comprimido: "+str(dicionario_comprimido)+"\n")

# Frequência de Palavras em Texto
# Conte a frequência de cada palavra em um texto usando um dicionário.

texto = """Conte a frequência de cada palavra em um texto usando um dicionário. Palavra no texto"""

texto = texto.lower()
texto = ''.join(caracter if caracter.isalnum() or caracter.isspace() else ' ' for caracter in texto)

# Dividir o texto em palavras
palavras = texto.split()

# Contar a frequência de cada palavra usando um dicionário
frequencia = {}
for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print("Contando Palavras:");
for palavra, frequencia in frequencia.items():
    print(f'{palavra}: {frequencia}')

# Ordenação de Dicionário por Valor
# Ordene um dicionário com base nos valores, em ordem decrescente.
dicionario = {'banana': 3, 'maçã': 7, 'laranja': 5, 'uva': 2}

dicionarioOrden = dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=True))

print("\nDicionário ordenado:"+str(dicionarioOrden)+"\n")

# Dicionário de Matrizes
# Crie um dicionário de matrizes, onde as chaves são coordenadas e os valores são os elementos correspondentes.

matriz = {'(0,0)': 3, '(0,1)': 7, '(0,2)': 5, '(1,0)': 2,'(1,1)':3,'(1,2)':6}

print("Dicionário de Matriz:")
for coordenada, elemento in matriz.items():
    print(f'{coordenada}: {elemento}')

# Mapeamento de Palavras
# Crie um dicionário que mapeie palavras em um texto para palavras diferentes com base em um dicionário de substituição.

textoExemplo= "Este é um exemplo de texto em python. O exemplo mostra como mapear palavras."
dicionarioSubstituicao = {
    'python': 'Programação',
    'exemplo': 'ilustração',
    'texto': 'conteúdo',
}


palavras = textoExemplo.split()
texto_mapeado = [dicionarioSubstituicao.get(palavra, palavra) for palavra in palavras]
print("\nNovo texto: "+' '.join(texto_mapeado))
