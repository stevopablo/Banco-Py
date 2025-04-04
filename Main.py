import Usuario
import Conta
import Menu
import random

systemON = True
while(systemON):
    Menu.chamar_Menu()
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        try:
            print("Criar Conta")
            nome = input("Digite seu nome: ").capitalize().strip()
            cpf = input("Digite seu CPF: ")
            endereco = input("Digite seu endereço: ")

            user = Usuario.Usuario(nome, cpf, endereco)

            numero = cpf[-4:]
            agencia = random.randint(1000, 9999)
            print("Número da conta gerado: ", numero)
            userAccount = Conta.Conta(numero, user.nome, agencia, user.cpf, user.endereco)

            print(user.info())
            print("Conta criada com sucesso!")
        except ValueError:
            print("Valor inválido, deve ser um número")
    elif opcao == 2:
        try:
            print(userAccount.info())
        except NameError:
            print("Conta não criada!")
    elif opcao == 3:
        try:
            valor = float(input("Digite o valor a depositar: "))
            userAccount.depositar(valor)
        except ValueError:
            print("Valor inválido, deve ser um número")
    elif opcao == 4:
        try:
            valor = float(input("Digite o valor a sacar: "))
            userAccount.sacar(valor)
        except str:
            print("Valor inválido, deve ser um número")
    elif opcao == 5:
        try:
            valor = float(input("Digite o valor a transferir: "))
            conta_destino = input("Digite nome da conta destino: ").capitalize().strip()
            userAccount.transferir(valor, userAccount2)
        except NameError:
            print("Conta não criada!")
    elif opcao == 6:
        print(userAccount.consultar_saldo())
    elif opcao == 7:
        try:
            print(userAccount.extrato)
        except NameError:
            print("Conta não criada!")
    elif opcao == 8:
        systemON = False
    else:
        print("Opção inválida!")