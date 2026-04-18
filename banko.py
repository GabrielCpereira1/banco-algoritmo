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

        

       
    
            
