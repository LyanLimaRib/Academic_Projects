# Imports necessários para bom funcionamento do código
from random import randint
from datetime import datetime

# Solicita um nome - impede entradas vazias
def solicitar_nome():
    while True:
        nome = input("Digite o nome da pessoa: ").strip()
        if nome:
            return nome
        else:
            print("O nome não pode ficar vazio.")

# Solicita e valida a idade - Só permitindo idades maiores que 0
def solicitar_idade():
    while True:
        entrada_idade = input("Digite a idade da pessoa: ").strip()
        try:
            idade = int(entrada_idade)
        except ValueError:
            print("Tipo de idade incorreto, digite um número inteiro.")
            continue
        if idade == 0:
            print("A idade não pode ser zero.")
        elif idade < 0:
            print("A idade não pode ser negativa.")
        else:
            return idade

# Solicita a nota de avaliação do usuário - Retornando um valor padronizado
def solicitar_avaliacao():
    while True:
        print()
        print("Qual nota gostaria de dar?")
        print("1. Excelente")
        print("2. Bom")
        print("3. Ruim")
        print()

        entrada_avaliacao = input("Digite a avaliação: ").strip().lower()

        if entrada_avaliacao == "1" or entrada_avaliacao == "excelente":
            return "Excelente"
        elif entrada_avaliacao == "2" or entrada_avaliacao == "bom":
            return "Bom"
        elif entrada_avaliacao == "3" or entrada_avaliacao == "ruim":
            return "Ruim"
        else:
            print(
                "Opção inválida, digite uma das opções disponíveis."
            )

# Gera um protocolo único para cada sessão
def gerar_protocolo_consulta(protocolos_utilizados):
    protocolo_consulta = randint(100000, 999999)

    while protocolo_consulta in protocolos_utilizados:
        protocolo_consulta = randint(100000, 999999)

    protocolos_utilizados.add(protocolo_consulta)
    return protocolo_consulta

# Permite realizar outra avaliação
def perguntar_continuidade(resposta_positiva, resposta_negativa):
    while True:
        resposta = input("Deseja realizar outra avaliação?: ").strip().lower()

        if resposta in resposta_positiva:
            return True
        elif resposta in resposta_negativa:
            return False
        else:
            print("Resposta inválida, digite SIM ou NÃO.")

# Exibe o resumo e histórico da sessão:
def exibir_historico_e_resumo(
    historico,
    protocolo_sessao,
    total_avaliacoes,
    contagem_avaliacoes,
    inicio_sessao,
    encerramento_sessao
):
    print()
    print("HISTÓRICO DE AVALIAÇÕES")
    print()

    for numero_consulta, registro in enumerate(historico, start=1):
        print(f"Consulta {numero_consulta}")
        print(
            f"Protocolo da consulta: "
            f"{registro['protocolo_consulta']}"
        )
        print(f"Nome: {registro['nome']}")
        print(f"Idade: {registro['idade']}")
        print(f"Avaliação: {registro['avaliacao']}")
        print(f"Data e hora: {registro['data_hora']}")
        print()

    print()
    print("ENCERRAMENTO DA SESSÃO")
    print()
    print(f"Protocolo da sessão: {protocolo_sessao}")
    print(f"Total de avaliações: {total_avaliacoes}")
    print(f"Início da sessão: {inicio_sessao}")
    print(f"Fim da sessão: {encerramento_sessao}")
    print(
        'Quantidade de respostas "Excelente": '
        f'{contagem_avaliacoes["Excelente"]}'
    )
    print(
        'Quantidade de respostas "Bom": '
        f'{contagem_avaliacoes["Bom"]}'
    )
    print(
        'Quantidade de respostas "Ruim": '
        f'{contagem_avaliacoes["Ruim"]}'
    )
    print("Sessão encerrada com sucesso.")
    print()

# Controla o inicio - Avaliações - Encerramento da sessão
def executar_programa():
    protocolo_sessao = randint(100000, 999999)
    data_hora_inicio = datetime.today()
    inicio_sessao = data_hora_inicio.strftime("%d/%m/%Y - %H:%M:%S")

    historico = []
    protocolos_utilizados = set()
    total_avaliacoes = 0

    contagem_avaliacoes = {"Excelente": 0,"Bom": 0,"Ruim": 0}

    resposta_positiva = {"sim", "s"}
    resposta_negativa = {"nao", "não", "n"}

    print()
    print("SISTEMA DE AVALIAÇÕES")
    print()
    print(f"Protocolo da sessão: {protocolo_sessao}")
    print(f"Início da sessão: {inicio_sessao}")
    print()

    while True:
        print()
        print("NOVA AVALIAÇÃO")
        print("-" * 30)

        nome = solicitar_nome()
        idade = solicitar_idade()
        avaliacao = solicitar_avaliacao()

        protocolo_consulta = gerar_protocolo_consulta(protocolos_utilizados)

        data_hora_consulta = datetime.today()
        consulta_formatada = data_hora_consulta.strftime("%d/%m/%Y - %H:%M:%S")

        registro = {
            "protocolo_consulta": protocolo_consulta,
            "nome": nome,
            "idade": idade,
            "avaliacao": avaliacao,
            "data_hora": consulta_formatada
        }

        historico.append(registro)
        contagem_avaliacoes[avaliacao] += 1
        total_avaliacoes += 1

        print()
        print("Avaliação registrada com sucesso.")
        print(f"Protocolo da consulta: {protocolo_consulta}")
        print(f"Data e hora: {consulta_formatada}")
        print("-" * 30)

        realizar_outra = perguntar_continuidade(resposta_positiva, resposta_negativa)

        if realizar_outra:
            continue
        else:
            break

    data_hora_encerramento = datetime.today()
    encerramento_sessao = data_hora_encerramento.strftime("%d/%m/%Y - %H:%M:%S")

    exibir_historico_e_resumo(
        historico,
        protocolo_sessao,
        total_avaliacoes,
        contagem_avaliacoes,
        inicio_sessao,
        encerramento_sessao
    )


if __name__ == "__main__":
    executar_programa()