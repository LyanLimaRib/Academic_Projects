"""
Calculadora de Consumo Energético
----------------------------------
Programa em Python (terminal) para estimar o consumo de energia elétrica
de um aparelho eletrodoméstico, com base na potência (W) e no tempo médio
de uso diário (horas).

Fórmulas utilizadas (conversão de Wh para kWh, dividindo por 1000):
    consumoDia    = (potencia * horasDia) / 1000
    consumoSemana = consumoDia * 7
    consumoMensal = consumoDia * 30
"""


def ler_texto(mensagem):
    """Lê uma string do usuário, garantindo que não seja vazia."""
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("Entrada inválida. Por favor, digite um valor não vazio.\n")


def ler_numero(mensagem, minimo=None, permitir_igual=True):
    """
    Lê um número (inteiro ou decimal) do usuário, validando:
    - se a entrada é realmente numérica;
    - se respeita o valor mínimo informado (quando houver).
    Aceita vírgula ou ponto como separador decimal.
    """
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(entrada)
        except ValueError:
            print("Entrada inválida. Digite apenas números (ex: 500 ou 8.5).\n")
            continue

        if minimo is not None:
            if permitir_igual and valor < minimo:
                print(f"O valor deve ser maior ou igual a {minimo}.\n")
                continue
            if not permitir_igual and valor <= minimo:
                print(f"O valor deve ser maior que {minimo}.\n")
                continue

        return valor


def ler_horas_uso(mensagem):
    """
    Lê o tempo médio de uso diário do aparelho (em horas).
    Um dia possui no máximo 24 horas, então o valor precisa estar
    dentro do intervalo de 1 a 24 horas.
    """
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(entrada)
        except ValueError:
            print("Entrada inválida. Digite apenas números (ex: 8 ou 5.5).\n")
            continue

        # Validação: valor acima do máximo permitido (24 horas em um dia)
        if valor > 24:
            print("Valor de horas inválido! O valor deve ser menor ou igual a 24 horas.\n")
            continue

        # Validação: valor abaixo do mínimo permitido (1 hora)
        if valor < 1:
            print("Valor de horas inválido! O valor deve ser maior ou igual a 1 hora.\n")
            continue

        return valor


def formatar_numero(valor):
    """Formata um número removendo casas decimais desnecessárias (ex: 8.0 -> 8)."""
    if valor == int(valor):
        return str(int(valor))
    return f"{valor:.2f}".rstrip("0").rstrip(".")


def calcular_consumo(potencia, horas_dia):
    """
    Calcula o consumo estimado de energia em kWh.
    consumoDia = (potencia em W * horas de uso por dia) / 1000
    """
    consumo_dia = (potencia * horas_dia) / 1000
    consumo_semana = consumo_dia * 7
    consumo_mensal = consumo_dia * 30
    return consumo_dia, consumo_semana, consumo_mensal


def exibir_resultado(aparelho, potencia, horas_dia, consumo_dia, consumo_semana, consumo_mensal):
    """Exibe o resumo formatado do consumo estimado."""
    print("\n" + "=" * 40)
    print("     CALCULADORA DE CONSUMO ENERGÉTICO")
    print("=" * 40 + "\n")
    print(f"Aparelho: {aparelho}")
    print(f"Potência: {formatar_numero(potencia)} W")
    print(f"Horas de uso por dia: {formatar_numero(horas_dia)} horas")
    print("\nConsumo estimado:")
    print(f"- Por dia:    {consumo_dia:.2f} kWh")
    print(f"- Por semana: {consumo_semana:.2f} kWh")
    print(f"- Por mês:    {consumo_mensal:.2f} kWh")
    print("=" * 40 + "\n")


def perguntar_continuar():
    """Pergunta ao usuário se deseja calcular outro aparelho e valida a resposta."""
    respostas_sim = ("s", "sim")
    respostas_nao = ("n", "nao", "não")
    while True:
        resposta = input("Deseja calcular o consumo de outro aparelho? (s/n): ").strip().lower()
        if resposta in respostas_sim:
            return True
        if resposta in respostas_nao:
            return False
        print("Resposta inválida. Digite 's' para sim ou 'n' para não.\n")


def main():
    """Função principal: controla o fluxo do programa em um laço de repetição."""
    continuar = True
    while continuar:
        # Etapa 1: dados do aparelho
        aparelho = ler_texto("Digite o nome do aparelho eletrodoméstico: ")
        potencia = ler_numero(
            "Digite a potência do aparelho em Watts (W): ", minimo=0, permitir_igual=False
        )
        horas_dia = ler_horas_uso(
            "Digite o tempo médio de uso diário em horas (1 a 24): "
        )

        # Etapa 2: cálculo do consumo
        consumo_dia, consumo_semana, consumo_mensal = calcular_consumo(potencia, horas_dia)

        # Etapa 3: exibição do resultado
        exibir_resultado(aparelho, potencia, horas_dia, consumo_dia, consumo_semana, consumo_mensal)

        # Etapa 4: pergunta se deseja repetir
        continuar = perguntar_continuar()

    print("\nPrograma encerrado. Obrigado por utilizar a calculadora!\n")


if __name__ == "__main__":
    main()
