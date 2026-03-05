dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
total = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R${total}')