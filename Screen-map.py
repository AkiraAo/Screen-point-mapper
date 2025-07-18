import pyautogui
import keyboard

coordenadas_salvas = []
print("movimentar mouse")
print("tecla S pra salvar.")
print("esc cancelar\n")
try:
    while True:
        if keyboard.is_pressed('s'):
            x, y = pyautogui.position()
            coordenadas_salvas.append((x, y))
            print(f"coordenada salva: ({x}, {y})")
            while keyboard.is_pressed('s'):
                pass 

        elif keyboard.is_pressed('esc'):
            print("\n encerrando")
            break
except KeyboardInterrupt:
    print("\n paro")
print("\n coordenadas salvas:")
for pos in coordenadas_salvas:
    print(pos)

