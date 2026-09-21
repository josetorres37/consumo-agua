#Sistema de classificação do consumo de água
#Projeto: consumo-agua
print("=" * 40)
print(" SISTEMA DE CONSUMO CONCIENTE DE ÁGUA")
print("=" * 0)

tipo_imovel = input(
    "Digite o tipo de imóvel "
).strip().lower()

try:
    consumo = float(
        input("Digite o consumo mensal de água em m³: ")
         .replace(",", ".")
    )
except ValueError:
    print("Erro: informe um valor numérico válido para o consumo. ")
    exit()

print("\nResultado da classificação:")

if tipo_imovel == "comercial":
    print("Tarifa comercial aplicada - consulte o plano corporativo.")

elif tipo_imovel == "apartamento" and consumo < 10:
    print("Consumo econômico - excelente controle de água!")

elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo <=25:
    print("consumo moderado - dentro do padrão residencial.")

elif tipo_imovel == "casa" or tipo_imovel == "apartamento":
    print(
        "Consumo excessivo - adote medidas de economia "
        "e verifique vazamentos."
    )

else:
    print(
        "Tipo de imóvel inválido. "
        "Informe comercial, casa ou apartamento."
    )
