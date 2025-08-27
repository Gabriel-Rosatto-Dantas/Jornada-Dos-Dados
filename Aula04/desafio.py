# Dicionário para armazenar todos os usuários cadastrados
usuarios_cadastrados = {}

def cadastrar_usuarios() -> tuple[str, float, float]:
    """
    Solicita e valida nome, salário e bônus de um usuário.
    Retorna os dados validados.
    """
    # 1. Validação do Nome
    while True:
        try:
            nome: str = input("Digite seu nome: ")
            if not nome:
                raise ValueError("O nome não pode estar vazio.")
            elif any(char.isdigit() for char in nome):
                raise ValueError("O nome não deve conter números.")
            else:
                print("Nome válido:", nome)
                break
        except ValueError as e:
            print(e)

    # 2. Validação do Salário
    while True:
        try:
            salario: float = float(input("Digite o valor do seu salário: "))
            if salario < 0:
                raise ValueError("Por favor, digite um valor positivo para o salário.")
            else:
                break
        except ValueError as e:
            print("Entrada inválida para o salário.", e)

    # 3. Validação do Bônus
    while True:
        try:
            bonus: float = float(input("Digite o valor do bônus recebido: "))
            if bonus < 0:
                raise ValueError("Por favor, digite um valor positivo para o bônus.")
            else:
                break
        except ValueError as e:
            print("Entrada inválida para o bônus.", e)

    return nome, salario, bonus

# Loop principal para permitir vários cadastros
while True:
    print("\n--- Novo Cadastro de Usuário ---")
    nome_usuario, salario_usuario, bonus_usuario = cadastrar_usuarios()

    # Cria um dicionário para o usuário atual
    dados_usuario = {
        'salario': salario_usuario,
        'bonus': bonus_usuario,
        'bonus_final': 1000 + salario_usuario * bonus_usuario
    }

    # Adiciona o novo usuário ao dicionário de usuários cadastrados
    usuarios_cadastrados[nome_usuario] = dados_usuario

    # Pergunta se o usuário quer continuar
    continuar = input("Deseja cadastrar outro usuário? (s/n): ").lower()
    if continuar != 's':
        break

# Imprime o dicionário completo com todos os usuários
print("\n--- Relatório Final ---")
print(f"Total de usuários cadastrados: {len(usuarios_cadastrados)}")
print("Detalhes dos usuários:")
for nome, dados in usuarios_cadastrados.items():
    print(f"Nome: {nome}")
    print(f"  Salário: R${dados['salario']:.2f}")
    print(f"  Bônus Recebido: {dados['bonus']:.2f}")
    print(f"  Bônus Final: R${dados['bonus_final']:.2f}")

print("\nCadastro finalizado. O dicionário de usuários está disponível para uso.")