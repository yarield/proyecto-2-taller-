import random
import time
random.seed(time.time())
# Declaraciones de listas y funciones utilizadas
palos = ["fuerte","debil","regular","regular"]
cartas = {
    'corazon': ["as♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "jota♥", "reina♥", "rey♥"],
    'diamante': ["as♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "jota♦", "reina♦", "rey♦"],
    'pica': ["as♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "jota♠", "reina♠", "rey♠"],
    'trebol': ["as♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "jota♣", "reina♣", "rey♣"]
}
jugadores, mazo_jugador, mazo_pc, mazo_depurado = [], [], [], []
puntos, jugo, puntaje, prediccion, regulares, debil, fuertes = 0, False, 0, 0, 0, 0, 0

def registro_de_jugadores():
    #aqui esta ubicado el registro de jugadores
    cedula, nombre= int(input("Ingrese su cedula: ")), input("Ingrese su nombre: ")
    while True:
        if cedula in [jugador["cedula"] for jugador in jugadores]:
            print("¡El jugador ya existe!")
            break
        else:
            jugadores.append({'cedula': cedula, 'nombre': nombre, 'jugo': jugo, 'puntaje':puntaje,
                              'prediccion': prediccion,'regulares':regulares,'debil':debil,'fuertes':fuertes})
            break

def verificar_jugador():
    #esta funcion se encarga de vericar si hay o no jugadores registrados
    global jugadores
    jugador = len(jugadores)
    if jugador == 0:
        print("No existen jugadores registrados"); menu()
        
def seleccion_jugador():
    #esta funcion es para poder escojer un jugador
    print("Ingrese el numero del jugador que desea jugar")
    n_jugadores, n = len(jugadores), 1
    while True:
        for jugador in jugadores:
            print(n,">","El jugador",jugador['nombre'],"y la cedula",jugador['cedula'])
            n += 1
        opcion = int(input("Ingrese el numero del jugador que deseas jugar"))
        opcion_indice, a_jugado = opcion - 1, jugadores[opcion]['jugo']
    #aqui verifica si un jugador a jugado
        if a_jugado == True:
            print("Ese jugador ya a jugado"); menu()
        if opcion >= 1 and opcion <= n_jugadores:
            global cedula ;       cedula = jugadores[opcion_indice]['cedula']
            print("El jugador",jugadores[opcion]['nombre'],"esta jugando\n")
            break
        else:
            n = 1  ;   print("opcion invalida")

def jugar():
    global cartas, puntos
    #esta funciones en palabras simples mesclan las listas del dicionario cartas
    clave_ramdom = random.sample(list(cartas.keys()), len(cartas))
    clave_carta = {clave: cartas[clave] for clave in clave_ramdom}
    
    p = 0
    for palo in clave_carta:
        print("El palo", palo, "es", palos[p])
        p += 1
    time.sleep(1)
    
    #crea una lista con las listas adentro del diccionario dando todas las cartas
    for carta in cartas["corazon"] + cartas["diamante"] + cartas["pica"] + cartas["trebol"]:
        mazo_depurado.append(carta)
        
    # crea las listas de la pc y el usuario
    mazo_jugador = random.sample(mazo_depurado, 10)
    for carta in mazo_jugador:
        mazo_depurado.remove(carta)

    mazo_pc = random.sample(mazo_depurado,10)
    print("\nLas cartas del jugador son:")
    for carta_j in mazo_jugador:
        print(carta_j, end=' ')


    while True:
        prediccion = int(input("\nIngrese la prediccion del 1 al 10 de cuantas partidas va a ganar"))
        if prediccion <= 10 and prediccion >= 0:
            break
        else:
            print("opcion no valida ingrese un numero entre el 1 y el 10")

    # por cada carta del usuario y la pc saca los indices de la carta y la lista donde se ubica 
    for x in range(len(mazo_jugador)):
        carta_pc = mazo_pc[x]
        carta_jugador = mazo_jugador[x]
        
        for clave_pc, lista_pc in clave_carta.items():
            if carta_pc in lista_pc:
                indice_pc = lista_pc.index(carta_pc)
                indice_lista_pc = list(clave_carta.keys()).index(clave_pc)  
                break
        
        for clave_jugador, lista_jugador in clave_carta.items():
            if carta_jugador in lista_jugador:
                indice_jugador = lista_jugador.index(carta_jugador)
                indice_lista_jugador = list(clave_carta.keys()).index(clave_jugador)  
                break
        print("La carta de la pc es",carta_pc,"y la del jugador",carta_jugador,)
        #saca cuantas cartas fuertes,debiles y regulares tiene el usuario
        if indice_lista_jugador == 0:
            global fuertes ; fuertes += 1
        elif indice_lista_jugador == 1:
            global debil ; debil += 1
        elif indice_lista_jugador == 2 or indice_lista_jugador == 3:
            global regulares ; regulares += 1
        # reparte puntos e indica si el usuario a perdido o ganado
        if (indice_lista_jugador == 0 and (indice_lista_pc == 2 or indice_lista_pc == 3))\
            or ((indice_lista_jugador == 2 or indice_lista_jugador == 3)and indice_lista_pc == 1)\
            or (indice_lista_jugador == 1 and indice_lista_pc == 0):
            print("gano el jugador")
            puntos += 1
        elif indice_lista_pc == indice_lista_jugador :
            if indice_jugador >= indice_pc:
                print("gano el jugador")
                puntos += 1
            elif indice_pc > indice_jugador:
                print("computadora gano")
        else:
            print("computadora gano")
    for jugador in jugadores:
        if jugador['cedula'] == cedula:
            jugador.update({'jugo': True, 'puntaje': 10 - abs(puntos - prediccion),
            'prediccion': prediccion, 'regulares': regulares, 'debil': debil, 'fuertes': fuertes})
            
            print("Has optenido ",jugador['puntaje'],"puntos")
    regulares , debil , fuertes= 0 , 0 , 0 
    
def tabla_de_posiciones():

    #aqui esta la tabla y el acomodo de posiciones
    jugadores_ordenados = sorted(jugadores, key=lambda x: (x['puntaje'], x['regulares'], x['debil']), reverse=True)

    print("Tabla de Posiciones:")
    print("{:<20} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Nombre", "Puntos", "Predicción", "Regulares", "Débil", "Fuertes"))
    for jugador in jugadores_ordenados:
        print("{:<20} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
            jugador["nombre"], jugador["puntaje"], jugador["prediccion"],
            jugador["regulares"], jugador["debil"], jugador["fuertes"]
        ))


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
                seleccion_jugador()
                jugar()
            elif opcionSelec == 3:
                tabla_de_posiciones()
            elif opcionSelec == 4:
                break
            else:
                print("Opción no válida. Por favor, ingrese un número del 1 al 4.")
        except ValueError:
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.")
menu()