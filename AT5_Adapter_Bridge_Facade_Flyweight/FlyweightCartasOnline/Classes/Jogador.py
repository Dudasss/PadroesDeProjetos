from typing import List

from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.FlyweightCartasOnline.Classes.Cartas import Carta
from PadroesDeProjetos.AT5_Adapter_Bridge_Facade_Flyweight.FlyweightCartasOnline.Factory.CartasFactory import \
    CartaFactory


class Jogador:
    def __init__(self, nome: str):
        self.nome = nome
        self.mao: List[Carta] = []

    def receber_carta(self, valor: str, naipe: str):
        carta = CartaFactory.get_carta(valor, naipe)
        self.mao.append(carta)
        print(f"{self.nome} recebeu a carta {carta}")

    def mostrar_mao(self):
        cartas_str = [str(c) for c in self.mao]
        print(f"Mão de {self.nome}: {', '.join(cartas_str)}")
