def contar_vogais(frase):
    # Definindo as vogais
    vogais = "aeiouAEIOU"
    
    # Contador de vogais
    contador = 0
    
    # Iterando sobre cada caractere na frase
    for letra in frase:
        if letra in vogais:
            contador += 1
            
    return contador

# Solicitando a entrada do usuário
frase_usuario = input("Digite uma frase: ")

# Chamando a função e exibindo o resultado
numero_vogais = contar_vogais(frase_usuario)
print(f"A frase contém {numero_vogais} vogais.")