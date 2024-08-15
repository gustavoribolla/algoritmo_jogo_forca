from collections import Counter

# 1- Função para calcular a quantidade de cada letra nas palavras

def calcula_quant_letra(content):
    quant = {}  
    for palavra in content:  
        for letra in palavra: 
            if letra in quant:  
                quant[letra] += 1  
            else:
                quant[letra] = 1  
    return quant  # Retorna o dicionário de contagens de letras

# 2- Função para calcular a probabilidade de cada letra ocorrer

def calcula_probabilidade(quant):
    total = sum(quant.values())  
    probs = {}  
    for key in quant:  
        probs[key] = quant[key] / total 
    return probs  # Retorna o dicionário de probabilidades

# 3- Função para encontrar a letra com a maior probabilidade de ocorrer, excluindo letras já jogadas

def maior_probabilidade(probs, letras_jogadas):
    maior = 0  
    letra = ''  
    for key in probs:  
        if probs[key] > maior and key not in letras_jogadas:  
            maior = probs[key]  
            letra = key  
    return letra  # Retorna a letra com a maior probabilidade

# 4- Função para remover palavras que contenham uma letra específica

def remove_palavra_por_letra(content, letra):
    new_content = [] 
    for palavra in content:  
        if letra not in palavra: 
            new_content.append(palavra)
    return new_content  # Retorna a nova lista de palavras

# 5- Função para remover palavras que contenham uma letra em uma posição específica

def remove_palavra_por_indice(content, indice, letra):
    new_content = []  
    for palavra in content: 
        if palavra[indice] == letra:
            new_content.append(palavra)
    return new_content  # Retorna a nova lista de palavras

# 6- Função para remover palavras com um tamanho específico

def remove_palavra_por_tamanho(content, tamanho):
    new_content = []  
    for palavra in content: 
        if len(palavra) == tamanho:
            new_content.append(palavra)
    return new_content  # Retorna a nova lista de palavras

# 7- Função para calcular a frequência de cada letra nas palavras

def calcular_frequencia_letras(palavras): 
    letras = [letra for palavra in palavras for letra in palavra] 
    frequencia = Counter(letras)
    return frequencia  # Retorna o dicionário de frequência de letras