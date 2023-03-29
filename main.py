import random
import os


def titulo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("❤️\tDominó \t  ❤️\n\n")


def generarFichas():
    fichas = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6],
              [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
              [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 3],
              [3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6],
              [5, 5], [5, 6], [6, 6]
              ]
    return fichas


def asignarFichas(fichas):
    jugador = []
    for f in range(7):
        max = len(fichas)
        n = random.randint(0, max-1)
        jugador.append(fichas[n])
        fichas.remove(fichas[n])
    return jugador


def repartirFichas(numeroJugadores):
    fichasGeneradas = generarFichas()
    jugadores = []
    for jugador in range(numeroJugadores):
        fichasJugador = asignarFichas(fichasGeneradas)
        jugadores.append(fichasJugador)
    return jugadores, fichasGeneradas

def comerFicha():
    print()
  
def jugarHumano(jugadores):
    titulo()
    listaJugadores, mazo = repartirFichas(jugadores)
    mesa = []
    jugadorInicial = random.randint(0 , jugadores-1)
    print("Inicia el jugador: ",jugadorInicial+1)
    input("Enter para continuar....")
    turno = jugadorInicial


    #Juego
    while True:
        titulo()
        print(turno)
        print("Jugador ", turno+1,
            "\n🎲Tus fichas:\n",
            listaJugadores[turno] 
            )
        print("\n🌏Tablero:\n", mesa)
        
        fichaIngresada = input("Elige una ficha para poner(Ejemplo '1-3')\n (Si no tienes una ficha válida, escribe N):")
        try:
            ficha = [int(fichaIngresada[0]), int(fichaIngresada[2])] 
        except:
            if fichaIngresada == 'N':
                #Comer ficha
                indice = random.randint(0, len(mazo)- 1)
                if len(mazo) != 0:
                    listaJugadores[turno].append(mazo[indice])
                    mazo.remove(mazo[indice])
                
                if (turno + 1) == (jugadores):
                    turno = 0
                else:
                    turno += 1
                input("Cambio de jugador") 
                continue
            else:
                input("Entrada incorrecta!\nEnter para volver a elegir...")
                continue
        
        if ficha in listaJugadores[turno]:
            fichaOriginal = ficha
            print(fichaOriginal)
            
            if len(mesa) == 0:
                mesa.append(ficha)
            else:
                while True:
                    titulo()
                    print("\n🌏Tablero:\n", mesa,'\n', 'Ficha: ', ficha)
                    
                    direccion = input("¿Izquierda o derecha?(I)(D): ")
                    if direccion is 'I' or direccion is 'D':
                        #IZQUIERDA
                        if direccion is 'I':
                            if ficha[1] == mesa[0][0]:
                                mesa.insert(0, ficha)
                            elif ficha[0] == mesa[0][0]:
                                ficha.reverse()
                                mesa.insert(0, ficha)
                                input("invertido")
                            else:
                                continue
                        #DERECHA
                        else:
                            if ficha[0] == mesa[-1][1]:
                                mesa.append(ficha)
                            elif ficha[1] == mesa[-1][1]:
                                ficha.reverse()
                                mesa.append(ficha)
                                input("invertido")
                            else:
                                continue
                        break
                    else:
                        continue
            
            #Quitar Ficha de las fichas del jugador
            try:
                listaJugadores[turno].remove(fichaOriginal)
            except:
                fichaOriginal.reverse()
                listaJugadores[turno].remove(fichaOriginal)
                fichaOriginal.reverse()

        else:
            input("Enter para volver a elegir...")
            continue
        
        #Verificar Ganador
        jugadorNumero = 0
        for jugador in listaJugadores:
            if jugador == []:
                titulo()
                print("🎉El ganador es el jugador ", jugadorNumero + 1, " 🎉")
                input("Enter para finalizar...")
                break
            jugadorNumero =+ 1
        
        #Cambio de turno
        if (turno + 1) == (jugadores):
            turno = 0
        else:
            turno += 1
        titulo()
        input("Cambio de jugador") 

       

def jugarMaquina(jugadores):
    #PENDIENTE#
    titulo()
    listaJugadores, mazo = repartirFichas(jugadores)
    mesa = []
    jugadorInicial = random.randint(0 , jugadores-1)
    print("Inicia el jugador: ",jugadorInicial+1)
    input("Enter para continuar....")
    turno = jugadorInicial


    #Juego
    while True:
        titulo()
        print(turno)
        print("Jugador ", turno+1,
            "\n🎲Tus fichas:\n",
            listaJugadores[turno] 
            )
        print("\n🌏Tablero:\n", mesa)
        
        fichaIngresada = input("Elige una ficha para poner(Ejemplo '1-3')\n (Si no tienes una ficha válida, escribe N):")
        try:
            ficha = [int(fichaIngresada[0]), int(fichaIngresada[2])] 
        except:
            if fichaIngresada == 'N':
                #Comer ficha
                indice = random.randint(0, len(mazo)- 1)
                if len(mazo) != 0:
                    listaJugadores[turno].append(mazo[indice])
                    mazo.remove(mazo[indice])
                
                if (turno + 1) == (jugadores):
                    turno = 0
                else:
                    turno += 1
                input("Cambio de jugador") 
                continue
            else:
                input("Entrada incorrecta!\nEnter para volver a elegir...")
                continue
        
        if ficha in listaJugadores[turno]:
            fichaOriginal = ficha
            print(fichaOriginal)
            
            if len(mesa) == 0:
                mesa.append(ficha)
            else:
                while True:
                    titulo()
                    print("\n🌏Tablero:\n", mesa,'\n', 'Ficha: ', ficha)
                    
                    direccion = input("¿Izquierda o derecha?(I)(D): ")
                    if direccion is 'I' or direccion is 'D':
                        #IZQUIERDA
                        if direccion is 'I':
                            if ficha[1] == mesa[0][0]:
                                mesa.insert(0, ficha)
                            elif ficha[0] == mesa[0][0]:
                                ficha.reverse()
                                mesa.insert(0, ficha)
                                input("invertido")
                            else:
                                continue
                        #DERECHA
                        else:
                            if ficha[0] == mesa[-1][1]:
                                mesa.append(ficha)
                            elif ficha[1] == mesa[-1][1]:
                                ficha.reverse()
                                mesa.append(ficha)
                                input("invertido")
                            else:
                                continue
                        break
                    else:
                        continue
            
            #Quitar Ficha de las fichas del jugador
            try:
                listaJugadores[turno].remove(fichaOriginal)
            except:
                fichaOriginal.reverse()
                listaJugadores[turno].remove(fichaOriginal)
                fichaOriginal.reverse()

        else:
            input("Enter para volver a elegir...")
            continue
        
        #Verificar Ganador
        jugadorNumero = 0
        for jugador in listaJugadores:
            if jugador == []:
                titulo()
                print("🎉El ganador es el jugador ", jugadorNumero + 1, " 🎉")
                input("Enter para finalizar...")
                break
            jugadorNumero =+ 1
        

        if (turno + 1) == (jugadores):
            turno = 0
        else:
            turno += 1
        titulo()
        input("Cambio de jugador") 

def menuPrincipal():
    while True:
        titulo()
        print(
            "\n\n",
            "🆚Jugar(1)\n",
            "📖Reglas(2)\n",
            #"🥇Tabla de puntaje(3)\n",
            "")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titulo()
            print("🎮Jugar🎮\n\n",
                "😜Humano(1)\n",
                #"🤖Computadora(2)\n"
                )
            opcionJugar = input("¡Selecciona a tu rival!: ")
            titulo()
            numeroJugadores = int(input("🎫¿Cuántos rivales?¿2, 3 o 4?: "))

            if opcionJugar == '1':
                jugarHumano(numeroJugadores)
            elif opcionJugar == '2':
                jugarMaquina()
        elif opcion == '2':
            titulo()
            print("Reglas\n\n")
            print("El clásico juego de Dominó\n En total se tienen 28 fichas, cada una con una combinación de dos números entre 0 y 6.",
                    "El juego puede ser de 2 a 4 jugadores. ¡Reta a tus amigos!\n",
                    "¿Cómo jugar?\n",
                    "1. Inicia el juego repartiendo 7 fichas a cada jugador al azar.\n", 
                    "2. El primer turno se indica al azar. El turno siguiente corresponde a la numeración de cada jugador consecutivo.\n",
                    "3. La primer ficha será seleccionada por el jugador al que le tocó el primer turno.\n",
                    "4. Cuando es tu turno tienes que seleccionar una de tus fichas que coincida con el número de puntos de alguno de los extremos de la fila.\n",
                    "5. En caso de que no haya fichas sobrantes, tendrás que dejar pasar tu turno al siguiente jugador. En tu siguiente turno encontrarás una nueva ficha en tu tablero lo que significa que 'comiste'.\n",
                    "6. El juego se termina cuando algún jugador se quede sin fichas.\n",
                    "7. En caso de que ningún jugador tenga fichas que coincidan con los extremos y no haya más fichas para 'comer', gana el jugador que se haya quedado con menos fichas.')\n")
            input("\nPresione enter para continuar...")
            continue
        elif opcion == '3':
            titulo()


menuPrincipal()
