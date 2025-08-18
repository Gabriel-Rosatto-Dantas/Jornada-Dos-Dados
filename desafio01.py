# Desafio - Cálculo de  Bônus com entrada do usuario

BONUS_KPI_2024 = 1000

# 1) Solicita ao usuário que digite seu nome
nome = input('Digite seu nome: ')
if nome.isdigit():
    print('Você digitou o nome incorretamente (Números)')
elif nome.isspace():
    print('Voce digitou apenas espaços')    

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input('Informe seu salário mensal: '))
salario.isinstance()

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input('Informe o valor do bônus: '))

# 4) Calcule o valor do bônus final
valor_bonus = BONUS_KPI_2024 + salario * bonus
# 5) Imprima cálculo do KPI para o usuário
print(f'Ola {nome}! Com base nas informações fornecidas, o valor do seu salario com bonus é: R${valor_bonus}')