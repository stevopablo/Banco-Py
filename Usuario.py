import datetime as dt
class Usuario:
    def __init__(self, nome, cpf, endereco, horario=None):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.horario = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
    def info(self):
        return f"Info do Usuario\nNome: {self.nome}\nCPF: {self.cpf}\nEndereço: {self.endereco}\nHorário de Criação: {self.horario}"