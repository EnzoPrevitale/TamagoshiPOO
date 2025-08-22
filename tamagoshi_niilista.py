from tamagoshi import Tamagoshi


class TamagoshiNiilista(Tamagoshi): # O niilismo é uma corrente filosófica que nega a existência de significado, propósito, valores e verdades absolutas intrínsecas à existência.
    def __init__(self, nome):
        super().__init__(nome)
        self.__negacao_do_sentido_da_vida: int = 0
        self.__negacao_dos_valores_morais: int = 0

    def niilismo_existencial(self): # Questiona o sentido da vida e do universo
        if self.__negacao_do_sentido_da_vida < 25:
            print("Tudo ok.")
        elif self.__negacao_do_sentido_da_vida < 50:
            print("Será que a vida tem sentido?")
        elif self.__negacao_do_sentido_da_vida < 75:
            print("A vida não faz sentido.")
        else:
            print("Deus está morto.")

    def niilismo_moral(self): # Questiona os valores morais e éticos da sociedade
        if self.__negacao_dos_valores_morais < 25:
            print("Existem valores morais e éticos absolutos.")
        elif self.__negacao_dos_valores_morais < 50: