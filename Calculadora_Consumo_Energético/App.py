def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("Entrada inválida, por favor, digite um valor não vazio.\n")


def ler_numero(mensagem, minimo=None, permitir_igual=True):
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(entrada)
        except ValueError:
            print("Entrada inválida, digite apenas números (ex: 500 ou 8.5).\n")
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
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(entrada)
        except ValueError:
            print("Entrada inválida, digite apenas números (ex: 8 ou 5.5).\n")
            continue
        if valor > 24:
            print("Valor de horas inválido! O valor deve ser menor que 24 horas.\n")
            continue
        if valor < 1:
            print("Valor de horas inválido! O valor deve ser maior que 1 hora.\n")
            continue
        return valor


def formatar_numero(valor):
    if valor == int(valor):
        return str(int(valor))
    return f"{valor:.2f}".rstrip("0").rstrip(".")


def calcular_consumo(potencia, horas_dia):
    consumo_dia = (potencia * horas_dia) / 1000
    consumo_semana = consumo_dia * 7
    consumo_mensal = consumo_dia * 30
    return consumo_dia, consumo_semana, consumo_mensal


def exibir_resultado(aparelho, potencia, horas_dia, consumo_dia, consumo_semana, consumo_mensal):
    print("")
    print("CALCULADORA DE CONSUMO ENERGÉTICO")
    print("")
    print(f"Aparelho consultado: {aparelho}")
    print(f"Potência média do aparelho em Watts: {formatar_numero(potencia)} W")
    print(f"Tempo médio de uso por dia: {formatar_numero(horas_dia)} horas")
    print("\nConsumo estimado:")
    print(f"- Por dia:    {consumo_dia:.2f} kWh")
    print(f"- Por semana: {consumo_semana:.2f} kWh")
    print(f"- Por mês (Considerando 30 dias):    {consumo_mensal:.2f} kWh")
    print("")


def perguntar_continuar():
    respostas_sim = ("s", "sim")
    respostas_nao = ("n", "nao", "não")
    while True:
        resposta = input("Deseja calcular o consumo de outro aparelho?: ").strip().lower()
        if resposta in respostas_sim:
            return True
        if resposta in respostas_nao:
            return False
        print("Resposta inválida. Digite 'sim' ou 'não'.\n")


def main():
    continuar = True
    while continuar:
        aparelho = ler_texto("Digite o nome do eletrodoméstico: ")
        potencia = ler_numero(
            "Digite a potência do aparelho em Watts (W): ", minimo=0, permitir_igual=False
        )
        horas_dia = ler_horas_uso(
            "Digite o tempo médio de uso diário em horas: "
        )
        consumo_dia, consumo_semana, consumo_mensal = calcular_consumo(potencia, horas_dia)
        exibir_resultado(aparelho, potencia, horas_dia, consumo_dia, consumo_semana, consumo_mensal)
        continuar = perguntar_continuar()

    print("\nPrograma encerrado, obrigado por utilizar a calculadora!\n")


if __name__ == "__main__":
    main()