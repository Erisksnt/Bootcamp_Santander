# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:
 
def exibir(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

class Paciente:
    def __init__(self, nome, idade, status):
        self.nome = nome
        self.idade = idade
        self.status = status 

    def prioridade(self):
        if self.idade >= 60:
            return 2
    
        elif self.idade >= 30 and self.idade <= 59:
            return 1
        else:
            return 0
    
# TODO: Exiba a ordem de atendimento com título e vírgulas:
list_pacient("Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)