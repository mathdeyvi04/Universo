def bigbang():
    """Função responsável por iniciar nosso universo."""

    # Criamos nossa malha
    janela = criando_espaco_tempo(
        variaveis_globais["Dimensões"]
    )

    # Criamos nossos corpos!
    juntando_materia(
        variaveis_globais[
            "Quantidade de Astros"
        ]
    )

    fonte = font.Font(
        None,
        20
    )

    # Nosso Universo__ rodando
    while True:

        janela.fill(
            variaveis_globais[
                "Cor Malha Espaço-Tempo"
            ]
        )

        # Decidimos o que será feito pelo usuário que age como Deus
        for evento in event.get():
            # Vamos fazer alguma coisa com esse evento
            fazer_alguma_coisa(evento)

        # Devemos colocar no universo nossos astros
        materializando_na_tela(janela)

        # Aplicando a Dinâmica da situação
        gravitacionando()

        # Devemos aplicar o movimento em cada sanhudo
        saindo_da_inercia()

        # Caso estejamos em uma simulação visionária.
        textos = obtendo_informacoes(
            fonte
        )
        for superficie_do_texto, retangulo_texto in textos:
            janela.blit(
                superficie_do_texto,
                retangulo_texto
            )

        # Os frames de nosso universo
        display.flip()

        # Quantiza a escala temporal
        tempo_de_planck(
            variaveis_globais[
                "Taxa de Atualizações Por Segundo"
            ]
        )


if __name__ == '__main__':
    bigbang()
