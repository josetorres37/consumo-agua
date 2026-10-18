# Atividade: Controle de Níveis de Água
# Sistema simples de monitoramento de reservatório

from colorama import init, Fore, Style

# Inicializa o colorama
init()

# Listas com os dados do reservatório
niveis = [1, 2, 3, 4, 5]
situacoes = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

# Função que define a cor conforme o nível informado
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Exibição do monitoramento
print("=== Monitoramento do Reservatório de Água ===")

for i in range(len(niveis)):
    nivel = niveis[i]
    situacao = situacoes[i]
    cor = definir_cor(nivel)

    print(cor + f"Nível {nivel}: {situacao}" + Style.RESET_ALL)

print("=== Fim do monitoramento ===")

# Restauração final do estilo padrão
print(Style.RESET_ALL)