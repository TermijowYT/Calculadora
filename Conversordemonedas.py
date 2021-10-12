menu = int(input("""
    [1] Conversor de BTC a USD
    [2] Conversor de ETH a USD
    [3] Conversor de BNB a USD
    [4] Conversor de ADA a USD
    [5] Conversor de SOL a USD
    [6] Conversor de DOT a USD
    [7] Conversor de DOGE a USD
    [8] Conversor de AVAX a USD
    [9] Conversor de LUNA a USD

    Ingresa La moneda a convertir: """))
dinero = int(input("Ingresa la cantidad de dinero a intercambiar: "))

def conversor(dinero, moneda):
    total = dinero / moneda
    total = round(total, 200)
    return total


if menu == 1:
    print("[BTC] " + conversor(dinero, 43158))
elif menu == 2:
    print("[ETH] " + conversor(dinero, 3053.98))
elif menu == 3:
    print("[BNB] " + conversor(dinero, 342))
elif menu == 4:
    print("[ADA] " + conversor(dinero, 2.19))
elif menu == 5:
    print("[SOL] " + conversor(dinero, 142.65))
elif menu == 6:
    print("[DOT] " + conversor(dinero, 28.39))
elif menu == 7:
    print("[DOGE] " + conversor(dinero, 0.2026))
elif menu == 8:
    print("[AVAX] " +  conversor(dinero, 69.02))
elif menu == 9:
    print("[LUNA] " + conversor(dinero, 39.08))

else:
    print("ingresa una respuesta valida")