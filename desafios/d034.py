salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250.00:
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${salario * 1.15:.2f} agora.')
else:
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${salario * 1.10:.2f} agora.')