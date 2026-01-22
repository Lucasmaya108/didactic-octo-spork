import random

def gerar_jogo():
    return sorted(random.sample(range(1, 81), 5))

def gerar_jogos(qtd):
    return [gerar_jogo() for _ in range(qtd)]