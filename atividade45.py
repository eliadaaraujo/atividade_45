# Controle de Temperatura de Servidores
# Leia 5 temperaturas e mostre a média delas.
# Use um laço para fazer as leituras e cálculos.

soma = 0
for i in range(5):
    t = float(input("Temperatura: "))
    soma += t
print("Média:", soma / 5)
