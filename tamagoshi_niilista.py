import random

from tamagoshi import Tamagoshi


class TamagoshiNiilista(Tamagoshi): # O niilismo é uma corrente filosófica que nega a existência de significado, propósito, valores e verdades absolutas intrínsecas à existência.
    def __init__(self, nome):
        super().__init__(nome)
        self.__negacao_do_sentido_da_vida: int = 0
        self.__negacao_dos_valores_morais: int = 0
        self.__negacao_da_existencia_de_verdades_absolutas: int = 0

    def niilismo_existencial(self) -> None: # Questiona o sentido da vida e do universo
        if self.__negacao_do_sentido_da_vida < 25:
            print("Tudo ok.")
        elif self.__negacao_do_sentido_da_vida < 50:
            print("Será que a vida tem sentido?")
        elif self.__negacao_do_sentido_da_vida < 75:
            print("A vida não faz sentido.")
        else:
            print("Deus está morto.")

    def niilismo_moral(self) -> None: # Questiona os valores morais e éticos da sociedade
        if self.__negacao_dos_valores_morais < 25:
            print("Existem valores morais e éticos absolutos.")
        elif self.__negacao_dos_valores_morais < 50:
            print("Será que existem valores morais e éticos absolutos?")
        elif self.__negacao_dos_valores_morais < 75:
            print("Não existem valores morais e éticos absolutos.")
        else:
            print("A moral é um grande conto de fadas.")

    def niilismo_epistemologico(self) -> None: # Questiona a exstência de verdades absolutas
        if self.__negacao_da_existencia_de_verdades_absolutas < 25:
            print("Existem verdades absolutas.")
        elif self.__negacao_da_existencia_de_verdades_absolutas < 50:
            print("Poderiam existir verdades absolutas?")
        elif self.__negacao_da_existencia_de_verdades_absolutas < 75:
            print("Não existem verdades absolutas?")
        else:
            print("A busca pela verdade é fútil.")

    def tempo_passando(self) -> None:
        self.vida()
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 5
        n = random.randint(0,  2)
        if n == 0:
            self.__negacao_do_sentido_da_vida += 5
            self.niilismo_existencial()
        elif n == 1:
            self.__negacao_dos_valores_morais += 5
            self.niilismo_moral()
        elif n == 2:
            self.__negacao_da_existencia_de_verdades_absolutas += 5
            self.niilismo_epistemologico()
