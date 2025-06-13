from datetime import datetime

# TODO: Crie a Classe Veiculo e armazene sua marca, modelo e ano como atributos:
class Veiculo:
    def __init__(self, nome, marca, modelo, ano):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    # TODO: Implemente o método verificar_antiguidade e calcule a diferença entre o ano atual e o ano do veículo:
    def verificar_antiguidade(self):
        ano_atual = datetime.now().year
        idade_veiculo = ano_atual - self.ano 
        if idade_veiculo <= 20:
            print("Veículo novo")
        else:
            print("Veículo antigo")

# Entrada direta
marca = input().strip()
modelo = input().strip()
ano = int(input().strip())

# Instanciando o objeto e verificando a antiguidade
veiculo = Veiculo(marca, modelo, ano)
print(veiculo.verificar_antiguidade())