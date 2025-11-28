# Adicionei um usuário de exemplo com saldo para testar o perfil
loginUsuario = [
    {"login": "admin", "senha": "admin", "saldo": 0},
    {"login": "teste", "senha": "123", "saldo": 50.00}
]

# Funções placeholder (para evitar erros de nome não definido)
def inventCar():
    print("Inventário de carros... (Implementação futura)\n")

def saldoCliente(usuario_logado): # Adicionei o parâmetro que precisa
    print(f"Função Saldo Cliente. Saldo atual: R${usuario_logado['saldo']:.2f}")
    print("Adicionando saldo... (Implementação futura)\n")
    
def menu():
    print("Bem-Vindo a FaustinoCar\n")
    print("1 - Entrar")
    print("2 - Cadastrar")
    print("3 - Sair")

def perfilCliente(usuario_logado): # <-- 1. Recebe o dicionário do usuário logado
    """Exibe os dados do usuário logado."""
    # 2. Código corretamente indentado dentro da função
    login = usuario_logado['login']
    saldo = usuario_logado['saldo']

    print("___________________________________________\n")
    print("-----------------FaustinoCar-----------------")
    print(f"Nome: {login}")
    print(f"Saldo: R${saldo:.2f}")
    print("---------------------------------------------")
    print("_____________________________________________\n")


def menuCliente(usuario_logado): # <-- 3. Recebe o dicionário do usuário logado

    while True: 
        print(f"\n=== MENU CLIENTE ({usuario_logado['login']}) ===")
        print("1 - Perfil de usuario")
        print("2 - Inventario de veiculos")
        print("3 - Adicionar saldo")
        print("4 - Fazer Logout")

        opcaoCliente = input ("Escolha a opção: ")

        match opcaoCliente:
            case "1":
                # 4. Repassa o dicionário para a função
                perfilCliente(usuario_logado)
            case "2":
                inventCar()
            case "3":
                # 5. Repassa o dicionário para a função
                saldoCliente(usuario_logado)
            case "4":
                print("👋 Logout realizado. Voltando ao menu inicial.\n")
                break
            case _:
                print("Opção inválida")

def menuLogin():
    entraL = input("Login: ")
    entraS = input("Senha: ")
    
    for user in loginUsuario:
        if user["login"] == entraL and user["senha"] == entraS:
             print("\n✔ Login realizado com sucesso!")
             print(f"Bem-vindo, {entraL}!\n")
             print("==================================")
             # 6. Passa o DICIONÁRIO 'user' completo
             menuCliente(user) 
             return
            
    print("\n❌ Login ou senha incorretos!\n")

def menuCadastro():
    ll = input("Informe Login: ")
    ss = input("Informe Senha: ")
    for user in loginUsuario:
        if user["login"] == ll:
            print("\n❌ Esse login já existe. Tente outro.\n")
            return
        
    # 7. Garante que o novo usuário tenha o campo 'saldo'
    loginUsuario.append({"login": ll, "senha": ss, "saldo": 0})
    print("\n✔ Usuário cadastrado com sucesso!\n")
    

while True:
    menu()

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            menuLogin()
        case "2":
            menuCadastro()
        case "3":
            print("Saindo...")
            break
        case _:
            print("Opção inválida!")