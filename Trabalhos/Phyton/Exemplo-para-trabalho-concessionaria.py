# ===========================
# SISTEMA DE LIVRARIA PYTHON
# ===========================

# -----------------------------------------
# CADASTRO INICIAL DO CLIENTE
# -----------------------------------------
# Criamos um dicionário chamado "cliente" para guardar informações importantes.
cliente = {
    "nome": input("Digite seu nome: "),          # Guarda o nome do cliente
    "email": input("Digite seu e-mail: "),       # Guarda o e-mail
    "saldo": float(input("Digite seu saldo inicial (R$): "))  # Saldo convertido para float
}


# -----------------------------------------
# TABELA DE PREÇOS (VALORES DE REFERÊNCIA)
# -----------------------------------------
# Dicionário que funciona como a "tabela FIPE" dos livros, com valores fixos.
tabela_precos = {
    "Dom Casmurro": 40.0,
    "O Pequeno Príncipe": 35.0,
    "1984": 50.0,
    "A Revolução dos Bichos": 28.0,
    "Harry Potter": 60.0
}


# -----------------------------------------
# LISTA DE LIVROS DISPONÍVEIS
# -----------------------------------------
# Usamos tuplas dentro de listas para representar livros (título, autor)
livros_para_aluguel = [
    ("Dom Casmurro", "Machado de Assis"),
    ("1984", "George Orwell")
]

livros_para_venda = [
    ("Harry Potter", "J. K. Rowling"),
    ("O Pequeno Príncipe", "Saint-Exupéry")
]


# =======================================
#               FUNÇÕES
# =======================================

# -----------------------------------------
# MENU PRINCIPAL
# -----------------------------------------
# Exibe opções para o usuário escolher
def menu():
    print("\n===== LIVRARIA PYTHON BOOKS =====")
    print("1 - Vender livro")
    print("2 - Alugar livro")
    print("3 - Comprar livro")
    print("4 - Ver saldo")
    print("0 - Sair")


# -----------------------------------------
# FUNÇÃO: VENDER LIVRO
# -----------------------------------------
def vender_livro():
    print("\n--- VENDA DE LIVRO ---")

    # Usuário informa título e autor
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")

    # Verifica se o livro existe na tabela de preços
    if titulo not in tabela_precos:
        print("Este livro não está na tabela de referência. Venda não realizada.")
        return  # Para a função aqui

    # Busca o valor de referência no dicionário
    valor_referencia = tabela_precos[titulo]

    # A livraria paga 20% a menos do valor de referência
    proposta = valor_referencia * 0.80

    print(f"\nValor de referência: R$ {valor_referencia:.2f}")
    print(f"Proposta da livraria: R$ {proposta:.2f}")

    # Confirmação do usuário
    confirmacao = input("Deseja vender o livro? (s/n): ").lower()

    if confirmacao == "s":
        # Adiciona o valor ao saldo do cliente
        cliente["saldo"] += proposta

        # Coloca o livro na lista de livros à venda
        livros_para_venda.append((titulo, autor))
        print("Livro vendido com sucesso!")
    else:
        print("Venda cancelada.")


# -----------------------------------------
# FUNÇÃO: ALUGAR LIVRO
# -----------------------------------------
def alugar_livro():
    print("\n--- ALUGUEL DE LIVRO ---")

    # Verifica se há livros disponíveis
    if not livros_para_aluguel:
        print("Não há livros disponíveis para aluguel.")
        return

    # Lista todos os livros disponíveis
    print("\nLivros disponíveis:")
    for i, livro in enumerate(livros_para_aluguel):
        print(f"{i + 1} - {livro[0]} ({livro[1]})")

    # Usuário escolhe o livro pelo número
    escolha = int(input("Escolha o número do livro: ")) - 1

    # Verificação de opção válida
    if escolha < 0 or escolha >= len(livros_para_aluguel):
        print("Opção inválida.")
        return

    # Número de dias do aluguel
    dias = int(input("Por quantos dias deseja alugar? "))

    # Calcula o valor total
    valor_total = dias * 5  # R$5 por dia

    print(f"Valor total do aluguel: R$ {valor_total:.2f}")

    # Verifica se o cliente tem saldo suficiente
    if cliente["saldo"] < valor_total:
        print("Saldo insuficiente.")
        return

    confirmacao = input("Confirmar aluguel? (s/n): ").lower()
    if confirmacao == "s":
        # Atualiza saldo do cliente
        cliente["saldo"] -= valor_total

        # Remove o livro da lista de aluguel
        livro = livros_para_aluguel.pop(escolha)

        print(f"Você alugou '{livro[0]}'.")
    else:
        print("Aluguel cancelado.")


# -----------------------------------------
# FUNÇÃO: COMPRAR LIVRO
# -----------------------------------------
def comprar_livro():
    print("\n--- COMPRA DE LIVRO ---")

    # Verifica se há livros à venda
    if not livros_para_venda:
        print("Não há livros disponíveis para venda.")
        return

    # Lista livros disponíveis
    print("\nLivros à venda:")
    for i, livro in enumerate(livros_para_venda):
        print(f"{i + 1} - {livro[0]} ({livro[1]})")

    escolha = int(input("Escolha o número do livro: ")) - 1

    # Verificação simples de escolha válida
    if escolha < 0 or escolha >= len(livros_para_venda):
        print("Opção inválida.")
        return

    # Pega o título do livro
    titulo = livros_para_venda[escolha][0]

    # Busca o preço base
    valor_base = tabela_precos[titulo]

    # A livraria vende com +15% de lucro
    valor_final = valor_base * 1.15

    print(f"Valor do livro: R$ {valor_final:.2f}")

    # Verifica saldo
    if cliente["saldo"] < valor_final:
        print("Saldo insuficiente.")
        return

    confirmacao = input("Confirmar compra? (s/n): ").lower()
    if confirmacao == "s":
        # Desconta saldo
        cliente["saldo"] -= valor_final

        # Remove da lista
        livro = livros_para_venda.pop(escolha)

        print(f"Você comprou '{livro[0]}'.")
    else:
        print("Compra cancelada.")


# =======================================
#  PROGRAMA PRINCIPAL (LOOP DA APLICAÇÃO)
# =======================================

# Loop infinito para manter o sistema rodando até o usuário escolher sair
while True:
    menu()
    
    # Usuário escolhe uma opção
    opcao = input("Escolha uma opção: ")

    # Usamos match case (igual ao switch case)
    match opcao:
        case "1":
            vender_livro()
        case "2":
            alugar_livro()
        case "3":
            comprar_livro()
        case "4":
            print(f"\nSaldo atual: R$ {cliente['saldo']:.2f}")
        case "0":
            print("Saindo do sistema. Até logo!")
            break  # Encerra o loop e finaliza o programa
        case _:
            print("Opção inválida. Tente novamente.")
