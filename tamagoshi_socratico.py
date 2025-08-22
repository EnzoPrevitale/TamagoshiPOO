from tamagoshi import Tamagoshi
import random

class TamagoshiSocratico(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.__conhecimento: int = 0

    def raciocinar(self) -> None:
        c = random.randint(1, 10)
        self.__conhecimento += c
        print(f"O seu Tamagoshi estudou e ganhou {c} de conhecimento. Conhecimento atual: {self.__conhecimento}")

    def reconhecer_a_propria_ignorancia(self) -> None:
        c = random.randint(1, 10)
        self.__conhecimento += c
        print("Só sabo que nada sebo.")

    def dialetica_socratica(self, argumento: str) -> None:
        print(f"Alguém falou que {argumento}!")
        c = random.randint(1, 10)
        self.__conhecimento += c
        print(f"Mas por que {argumento}?")