from pygame import *
from sys import exit
from random import randint, choice
from math import sqrt



variaveis_globais = {
    # Representa o quanto nossas funções vão ser usadas a cada segundo.
    # Cuidado com esse valor
    "Taxa de Atualizações Por Segundo": 50,

    # Representa as dimensões de nossa janela.
    "Dimensões": (1200, 800),

    # Obviamente a quantidade de astros no universo.
    "Quantidade de Astros": 1,

    # Quão Forte a interação vai ser
    "Constante Gravitacional": 0.1,

    # Quantas casas os números terão, pode ser ótimo, dado que estaremos fazendo muitos cálculos
    "Casas Decimais": 8,

    "Cor Malha Espaço-Tempo": (28, 28, 28),

    # Para poder controlar o fluxo de informações
    "Visualizar": True,

    # Para permitir colisões
    "Colisões": False,

    # Para termos acesso a informações cruciais de simulação.
    "Informações De Física": True,
}

astros_globais = {
    # Vamos caracterizar nossos astros

    "Usuário": {
        "Cores Possíveis": [
          (242, 92, 240),
        ],

        # Já que não é espontâneo
        "Prob Nascim": 1 / variaveis_globais[
            "Quantidade de Astros"
        ],

        "Raio Mínimo": 4,
        "Raio Máximo": 4,

        # Quanto maior, mais massivo
        "Relação": 0.1,

        # Constanstes de Movimentação Forçada
        "Vel_f": 0.5,
    },

    "SubPlanetas": {
        "Cores Possíveis": [
            # Tons de Amarelo
            (255, 0, 0),
            (156, 0, 5),
            (117, 34, 37)
        ],

        # Metade dos Caras deve ser só isso
        "Prob Nascim": 1,

        "Raio Mínimo": 10,
        "Raio Máximo": 10,

        # A partir dela, obtemos a massa
        "Relação": 1000,
    },


}

# Vamos guardar todos as entidades dentro daqui.
entidades = []


if variaveis_globais[
    "Visualizar"
]:
    print("\033[1m\033[7m")
