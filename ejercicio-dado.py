import random


def lanzamiento_dado():
    dinero = 100
    dinero_maximo = 0
    movimiento = 0

    while dinero != 0:
        dado = random.randint(1, 6)

        if dado % 2 == 0:
            dinero += 100
        else:
            dinero -= 100

        if dinero > dinero_maximo:
            dinero_maximo = dinero

        movimiento += 1

    mostrar_Resultado(dinero_maximo, movimiento)


def mostrar_Resultado(maximo, movimiento):
    print(f"Cantidad de movimientos antes de caer en bancarrota: {movimiento}")
    print(
        f"Cantidad de dinero máxima alcanzada antes de caer en bancarrota: {maximo}")


def main():
    lanzamiento_dado()


main()
