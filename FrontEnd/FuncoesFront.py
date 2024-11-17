from Diversão.Universo.BackEnd.Back import *


def criando_espaco_tempo(dimensoes: tuple[int, int]) -> surface.Surface:
    """Função responsável por iniciar o espaço com seu vácuo absoluto."""
    # Iniciando com Big Bang
    init()

    # Configurações de Tela
    tela = display.set_mode(
        dimensoes
    )
    display.set_caption(
        "Universo__"
    )

    return tela


def tempo_de_planck(taxa_de_atualizacoes_por_segundo: int) -> None:
    """Função responsável por definir a quantização temporal."""

    time.Clock().tick(
        taxa_de_atualizacoes_por_segundo
    )


def saindo_da_inercia() -> None:
    """Função responsável por aplicar todos os movimentos"""

    for astro in entidades:
        astro: Objeto

        astro.movimentar()


def materializando_na_tela(tela: surface.Surface) -> None:
    """Função Responsável por Colocar na Tela cada um dos astros."""

    # Para cada classe de astros
    for astro in entidades:
        astro: Objeto

        draw.circle(
            tela,
            astro.cor,
            astro.obter_posicao(),
            astro.raio,
        )


def fazer_alguma_coisa(evt: event.Event) -> None:
    if evt.type == QUIT:
        exit(-5)

    elif evt.type == KEYDOWN:
        # A única coisa possível ao se teclar algo
        # É o movimento do usuário.

        movimentar_usuario(
            evt.key
        )


def obtendo_informacoes(fonte: font.Font) -> list[tuple]:
    """Função responsável por obter as informações e apresentá-las."""

    usuario: Objeto = entidades[0]
    centro: Objeto = entidades[1]

    # Muito importante, termos:
    vetor_posicao_relativa = Vetor(
        usuario.obter_posicao(),
        centro.obter_posicao()
    )

    conjunto = []

    # É interessante darmos informações relevantesb
    def obtendo_informacoes_de_usuario() -> None:
        """Função responsável por obter as componentes radial e tangencial da "nave"."""

        def obtendo_modulo_velocidade() -> tuple:
            """Vamos obter a módulo total da velocidade"""

            sup = fonte.render(
                f"Módulo da Velocidade Instântanea: {round(usuario.velocidade.modulo(), 2)}",
                True,
                (255, 255, 255)
            )
            retang = sup.get_rect(
                topleft=(10, 10)
            )

            return (
                round(usuario.velocidade.modulo(), 2),
                sup,
                retang
            )

        velocidade_modulo_total, *tupla_1 = obtendo_modulo_velocidade()

        conjunto.append(
            tupla_1
        )

        def obtendo_vel_radial() -> tuple:
            """Vamos obter apenas a componente radial da velocidade"""

            versor_radial = vetor_posicao_relativa.multiplicar_por_escalar(
                - 1 / vetor_posicao_relativa.modulo()
            )  # Colocamos esse menos, caso não, o versor indicaria para fora do centro.

            # Vetor Velocidade Radial
            velocidade_radial = versor_radial.multiplicar_por_escalar(
                usuario.velocidade * versor_radial
            )

            sup = fonte.render(
                f"Módulo Velocidade Radial Instântanea: {round(velocidade_radial.modulo(), 2)}",
                True,
                (255, 255, 255)
            )
            retang = sup.get_rect(
                topleft=(10, 30)
            )

            return (
                velocidade_radial, sup, retang
            )

        # Vetor Velocidade Radial
        vel_radial, *tupla_2 = obtendo_vel_radial()

        conjunto.append(
            tupla_2
        )

        def obtendo_vel_tangencial() -> tuple:
            """Vamos pegar a componente tangencial"""

            vel_tan1 = (
                    usuario.velocidade - vel_radial
            )

            sup = fonte.render(
                f"Módulo Velocidade Tangencial Instântanea: {round(vel_tan1.modulo(), 2)}",
                True,
                (255, 255, 255)
            )
            retang = sup.get_rect(
                topleft=(10, 50)
            )

            return (
                vel_tan1,
                sup,
                retang
            )

        # Vetor Velocidade Tangencial
        vel_tan, *tupla_3 = obtendo_vel_tangencial()

        conjunto.append(
            tupla_3
        )

        def obtendo_modulo_momento_angular() -> tuple:
            """Função responsável por obter o momento angular do sistema."""

            # Primeiro, módulo momento angular
            modulo_L = usuario.massa * (
                usuario.velocidade.modulo_produto_vetorial(
                    vetor_posicao_relativa
                )
            )

            sup = fonte.render(
                f"Módulo Momento Angular Instântaneo: {round(modulo_L, 2)}",
                True,
                (255, 255, 255)
            )
            retang = sup.get_rect(
                topleft=(10, 100)
            )

            return (
                modulo_L,
                sup,
                retang
            )

        modulo_momento_angular, *tupla_4 = obtendo_modulo_momento_angular()

        conjunto.append(
            tupla_4
        )

    obtendo_informacoes_de_usuario()

    def colocando_informacoes_de_centro() -> None:
        """Vamos colocar as informações que em teoria 'nao variam'."""

        def obtendo_velocidade_de_escape() -> tuple:
            modulo_velocidade_escape = sqrt(
                (2 * variaveis_globais[
                    "Constante Gravitacional"
                ] * centro.massa) / Vetor(
                    usuario.obter_posicao(),
                    centro.obter_posicao()
                ).modulo()
            )

            sup = fonte.render(
                f"Velocidade de Escape: {round(modulo_velocidade_escape, 2)}",
                True,
                (255, 255, 255)
            )
            retang = sup.get_rect(
                topleft=(variaveis_globais["Dimensões"][0] - sup.get_width() - 10, 10)
            )

            return (
                modulo_velocidade_escape,
                sup,
                retang
            )

        # Módulo da Velocidade de Escape.
        vel_escape, *tupla = obtendo_velocidade_de_escape()

        conjunto.append(
            tupla
        )

        def obtendo_excentricidade() -> tuple:
            """Função responsável por obter o valor da excentricidade"""

            def obtendo_energia_total() -> float:
                """Função responsável por obter o valor da energia total do sistema.
                Note que os impulsos que damos ao usuário violam completamente a Lei de
                Conservação da Massa e da Energia"""

                def obtendo_energia_gravitacional() -> float:
                    return variaveis_globais[
                        "Constante Gravitacional"
                    ] * usuario.massa * centro.massa / vetor_posicao_relativa.modulo()

                return (
                        # Energia Cinética, apenas do usuário,
                        # que o centro fica muito estático.
                        usuario.obter_energia_cinetica() - obtendo_energia_gravitacional()
                )

            def coeficiente_da_forca_gravitacional() -> float:
                return variaveis_globais[
                    "Constante Gravitacional"
                ] * usuario.massa * centro.massa

            Energia_Total = obtendo_energia_total()

            coeficiente = coeficiente_da_forca_gravitacional()
            coeficiente_ao_quadrado = coeficiente * coeficiente

            modulo_L = usuario.massa * (
                usuario.velocidade.modulo_produto_vetorial(
                    vetor_posicao_relativa
                )
            )

            valor_sanhudo = (
                    # Aqui vai uma coisa muito louca
                    (
                            2 * Energia_Total * modulo_L * modulo_L
                    ) / (
                            pow(
                                usuario.massa,
                                3
                            ) * coeficiente_ao_quadrado
                    )

            )

            try:

                exc = sqrt(

                    1 + valor_sanhudo

                )

            except ValueError:
                # Quer dizer que obtivemos uma energia total muito negativa!
                exc = -1
                print(valor_sanhudo)

            sup = fonte.render(
                f"Excentricidade Instântanea: {round(exc, 2)}",
                True,
                (255, 255, 255)
            )
            retang = sup.get_rect(
                topleft=(variaveis_globais["Dimensões"][0] - sup.get_width() - 10, 30)
            )

            return (
                exc,
                sup,
                retang
            )

        excentricidade, *tupla_1 = obtendo_excentricidade()

        conjunto.append(
            tupla_1
        )

    colocando_informacoes_de_centro()

    return conjunto
