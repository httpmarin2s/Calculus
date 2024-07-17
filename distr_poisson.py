import math

print("Contexto: Suponha que um hospital atende, em média, 5 pacientes por dia. Queremos saber a probabilidade de o hospital atender exatamente 7 pacientes em um determinado dia.")
print("")
print("Solução: Vamos usar a distribuição de Poisson, que é adequada para modelar o número de eventos (pacientes atendidos) ocorrendo em um intervalo fixo de tempo (um dia), dado que os eventos ocorrem independentemente e com uma taxa média constante.")
print("")
#Parâmetros
lambda_valor = int(input("Digite a ocorrência Média: ")) # taxa média de ocorrência
k = int(input("Digite o número de ocorrências desejadas:"))

#Cálculo da probabilidade usando a fórmula de Poisson
probabilidade = (lambda_valor** k) * math.exp(-lambda_valor) / math.factorial(k)

print(f"A probabilidade de atender exatamente {k} pacientes em um dia é {probabilidade:.4f}")
porcentagem = probabilidade*100
print(f"A resposta em porcentagem equivale a {porcentagem:.4f}¢")