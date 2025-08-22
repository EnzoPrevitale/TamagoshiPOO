from tamagoshi import Tamagoshi
from tamagoshi_socratico import TamagoshiSocratico
from tamagoshi_estoico import TamagoshiEstoico
from tamagoshi_niilista import TamagoshiNiilista
import types

running = True

print("Escolha um Tamagoshi: ")
t = int(input("[1] Socrático\n[2] Estoico\n[3] Niilista\n[Outro] Sair\n"))
if t == 1:
    player = TamagoshiSocratico(input("Digite o nome do seu Tamagoshi: "))
elif t == 2:
    player = TamagoshiEstoico(input("Digite o nome do seu Tamagoshi: "))
elif t == 3:
    player = TamagoshiNiilista(input("Digite o nome do seu Tamagoshi: "))
else:
    running = False

while running:
    metodos = [attr for attr in dir(player) if isinstance(getattr(player, attr), types.MethodType)]
    metodos.remove("__init__")
    
    print(f"Escolha o que fazer:")
    for i in range(len(metodos)):
        print(f"[{i + 1}] - {metodos[i].replace("_", " ").title()}")
    m = metodos[int(input()) - 1]

    if m != "dialetica_socratica":
        eval(f"player.{m}()")
    else:
        eval(f"player.{m}('Coca é melhor que Pepsi')")

    player.tempo_passando()