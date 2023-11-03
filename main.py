# Func Defs:


def menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Usuarios
    [c] Contas
    [q] Sair
    =>
    """

    return input(menu)


def main():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor_deposito = float(input("Insira o valor do depósito:"))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        if opcao == "s":
            valor_saque = float(input("Insira o valor a ser sacado:"))
            saldo, extrato = sacar(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )

        if opcao == "e":
            emitir_extrato(saldo, extrato=extrato)

        if opcao == "q":
            break

        if opcao == "c":
            criar_conta(AGENCIA, usuarios, contas)

        if opcao == "u":
            criar_usuario(usuarios)


def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato.append(f"DEPÓSITO: R${valor_deposito:.2f}")
        print(f"O depósito de R${valor_deposito:.2f} foi feito!")
    else:
        print("Esse não é um valor válido, tente novamente.")

    return saldo, extrato


def sacar(*, saldo, valor_saque, extrato, limite, numero_saques, LIMITE_SAQUES):
    if numero_saques < LIMITE_SAQUES:
        if valor_saque > 0:
            if valor_saque > limite:
                print(
                    f"O valor do saque excede o limite, tente novamente.\nLembre-se de que seu limite para saques é de {limite}."
                )
            elif valor_saque > saldo:
                print("O valor do saque excede o seu saldo, tente novamente.")
            else:
                numero_saques += 1
                saldo -= int(valor_saque)
                extrato.append(f"SAQUE: R${valor_saque:.2f}")
                print(f"Saque de R${valor_saque:.2f} efetuado.")
        else:
            print("O valor do saque deve ser maior que zero!\nTente novamente!")
    else:
        print("O número de saques diários já foi atingido!")
    return saldo, extrato


def emitir_extrato(saldo, /, *, extrato):
    print("Extrato\n\n")
    actions = "\n".join(i for i in extrato)
    print(f"Suas atividades:\n{actions}\n\nSeu saldo atual é de R${float(saldo):.2f}")


def checar_usuario(cpf, usuarios):
    for i in usuarios:
        if i["cpf"] == cpf:
            return True
    return False


def criar_usuario(usuarios):
    cpf = input("Digite seu cpf:")
    usuario = checar_usuario(cpf, usuarios)

    if usuario:
        print("Esse usuario já foi cadastrado")
        return

    nome = input("Informe seu nome:")
    nascimento = input("Informe sua data de nascimento")
    endereco = input("Informe seu endereço")

    usuarios.append(
        {"nome": nome, "cpf": cpf, "nascimento": nascimento, "endereco": endereco}
    )


def criar_conta(AGENCIA, usuarios, contas):
    cpf = input("Insira seu CPF:")
    usuario = checar_usuario(cpf, usuarios)

    if usuario:
        print("A Conta foi criada com sucesso!")
        contas.append(
            {
                "agencia": AGENCIA,
                "usuario": [user for user in usuarios if user["cpf"] == cpf][0],
                "numero_conta": (len(contas) + 1),
            }
        )
    else:
        print("Usuário não encontrado! Tente novamente!")


main()
