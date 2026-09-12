# Realizei as importações de funções que serão utilizadas no código, como datetime para manipulação de datas e decimal para cálculos precisos com valores monetários.
from datetime import datetime, date
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP 
CASAS_DECIMAIS = Decimal("0.01")

# Função para arredondar valores monetários para duas casas decimais, utilizando o método de arredondamento "round half up".
def arredondar_moeda(valor):
    return valor.quantize(CASAS_DECIMAIS, rounding=ROUND_HALF_UP)

# Função para calcular o desconto com base no valor da compra, aplicando diferentes percentuais de desconto conforme faixas de valor.
def calcular_desconto(valor_da_compra):
    if valor_da_compra < Decimal("150.00"):
        percentual_desconto = Decimal("0.00"
    )
    elif valor_da_compra < Decimal("300.00"):
        percentual_desconto = Decimal("0.15"
    )
    elif valor_da_compra < Decimal("400.00"):
        percentual_desconto = Decimal("0.12"
    )
    elif valor_da_compra < Decimal("500.00"):
        percentual_desconto = Decimal("0.08"
    )
    elif valor_da_compra < Decimal("600.00"):
        percentual_desconto = Decimal("0.10"
    )
    elif valor_da_compra < Decimal("850.00"):
        percentual_desconto = Decimal("0.12"
    )
    else:
      percentual_desconto = Decimal("0.20"
    )
    valor_desconto = arredondar_moeda(valor_da_compra * percentual_desconto)
    valor_final = arredondar_moeda(valor_da_compra - valor_desconto)
    return percentual_desconto, valor_desconto, valor_final

# Função para ler o valor da compra do usuário, garantindo que a entrada seja válida e convertendo-a para um valor Decimal.
def ler_valor_da_compra():
    while True:
        entrada = input("Digite o valor total da compra: R$ ").strip()

        try:
            if not entrada:
                raise ValueError
            entrada_normalizada = entrada.replace(" ", "")
            entrada_normalizada = entrada_normalizada.replace("R$", "")
            entrada_normalizada = entrada_normalizada.replace("r$", "")
            
            if "," in entrada_normalizada:
                entrada_normalizada = entrada_normalizada.replace(".", "")
                entrada_normalizada = entrada_normalizada.replace(",", ".")

            valor_da_compra = Decimal(entrada_normalizada)
            if (not valor_da_compra.is_finite() or valor_da_compra <= 0):
                print("Valor inválido, digite um valor maior que zero.")
                continue

            return arredondar_moeda(valor_da_compra)
        
        except (InvalidOperation, ValueError):
            print("Entrada inválida, digite apenas um valor numérico positivo.")

# Função para formatar valores monetários em reais, utilizando vírgula como separador decimal e ponto como separador de milhar.
def formatar_moeda(valor):
    valor = arredondar_moeda(valor)
    valor_formatado = f"{valor:,.2f}"

    valor_formatado = (
        valor_formatado
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", "."))

    return f"R$ {valor_formatado}"

# Função para gerar um protocolo único para cada consulta, utilizando a data atual e o número da consulta.
def gerar_protocolo(numero_consulta):
    data_atual = datetime.now().strftime("%d%m%y")
    return f"DSC-{data_atual}-{numero_consulta:04d}"

# Função para perguntar ao usuário se deseja realizar outra consulta, aceitando respostas "sim" ou "não" (ou suas variações).
def nova_consulta():
    respostas_sim = {"sim", "s"}
    respostas_nao = {"não", "nao", "n"}

    while True:
        resposta = input("Deseja realizar outra consulta? ").strip().lower()

        if resposta in respostas_sim:
            return True

        if resposta in respostas_nao:
            return False

        print("Opção inválida, digite SIM ou NÃO")

# Função para mostrar o resultado da consulta, incluindo protocolo, valor da compra, percentual aplicado, valor do desconto e valor final com desconto.
def mostrar_resultado(protocolo, valor_compra, percentual_aplicado, valor_desconto, valor_final):
    percentual_formatado = int(percentual_aplicado * 100)

    print("")
    print("RESULTADO DA CONSULTA")
    print("")
    print(f"Protocolo: {protocolo}"
    )
    print(f"Valor da compra: {formatar_moeda(valor_compra)}"
    )
    print(f"Percentual de desconto: {percentual_formatado}%"
    )
    print(f"Economia: {formatar_moeda(valor_desconto)}"
    )
    print(f"Valor com desconto: {formatar_moeda(valor_final)}"
    )
    print(f"Data da Consulta: {date.today()}"
    )
    print("")

# Função para mostrar um resumo de todas as consultas realizadas na sessão, incluindo total de compras, total de descontos e total final.
def mostrar_resumo(historico):
    protocolo_sessao = gerar_protocolo(0)
    quantidade_consultas = len(historico)

    total_compras = sum((consulta["valor_compra"] 
        for consulta 
        in historico),Decimal("0.00")
    )    
    total_descontos = sum((consulta["valor_desconto"] 
        for consulta
        in historico), Decimal("0.00")
    )
    total_final = sum((consulta["valor_final"]
        for consulta
        in historico), Decimal("0.00")
    )
    print("")
    print("RESUMO DAS CONSULTAS")
    print("")

    for numero, consulta in enumerate(historico, start=1):
        percentual = int(
            consulta["percentual_desconto"] * 100)

        print("")
        print(f"Consulta {numero}"
        )
        print(f"Protocolo: {consulta['protocolo']}"
        )
        print(f"Valor da compra: "f"{formatar_moeda(consulta['valor_compra'])}"
        )
        print(f"Percentual aplicado: {percentual}%"
        )
        print(f"Desconto concedido: " f"{formatar_moeda(consulta['valor_desconto'])}"
        )
        print(f"Valor final: " f"{formatar_moeda(consulta['valor_final'])}"
        )
        print("")

    print("")
    print("TOTAL DA SESSÃO")
    print("")
    print(f"Protocolo da sessão {protocolo_sessao}"
    )
    print(f"Quantidade de consultas: {quantidade_consultas}"
    )
    print(f"Total original das compras: {formatar_moeda(total_compras)}"
    )
    print(f"Total concedido em descontos: {formatar_moeda(total_descontos)}"
    )
    print(f"Total final das compras: {formatar_moeda(total_final)}"
    )
    print("")

# Função principal que gerencia o fluxo do programa, incluindo a leitura de valores, cálculo de descontos, armazenamento do histórico e exibição de resultados.
def main():
    historico = []
    numero_consulta = 1

    while True:
        print("")
        print("CÁLCULO DE DESCONTO")
        print("")

        valor_compra = ler_valor_da_compra()
        (percentual_aplicado, 
        valor_do_desconto, 
        valor_final ) = calcular_desconto(valor_compra)

        protocolo = gerar_protocolo(numero_consulta)
        consulta = {
        "protocolo": protocolo,
        "data_hora": datetime.now(),
        "valor_compra": valor_compra,
        "percentual_desconto": percentual_aplicado,
        "valor_desconto": valor_do_desconto,
        "valor_final": valor_final
        }

        historico.append(consulta)
        mostrar_resultado(
        protocolo,
        valor_compra,
        percentual_aplicado,
        valor_do_desconto,
        valor_final
        )

        numero_consulta += 1

        if not nova_consulta():
            mostrar_resumo(historico)

            print("ENCERRANDO SISTEMA")
            print("")
            break


if __name__ == "__main__":
    main()
