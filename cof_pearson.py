#Calculando o coeficiete de pearson 
import math

x = [2,4,6,8,10]
y = [3,5,7,9,11]

# Item 1 - calcule as médias das variáveis 
mediax = sum(x)/len(x)
print(f" A média de y é igual a: {mediax}")

mediay = sum(y)/len(y)
print(f" A média de y é igual a: {mediay}")

# Item 2 - Subtrari as médias de cada valor 
sub_media_x = [item - mediax for item in x]
sub_media_y = [item2 - mediay for item2 in y] 
print(f"Subtraindo cada valor de x pela média {sub_media_x}")
print(f"Subtraindo cada valor de y pela média {sub_media_y}")

# Item 3 - calcular o produto dessas diferencas 
produto = [a * b for a,b in zip(sub_media_x, sub_media_y)]
print(produto)

#Item 4 - soma dos valores 
soma_produto = sum(produto)
print(f"Soma dos valores dos produtos {soma_produto}")

#Item 5 - Calcular as somas das diferenças ao quadrado 
quadradox = [item ** 2 for item in sub_media_x]
soma_quadrados = sum(quadradox) 
print(f"Soma das diferenças ao quadrados: {soma_quadrados}")

quadradoy = [item ** 2 for item in sub_media_y]
soma_quadradosy = sum(quadradoy) 
print(f"Soma das diferenças ao quadrados: {soma_quadradosy}")

#Item 6 - Cálculo do coeficiente 
numerador = soma_quadrados * soma_quadradosy
denominador = (soma_quadrados*soma_quadrados)*(soma_quadradosy*soma_quadradosy)
denominador = math.sqrt(denominador)

calculo = numerador/denominador
print(calculo)