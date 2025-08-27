### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

quantidade = -2
preco = 100

if quantidade < 0 and preco < 0:
    print("Dados invalidos")
else:
    print("Dados validos")

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:temperatura abaixo de 10°C é 'Baixa', entre 10°C e 25°C é 'Normal', e acima de 25°C é 'Alta'

temperatura = 15
if temperatura < 10:
    print("Tempreratura baixa")
elif temperatura < 20:
    print("Temperatura media")
elif temperatura < 30:
    print("Temperatura alta")

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
if log['level'] == 'ERROR':
    print("Log com mensagem de ERROR")
    

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

bd_email = ["teste@gmail.com","teste2@gmail.com", "teste3@gmail.com"]
idade_valida = range(18,65)

idade_usuario = int(input("Informe sua idade:"))
email_usuario = input("Informe seu email:")

if idade_usuario in idade_valida and email_usuario in bd_email:
    print("Usuario validado!")
else:
    print("Usuario invalido!")
    
### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

transacao = {"valor": 12000, "hora": 20}
if transacao["valor"] > 10000 and transacao["hora"] < 9 or transacao["hora"] > 18:
    print("Transação suspeita")
else:
    print("Transação OK")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = "Ola, estou aprendendo a contar quantas vezes cada palavra unica aparece"
contagem_palavras = {}

novo_texto = texto.upper()
lista_palavras = novo_texto.split()

for palavra in lista_palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

lista = [10,20,30,40,50]
valor_minimo = min(lista)
valor_maximo = max(lista)

nova_lista = []
for valor in lista:
    valor_normalizado = (valor - valor_minimo) / (valor_maximo - valor_minimo)
    nova_lista.append(valor_normalizado)
print(nova_lista)
    

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

usuarios = {
    "usuario1": {
        "Nome": "Gabriel",
        "Idade": 20
    },
    "usuario2": {
        "Nome": "Juliana",
        "Idade": 25
    },
    "usuario3": {
        "Nome": "Pedro",
        "Idade": None
    }
}

for chave_usuario, dados_usuario in usuarios.items():
    idade = dados_usuario["Idade"]
    if idade is None:
        print(f"O usuario {chave_usuario} tem idade faltando")
        
### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

lista_numeros = [0,1,2,3,4,5,6,7,8,9,10]
lista_pares = []
for numero in lista_numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
print(lista_pares)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {"categoria": "Eletrônicos", "valor": 1500},
    {"categoria": "Livros", "valor": 50},
    {"categoria": "Eletrônicos", "valor": 800},
    {"categoria": "Livros", "valor": 25},
    {"categoria": "Vestuário", "valor": 120},
    {"categoria": "Livros", "valor": 75}
]

total_vendas_por_categoria = {}

for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in total_vendas_por_categoria:
        total_vendas_por_categoria[categoria] += valor
    else:
        total_vendas_por_categoria[categoria] = valor
        
print(total_vendas_por_categoria)

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

while True:
    texto = input("Digite um texto qualquer:")
    if texto.upper() == "SAIR":
        break
        

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

valores = [0,1,2,3,4,5]
valor_usuario = int(input("Informe um valor:"))
if valor_usuario in valores:
    print("Entrada valida")
else:
    print("Entrada invalida")

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

lista_paginas = ["pagina1","pagina2","pagina3","pagina4","pagina5"]
for pagina in lista_paginas:
    print(f"Processando pagina {pagina}")

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

tentativas = 5
login = "teste"
while tentativas > 0:
    login_usuario = input("Digite seu usuario:")
    if login_usuario != login:
        tentativas -= 1
        print("Usuario incorreto, tente novamente:")   
    else:
        print("Login efetuado")
        break
print("Numero de tentativas excedido")

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.
valor_parada = 3
lista_valores = [0,1,2,3,4,5]
for valor in lista_valores:
    print(f"Processando item {valor}")
    if valor == valor_parada:
        print("Valor encontrado")
        break
    else:
        print("Valor não encontrado")
        continue