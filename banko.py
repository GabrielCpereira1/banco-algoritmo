usuario_correto = "Edson Dalbogas"
senha_correta = "Edson123"

saldo = 500.00
limite = 5000.00

def menu():
    while True:
     print("\n- Univille Internet Banking -")
     print("1. Acessar conta")
     print("2. Encerrar sessão")
     opcao = input("Escolha sua opção: ")

     if opcao == "1":
         if login():
             menu_principal()
     elif opcao == "2":
         print("Sessão Encerrada.")
         break
     else:
         print("Opção inválida.")

def login():
    tentativas = 3
    while tentativas > 0:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario == usuario_correto and senha == senha_correta:
            print("Login realizado com sucesso")
            return True
        else:
            tentativas -= 1
            if tentativas == 0:
                print(f"Usuário ou senha incorretos. Tentativas restantes: {tentativas}")
            else:
                print("Sem mais tentativas.")
                print("Sessão Encerrada.")
                exit()

def menu_principal():
    global saldo

    while True:
        print("\n--Univille Internet Banking--")
        print("1. Consultar Saldo")
        print("2. Realizar Saque")
        print("3. Realizar Depósito")
        print("4. Consultar Limite")
        print("5. Encerrar Sessão")    
        opcao = input("Escolha sua opção:")
        if opcao == "1":
            consultar_saldo()
        elif opcao == "2":
            realizar_saque()
        elif opcao == "3":
            realizar_deposito()
        elif opcao == "4":
            consultar_limite()
        elif opcao == "5":
            print("Sessão Encerrada.")
            break
        else:
            print("Opção inválida.")

def consultar_saldo():
    print(f"Saldo R$: {saldo:.2f}")

def realizar_saque():
    global saldo
    try:
        valor = float(input("Valor do saque: R$ "))
        
        if valor <= 0:
            print("Valor inválido.")
        elif valor > (saldo + limite):
            print("Saldo insuficiente.")
        else:
            saldo -= valor
            print("Saque realizado")
    except ValueError:
        print("Valor inválido.")

def realizar_deposito():
    global saldo
    try:
        valor = float(input("Valor do depósito: R$ "))
        
        if valor <= 0:
            print("Valor inválido.")
        else:
            saldo += valor
            print("Depósito realizado")
    except ValueError:
        print("Valor inválido.")

def consultar_limite():
    print(f"Limite da Conta R$: {limite:.2f}")

# Executar o sistema
menu()

       

       
    
            
