usuario_correto = "Edson Dalbogas"
senha_correta = "Edson123"
saldo = 300.00
limite = 5000.00
def menu():
    while True:
    print("\n--Univille Internet Banking--")
    print("1. Acessar conta")
    print("2. Encerrar sessão")
    opcao = input("Digite a opção desejada:")
    if opcao == "1":
        if login():
            menu_principal()
    elif opcao == "2":
        print("Sessão Encerrada")
        break
    
            
