# Juros simples

c = float(input("Qual o valor do Capital?: "))
i = float(input("Qual a porcentagem da Taxa mensal de juros?: "))
p = int(input("Qual o prazo em meses?: "))

j = (c * i * p) / 100

montante = c + j

print(f"O juros é de R$ {j:.2f} e o montante final é de R$ {montante:.2f}")
