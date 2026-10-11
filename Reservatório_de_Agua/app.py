# Importa a biblioteca colorama para colorir o texto no terminal
from colorama import Fore, Style, init
init(autoreset=True)

# Lista de níveis do reservatório de água
niveis = [
    "Nível 1 - Muito baixo (Crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto",]

# Retorna a cor colorama correspondente ao nível (1 a 5).
def escolher_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    else:
        return Fore.BLUE


# Exibe a lista dos 5 níveis
def mostrar_lista():
    for i in range(len(niveis)):
        cor = escolher_cor(i + 1)
        print(cor + niveis[i] + Style.RESET_ALL)


# Pergunta até receber resposta válida
def perguntar_sim_nao():
    while True:
        resposta = input(
            "Deseja consultar o nível de água do reservatório?: ")
        resposta = resposta.strip().lower()

        if resposta in ("s", "sim", "SIM"):
            return True
        elif resposta in ("n", "nao", "não", "NAO", "NÃO"):

            return False
        else:
            print("Resposta inválida, digite SIM ou NÃO.")


# Pede o nível até receber um inteiro de 1 a 5
def perguntar_nivel():
    while True:
        texto = input("Informe o nível atual do reservatório (1 a 5): ")
        texto = texto.strip()
        if texto in ("1", "2", "3", "4", "5"):
            return int(texto)
        print("Nível inválido, digite um número de 1 a 5.")


# Exibe a situação atual na cor do nível e restaura o estilo padrão.
def mostrar_situacao(nivel):
    cor = escolher_cor(nivel)
    texto = niveis[nivel - 1]
    print("Situação atual do reservatório: " + cor + texto + Style.RESET_ALL)


# Executa o fluxo completo do programa.
def main():
    init()
    if not perguntar_sim_nao():
        print("Programa encerrado.")
        return
    mostrar_lista()
    nivel = perguntar_nivel()
    mostrar_situacao(nivel)


if __name__ == "__main__":
    main()