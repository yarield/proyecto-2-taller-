import random
import time
random.seed(time.time())
puntos = 0
jugadores = []
mazo_jugador = []
mazo_pc = []
mazo_depurado = []
palos = ["fuerte","debil","regular","regular"]
cartas = {
    'corazon': ["as♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "jota♥", "reina♥", "rey♥"],
    'diamante': ["as♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "jota♦", "reina♦", "rey♦"],
    'pica': ["as♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "jota♠", "reina♠", "rey♠"],
    'trebol': ["as♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "jota♣", "reina♣", "rey♣"]
}


def verificar_jugador():
    global jugadores
    jugador = len(jugadores)
    if jugador == 0:
        print("No existen jugadores registrados")

def registro_de_jugadores():
    cedula = int(input("Ingrese su cedula: "))
    nombre = input("Ingrese su nombre: ")
    jugo = False
    puntaje = 0
    prediccion = 0
    regulares = 0
    debil = 0 
    fuertes = 0


    while True:
        if cedula in [jugador["cedula"] for jugador in jugadores]:
            print("¡El jugador ya existe!")
            break
        else:
            jugadores.append({'cedula': cedula, 'nombre': nombre, 'jugo': jugo, 'puntaje':puntaje,
                              'prediccion': prediccion,'regulares':regulares,'debil':debil,'fuertes':fuertes})
            break

def jugar():
    global cartas
    global puntos
    clave_ramdom = random.sample(list(cartas.keys()), len(cartas))
    clave_carta = {clave: cartas[clave] for clave in clave_ramdom}

    for cartas in cartas["corazon"] + cartas["diamante"] + cartas["pica"] + cartas["trebol"]:
        mazo_depurado.append(cartas)
    
    mazo_jugador = random.sample(mazo_depurado, 10)
    mazo_pc = random.sample(mazo_depurado,10)
    for cartas in mazo_jugador:
        mazo_depurado.remove(cartas)

    for palo in clave_carta:
        print("El palo", palo, "es", palos.pop(0))
        
    print(clave_carta)
    for x in range(len(mazo_jugador)):
        carta_pc = mazo_pc[x]
        carta_jugador = mazo_jugador[x]
        
        for clave, lista in clave_carta.items():
            if carta_pc in lista:
                indice = lista.index(carta_pc)
                indice_lista = list(clave_carta.keys()).index(clave)  
                print(f"La carta de la computadora '{carta_pc}' se encuentra en la lista '{clave}' en el índice {indice}, "
                    f"y la lista está en el índice {indice_lista}.")
                break
        
        for clave2, lista2 in clave_carta.items():
            if carta_jugador in lista2:
                indice2 = lista2.index(carta_jugador)
                indice_lista2 = list(clave_carta.keys()).index(clave2)  
                print(f"La carta de la persona '{carta_jugador}' se encuentra en la lista '{clave2}' en el índice {indice2}, "
                    f"y la lista está en el índice {indice_lista2}.")
                break
        if ((indice_lista2 == 0 and indice_lista == 2) or indice_lista == 3) or ((indice_lista2 == 2 or indice_lista2 == 3) and indice_lista == 1) or (indice_lista2 == 1 and indice_lista == 0):
            print("gano el jugador")
        elif indice_lista == indice_lista2 :
            if indice2 >= indice:
                print("gano el jugador")
            elif indice > indice2:
                print("computadora gano")
        else:
            print("computadora gano")
            

def menu():
    """Función menú permite a los usuarios selccionar la funcion
    que deseen ejecutar
    """
    while True:
        print("Menú")
        print("1 > Registro de jugadores \n2 > Iniciar el juego \n3 > Tabla de posiciones \n4 > Finalizar juego")
        opcionSelec = input("Ingrese el código de la opción que desea abrir: ")

        try:
            opcionSelec = int(opcionSelec)
            if opcionSelec == 1:
                registro_de_jugadores()
            elif opcionSelec == 2:
                verificar_jugador()
                jugar()
            elif opcionSelec == 3:
                print("Menú")
            elif opcionSelec == 4:
                break
            else:
                print("Opción no válida. Por favor, ingrese un número del 1 al 4.")
        except ValueError:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.")
menu()