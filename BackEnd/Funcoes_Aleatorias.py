def obtendo_cor_aleatoria(tipo: str) -> tuple[int, int, int]:
    """Função responsável por, a partir do tipo de um astro, sortear uma das
    cores possíveis para sua classe"""
    return choice(
        astros_globais[
            tipo
        ][
            "Cores Possíveis"
        ]
    )


def obtendo_posicao_aleatoria() -> tuple[int, int]:
    return (
        randint(
            0,
            variaveis_globais[
                "Dimensões"
            ][0],
        ),
        randint(
            0, variaveis_globais[
                "Dimensões"
            ][1]
        )
    )


def obtendo_raio_aleatorio(tipo: str) -> float:
    """Função responsável por sortear um raio e, pela relação, uma massa"""

    return randint(
        astros_globais[tipo]["Raio Mínimo"] * 100,
        astros_globais[tipo]["Raio Máximo"] * 100
    ) / 100

