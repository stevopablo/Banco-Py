import Usuario
import Conta
import random
print("Sistema de Controle de Conta Bancária")

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


user2 = Usuario.Usuario("Lucas", "12345678900", "Rua A, 123")
print(user2.info())

userAccount2 = Conta.Conta("1234", user2.nome, 5678, user2.cpf, user2.endereco)
print(userAccount2.info())
userAccount2.depositar(1000)
userAccount2.transferir(500, userAccount)
