import datetime as dt

class Conta:
    def __init__(self, numero, titular, agencia, cpf, endereco, saldo=0, horario=None):
        self.numero = numero
        self.titular = titular
        self.cpf = cpf
        self.endereco = endereco
        self.saldo = saldo
        self.agencia = agencia
        self.extrato = []
        self.horario = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
    def info(self):
        return f"Nome do Titular\t {self.titular}\n Número da Conta\t {self.numero}\n Agência\t {self.agencia}\n CPF\t {self.cpf}\n Endereço\t {self.endereco}\n Saldo\t {self.saldo}\n Horário de Crialção\t {self.horario}"
    
    def consultar_saldo(self):
        return f'Saldo atual é de : {self.saldo}'
    
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: {valor} em {dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Saque de {valor} realizado com sucesso. Novo saldo: {self.saldo}")
            
    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido, deve ser maior que zero")
        else:
            self.saldo += valor
            self.extrato.append(f"Depósito: {valor} em {dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Depósito de {valor} realizado com sucesso. Novo saldo: {self.saldo}")
        
    def transferir(self, valor, conta_destino):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            conta_destino.depositar(valor)
            self.saldo -= valor
            self.extrato.append(f"Transferência: {valor} para {conta_destino.titular} em {dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Transferência de {valor} realizada com sucesso. Novo saldo: {self.saldo}")