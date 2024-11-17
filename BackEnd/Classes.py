class Vetor:
    """Obviamente vai representar nossas grandezas vetoriais"""

    def __init__(self, final: tuple[float, float], inicio: tuple[float, float] = (0, 0)):

        self.delta_x = final[0] - inicio[0]

        self.delta_y = final[1] - inicio[1]

    def __str__(self):
        return f"{self.delta_x}i + {self.delta_y}j"

    def __add__(self, other):

        # Afinal de contas, só podemos aplicar operações em grandezas vetoriais
        if not isinstance(other, Vetor):
            raise TypeError

        return Vetor(
            (
                self.delta_x + other.delta_x,
                self.delta_y + other.delta_y
            ),
            (0, 0)
        )

    def __sub__(self, other):
        # Afinal de contas, só podemos aplicar operações em grandezas vetoriais
        if not isinstance(other, Vetor):
            raise TypeError

        return Vetor(
            (
                self.delta_x - other.delta_x,
                self.delta_y - other.delta_y
            ),
            (0, 0)
        )

    def __mul__(self, other):
        """Vai representar nosso produto escalar"""

        # Afinal de contas, só podemos aplicar operações em grandezas vetoriais
        if not isinstance(other, Vetor):
            raise TypeError

        return self.delta_x * other.delta_x + self.delta_y * other.delta_y

    def __round__(self, n=None):
        """Função responsável por ditar como o tipo se comportar ao entrar um round"""

        return Vetor(
            (
                round(
                    self.delta_x,
                    n
                ),
                round(
                    self.delta_y,
                    n
                )
            )
        )

    def multiplicar_por_escalar(self, other):
        """Autoexplicativo"""

        if isinstance(other, Vetor):
            raise TypeError

        return Vetor(
            (
                self.delta_x * other,
                self.delta_y * other
            )
        )

    def modulo_produto_vetorial(self, other) -> float:
        """Autoexplicativo"""

        if not isinstance(other, Vetor):
            raise TypeError

        return abs(
            self.delta_x * other.delta_y - self.delta_y * other.delta_x
        )

    def modulo(self) -> float:

        return sqrt(
            self.delta_x * self.delta_x + self.delta_y * self.delta_y
        )

    def direcionar(self, other):
        """Função responsável por multiplicar cada entrada do self pela mesma entrada do other"""

        if not isinstance(other, Vetor):
            raise TypeError

        return Vetor(
            (self.delta_x * other.delta_x, self.delta_y * other.delta_y)
        )

    def projecao_em(self, other):
        """Função responsável por calcular a projeção de self em other"""

        # Afinal de contas, só podemos aplicar operações em grandezas vetoriais
        if not isinstance(other, Vetor):
            raise TypeError

        fator = (self * other) / (self.modulo() * other.modulo())

        return Vetor(
            (
                fator * other.delta_x,
                fator * other.delta_y,
            )
        )

    def angulo_entre(self, other) -> float:

        if not isinstance(other, Vetor):
            raise TypeError

        return acos(
            (self * other) / (self.modulo() * other.modulo())
        )


versores_direcionais = {
    # Para quando formos movimentar o usuário
    100: Vetor(
        (1, 0)
    ),

    97: Vetor(
        (-1, 0)
    ),

    # Devido ao sistema cartesiano ser mais estranho, precisamos alterar o sentido
    115: Vetor(
        (0, 1)
    ),

    119: Vetor(
        (0, -1)
    )
}


class Objeto:
    """Classe que representará o cerne de cada coisa.
    É fato que qualquer coisa que colocarmos deve ter uma relação
    entre 'massa' e raio, mas como queremos colocar vários astros,
    deveremos uma relação para cada um deles então..."""

    def __init__(self, tipo: str):
        """Vamos definir as características que cada astro
        deve possuir."""

        # Definindo Variáveis de Apresentação
        self.cor = obtendo_cor_aleatoria(
            tipo
        )
        self.posicao = Vetor(
            obtendo_posicao_aleatoria(),
            (0, 0)
        )
        self.raio = obtendo_raio_aleatorio(
            tipo
        )

        # Definindo Variáveis de Cinemática / Dinâmica
        self.massa = self.raio * astros_globais[tipo]["Relação"]
        self.aceleracao = Vetor(
            (0, 0),
            (0, 0)
        )
        self.velocidade = Vetor(
            (0, 0),
            (0, 0)
        )

    def obter_posicao(self):
        return (
            self.posicao.delta_x,
            self.posicao.delta_y
        )

    def obter_momento_linear(self):
        """Óbvio"""
        return self.velocidade.multiplicar_por_escalar(
            self.massa
        )

    def obter_energia_cinetica(self):
        """Autoexplicativo"""

        modulo_momento = self.obter_momento_linear()

        return (
                (
                        modulo_momento * modulo_momento
                ) / (
                        2 * self.massa
                )
        )

    def movimentar(self):
        """Função responsável por aplicarmos os conceitos de movimento.
        Tenha atenção, pois já estamos iterando pelo tempo."""

        # Sabemos que a aceleração está constante em um curto tempo
        self.velocidade = round(
            self.velocidade + self.aceleracao,
            variaveis_globais[
                "Casas Decimais"
            ]
        )

        # E devemos mudar a posicao também
        self.posicao = round(
            self.posicao + self.velocidade,
            variaveis_globais[
                "Casas Decimais"
            ]
        )


class Usuario(Objeto):
    """Vai representar como o usuário vai interagir com o jogador"""

    def __init__(self):
        super().__init__(
            "Usuário"
        )

        self.vel_forcada = Vetor(
            (
                astros_globais["Usuário"]["Vel_f"],
                astros_globais["Usuário"]["Vel_f"],
            ),
        )

    def forcar_movimento(self, versor: Vetor):
        """Função responsável por forçar o movimento do usuário
        a partir da tecla direcional."""

        self.velocidade = round(
            self.velocidade + self.vel_forcada.direcionar(versor),
            variaveis_globais[
                "Casas Decimais"
            ]
        )

        if variaveis_globais[
            "Visualizar"
        ]:
            print(f"Nova Velocidade Usuário {self.velocidade}")


class SubPlaneta(Objeto):
    """Classe que representa as coisas abaixo de planetas."""

    def __init__(self):
        super().__init__(
            "SubPlanetas"
        )


class Planeta(Objeto):
    """Classe que representa as coisas abaixo de planetas."""

    def __init__(self):
        super().__init__(
            "Planetas"
        )


mae_dos_astros = {

    "Usuário": Usuario,

    "SubPlanetas": SubPlaneta,

    "Planetas": Planeta,

}
