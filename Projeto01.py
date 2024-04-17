Saques = ""
limite = 0
saldo = 0   
while True:
    print("Qual opcao voce deseja: ")
    print("1)Sacar\n2)Depositar\n3)Extrato\n4)Sair")
    entrada = int(input("Digite a opcao Desejada: "))
    if entrada == 1:
            print(saldo)
            saque = int(input("Qual valor deseja sacar: "))
            if(saque <= saldo):
                limite += saque
                if limite > 500:
                    print("impossivel sacar limite max atigido!!!")
                else:
                    saldo-= saque
                    Saques+= f"{saque} "
            else:
                print("Sem valor!!!")
    
    elif entrada == 2:
            deposito = int(input("Qual valor deseja depositar: "))
            saldo+= deposito
            

    elif entrada == 3:
         print(Saques)
        
    elif entrada == 4:
        break
    else:
        print("Opcao invalida!!!")


