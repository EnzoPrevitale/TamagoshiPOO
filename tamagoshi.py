class Tamagoshi():
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0

    def alimentar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade/100)

    def brincar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.tedio -= self.tedio * (quantidade/100)

    def get_humor(self):
        return 100 - ((self.fome + self.tedio)/2)

    def vida(self):
        if 50 < self.fome <= 60 or 50 < self.tedio <= 60:
            self.saude -= 10
        elif 60 < self.fome <= 80 or 60 < self.tedio <= 80:
            self.saude -= 30
        elif 80 < self.fome <= 90 or 80 < self.tedio <= 90:
            self.saude -= 50
        elif self.fome > 90 or self.tedio > 90:
            self.saude -= 70
            print("Estou morrendo... AAAAAAAAH")
        elif (self.fome > 99) or (self.tedio > 99):
            self.saude = 0
            print("Seu bichinho morreu T_T")

    def tempo_passando(self):
        self.vida()
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 5