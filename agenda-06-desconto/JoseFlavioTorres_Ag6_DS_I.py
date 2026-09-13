# =============================================================================
# SISTEMA DE DESCONTO PROGRESSIVO 
# =============================================================================

def calcular_desconto():
    while True:
        print("\n" + "-" * 50)
        print("      SISTEMA DE DESCONTO PROGRESSIVO      ")
        print("-" * 50)
        
        # 1. ENTRADA DINÂMICA E CONDIÇÃO DE PARADA (LOOP DE REPETIÇÃO)
        try:
            # Captura a entrada, remove espaços extras (.strip) e padroniza em minúsculas (.lower)
            entrada = input("Digite o valor da compra (R$) ou 'sair' para encerrar: ").strip().lower()
            
            # Critério para quebrar o loop e fechar o programa de forma limpa
            if entrada == 'sair':
                print("\n[SISTEMA] Rotina finalizada com sucesso. Até logo!")
                break
                
            valor_compra = float(entrada)
            if valor_compra < 0:
                print("[ERRO] O valor da compra não pode ser negativo! Tente novamente.")
                continue # Volta para o início do laço sem quebrar o programa
                
        except ValueError:
            print("[ERRO] Entrada inválida! Digite números válidos (ex: 150.75) ou a palavra 'sair'.")
            continue # Ignora o erro e reinicia o loop para a próxima digitação

        # 2. ESTRUTURA DE DECISÃO
        if valor_compra < 200.00:
            porcentagem = 5
        elif valor_compra < 300.00: 
            porcentagem = 10
        else: 
            porcentagem = 15

        # 3. CÁLCULO DOS VALORES
        valor_desconto = valor_compra * (porcentagem / 100)
        valor_final = valor_compra - valor_desconto

        # 4. SAÍDA FORMATADA NO TERMINAL
        print("\n" + "=" * 50)
        print("                    RESUMO DO PEDIDO                    ")
        print("=" * 50)
        print(f"Valor original da compra: R$ {valor_compra:,.2f}")
        print(f"Desconto aplicado:       {porcentagem}%")
        print(f"Valor do desconto:        R$ {valor_desconto:,.2f}")
        print("-" * 50)
        print(f"VALOR TOTAL A PAGAR:      R$ {valor_final:,.2f}")
        print("=" * 50)

if __name__ == "__main__":
    calcular_desconto()