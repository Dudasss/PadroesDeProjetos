class Carta:
    """"
    A classe Carta é imutável.
    Usamos __slots__  para reduzir drasticamente o uso de memória,
    impedindo a criação do dicionário interno __dict__ para cada instância.
    """
    __slots__ = ['_valor', '_naipe']

    def __init__(self, valor: str, naipe: str):
        self._valor = valor
        self._naipe = naipe

    @property
    def valor(self) -> str:
        return self._valor

    @property
    def naipe(self) -> str:
        return self._naipe

    def __str__(self) -> str:
        return f"{self._valor} de {self._naipe}."
