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
            self.status = 'Urgente'
            return 2
        elif self.idade >= 30 and self.idade <= 59:
            self.status = 'Normal'
            return 1
        else:
            self.status = 'Não precisa de Prioridade'
            return 0
    
# TODO: Exiba a ordem de atendimento com título e vírgulas:
ordem_prioridade = sorted(pacientes, key=lambda p: (-Paciente(*p).prioridade(), p[0]))
paciente_prioridade = (f"{nome}", for nome in ordem_prioridade)
exibir(f"Ordem de atendimento {ordem_prioridade}")


