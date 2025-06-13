# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

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
        if self.status.lower() == "urgente":
            return 3
        elif self.idade >= 60:
            return 2
        elif self.idade >= 30:
            return 1
        else:
            return 0

# Ordenação por prioridade e nome
ordem_prioridade = sorted(
    pacientes,
    key=lambda p: (-Paciente(*p).prioridade(), p[0])
)

# Formatação dos pacientes
paciente_prioridade = [f"{nome}, {idade}, {status}" for nome, idade, status in ordem_prioridade]
nomes_prioridade = [nome for nome, _, _ in ordem_prioridade]

# Exibição final
exibir(
    "Ordem de atendimento:",
    *paciente_prioridade,
    Total=len(pacientes)
    )
#list_pacient("Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)


