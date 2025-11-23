from typing import Dict

from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.FlyweightCartasOnline.Classes.Cartas import Carta


class CartaFactory:
    _cartas_existente: Dict[str, Carta] = {}

    @classmethod
    def get_carta(cls, valor: str, naipe: str) -> Carta:
        # chave unica para identificar a carta
        chave = f"{valor}-{naipe}"

        # se carta já foi criada, retornamos a referencia
        if chave in cls._cartas_existente:
            print(f"Retornando carta existente: {valor} de {naipe}")
            return cls._cartas_existente[chave]

        # se a carta ainda não existe, será criada e retornada
        print(f"Criando nova instâcia: {valor} de {naipe}")
        nova_carta = Carta(valor, naipe)
        cls._cartas_existente[chave] = nova_carta
        return nova_carta
