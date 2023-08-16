menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>
"""

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito\n\n")
        valor_deposito = input("Insira o valor do depósito:")
        if int(valor_deposito) > 0:
            saldo += int(valor_deposito)
            extrato.append(f'DEPÓSITO: R${float(valor_deposito):.2f}')
            print(f'O depósito de R${float(valor_deposito):.2f} foi feito!')
        else:
            print("Esse não é um valor válido, tente novamente.")

    if opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor_saque = input("Insira o valor a ser sacado:")
            if int(valor_saque) > 0:
                if int(valor_saque) > limite:
                    print(f'O valor do saque excede o limite, tente novamente.\nLembre-se de que seu limite para saques é de {limite}.')
                elif int(valor_saque) > saldo:
                    print("O valor do saque excede o seu saldo, tente novamente.")
                else:
                    numero_saques += 1
                    saldo -= int(valor_saque)
                    extrato.append(f'SAQUE: R${float(valor_saque):.2f}')
                    print(f'Saque de R${float(valor_saque):.2f} efetuado.')

    if opcao == "e":
        print("Extrato\n\n")
        actions = "\n".join(i for i in extrato)
        print(f'Suas atividades:\n{actions}\n\nSeu saldo atual é de R${float(saldo):.2f}')

    if opcao == "q":
        print("Adeus!")
        break
