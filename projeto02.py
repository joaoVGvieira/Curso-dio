class ContaCorrente:
    def __init__(self, nome, cpf, agencia="0001", saldo=0, limite_saque=500, saques_restantes=3):
        self.nome = nome
        self.cpf = cpf
        self.agencia = agencia
        self.saldo = saldo
        self.limite_saque = limite_saque
        self.saques_restantes = saques_restantes
        self.extrato = []

    def saque(self, valor):
        if self.saques_restantes <= 0:
            print("Limite de saques atingido para esta conta.")
            return False
        if valor > self.limite_saque:
            print("Valor de saque excede o limite permitido.")
            return False
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False

        self.saldo -= valor
        self.extrato.append(f"Saque: -R${valor:.2f}")
        self.saques_restantes -= 1
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
        return True

    def deposito(self, valor):
        self.saldo += valor
        self.extrato.append(f"Depósito: +R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def extrato_exibir(self):
        print(f"Extrato para {self.nome} (CPF: {self.cpf}, Agência: {self.agencia}):")
        for item in self.extrato:
            print(item)
        print(f"Saldo atual: R${self.saldo:.2f}")


def cadastrar_cliente(clientes):
    cpf = input("Qual o seu CPF: ")
    for cliente in clientes:
        if cpf == cliente.cpf:
            print("Cliente já cadastrado.")
            return
    nome = input("Digite seu nome: ")
    clientes.append(ContaCorrente(nome, cpf))
    print(f"Cliente {nome} cadastrado com sucesso.")


def cadastrar_conta(usuarios, contas):
    cpf = input("Qual o seu CPF: ")
    for usuario in usuarios:
        if cpf == usuario.cpf:
            contas.append(usuario)
            print(f"Conta cadastrada para {usuario.nome} (CPF: {usuario.cpf}, Agência: {usuario.agencia}).")
            return
    print("Usuário não encontrado.")


def menu_principal():
    print("=== Menu ===")
    print("1. Saque")
    print("2. Depósito")
    print("3. Extrato")
    print("4. Cadastrar Cliente")
    print("5. Cadastrar Conta")
    print("6. Sair")


clientes = []
contas = []

while True:
    menu_principal()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Saque
        cpf = input("Digite o CPF: ")
        for conta in contas:
            if cpf == conta.cpf:
                valor_saque = float(input("Digite o valor do saque: "))
                conta.saque(valor_saque)
                break
        else:
            print("Cliente não encontrado.")
    elif opcao == "2":
        # Depósito
        cpf = input("Digite o CPF: ")
        for conta in contas:
            if cpf == conta.cpf:
                valor_deposito = float(input("Digite o valor do depósito: "))
                conta.deposito(valor_deposito)
                break
        else:
            print("Cliente não encontrado.")
    elif opcao == "3":
        # Extrato
        cpf = input("Digite o CPF: ")
        for conta in contas:
            if cpf == conta.cpf:
                conta.extrato_exibir()
                break
        else:
            print("Cliente não encontrado.")
    elif opcao == "4":
        # Cadastrar Cliente
        cadastrar_cliente(clientes)
    elif opcao == "5":
        # Cadastrar Conta
        cadastrar_conta(clientes, contas)
    elif opcao == "6":
        # Sair
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")


