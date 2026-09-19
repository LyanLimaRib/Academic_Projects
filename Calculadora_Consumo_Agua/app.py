from random import randint
from datetime import datetime


def solicitar_tipo_imovel():
    while True:
        print("-" * 30)
        print("Qual é o tipo de imóvel?")
        print("")
        print("1. Comercial")
        print("2. Casa")
        print("3. Apartamento")
        print("")

        resposta = input("Digite a opção ou o nome do imóvel: ").strip().lower()

        if resposta == "1" or resposta == "comercial":
            return "Comercial"
        elif resposta == "2" or resposta == "casa":
            return "Casa"
        elif resposta == "3" or resposta == "apartamento":
            return "Apartamento"
        else:
            print(
                "Tipo de imóvel inválido, escolha entre as opções: Comercial, Casa ou Apartamento.")


def solicitar_consumo():
    while True:
        entrada = input(
            "Qual é o consumo mensal de água em m³? ").strip().replace(",", ".")

        try:
            consumo = float(entrada)

            if consumo < 0:
                print("O consumo não pode ser negativo.")
            else:
                return consumo

        except ValueError:
            print("Consumo inválido, digite um número.")


def classificar_consumo(tipo_imovel, consumo):
    if tipo_imovel == "Apartamento" and consumo < 10:
        return "Consumo econômico"

    elif tipo_imovel in ("Apartamento", "Casa") and consumo <= 25:
        return "Consumo moderado"

    elif consumo > 25:
        return "Consumo excessivo"

    elif tipo_imovel == "Comercial":
        return "Consumo comercial dentro do limite de 25 m³"

    else:
        return "Classificação não definida"


def calcular_valor(tipo_imovel, consumo):

    if tipo_imovel in ("Casa", "Apartamento"):
        if consumo < 10:
            valor = 82.32
            descricao = "Valor fixo mensal de R$ 82,32"

        elif consumo <= 20:
            tarifa = 2.79
            valor = consumo * tarifa
            descricao = "R$ 2,79 por m³"

        elif consumo <= 30:
            tarifa = 2.82
            valor = consumo * tarifa
            descricao = "R$ 2,82 por m³"

        elif consumo <= 60:
            tarifa = 2.88
            valor = consumo * tarifa
            descricao = "R$ 2,88 por m³"

        elif consumo <= 100:
            tarifa = 4.25
            valor = consumo * tarifa
            descricao = "R$ 4,25 por m³"

        else:
            tarifa = 9.68
            valor = consumo * tarifa
            descricao = "R$ 9,68 por m³"

    else:
        if consumo < 10:
            valor = 97.53
            descricao = "Valor fixo mensal de R$ 97,53"

        elif consumo <= 20:
            tarifa = 3.89
            valor = consumo * tarifa
            descricao = "R$ 3,89 por m³"

        elif consumo <= 30:
            tarifa = 3.95
            valor = consumo * tarifa
            descricao = "R$ 3,95 por m³"

        elif consumo <= 60:
            tarifa = 4.00
            valor = consumo * tarifa
            descricao = "R$ 4,00 por m³"

        elif consumo <= 100:
            tarifa = 5.96
            valor = consumo * tarifa
            descricao = "R$ 5,96 por m³"

        else:
            tarifa = 13.54
            valor = consumo * tarifa
            descricao = "R$ 13,54 por m³"

    return valor, descricao


def gerar_protocolo(inicio, fim):
    return randint(inicio, fim)


def exibir_resultado(
    protocolo_sessao,
    protocolo_consulta,
    data_hora_consulta,
    tipo_imovel,
    consumo,
    classificacao,
    tarifa_aplicada,
    valor
):

    consumo_formatado = f"{consumo:.2f}".replace(".", ",")
    valor_formatado = f"{valor:.2f}".replace(".", ",")

    print("")
    print("CONSULTA DE CONSUMO DE ÁGUA")
    print("")
    print(f"Protocolo da sessão: {protocolo_sessao}")
    print(f"Protocolo da consulta: {protocolo_consulta}")
    print(
        "Data e hora da consulta: "
        f"{data_hora_consulta.strftime('%d/%m/%Y %H:%M:%S')}"
    )
    print(f"Tipo de imóvel: {tipo_imovel}")
    print(f"Consumo mensal: {consumo_formatado} m³")
    print(f"Classificação: {classificacao}")
    print(f"Tarifa aplicada: {tarifa_aplicada}")
    print(f"Valor estimado: R$ {valor_formatado}")
    print("")


def historico_consultas(consultas):

    total_consumo = 0.0
    total_valor = 0.0

    print("")
    print("HISTÓRICO DAS CONSULTAS")
    print("")

    if not consultas:
        print("Nenhuma consulta foi realizada.")
    else:
        for numero, consulta in enumerate(consultas, start=1):
            consumo_formatado = f"{consulta['consumo']:.2f}".replace(
                ".", ","
            )
            valor_formatado = f"{consulta['valor']:.2f}".replace(
                ".", ","
            )

            print(f"Consulta {numero}:")
            print(f"  Protocolo: {consulta['protocolo']}")
            print(
                "  Data e hora: "
                f"{consulta['data_hora'].strftime('%d/%m/%Y %H:%M:%S')}"
            )
            print(f"  Tipo de imóvel: {consulta['tipo_imovel']}")
            print(f"  Consumo: {consumo_formatado} m³")
            print(f"  Classificação: {consulta['classificacao']}")
            print(f"  Valor estimado: R$ {valor_formatado}")
            print()

            total_consumo += consulta["consumo"]
            total_valor += consulta["valor"]

    return total_consumo, total_valor


def main():
    inicio_sessao = datetime.today()
    protocolo_sessao = gerar_protocolo(10000000, 99999999)

    consultas = []

    resposta_positiva = {"s","sim","si","ss",}
    resposta_negativa = {"n","nao","não","nn",}

    print("")
    print("SISTEMA DE CONSUMO DE ÁGUA")
    print("")
    print(f"Protocolo da sessão: {protocolo_sessao}")
    print(
        "Início da sessão: "
        f"{inicio_sessao.strftime('%d/%m/%Y %H:%M:%S')}"
    )

    while True:
        protocolo_consulta = gerar_protocolo(100000, 999999)

        data_hora_consulta = datetime.today()

        tipo_imovel = solicitar_tipo_imovel()
        consumo = solicitar_consumo()

        classificacao = classificar_consumo(tipo_imovel, consumo)
        valor, tarifa_aplicada = calcular_valor(tipo_imovel, consumo)

        consulta = {
            "protocolo": protocolo_consulta,
            "data_hora": data_hora_consulta,
            "tipo_imovel": tipo_imovel,
            "consumo": consumo,
            "classificacao": classificacao,
            "tarifa": tarifa_aplicada,
            "valor": valor
        }

        consultas.append(consulta)

        exibir_resultado(
            protocolo_sessao,
            protocolo_consulta,
            data_hora_consulta,
            tipo_imovel,
            consumo,
            classificacao,
            tarifa_aplicada,
            valor
        )

        while True:
            resposta = input(
                "Deseja realizar outra consulta?: ").strip().lower()

            if resposta in resposta_positiva:
                continuar = True
                break
            elif resposta in resposta_negativa:
                continuar = False
                break
            else:
                print("Resposta inválida, digite SIM ou NÃO.")

        if not continuar:
            break

    fim_sessao = datetime.today()

    total_consumo, total_valor = historico_consultas(consultas)

    total_consumo_formatado = f"{total_consumo:.2f}".replace(".", ",")
    total_valor_formatado = f"{total_valor:.2f}".replace(".", ",")

    print("")
    print("ENCERRAMENTO DA SESSÃO")
    print("")
    print(f"Protocolo da sessão: {protocolo_sessao}")
    print(f"Total de consultas: {len(consultas)}")
    print(
        "Início da sessão: "
        f"{inicio_sessao.strftime('%d/%m/%Y %H:%M:%S')}"
    )
    print(
        "Fim da sessão: "
        f"{fim_sessao.strftime('%d/%m/%Y %H:%M:%S')}"
    )
    print("-" * 30)
    print(f"Valor mensal estimado: R$ {total_valor_formatado}")
    print(f"Consumo mensal estimado: {total_consumo_formatado} m³")
    print("")
    print("Sessão encerrada com sucesso.")
    print("")

    
if __name__ == "__main__":
    main()
