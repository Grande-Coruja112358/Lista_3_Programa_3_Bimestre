valor = float(input("Valor da conta: "))
pessoas = int(input("Quantidade de pessoas: "))
taxa = input("Adiciona 10%? ('s' ou 'n'): ")

if taxa == "s":
    valor = valor * (110 / 100)
    valor_por_pessoa = valor / pessoas 

elif taxa == "n":
    valor = valor
    valor_por_pessoa = valor / pessoas

else:
    print(f' valor inválido; Digite "s" para sim e "n" para não.')

print(f'===== Resumo da Conta =====')
print(f'Valor por pessoa: = R$ {valor_por_pessoa:.2f}')
print(f'Valor total: R$ {valor}')
print(f'===== Resumo da Conta =====')