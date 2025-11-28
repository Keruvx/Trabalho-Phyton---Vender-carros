'  ####                      #     #                 ## '
'  #                         #                      #  # '
'  ###    ###  #  #   ###   ###   ##    ###    ##   #      ###  ###'
'  #     #  #  #  #  ##      #     #    #  #  #  #  #     #  #  #  #'
'  #     # ##  #  #    ##    #     #    #  #  #  #  #  #  # ##  #'
'  #      # #   ###  ###      ##  ###   #  #   ##    ##    # #  #'



loginUsuario = [
    {"login": "admin", "senha":"admin", "saldo":0, "telefone":"99999999"},
    {"login": "joji", "senha":"joji", "saldo":150, "telefone":"27996457519"},
    
]
marcasCarro = {
    "algo" : [
    {"marca":"TOYOTA"},
    {"marca":"MAZDA"},
    {"marca": "HONDA"},
    {"marca": "SUBARU"},
    ]
}
listaCarros = [
    
    {"id":1,"modelo": "Corolla", "marca": "TOYOTA", "valor": 150000},
    {"id":2,"modelo": "Corolla Cross", "marca": "TOYOTA", "valor": 250000},
    {"id":3,"modelo": "RX7", "marca": "MAZDA", "valor": 450000},
    {"id":4,"modelo": "Civic", "marca": "HONDA", "valor": 110000},
    {"id":5,"modelo": "WRX", "marca": "SUBARU", "valor": 300000},
    
]

def mostrarMarca():

  
        for i, v in enumerate(marcasCarro["algo"]):
            print(f"Marcas disponíveis:\n{i+1} - {v['marca']}")  

def inventarioCarros():
    
    mostrarMarca()

    escolha_marca = input("Informe a marca desejada (número): ")
    
    marcaEscolhida = escolha_marca
    
    match escolha_marca:
        case "1":
            marcaEscolhida = "TOYOTA"
        case "2":
            marcaEscolhida = "MAZDA"
        case "3":
            marcaEscolhida = "SUBARU"
        case "4":
            marcaEscolhida = "NISSAN"    
        case _:
            print("\nOpção de marca inválida. Tente novamente.")
            return

    print(f"\n--- Carros {marcaEscolhida} Disponíveis ---")
    
    carros_exibidos = 0
    
    for carro in listaCarros: 
        if carro["marca"] == marcaEscolhida:
            modelo = carro["modelo"]
            valor = carro["valor"]
            
            print(f"| Modelo: {modelo:<10} | Valor: R${valor:,.2f} |")
            
            carros_exibidos += 1

    if carros_exibidos == 0:
        print(f"Nenhum veículo encontrado para a marca {marcaEscolhida}.")
        
    print("-------------------------------------------\n")
      
def comprarCarro(usuarioLogado): 
    
    print("\nComprar Carro: ")
    
    mostrarMarca()

    escolha_marca = input("Informe a marca desejada (número): ")
    
    marcaSelecionada = ""
    
    match escolha_marca:
        case "1":
            marcaSelecionada = "TOYOTA"
        case "2":
            marcaSelecionada = "MAZDA"
        case "3":
            marcaSelecionada = "SUBARU"
        case "4":
            marcaSelecionada = "NISSAN"    
        case _:
            print("\nOpção de marca inválida. Tente novamente.")
            return

    print(f"\nCarros {marcaSelecionada} Disponíveis")
    
    carroDisponivel = [] 
    numeroCarro = 0
    
    for carro in listaCarros: 
        if carro["marca"] == marcaSelecionada:
            carroDisponivel.append(carro) 
            
            modelo = carro["modelo"]
            valor = carro["valor"]
            
            print(f"[{numeroCarro + 1}] | Modelo: {modelo:<10} | Valor: R${valor:,.2f} |")
            
            numeroCarro += 1
            
    if numeroCarro == 0:
        print(f"Nenhum veículo encontrado para a marca {marcaSelecionada}.")
        print("------------------------------------------")
        return 

    
    escolhaCarro = input("Escolha o número do carro para comprar (ou 0 para cancelar): ")

    if not escolhaCarro:
        print("\nEntrada inválida. Digite apenas números.")
        return

    escolhaInd = int(escolhaCarro)

    if escolhaInd <= 0 or escolhaInd > numeroCarro:
        print("Compra cancelada ou opção inválida.")
        return

    carroEscolhido = carroDisponivel[escolhaInd - 1]
    
    valorCarro = carroEscolhido["valor"]

    print(f"Confirmação de Compra:")
    print(f"Carro: {carroEscolhido['modelo']} - R${valorCarro:,.2f}")
    print(f"Seu saldo atual: R${usuarioLogado['saldo']:,.2f}")

    if usuarioLogado["saldo"] < valorCarro:
        print("\nSaldo insuficiente para esta compra.\n")
        return
        
    confirmarCompra = input("Confirmar compra? (sim/não): ").lower()
    
    if confirmarCompra == "sim":
        usuarioLogado["saldo"] -= valorCarro*1.25
        
        removerCarro = carroEscolhido['id']
        carroVendidoSairDaLista = -1
        for i, todosCarros in enumerate(listaCarros):
            if todosCarros['id'] == removerCarro:
                carroVendidoSairDaLista = i
                break

        if carroVendidoSairDaLista != -1:
            carroRetirado = listaCarros.pop(carroVendidoSairDaLista)
            print("Compra realizada com sucesso!")
            print("------------------------------------------")
            print(f"Novo saldo: R${usuarioLogado['saldo']:,.2f}")
            print(f"Você comprou um {carroRetirado['modelo']}!")
            print("------------------------------------------")
        else:
            print("Erro ao processar a remoção do carro.")
    else:
        print("Compra cancelada.")
    print("------------------------------------------")
    
def venderCarro(usuarioLogado):
    print("\nVender Carro: ")

    marcaN = input("Informe a marca do carro: ")
    modeloN = input("Informe o modelo do carro: ")
    valorN = int(input("Informe valor: "))

    valorRealDeVenda = valorN*0.88

    print(f"Valor total oferecido pela concessionaria: {valorRealDeVenda}")

    acetas = input("Aceita a proposta? (sim/não): ")

    if acetas == "sim":
        print("\n\nVenda aprovada!! \n\n")

        listaCarros.append({"marca" : marcaN, "modelo": modeloN,"valor" : valorN})
        
        usuarioLogado['saldo'] += valorRealDeVenda
    else:
        return
def alugarCarro(usuarioLogado):
    print("\nComprar Carro: ")
    
    mostrarMarca()

    escolha_marca = input("Informe a marca desejada (número): ")
    
    marcaSelecionada = ""
    
    match escolha_marca:
        case "1":
            marcaSelecionada = "TOYOTA"
        case "2":
            marcaSelecionada = "MAZDA"
        case "3":
            marcaSelecionada = "SUBARU"
        case "4":
            marcaSelecionada = "NISSAN"    
        case _:
            print("\nOpção de marca inválida. Tente novamente.")
            return

    print(f"\nCarros {marcaSelecionada} Disponíveis")
    
    carroDisponivel = [] 
    numeroCarro = 0
    
    for carro in listaCarros: 
        if carro["marca"] == marcaSelecionada:
            carroDisponivel.append(carro) 
            
            modelo = carro["modelo"]
            valor = carro["valor"]
            
            print(f"[{numeroCarro + 1}] | Modelo: {modelo:<10} | Valor: R${valor:,.2f} |")
            
            numeroCarro += 1
            
    if numeroCarro == 0:
        print(f"Nenhum veículo encontrado para a marca {marcaSelecionada}.")
        print("------------------------------------------")
        return 

    
    escolhaCarro = input("Escolha o número do carro para comprar (ou 0 para cancelar): ")

    if not escolhaCarro:
        print("\nEntrada inválida. Digite apenas números.")
        return

    escolhaInd = int(escolhaCarro)

    if escolhaInd <= 0 or escolhaInd > numeroCarro:
        print("Compra cancelada ou opção inválida.")
        return

    carroEscolhido = carroDisponivel[escolhaInd - 1]
    
    valorAluguel = 77
    print(f"Confirmação de Aluguel:")
    dias = int(input("Quantos dias de aluguel"))
    print(f"Carro: {carroEscolhido['modelo']}") 
    print(f"Total de dias{dias}- Valor das diarias R${valorAluguel*dias:,.2f}")
    print(f"Seu saldo atual: R${usuarioLogado['saldo']:,.2f}")

    if usuarioLogado["saldo"] < valorAluguel:
        print("\nSaldo insuficiente para esta compra.\n")
        return
        
    confirmarCompra = input("\nConfirmar compra? (sim/não): ").lower()
    
    if confirmarCompra == "sim":
        usuarioLogado["saldo"] -= valorAluguel
        
        removerCarro = carroEscolhido['id']
        carroVendidoSairDaLista = -1
        for i, todosCarros in enumerate(listaCarros):
            if todosCarros['id'] == removerCarro:
                carroVendidoSairDaLista = i
                break

        if carroVendidoSairDaLista != -1:
            carroRetirado = listaCarros.pop(carroVendidoSairDaLista)
            print("Aluguel realizada com sucesso!")
            print("------------------------------------------")
            print(f"Novo saldo: R${usuarioLogado['saldo']:,.2f}")
            print(f"Você alugou um {carroRetirado['modelo']}, por {dias}!")
            print("------------------------------------------")
        else:
            print("\nErro ao processar a remoção do carro.")
    else:
        print("\nAluguel cancelada.")
    print("------------------------------------------")

def addSaldo(usuarioLogado):

    login = usuarioLogado['login']
    saldo = usuarioLogado['saldo']

    print(f"Usuario {login}\n")
    print(f"Saldo atual {saldo:.2f}\n")
    addSaldo = input("Deseja adicionar saldo? (sim/não): ")
    if addSaldo == "sim":
        nvSaldo = float(input("Digite o valor: "))
        usuarioLogado["saldo"] += (nvSaldo)
    else:
        return

def perfilCliente(usuarioLogado):

    login = usuarioLogado['login']
    saldo = usuarioLogado['saldo']
    telefone = usuarioLogado['telefone']

    print("___________________________________________\n")
    print("-----------------FaustinoCar-----------------")
    print(f"Nome: {login}")
    print(f"Telefone: ({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}")
    print(f"Saldo: R${saldo:.2f}")
    print("---------------------------------------------")
    print("_____________________________________________\n")

def menuEntrada():
    print("Bem-Vindo a FaustinoCar\n")
    print("1 - Entrar")
    print("2 - Cadastrar")
    print("3 - Sair")

def menuCliente(usuarioLogado): 

    while True: 
        print(f"MENU CLIENTE ({usuarioLogado['login']}) ===")
        print("1 - Perfil de usuario")
        print("2 - Inventario de veiculos")
        print("3 - Comprar carro")
        print("4 - Vender carro")
        print("5 - Alugel carro")
        print("6 - Adicionar saldo")
        print("7 - Fazer Logout")


        opcaoCliente = input ("Escolha a opção: ")

        match opcaoCliente:
            case "1":
                perfilCliente(usuarioLogado)
            case "2":
                inventarioCarros()
            case "3":
                comprarCarro(usuarioLogado)
            case "4":
                venderCarro(usuarioLogado)  
            case "5":
                alugarCarro(usuarioLogado) 
            case "6":
                addSaldo(usuarioLogado)
            case "7":
                print("Logout realizado. Voltando ao menu inicial.\n")

                break
            case _:
                print("Opção inválida")

def menuLogin():

    entraL = input("Login: ")
    entraS = input("Senha: ")
    for user in loginUsuario:
        if user["login"] == entraL and user ["senha"] == entraS:
             print("\n✔ Login realizado com sucesso!")
             print(f"Bem-vindo, {entraL}!\n")
             print("==================================")

             menuCliente(user) 
             return
            
    print("\nLogin ou senha incorretos!\n")

def menuCadastro():

    ll = input("Informe Login: ")
    ss = input("Informe Senha: ")
    tt = str(input("Informe Telefone com DDD: "))
    for user in loginUsuario:
        if user["login"] == ll:
            print("\nEsse login já existe. Tente outro.\n")
            return
        
    loginUsuario.append({"login": ll, "senha": ss, "saldo": 0,"telefone":tt})
    print("\nUsuário cadastrado com sucesso!\n")
    

while True:
    menuEntrada()

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            menuLogin()
        case "2":
            menuCadastro()
        case "3":
            print("Saindo")
            break
            
        case _:
            print("Opção inválida!")