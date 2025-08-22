from tamagoshi import Tamagoshi
import random

class TamagoshiEstoico(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.__virtude: int = 0

    def eudaimonia(self) -> bool:
        if self.__virtude > 100:
            return True
        return False

    def catastrofe(self) -> None:
        if self.__virtude > 50:
            print("Você tem controle sobre a situação?")
            opcao: str = "Sim" if input("[S] Sim | [N] Não") else "Não"
            if opcao == "Sim":
                print("Fodase!!! KKKKKKKKKKKKK")
            else:
                print("Talvez você deva se preocupar com isso.")

    def cultivar_virtudes(self) -> None:
        v = random.randint(1, 10)
        self.__virtude += v
        print(f"Ganhou {v} de virtude | Virtude: {self.__virtude}")