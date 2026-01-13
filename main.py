import time
import random
from pynput.mouse import Button, Controller, Listener
# python3 -m pip install pynput

# Creamos un controlador para el ratón
mouse = Controller()

def infinite():
    print("Inicializando...")
    time.sleep(10)

    # Obtener la posición inicial del ratón
    initial_position = mouse.position

    # Variable para detener el ciclo cuando el ratón se mueve
    stop_listener = False

    def on_move(x, y):
        nonlocal stop_listener
        # Si el ratón se mueve, se termina el ciclo
        if (x, y) != initial_position:
            stop_listener = True

    # Inicia el listener solo una vez
    listener = Listener(on_move=on_move)
    listener.start()

    while not stop_listener:
        # Realiza un clic
        mouse.click(Button.left)  # Usamos Button.left correctamente
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f"[{now}] click")

        # Espera aleatoria entre 180 y 360 segundos
        awaiting = random.randint(180, 360)
        time.sleep(awaiting)

    # Asegura que el listener se cierre después de que el ratón se mueva
    listener.stop()

if __name__ == "__main__":
    infinite()
