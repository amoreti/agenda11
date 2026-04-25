from colorama import Fore, Style, init


# Lista de níveis do reservatório
niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

# Função para retornar a cor conforme o nível
def cor_por_nivel(nivel):
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
        return Fore.WHITE  # padrão

# Exemplo: solicitar nível ao usuário
nivel_atual = int(input("Informe o nível do reservatório (1 a 5): "))

# Verifica se o nível é válido
if 1 <= nivel_atual <= 5:
    mensagem = niveis[nivel_atual - 1]
    cor = cor_por_nivel(nivel_atual)

    print(cor + f"Nível {nivel_atual}: {mensagem}" + Style.RESET_ALL)
else:
    print("Nível inválido! Informe um valor entre 1 e 5.")

