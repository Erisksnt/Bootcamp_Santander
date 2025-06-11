# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for _ in range(n):
    linha = input().strip()    
    participantes, tema = linha.rsplit(' ', 1)
    participantes = participantes.strip().replace(",", "")
    tema = tema.strip()
        
    if participantes:
        if tema not in eventos:
            eventos[tema] = []
        eventos[tema].append(participantes)
        
# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {' '.join(participantes)}")