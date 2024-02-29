def contar_vogais(texto):
    vogais = 'aeiouáéíóúàèìòùâêîôûãõ'
    return sum(1 for char in texto.lower() if char in vogais)

print(contar_vogais('Olá, mundo!'))  

