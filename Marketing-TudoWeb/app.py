# Pesquisa de Satisfação - Empresa TudoWeb

# Inicialização dos contadores
qtd_excelente = 0
qtd_bom = 0
qtd_ruim = 0

# Definição do número de entrevistados (10 para teste / 50 para a versão final)
TOTAL_ENTREVISTADOS = 10

print("--- PESQUISA DE SATISFAÇÃO TUDOWEB ---")

# Estrutura de repetição para coletar os dados dos entrevistados
for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\nEntrevistado nº {i}")
    
    # Coleta de dados básicos
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    # Menu de opções para a opinião
    print("Opiniões disponíveis:")
    print("1: EXCELENTE")
    print("2: BOM")
    print("3: RUIM")
    
    # Loop de validação para garantir que o usuário digite uma opção válida
    while True:
        opiniao = int(input("Digite o número correspondente à sua opinião: "))
        if opiniao in [1, 2, 3]:
            break
        print("Opção inválida! Por favor, digite 1, 2 ou 3.")
    
    # Estrutura de decisão para das respostas
    if opiniao == 1:
        qtd_excelente += 1
    elif opiniao == 2:
        qtd_bom += 1
    elif opiniao == 3:
        qtd_ruim += 1

# Exibição dos resultados finais 
print("\n" + "="*30)
print("       RESULTADO DA PESQUISA       ")
print("="*30)
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")
print(f"-> Quantidade de respostas 'BOM': {qtd_bom} (Informativo)")
print(f"Total de pessoas entrevistadas: {TOTAL_ENTREVISTADOS}")
print("="*30)
