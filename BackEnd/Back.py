def juntando_materia(quant: int) -> None:
    """Função Responsável por criar os objetos."""

    # Para nos ajudar a sempre ter apenas a quantidade correta

    # Para cada tipo de astro.
    for tipo_de_astro in astros_globais.keys():
        print(f"Vou criar {int(quant * astros_globais[tipo_de_astro]['Prob Nascim'])} astros desse tipo")

        for quantidade_de_astros_desse_tipo in range(0,
                                                     int(quant * astros_globais[tipo_de_astro]["Prob Nascim"])):

            if variaveis_globais[
                "Visualizar"
            ]:
                print(f"Criando {tipo_de_astro} pela {quantidade_de_astros_desse_tipo + 1}° vez.")

            # Devemos criar
            entidades.append(

                mae_dos_astros[
                    tipo_de_astro
                ]()

            )


def movimentar_usuario(numero_tecla_digitada: int) -> None:
    """Função responsável por, utilizando vetores, movimentar o jogador
    de forma forçada."""

    # De posse dos vetores direcionais, podemos fazer o seguinte.
    # Se não for None
    versor = versores_direcionais.get(
        numero_tecla_digitada
    )
    if versor:
        # Precisamos pegar o usuário
        usuario: Usuario = entidades[0]

        # E então aplicar
        usuario.forcar_movimento(
            versor
        )


def gravitacionando() -> None:
    """Função responsável por criar as interações gravitacionais dos astros.
    Vai ser sanhudo."""

    def aplicando_conservacoes(astro_maior: Objeto, astro_menor: Objeto) -> None:
        """Função responsável por conservarmos as grandezes físicas após uma colisão.
        Devemos considerar que o menor entra no maior."""

        # Conservando Momento Linear, antes de considerar o aumento de massa
        astro_maior.velocidade = (
            # Momento Linear total
                astro_maior.obter_momento_linear() + astro_menor.obter_momento_linear()
        ).multiplicar_por_escalar(
            1 / (astro_maior.massa + astro_menor.massa)
        )

        # Conservando massa
        astro_maior.massa += astro_menor.massa
        # Conservando o raio também
        astro_maior.raio += astro_menor.raio

    def calculando_a_aceleracao(massa_1: float, massa_2: float, r: Vetor) -> tuple[Vetor, Vetor]:
        """Função responsável por obter as variáveis e calcular a aceleração resultante
        da interação."""

        escalar_resultante = (
                                     variaveis_globais[
                                         "Constante Gravitacional"
                                     ] * massa_1 * massa_2
                             ) / (
                                     r.modulo() * r.modulo() * r.modulo()
                             )

        Forca_Resultante: Vetor = r.multiplicar_por_escalar(
            escalar_resultante
        )

        sinal: int = -1 if massa_1 > massa_2 else 1

        return (
            Forca_Resultante.multiplicar_por_escalar(
                sinal / massa_1
            ),
            Forca_Resultante.multiplicar_por_escalar(
               - sinal / massa_2
            )
        )

    def se_ha_colisao(distancia_minima_de_colisao: float, r: Vetor) -> bool:
        """Função que verifica se há uma colisão

        Há um problema a ser discutido. Pense em uma lista A, B, C, D.
        Suponha que A explode logo em B. Como vai ficar a interação entre AC, AD?
        Podemos realmente ignorá-la?

        O erro gerado é diminuído conforme consideramos que a colisão ocorre
        em distâncias menores."""

        if not variaveis_globais[
            "Colisões"
        ]:
            return False

        if r.modulo() < distancia_minima_de_colisao:
            return True

        return False

    """
    Devido à explosão o número de astros totais também diminui e isso não afetava o range,
    algo que gerou muitos sanhas, entretanto, é possível resolvermos com while.
    
    Não devemos considerar uma colisão quando vai parar fora da borda, pois ainda deve haver 
    interações gravitacionais."""
    i: int = 0  # Vamos iterar sobre a lista de forma primária
    while i < len(entidades):
        j: int = i + 1  # Para iterar sobre a lista de forma secundária
        # Note como garantimos que nunca vamos ter i = j.

        while j < len(entidades):

            try:
                # Então, pegamos nossos astros. Como vamos precisar saber qual é o de maior massa e o de menor
                # Para não usarmos mais memória que o necessário, basta:
                maior: Objeto
                menor: Objeto
                maior, menor = (
                    entidades[i],
                    entidades[j]
                ) if entidades[i].massa > entidades[j].massa else (
                    # Apenas o inverso da outra
                    entidades[j],
                    entidades[i]
                )

                # Também vamos precisar da posição relativa
                posicao_relativa = Vetor(
                    entidades[j].obter_posicao(),  # Posição Final do Vetor
                    entidades[i].obter_posicao()  # Posição Inicial do Vetor
                )

                if se_ha_colisao(
                        maior.raio,
                        posicao_relativa
                ):
                    print("Houve uma colisão")

                    aplicando_conservacoes(
                        maior,
                        menor
                    )

                    # A quantidade total de astros também diminui
                    variaveis_globais[
                        "Quantidade de Astros"
                    ] += -1

                    # Agora, devemos tratar essa remoção
                    if menor == entidades[j]:
                        # Então devemos diminuir em uma unidade o j
                        j += -1
                        # Daí meu padrão, explodimos o menor
                        entidades.remove(
                            menor
                        )
                    else:
                        # Então menor == astro_1
                        # Daí meu padrão, explodimos o menor
                        entidades.remove(
                            menor
                        )
                        break
                else:
                    # Só resta interagir
                    a1, a2 = calculando_a_aceleracao(
                        maior.massa,
                        menor.massa,
                        posicao_relativa
                    )

                    # De posse das acelerações, devemos aplicar elas
                    maior.aceleracao = round(
                        a1,
                        variaveis_globais[
                            "Casas Decimais"
                        ]
                    )
                    menor.aceleracao = round(
                        a2,
                        variaveis_globais[
                            "Casas Decimais"
                        ]
                    )

                j += 1
            except:
                print(f"Erro ao acessar elemento em {j}")

        i += 1
