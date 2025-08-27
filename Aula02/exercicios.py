# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digote o segundo número: '))
resultado = numero_1 + numero_2
print(f'O resultado da soma é: {resultado}')

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

numero_1 = int(input('Digite seu número: '))
resultado = numero_1 % 5
print(f'O resto da divisão do número por 5 é: {resultado}')

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))
resultado = numero_1 * numero_2
print(f'A multiplicação de {numero_1} por {numero_2} é :{resultado}')

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))
resultado = numero_1 // numero_2
print(f'A divisão inteira de {numero_1} por {numero_2} é: {resultado}')

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

numero_1 = int(input('Digite seu número: '))
resultado = numero_1 ** 2
print(f'O quadrado de {numero_1} é: {resultado}')

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

numero_1 = 6.4
numero_2 = 3.7
resultado = numero_1 + numero_2

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o segundo número: '))
resultado = numero_1 + numero_2
media = resultado / 2
print(f'A soma de {numero_1} + {numero_2} é:{resultado} e a média desses dois números é: {media}')

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

base = int(input('Digite o numero base: '))
expoente = int(input('Digite o expoente: '))
resultado = base ** expoente
print(f'A potencia do número:{base} pelo expoente:{expoente} é: {resultado}')

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

temp_celsus = int(input('Digite a temperatura:'))
resultado_fahrenheit = (temp_celsus + 9/5) + 32
print(resultado_fahrenheit)

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math
circulo_raio = float(input('Digite o raio do círculo: '))
resultado_area = math.pi * (circulo_raio ** 2)
print(f'A área do círculo com raio {circulo_raio} é: {resultado_area}')

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

palavra = input('Digite uma palavra: ')
palavra_maiuscula = palavra.upper()

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

nome = input('Digite seu nome completo: ')
nome_minusculo = nome.lower()
print(nome_minusculo)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase = input('Digite uma frase: ')
frase_sem_espacos = frase.strip()

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data = input('Digite uma data no formato dd/mm/aaaa : ')
lista_data = data.split("/")
dia = lista_data[0]
mes = lista_data[1]
ano = lista_data[2]

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

palavra1 = input('Digite a primeira palavra: ')
palavra2 = input('Digite a segunda palavra: ')
palavra_concatenada = palavra1 + palavra2
print(palavra_concatenada)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

expressao1 = input('Digite a primeira expressão booleana (True/False): ')
expressao2 = input('Digite a segunda expressão booleana (True/False): ')
resultado = (expressao1 == 'True') and (expressao2 == 'True')
print(f'O resultado da operação AND entre as expressões é: {resultado}')

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

valorbooleano1 = input('Digite o primeiro valor booleano (True/False): ')
valorbooleano2 = input('Digite o segundo valor booleano (True/False): ')
resultado = (valorbooleano1 == 'True') or (valorbooleano2 == 'True')
print(f'O resultado da operação OR entre os valores é: {resultado}')

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

valor_booleano = input('Digite um valor booleano (True/False): ')
if valor_booleano == 'True':
    valor_invertido = False
else:
    valor_invertido = True

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
resultado = numero1 == numero2
print(f'Os números {numero1} e {numero2} são iguais? {resultado}')

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))   
resultado = numero1 != numero2
print(f'Os números {numero1} e {numero2} são diferentes? {resultado}')

# #### try-except e if

# 21: Conversor de Temperatura

conversor = input('Digite "C" para converter de Celsius para Fahrenheit ou "F" para converter de Fahrenheit para Celsius: ').upper()
if conversor == 'C':
    try:
        temp_celsius = float(input('Digite a temperatura em Celsius: '))
        temp_fahrenheit = (temp_celsius * 9/5) + 32
        print(f'A temperatura em Fahrenheit é: {temp_fahrenheit}')
    except ValueError:
        print('Por favor, insira um número válido.')

# 22: Verificador de Palíndromo

palavra = input('Digite uma palavra: ')
try:
    if palavra == palavra[::-1]:
        print(f'A palavra "{palavra}" é um palíndromo.')
    else:
        print(f'A palavra "{palavra}" não é um palíndromo.')    
except TypeError:
    print('Por favor, insira uma palavra válida.')

# 23: Calculadora Simples

def calculadora():
    try:
        num1 = float(input('Digite o primeiro número: '))
        operador = input('Digite o operador (+, -, *, /): ')
        num2 = float(input('Digite o segundo número: '))

        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 == 0:
                raise ZeroDivisionError('Divisão por zero não é permitida.')
            resultado = num1 / num2
        else:
            raise ValueError('Operador inválido.')

        print(f'O resultado é: {resultado}')
    except ValueError as e:
        print(f'Erro: {e}')
    except ZeroDivisionError as e:
        print(f'Erro: {e}')

# 24: Classificador de Números

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
if numero1 > numero2:
    print(f'O número {numero1} é maior que {numero2}.') 
elif numero1 < numero2:
    print(f'O número {numero1} é menor que {numero2}.')

# 25: Conversão de Tipo com Validação

def conversao_tipo():
    try:
        numero = input('Digite um número: ')
        numero_inteiro = int(numero)
        print(f'O número {numero} foi convertido para inteiro: {numero_inteiro}')
    except ValueError:
        print('Erro: O valor digitado não é um número válido.')