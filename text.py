import re
import string
from collections import Counter

def analisar_texto(texto):
    texto = texto.lower()
    texto = texto.translate(str.maketrans("", "", string.punctuation))

    
    palavras = texto.split()
    frases = re.split(r'[.!?]', texto)

   
    palavras = [palavra for palavra in palavras if palavra]
    frases = [frase for frase in frases if frase]

    
    total_palavras = len(palavras)
    total_frases = len(frases)
    media_palavras_por_frase = total_palavras / total_frases if total_frases > 0 else 0

    
    contagem_palavras = Counter(palavras)
    palavras_mais_frequentes = contagem_palavras.most_common(5)  

   
    print(f"Total de palavras: {total_palavras}")
    print(f"Total de frases: {total_frases}")
    print(f"Média de palavras por frase: {media_palavras_por_frase:.2f}")
    print("\nPalavras mais frequentes:")
    for palavra, contagem in palavras_mais_frequentes:
        print(f"{palavra}: {contagem}")

# Exemplo de uso
texto_exemplo = """
Este é um exemplo de texto que será analisado. Ele contém várias palavras e frases.
Vamos ver como a ferramenta funciona.
"""
analisar_texto(texto_exemplo)
