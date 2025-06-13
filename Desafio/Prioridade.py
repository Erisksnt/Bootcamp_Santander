# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

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
    key=lambda p: (-Paciente(*p).prioridade(), -p[1], p[2])
)
# Formatação dos pacientes
paciente_prioridade = [f"{nome}, {idade}, {status}" for nome, idade, status in ordem_prioridade]
nomes_prioridade = [nome for nome, _, _ in ordem_prioridade]

# Exibição final
print("Ordem de Atendimento:", ", ".join(nomes_prioridade))


