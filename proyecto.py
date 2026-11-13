import csv
import time

#Apartado Funciones

def actualizacionMatrices():
    try:
        matriz1 = ""
        matriz2 = ""
        matriz3 = ""
        encabezado = ""

        with open("logica de programacion U/- PROYECTO FINAL/estacion.csv", "r", encoding="utf-8") as Archivo_Estacion:
            encabezado = Archivo_Estacion.readline()
            informacionEstacion = csv.reader(Archivo_Estacion)
            matriz = []
            componenteMatriz = []
            for comparacionEstacion in informacionEstacion:
                with open("logica de programacion U/- PROYECTO FINAL/anclajes.csv", "r", encoding="utf-8") as Archivo_Anclaje:
                    Archivo_Anclaje.readline()
                    informacionAnclaje = csv.reader(Archivo_Anclaje)
                    for anclaje in informacionAnclaje:
                        if anclaje[0] == comparacionEstacion[0]:
                            if anclaje[3] == "BICI":
                                componenteMatriz.insert(int(anclaje[2]), anclaje[4])
                            elif anclaje[3] == "VACIO":
                                componenteMatriz.insert(int(anclaje[2]), "000")
                            elif anclaje[3] == "MANTENIMIENTO":
                                componenteMatriz.insert(int(anclaje[2]), "XXX")
                            if len(componenteMatriz) == int(comparacionEstacion[2]):
                                matriz.insert(int(anclaje[1]) - 1, componenteMatriz)
                                componenteMatriz = []
                        else:
                            continue
            matriz1 = matriz[6:9]
            matriz2 = matriz[3:6]
            matriz3 = matriz[0:3]

            return matriz1, matriz2, matriz3, encabezado
    except Exception as e:
        return e

def clasificacionEstacion(estacion:int, matriz1:list, matriz2:list, matriz3:list):
    try:
        matrizElegida = []
        nombre = ""
        codigo = ""
        if estacion == 1:
            nombre = "SAN BURITICA"
            matrizElegida = matriz1
            codigo = "E01"
        elif estacion == 2:
            nombre = "PARQUE ESPINOSA"
            matrizElegida = matriz2
            codigo = "E02"
        elif estacion == 3:
            nombre = "UPB"
            matrizElegida = matriz3
            codigo = "E03"
        return matrizElegida, nombre, codigo
    except Exception as e:
        return "Error en la función de clasificación de estación"

def leerArchivo(nombre:str):
    try:
        with open(f"logica de programacion U/- PROYECTO FINAL/{nombre}.csv", "r", encoding="utf-8", newline="") as Lectura_Archivo:
            encabezado = Lectura_Archivo.readline()
            informacion = list(csv.reader(Lectura_Archivo))

            return informacion, encabezado
    except FileNotFoundError as fe:
        return None, None

def reescribirArchivo(info, encabezado, nombre:str):
    try:
        with open(f"logica de programacion U/- PROYECTO FINAL/{nombre}.csv","w",encoding="utf-8", newline="") as Actualizacion_Archivo:
            Actualizacion_Archivo.write(encabezado)
            informacionActualizada = csv.writer(Actualizacion_Archivo)
            informacionActualizada.writerows(info)
    except Exception as e:
        return e

def validarFecha(tiempo: str):
    try:
        tiempoSeparado = tiempo.strip().split("-")
        anio = int(tiempoSeparado[0].strip())
        mes = int(tiempoSeparado[1].strip())
        dia = int(tiempoSeparado[2].strip())

        formatoHora = tiempoSeparado[3].strip().split(":")
        hora = int(formatoHora[0].strip())
        minutos = int(formatoHora[1].strip())

        if not(anio == 2026):
            raise Exception("Año inválido")
        elif not(1 <= mes <= 12):
            raise Exception("Mes inválido")
        elif not(1 <= dia <= 30):
            raise Exception("Día inválido")
        elif not(0 <= hora <= 23) or not (0 <= minutos <= 59):
            raise Exception("Hora inválida")
        else:
            return anio, mes, dia, hora, minutos

    except ValueError:
        raise
    except IndexError:
        raise

def calcularCosto(hora1:int, minuto1:int, hora2:int, minuto2:int):
    try:
        precio = 0
        total = 0
        vecesCobro = 0
        vecesCobroEntero = 0
        tarifa30Min = 4000
        minutosTotales1 = 0
        minutosTotales2 = 0
        
        minutosTotales1 = (hora1 * 60) + minuto1
        minutosTotales2 = (hora2 * 60) + minuto2
        total = abs(minutosTotales2 - minutosTotales1) 
        vecesCobro = total/30
        vecesCobroEntero = int(vecesCobro)
        
        if vecesCobro > vecesCobroEntero:
            vecesCobroEntero += 1
        
        precio = vecesCobroEntero * tarifa30Min
        
        return total, precio
    
    except Exception as e:
        return f"Error en la función \"Calcular Costos\""
    
def cantidadBicicletas(matrizEstacion:list):
    try:
        bicis = 0
        for recorrido in matrizEstacion:
            for elementos in recorrido:
                if elementos != "000":
                    bicis += 1
        return bicis
    except Exception as e:
        return e

def sugerirRedistribuciones(estacion1:int, estacion2:int, estacion3:int):
    
    presta = ""
    codigoPresta = ""
    recibe = ""
    codigoRecibe = ""
    
    if estacion1 >= 6:
        presta = "ESTACION SAN BURITICA"
        codigoPresta = "E01"
    elif estacion2 >= 6:
        presta = "ESTACION PARQUE ESPINOSA"
        codigoPresta = "E02"
    elif estacion3 >= 6:
        presta = "ESTACION UPB"
        codigoPresta = "E03"

    if estacion1 < 3:
        recibe = "ESTACION SAN BURITICA"
        codigoRecibe = "E01"
    elif estacion2 < 3:
        recibe = "ESTACION PARQUE ESPINOSA"
        codigoRecibe = "E02"
    elif estacion3 < 3:
        recibe = "ESTACION UPB"
        codigoRecibe = "E03"
    else:
        codigoRecibe = "NO APLICA"
        recibe = ""
    return presta, codigoPresta, recibe, codigoRecibe

#Apartado Principal

try:
    #variables generales
    opciones = 0
    informacionEstacion= ""
    informacionAnclajes = ""
    consultaEstacion = 0
    nombreCSV = ""

    matriz = []
    componenteMatriz = []
    matrizEstacion1 = ""
    matrizEstacion2 = ""
    matrizEstacion3 = ""
    encabezadoAnclajes = ""

    interfazEstaciones = (f"""
-----------------------------------------------
    ESTACIONES DE NUESTRO SERVICIO IN-BIKE
-----------------------------------------------
1. Estación San Buritica (E01)
2. Estación Parque Espinosa (E02)
3. Estacion UPB (E03)
""")

    #variables de tiempo
    tiempoInicio = ""
    anioInicio = 0
    mesInicio = 0
    diaInicio = 0
    horaInicio = 0
    minutosInicio = 0
    tiempoFin = ""
    anioFin = 0
    mesFin = 0
    diaFin = 0
    horaFin = 0
    minutosFin = 0

    #case 1 -> variables internas
    numeroEstaciones = 1
    contador = 0
    nombreEstacion = ""
    matrizRecorridaCase1 = []
    celdasIndependientes = ""
    vueltaDisponibilidad = 0

    #case 2 -> variables internas
    estacionOrigen = 0
    clienteID = ""
    nombreCliente = ""
    nombreClienteValidacion = ""
    estadoClientes = {}
    informacionPrestamosClientes = ""
    claveCliente = ""
    valorCliente = ""
    informacionClientes = ""
    matrizRecorridaCase2 = []
    nombreEstacionOrigen = ""
    codigoEstacionPrestamo = ""
    biciDisponible = False
    biciAlquilada = ""
    posicion = 0
    encabezadoBicicletas = ""
    informacionBicicletas = ""
    prestamoID = ""
    cambioPrestamoBici = ""
    registroPrestamo = ""
    bicisPrestadas = []
    listaPrestamos = ""

    #case 3 -> Variables internas
    informacionBicicletasPrestadas = ""
    listado = []
    opcionBici = ""
    contadorCase3 = 0

    #case 4 -> Variables internas
    estacionFin = 0
    nombreEstacionFin = ""
    codigoEstacionFin = ""
    biciDevuelta = ""
    verificacionBicicletasPrestadas = ""
    informacionBicicletasDevolucion = ""
    encabezadoBicicletasDevolucion = ""
    biciEncontrada = False
    anclajesDevolucion = ""
    AnclajeDisponible = False
    prestamoDevolucion = ""
    encabezadoPrestamoDevolucion = ""
    nombreUsuarioDevolucion = ""
    nombreUsuario = ""
    encabezadoNombreUsuario = ""
    tiempoUso = 0
    cobroBicicletas = 0
    

    #case 5 -> variables internas
    consultaEstacionMantenimiento = 0
    consultaServicioMantenimiento = 0
    codigoEstacionMantenimiento = ""
    estacionMantenimiento = ""
    idBicicleta = ""
    coordenadaY = 0
    coordenadaX = 0
    informacionMantenimiento = ""
    encabezadoMantenimiento = ""
    idEstacionMantenimiento = ""
    idEstacionReactivacion = ""

    #case 6 -> variables internas
    bicisEstacion1 = 0
    bicisEstacion2 = 0
    bicisEstacion3 = 0
    estacionRecibe = ""
    estacionPresta = ""
    codigoEstacionPresta = ""
    codigoEstacionRecibe = ""
    aceptarDistribucion = 0
    informacionCambio = ""
    idBicicleta = ""
    cantidadCambios = 0
    informacionCambioBicicletas = ""
    encabezadoCambioBicicletas = ""
    encabezadoCambio = ""
    
    #case 7 -> variables internas
    
    # CASE 1 - Prestamos
    lineaPrestamoIniciado = ""
    datosPrestamoIniciado = []

    # CASE 2 - Devoluciones
    lineaDevolucionCompletada = ""
    datosDevolucionCompletada = []

    # CASE 3 - Prestamos y Devoluciones
    cadenasPrestamosDevoluciones = []
    lineaPrestamo = ""
    datosPrestamo = []
    lineaDevolucion = ""
    datosDevolucion = []

    # CASE 4 - Mantenimientos
    lineaMantenimiento = ""
    datosMantenimiento = []

    # CASE 5 - Reactivaciones
    lineaReactivacion = ""
    datosReactivacion = []

    # CASE 6 - Mantenimientos y Reactivaciones
    cadenasMantenimientosReactivaciones = []

    # CASE 7 - Transferencias
    lineaTransferencia = ""
    datosTransferencia = []
    noExiste2 = True
    
    #CASE 8 - Ranking Estaciones
    rankingEstacion1 = 0
    rankingEstacion2 = 0
    rankingEstacion3 = 0
    noExiste = True
    
    

    #Proceso

    while True:
        print("""
-----------------------------------------------
            BIENVENIDO A IN-BIKE
-----------------------------------------------
1. Consultar mapas de estaciones y disponibilidad
2. Iniciar prestamo de bicicletas
3. Consultar prestamos activos
4. Devolver bicicletas y facturar
5. Registrar anclaje en mantenimiento / reactivar
6. Proponer y ejecutar redistribucion
7. Consultar historial y reportes
0. Salir""")

        matrizEstacion1, matrizEstacion2, matrizEstacion3, encabezadoAnclajes = actualizacionMatrices()

        while True:
            try:
                opciones = int(input("\nSelecione una de las opciones \n(Por favor solo digite valores numericos)\n-> "))
                if not(0 <= opciones <= 7):
                    raise ValueError ("Por favor selecciones un numero dentro del rango de opciones")
                else:
                    break
            except ValueError as ve:
                print(f"Digite un valor disponible en el menú")
                continue
        match opciones:
            case 1:
                while True:            
                    print(interfazEstaciones)
                    while True:
                        try:
                            consultaEstacion = int(input("Ingrese el índice de la estación que desea consultar -> "))
                            if not(1 <= consultaEstacion <= 3): raise ValueError
                            else: break
                        except ValueError as ve:
                            print("Opción inexistente. Digite nuevamente su opción")
                            continue

                    matrizRecorridaCase1, nombreEstacion, _ = clasificacionEstacion(consultaEstacion, matrizEstacion1, matrizEstacion2, matrizEstacion3)

                    print(f"""
---------------------------------------------------------------
                ESTACION: {nombreEstacion}
---------------------------------------------------------------""")
                    print("              MAPA DE DISPONIBILIDAD DE ANCLAJES               ")
                    print("---------------------------------------------------------------")
                    print("          1            2            3            4            5")
                    numeroEstaciones = 1
                    for mapaEstacionesGenerales in matrizRecorridaCase1:
                        contador = 0
                        for celdas in mapaEstacionesGenerales:
                            if contador == 0:
                                print(numeroEstaciones, "|", end=" ")
                            celdasIndependientes = celdas
                            print(f"""[    {celdas}    ]""", end="")    
                            contador += 1
                            if contador == 5:
                                contador = 0
                                numeroEstaciones += 1
                                print()
                    print("""
Tener en cuenta:
    - 000: Anclaje vacío
    - XXX: Anclaje mantenimiento
                        """)
                    time.sleep(3)
                    print ("¿DESEA MIRAR LA DISPONIBILIDAD EN OTRA ESTACION? -> 1.SI - MIRAR OTRAS ESTACIONES | 2. NO - SALIR AL MENU PRINCIPAL")
                    while True:
                        try:
                            vueltaDisponibilidad = int(input(""))
                            if not(1 <= vueltaDisponibilidad <= 2): raise ValueError
                            else: break
                        except ValueError as ve:
                            print("Opción inexistente")
                            continue
                    if int(vueltaDisponibilidad) == 1: continue
                    elif int(vueltaDisponibilidad) == 2: break
            
            case 2:
                nombreCSV = "clientes"
                informacionPrestamosClientes, _ = leerArchivo(nombreCSV)
                if informacionPrestamosClientes is not None:
                    for linea in informacionPrestamosClientes:
                        claveCliente = linea[1]
                        valorCliente = linea[2] == "True"
                        estadoClientes[claveCliente] = valorCliente
        
                print(interfazEstaciones)
                while True:
                    try:
                        estacionOrigen = int(input("Ingrese el índice de la estación en la que desea realizar el prestamo -> "))
                        if not(1 <= estacionOrigen <= 3): raise ValueError
                        else: break
                    except ValueError as ve:
                        print("Opción inexistente. Digite nuevamente su opción")
                        continue

                matrizRecorridaCase2 ,nombreEstacionOrigen ,codigoEstacionPrestamo = clasificacionEstacion(estacionOrigen, matrizEstacion1, matrizEstacion2, matrizEstacion3)
                biciDisponible = False

                for recorridoDisponibilidad in matrizRecorridaCase2:
                    for bicicletas in recorridoDisponibilidad:
                        if (bicicletas != "000")  and (bicicletas != "XXX"):
                            biciDisponible = True
                            break
                    if biciDisponible == True: break
                if biciDisponible == False:
                    print(f"No hay bicicletas disponibles en la estacion {nombreEstacionOrigen}")
                    time.sleep(3)
                    continue

                while True:
                    nombreCliente = (input("Ingrese su nombre y su primer apellido -> ")).upper().strip()
                    nombreClienteValidacion = nombreCliente.split(" ")

                    if len(nombreClienteValidacion) != 2 or not(nombreCliente.replace(" ","").isalpha()):
                        print("Nombre y/o apellido en formato inválido")
                        continue
                    else:
                        break

                if nombreCliente not in estadoClientes:
                    estadoClientes[nombreCliente] = False

                if estadoClientes[nombreCliente] == True:
                    print("No se puede realizar el préstamo. Ya hay un préstamo activo por parte de este usuario")
                    time.sleep(3)
                    continue

                while True:
                    try:
                        tiempoInicio = input("""
-----------------------------------------------
  INGRESE FECHA Y HORA DE INICIO DEL PRÉSTAMO
-----------------------------------------------
Tener en cuenta:
 - La fecha y hora debe ir en formato AAAA-MM-DD-HH:HH
 - La hora debe ir en formato 24h
 - Solo es válido el año 2026
 - Los préstamos se realizan entre las |4:00| y las |21:59|

-> """) 

                        anioInicio, mesInicio, diaInicio, horaInicio, minutosInicio = validarFecha(tiempoInicio)

                        if not(4 <= horaInicio < 22):
                            raise Exception("No se permiten préstamos a esta hora")
                        else:
                            break

                    except ValueError as ve:
                        print("Error. Por favor ingrese la fecha en números y/o en formato válido")
                        continue
                    except IndexError as ie:
                        print("Error. Formato de fecha y hora inválido")
                        continue
                    except Exception as e:
                        print(e)
                
                nombreCSV = "anclajes"
                cambioPrestamoBici, _ = leerArchivo(nombreCSV)

                for recorridoPrestamo in cambioPrestamoBici:
                    if recorridoPrestamo[3] == "BICI" and recorridoPrestamo[0] == codigoEstacionPrestamo:
                        biciAlquilada = recorridoPrestamo[4]
                        estadoClientes[nombreCliente] = True
                        recorridoPrestamo[3] = "VACIO"
                        recorridoPrestamo[4] = "VACIO"
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(f"Préstamo exitoso\nLa bicicleta {biciAlquilada} ha sido prestada")
                        reescribirArchivo(cambioPrestamoBici, encabezadoAnclajes, nombreCSV)
                        time.sleep(3)
                        break

                nombreCSV = "bicicletas"
                informacionBicicletas, encabezadoBicicletas = leerArchivo(nombreCSV)

                for recorridoBicicletas in informacionBicicletas:
                    if recorridoBicicletas[0] == biciAlquilada:
                        recorridoBicicletas[1] = "EN_USO"
                        recorridoBicicletas[2] = "NINGUNA"
                        reescribirArchivo(informacionBicicletas, encabezadoBicicletas, nombreCSV)
                        break

                with open("logica de programacion U/- PROYECTO FINAL/clientes.csv", "w", encoding="utf-8", newline="") as Archivo_Clientes:
                    informacionClientes = csv.writer(Archivo_Clientes)
                    informacionClientes.writerow(["clienteID","nombre","prestamoActivo"])

                    posicion = 0
                    for cliente, estado in estadoClientes.items():
                        posicion += 1

                        if posicion <= 9:
                            clienteID = f"C0{posicion}"
                        else:
                            clienteID = f"C{posicion}"

                        informacionClientes.writerow([clienteID,cliente,estado])

                nombreCSV = "prestamo"
                bicisPrestadas = []
                registroPrestamo, _ = leerArchivo(nombreCSV)
                
                if registroPrestamo is not None:
                    bicisPrestadas = registroPrestamo

                with open("logica de programacion U/- PROYECTO FINAL/prestamo.csv", "w", encoding="utf-8", newline="") as Archivo_Prestamo:
                    informacionPrestamos = csv.writer(Archivo_Prestamo)
                    informacionPrestamos.writerow(["prestamoID","clienteID","biciID","estacionOrigen","inicio","estacionDestino","fin","total","estadoPrestamo"])
                    informacionPrestamos.writerows(bicisPrestadas)

                    posicion = 1
                    for recorrerPosicion in bicisPrestadas:
                        posicion += 1

                    if len(str(posicion)) <= 9:
                        prestamoID = f"PR00{posicion}"
                    elif 10 <= len(str(posicion)) <= 99:
                        prestamoID = f"PR0{posicion}"
                    else:
                        prestamoID = f"PR{posicion}"

                    informacionPrestamos.writerow([prestamoID,clienteID,biciAlquilada,codigoEstacionPrestamo,tiempoInicio,"","","","ACTIVO"])
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                with open("logica de programacion U/- PROYECTO FINAL/historial_General.txt","a+",encoding="utf-8",newline="") as Archivo_Historial_Prestamo:
                        Archivo_Historial_Prestamo.seek(0)
                        encabezado = Archivo_Historial_Prestamo.read()
                        if encabezado == "":
                            Archivo_Historial_Prestamo.write(f"HISTORIAL DE MODIFICACIONES GENERALES DE IN-BIKE\n")
                        Archivo_Historial_Prestamo.write(f"La bicicleta | {biciAlquilada} | tiene estado de prestamo | INICIADO | por el cliente {nombreCliente}  \n")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            case 3:

                print("Analizando la información")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                nombreCSV = "bicicletas"
                informacionBicicletasPrestadas, _ = leerArchivo(nombreCSV)
                listado = []
                for listaPrestamos in informacionBicicletasPrestadas:
                    if listaPrestamos[1] == "EN_USO":
                        listado.append(listaPrestamos[0])

                if listado == []:
                    print("No hay préstamos activos en el momento")
                    time.sleep(3)
                    continue

                print(f"""
------------------------------
    BICICLETAS EN PRÉSTAMO
------------------------------""")
                contadorCase3 = 0
                while True:
                    if contadorCase3 < len(listado):
                        print(f"|  {listado[contadorCase3]}  |", end="")
                        contadorCase3 += 1

                        if contadorCase3 % 3 == 0:
                            print()
                    else:
                        break


                while True:
                    opcionBici = input(f"\nIngrese el ID de la bicicleta en préstamo que desea consultar -> ")

                    if len(opcionBici) != 3 or opcionBici[0] != "B" or not(opcionBici[1:].isnumeric()) or opcionBici not in listado:
                        print("ID de consulta inválido")
                        continue
                    else:
                        break

                nombreCSV = "prestamo"
                busquedaBiciPrestada, _ = leerArchivo(nombreCSV)

                for recorridoBusqueda in busquedaBiciPrestada:
                    if opcionBici == recorridoBusqueda[2] and recorridoBusqueda[8] == "ACTIVO":
                        nombreCSV = "clientes"
                        nombreUsuarioBusqueda, _ = leerArchivo(nombreCSV)
                        for usuario in nombreUsuarioBusqueda:
                            print(f"La bicicleta {opcionBici} ha sido prestada por el usuario {usuario[1]} el {recorridoBusqueda[4]}")
                            break
                        time.sleep(3)
                        break

            case 4:
                nombreCSV = "bicicletas"
                verificacionBicicletasPrestadas, _ = leerArchivo(nombreCSV)
                biciEncontrada = False
                for recorridoVerificacion in verificacionBicicletasPrestadas:
                    if recorridoVerificacion[1] == "EN_USO":
                        biciEncontrada = True
                        break
                if biciEncontrada == False:
                    print("No hay bicicletas en préstamo. No hay ninguna devolución que se pueda hacer")
                    time.sleep(3)
                    continue
                
                nombreCSV = "anclajes"
                anclajesDevolucion, _ = leerArchivo(nombreCSV)
                AnclajeDisponible = False
                for recorridoAnclajesDevolucion in anclajesDevolucion:
                    if recorridoAnclajesDevolucion[3] == "VACIO":
                        AnclajeDisponible = True
                        break
                    
                if AnclajeDisponible == False:
                    print(f"Ninguna estación cuenta con anclajes vacíos. No se puede hacer devolución de bicicletas\nTRABAJAMOS PARA SOLUCIONARLO PRONTO")
                    time.sleep(3)
                    continue
                
                print(interfazEstaciones)
                while True:
                    while True:
                        try:
                            estacionFin = int(input("Ingrese el índice de la estación en la que desea realizar la devolución -> "))
                            if not(1 <= estacionFin <= 3): raise ValueError
                            else: break
                        except ValueError as ve:
                            print("Opción inexistente. Digite nuevamente su opción")
                            continue

                    _, nombreEstacionFin, codigoEstacionFin = clasificacionEstacion(estacionFin, matrizEstacion1, matrizEstacion2, matrizEstacion3)
                    AnclajeDisponible = False
                    for recorridoAnclajesDevolucion in anclajesDevolucion:
                        if recorridoAnclajesDevolucion[3] == "VACIO" and recorridoAnclajesDevolucion[0] == codigoEstacionFin:
                            AnclajeDisponible = True
                            break
                    
                    if AnclajeDisponible == True:
                        break
                    else:
                        print(f"La estación {nombreEstacionFin} no tiene anclajes vacíos. No se puede realizar la devolución en esta estación")
                        continue
                    
                print(f"""
-------------------------------------------
    SISTEMA DE DEVOLUCIÓN DE BICICLETAS
          ESTACION {nombreEstacionFin}
-------------------------------------------
""")
                while True:
                    biciDevuelta = input("Ingrese el ID de la bicicleta que será devuelta -> ")

                    if len(biciDevuelta) != 3 or biciDevuelta[0] != "B" or not(biciDevuelta[1:].isnumeric()):
                        print("ID Inexistente")
                        continue
                    
                    nombreCSV = "bicicletas"
                    informacionBicicletasDevolucion, encabezadoBicicletasDevolucion = leerArchivo(nombreCSV)

                    biciEncontrada = False
                    for busquedaPrestamo in informacionBicicletasDevolucion:
                        if busquedaPrestamo[0] == biciDevuelta and busquedaPrestamo[1] == "EN_USO":
                            busquedaPrestamo[1] = "DISPONIBLE"
                            busquedaPrestamo[2] = codigoEstacionFin
                            biciEncontrada = True
                            reescribirArchivo(informacionBicicletasDevolucion, encabezadoBicicletasDevolucion, nombreCSV)
                            break

                    if biciEncontrada == False:
                        print(f"La bicicleta ingresada no se encuentra en préstamo\n")
                        time.sleep(2)
                        continue
                    else:
                        break
                nombreCSV = "anclajes"
                for recorridoAnclajesDevolucion2 in anclajesDevolucion:
                    if recorridoAnclajesDevolucion2[3] == "VACIO" and recorridoAnclajesDevolucion2[0] == codigoEstacionFin:
                        recorridoAnclajesDevolucion2[3] = "BICI"
                        recorridoAnclajesDevolucion2[4] = biciDevuelta
                        print(f"La bicicleta {biciDevuelta} ha sido devuelta con éxito.\nLa bicicleta {biciDevuelta} ha sido colocada en el anclaje ubicado en la fila {recorridoAnclajesDevolucion2[1]} en la columna {recorridoAnclajesDevolucion[2]}")
                        break
                reescribirArchivo(anclajesDevolucion, encabezadoAnclajes, nombreCSV)
                
                nombreCSV = "prestamo"
                prestamoDevolucion, encabezadoPrestamoDevolucion = leerArchivo(nombreCSV)
                
                nombreCSV = "clientes"
                nombreUsario, encabezadoNombreUsuario = leerArchivo(nombreCSV)
                
                
                for recorridoPrestamoDevolucion in prestamoDevolucion:
                    if recorridoPrestamoDevolucion[2] == biciDevuelta and recorridoPrestamoDevolucion[8] == "ACTIVO":
                        
                        for recorridoNombreUsuario in nombreUsario:
                            if recorridoPrestamoDevolucion[1] == recorridoNombreUsuario[0]:
                                nombreUsuarioDevolucion = recorridoNombreUsuario[1]
                                recorridoNombreUsuario[2] = False
                                break
                        break
                
                reescribirArchivo(nombreUsario,encabezadoNombreUsuario,nombreCSV)
                
                nombreCSV = "prestamo"                
                
                anioInicio, mesInicio, diaInicio, horaInicio, minutosInicio = validarFecha(tiempoInicio)
                
                while True:
                    try:
                        tiempoFin = input("""
----------------------------------------------------------
    INGRESE FECHA Y HORA DE FINALIZACIÓN DEL PRÉSTAMO
----------------------------------------------------------
Tener en cuenta:
    - La fecha y hora debe ir en formato AAAA-MM-DD-HH:HH
    - La hora debe ir en formato 24h
    - Solo es válido el año 2026
    - Los devoluciones se realizan entre las |4:00| y las |22:59|
    - Es erróneo ingresar una hora de devolución de préstamo anterior a la hora de inicio del préstamo

-> """) 

                        anioFin, mesFin, diaFin, horaFin, minutosFin = validarFecha(tiempoFin)
                        
                        if (diaInicio != diaFin) or (mesInicio != mesFin):
                            raise Exception("El día de inicio")
                        elif not(4 <= horaFin < 23):
                            raise Exception("No se permiten devoluciones a esta hora")
                        elif (horaInicio > horaFin) or (horaInicio == horaFin and minutosInicio >= minutosFin):
                            raise Exception("La hora de Fin es mayor o igual a la hora de finalización")
                        else:
                            break

                    except ValueError as ve:
                        print("Error. Por favor ingrese la fecha en números y/o en formato válido")
                        continue
                    except IndexError as ie:
                        print("Error. Formato de fecha y hora inválido")
                        continue
                    except Exception as e:
                        print(e)
                tiempoUso, cobroBicicletas = calcularCosto(horaInicio, minutosInicio, horaFin, minutosFin)
                
                for recorridoPrestamoDevolucion2 in prestamoDevolucion:
                    if recorridoPrestamoDevolucion2[2] == biciDevuelta and recorridoPrestamoDevolucion2[8] == "ACTIVO":
                        recorridoPrestamoDevolucion2[5] = estacionFin
                        recorridoPrestamoDevolucion2[6] = tiempoFin
                        recorridoPrestamoDevolucion2[7] = tiempoUso
                        recorridoPrestamoDevolucion2[8] = "FINALIZADO"
                        break
                reescribirArchivo(prestamoDevolucion, encabezadoPrestamoDevolucion, nombreCSV)
                print(f"Se le cobra ${cobroBicicletas} al usuario {nombreUsuarioDevolucion} por haber utilizado nuestro servicio de préstamo de bicicletas durante {tiempoUso} minutos")
                time.sleep(3)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
                with open("logica de programacion U/- PROYECTO FINAL/historial_General.txt","a+",encoding="utf-8",newline="") as Archivo_Historial_Prestamo_Devolucion:
                    Archivo_Historial_Prestamo_Devolucion.seek(0)
                    encabezado = Archivo_Historial_Prestamo_Devolucion.read()
                    if encabezado == "":
                        Archivo_Historial_Prestamo_Devolucion.write(f"HISTORIAL DE MODIFICACIONES GENERALES DE IN-BIKE\n")
                    Archivo_Historial_Prestamo_Devolucion.write(f"La bicicleta | {biciDevuelta} | tiene estado de prestamo | COMPLETADO | por el cliente {nombreUsuarioDevolucion}\n")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

            case 5:
                print(interfazEstaciones)
                while True:
                    try:
                        consultaEstacionMantenimiento = int(input("Ingrese el índice de la estación que desea consultar -> "))
                        if not(1 <= consultaEstacionMantenimiento <= 3): raise ValueError
                        else: break
                    except ValueError as ve:
                        print("Opción inexistente. Digite nuevamente su opción")
                        continue

                _, estacionMantenimiento, codigoEstacionMantenimiento = clasificacionEstacion(consultaEstacionMantenimiento, matrizEstacion1, matrizEstacion2, matrizEstacion3)
                print(f"""
-----------------------------------------------
        Estacion: {estacionMantenimiento}({codigoEstacionMantenimiento})
-----------------------------------------------

1. Servicio de MANTENIMIENTO
2. Proceso de REACTIVACION
""")
                while True:
                    try:
                        consultaServicioMantenimiento = int(input("Ingrese el índice del servicio que desea realizar-> "))
                        if not(1 <= consultaServicioMantenimiento <= 2): raise ValueError
                        else: break
                    except ValueError as ve:
                        print("Opción inexistente. Digite nuevamente su opción")
                        continue

                print(f"\nINGRESE LAS COORDENADAS DEL ANCLAJE")
                while True:
                    try:
                        coordenadaX = int(input("Ingrese la fila -> "))
                        if not(1 <= coordenadaX <= 3): raise ValueError
                        else: break
                    except ValueError as ve:
                            print("Fila inexistente")
                            continue
                while True:
                    try:
                        coordenadaY = int(input("Ingrese la columna -> "))
                        if not(1 <= coordenadaY <= 5): raise ValueError
                        else: break
                    except ValueError as ve:
                            print("Columna inexistente")
                            continue

                nombreCSV = "anclajes"
                informacionMantenimiento, encabezadoMantenimiento = leerArchivo(nombreCSV)

                match consultaServicioMantenimiento:

                    case 1:
                        for recorrido in informacionMantenimiento: 
                            if int(recorrido[1]) == coordenadaX and int(recorrido[2]) == coordenadaY and codigoEstacionMantenimiento == recorrido[0]:
                                idEstacionMantenimiento = recorrido[0]
                                if recorrido[3] == "VACIO":
                                    recorrido[3] = "MANTENIMIENTO"
                                    time.sleep(1)
                                    print(".")
                                    time.sleep(1)
                                    print(".")
                                    time.sleep(1)
                                    print(".")
                                    time.sleep(1)
                                    print("Cambio realizado correctamente")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                    with open("logica de programacion U/- PROYECTO FINAL/historial_General.txt","a+",encoding="utf-8",newline="") as Archivo_Historial_Anclajes:
                                        Archivo_Historial_Anclajes.seek(0)
                                        encabezado = Archivo_Historial_Anclajes.read()

                                        if encabezado == "":
                                            Archivo_Historial_Anclajes.write(f"HISTORIAL DE MODIFICACIONES GENERALES DE IN-BIKE\n")

                                        Archivo_Historial_Anclajes.write(f"La estacion {idEstacionMantenimiento} en el anclaje | {coordenadaX},{coordenadaY} | tuvo un servicio de | MANTENIMIENTO |\n")
##-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                    break
                                elif recorrido[3] == "MANTENIMIENTO":
                                    print("Este anclaje ya se encuentra en mantenimiento")
                                    break
                                else:
                                    print("Este anclaje está siendo utilizado en este momento")
                                    break
                        reescribirArchivo(informacionMantenimiento, encabezadoMantenimiento, nombreCSV)
                        time.sleep(3)

                    case 2:
                        for recorrido in informacionMantenimiento: 
                            if int(recorrido[1]) == coordenadaX and int(recorrido[2]) == coordenadaY and codigoEstacionMantenimiento == recorrido[0]:
                                idEstacionReactivacion = recorrido[0]
                                if recorrido[3] == "MANTENIMIENTO":  
                                    recorrido[3] = "VACIO"
                                    time.sleep(1)
                                    print(".")
                                    time.sleep(1)
                                    print(".")
                                    time.sleep(1)
                                    print(".")
                                    time.sleep(1)
                                    print("Cambio realizado correctamente")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
                                    with open("logica de programacion U/- PROYECTO FINAL/historial_General.txt","a+",encoding="utf-8",newline="") as Archivo_Historial_Anclajes:
                                        Archivo_Historial_Anclajes.seek(0)
                                        encabezado = Archivo_Historial_Anclajes.read()

                                        if encabezado == "":
                                            Archivo_Historial_Anclajes.write(f"HISTORIAL DE MODIFICACIONES GENERALES DE IN-BIKE\n")

                                        Archivo_Historial_Anclajes.write(f"La estacion {idEstacionReactivacion} en el anclaje | {coordenadaX},{coordenadaY} | tuvo un servicio de | REACTIVACION |\n")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
                                    break
                                else:
                                    print("Este anclaje no se encuentra en mantenimiento")
                                    break
                        reescribirArchivo(informacionMantenimiento, encabezadoMantenimiento, nombreCSV)
                        time.sleep(3)

            case 6:
                print("""
-----------------------------------------------
          SERVICIO DE REDISTRIBUCION
-----------------------------------------------
                    """)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                while True:
                    matrizEstacion1, matrizEstacion2, matrizEstacion3, encabezadoAnclajes = actualizacionMatrices()                          
                    bicisEstacion1 = cantidadBicicletas(matrizEstacion1)
                    bicisEstacion2 = cantidadBicicletas(matrizEstacion2)
                    bicisEstacion3 = cantidadBicicletas(matrizEstacion3)
                    estacionPresta, codigoEstacionPresta, estacionRecibe, codigoEstacionRecibe = sugerirRedistribuciones(bicisEstacion1, bicisEstacion2, bicisEstacion3)

                    if codigoEstacionRecibe == "NO APLICA":
                        print("TODAS LAS ESTACIONES TIENEN LAS BICICLETAS NECESARIAS PARA SEGUIR FUNCIONANDO CORRECTAMENTE")
                        print("Volviendo al menu principal")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        break
                    else:
                        if cantidadCambios >= 1:
                            time.sleep(1)
                            print("""
 █   █    ███  ███
███  █     █   █ █
█ █  ███   █   ███
""")
                            print("SE SUGIERE HACER OTRO CAMBIO")
                            time.sleep(0.5)
                        print(f"""
---------------------------------------------------------
La estacion de ORIGEN es: 
              | {estacionPresta} |
Esta estacion tiene vehiculos suficientes para distribuir""")
                        print(f"""---------------------------------------------------------
La estacion de DESTINO es: 
              | {estacionRecibe} |
Esta estacion recibira bicicletas de:
              | {estacionPresta} |""")
                    print("---------------------------------------------------------")
                    try:
                        while True:
                            aceptarDistribucion = int(input("¿Desea efectuar este cambio?   1. SI | 2. NO   "))
                            if not(1 <= aceptarDistribucion <= 2): raise ValueError
                            else: break
                    except ValueError as ve:
                        print("Opción inexistente. Digite nuevamente su opción")
                        continue
                    match aceptarDistribucion:
                        case 2:
                            print("Volviendo al menu principal")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            break
                        case 1:
                            with open("logica de programacion U/- PROYECTO FINAL/anclajes.csv","r", encoding="utf-8", newline="") as Archivo_Anclaje3:
                                nombreCSV = "anclajes"
                                encabezadoCambio = Archivo_Anclaje3.readline()
                                informacionCambio = list(csv.reader(Archivo_Anclaje3))
                                for escanear in informacionCambio:
                                    if escanear[3] == "BICI" and escanear[0] == codigoEstacionPresta:
                                        idBicicleta = escanear[4]
                                        escanear[3] = "VACIO"
                                        escanear[4] = "VACIO"
                                        break
                                for escanear2 in informacionCambio:        
                                    if escanear2[3] == "VACIO" and escanear2[4] == "VACIO" and escanear2[0] == codigoEstacionRecibe:
                                        escanear2[3] = "BICI"
                                        escanear2[4] = idBicicleta
                                        break
                                reescribirArchivo(informacionCambio, encabezadoCambio, nombreCSV)

                            with open("logica de programacion U/- PROYECTO FINAL/bicicletas.csv", "r", encoding="utf-8", newline="") as Archivo_Bicicletas2:
                                nombreCSV = "bicicletas"
                                encabezadoCambioBicicletas = Archivo_Bicicletas2.readline()
                                informacionCambioBicicletas = list(csv.reader(Archivo_Bicicletas2))
            
                                for recorridoBicicletas in informacionCambioBicicletas:
                                    if recorridoBicicletas[0] == idBicicleta:
                                        recorridoBicicletas[2] = codigoEstacionRecibe
                                        reescribirArchivo(informacionCambioBicicletas, encabezadoCambioBicicletas, nombreCSV)
                                        break

                            print(f"¡ENHORABUENA! Cambio realizado correctamente\n")
                            cantidadCambios += 1
                            with open("logica de programacion U/- PROYECTO FINAL/historial_General.txt","a+",encoding="utf-8",newline="") as Archivo_Historial_Cambios:
                                Archivo_Historial_Cambios.seek(0)
                                encabezado = Archivo_Historial_Cambios.read()
                                if encabezado == "":
                                    Archivo_Historial_Cambios.write(f"HISTORIAL DE MODIFICACIONES GENERALES DE IN-BIKE\n")
                                Archivo_Historial_Cambios.write(f"La bicicleta | {idBicicleta} | se ha transferido de la estacion | {estacionPresta} | a | {estacionRecibe} |\n")
                    continue
            
            case 7:
                try:
                    with open("logica de programacion U/- PROYECTO FINAL/historial_General.txt","r",encoding="utf-8",newline="") as Archivo_Historial_General:
                        contenidoArchivoGeneral = Archivo_Historial_General.read()
                        print("""
---------------------------------------------------------------
                HISTORIAL DE REGISTROS
---------------------------------------------------------------
Escoja un indice para verificar el historial especificado:
1. Prestamos
2. Devoluciones
3. Prestamos y Devoluciones
4. Mantenimientos
5. Reactivaciones
6. Matenimientos y Reactivaciones
7. Transeferencias
8. Ranking de estaciones
    """)
                        while True:
                            try:
                                indiceHistorial = int(input("Ingrese el índice del historial que desea consultar -> "))
                                if not(1 <= indiceHistorial <= 8): raise ValueError
                                else: break
                            except ValueError as ve:
                                print("Opción inexistente. Digite nuevamente su opción")
                                continue
                        
                        match indiceHistorial:
                            
                            case 1:
                                for lineaPrestamoIniciado in contenidoArchivoGeneral.splitlines():
                                    datosPrestamoIniciado = lineaPrestamoIniciado.split("|")
                                    if len(datosPrestamoIniciado) == 5:
                                        if datosPrestamoIniciado[3].strip() == "INICIADO":
                                            print(lineaPrestamoIniciado)
                                    else:
                                        print("No se ha realizado el proceso aun, realicelo y vuelva")

                            case 2:
                                for lineaDevolucionCompletada in contenidoArchivoGeneral.splitlines():
                                    datosDevolucionCompletada = lineaDevolucionCompletada.split("|")
                                    if len(datosDevolucionCompletada) == 5:
                                        if datosDevolucionCompletada[3].strip() == "COMPLETADO":
                                            print(lineaDevolucionCompletada)
                                    else:
                                        print("No se ha realizado el proceso aun, realicelo y vuelva")

                            case 3:
                                cadenasPrestamosDevoluciones = contenidoArchivoGeneral.splitlines()
                                for posicionPrestamo in range(len(cadenasPrestamosDevoluciones)):
                                    lineaPrestamo = cadenasPrestamosDevoluciones[posicionPrestamo]
                                    datosPrestamo = lineaPrestamo.split("|")
                                    for posicionDevolucion in range(posicionPrestamo + 1, len(cadenasPrestamosDevoluciones)):
                                        lineaDevolucion = cadenasPrestamosDevoluciones[posicionDevolucion]
                                        datosDevolucion = lineaDevolucion.split("|")
                                        if len(datosPrestamo) == 5 and len(datosDevolucion) == 5:
                                            if (datosPrestamo[1].strip() == datosDevolucion[1].strip() and datosPrestamo[4].strip() == datosDevolucion[4].strip()):
                                                if datosPrestamo[3].strip() == "INICIADO" and datosDevolucion[3].strip() == "COMPLETADO":
                                                    print(lineaPrestamo)
                                                    print(lineaDevolucion)
                                    else:
                                        print("No se ha realizado el proceso aun, realicelo y vuelva")
                                        
                            case 4:
                                for lineaMantenimiento in contenidoArchivoGeneral.splitlines():
                                    datosMantenimiento = lineaMantenimiento.split("|")
                                    if len(datosMantenimiento) == 5:
                                        if datosMantenimiento[3].strip() == "MANTENIMIENTO":
                                            print(lineaMantenimiento)
                                    else:
                                        print("No se ha realizado el proceso aun, realicelo y vuelva")
                                        
                            case 5:
                                for lineaReactivacion in contenidoArchivoGeneral.splitlines():
                                    datosReactivacion = lineaReactivacion.split("|")
                                    if len(datosReactivacion) == 5:
                                        if datosReactivacion[3].strip() == "REACTIVACION":
                                            print(lineaReactivacion)
                                    else:
                                        print("No se ha realizado el proceso aun, realicelo y vuelva")
                                        
                            case 6:
                                cadenasMantenimientosReactivaciones = contenidoArchivoGeneral.splitlines()
                                for posicionMantenimiento in range(len(cadenasMantenimientosReactivaciones)):
                                    lineaMantenimiento = cadenasMantenimientosReactivaciones[posicionMantenimiento]
                                    datosMantenimiento = lineaMantenimiento.split("|")
                                    for posicionReactivacion in range(posicionMantenimiento + 1, len(cadenasMantenimientosReactivaciones)):
                                        lineaReactivacion = cadenasMantenimientosReactivaciones[posicionReactivacion]
                                        datosReactivacion = lineaReactivacion.split("|")
                                        if len(datosMantenimiento) == 5 and len(datosReactivacion) == 5:
                                            if (datosMantenimiento[0].strip() == datosReactivacion[0].strip() and datosMantenimiento[1].strip() == datosReactivacion[1].strip()):
                                                if datosMantenimiento[3].strip() == "MANTENIMIENTO" and datosReactivacion[3].strip() == "REACTIVACION":
                                                    print(lineaMantenimiento)
                                                    print(lineaReactivacion)
                                    else:
                                        print("No se ha realizado el proceso aun, realicelo y vuelva")
                                        
                            case 7:
                                noExiste2 = True
                                for lineaTransferencia in contenidoArchivoGeneral.splitlines():
                                    datosTransferencia = lineaTransferencia.split("|")
                                    if len(datosTransferencia) == 7:
                                        if datosTransferencia[2].strip() == "se ha transferido de la estacion":
                                            print(lineaTransferencia)
                                            noExiste2 = False
                                if noExiste2 == True:    
                                    print("No se ha realizado el proceso aun, realicelo y vuelva")
                            case 8: 
                                noExiste = True
                                print("""
    --------------------------------------------------
                RANKING ESTACIONES
    --------------------------------------------------
    El orden de las estaciones segun la cantidad de
    prestamos es:""")
                                nombreCSV = "prestamo"
                                informacionRanking, _ = leerArchivo(nombreCSV)
                                rankingEstacion1 = 0
                                rankingEstacion2 = 0
                                rankingEstacion3 = 0
                                for recorridoRanking in informacionRanking:
                                    if recorridoRanking[3] == "E01":
                                        rankingEstacion1 += 1
                                        codigoRanking1 = "E01"
                                    elif recorridoRanking[3] == "E02":
                                        rankingEstacion2 += 1
                                        codigoRanking2 = "E02"
                                    elif recorridoRanking[3] == "E03":
                                        rankingEstacion3 += 1
                                        codigoRanking3 = "E03"
                                    else:
                                        noExiste = True
                                    
                                    if noExiste != True:
                                        if rankingEstacion1 >= rankingEstacion2 and rankingEstacion1 >= rankingEstacion3:
                                            print(f"1. {codigoRanking1}: {rankingEstacion1} prestamos")
                                            if rankingEstacion2 >= rankingEstacion3:
                                                print(f"2. {codigoRanking2}: {rankingEstacion2} prestamos")
                                                print(f"3. {codigoRanking3}: {rankingEstacion3} prestamos")
                                            else:
                                                print(f"2. {codigoRanking3}: {rankingEstacion3} prestamos")
                                                print(f"3. {codigoRanking2}: {rankingEstacion2} prestamos")
                                        elif rankingEstacion2 >= rankingEstacion1 and rankingEstacion2 >= rankingEstacion3:
                                            print(f"1. {codigoRanking2}: {rankingEstacion2} prestamos")
                                            if rankingEstacion1 >= rankingEstacion3:
                                                print(f"2. {codigoRanking1}: {rankingEstacion1} prestamos")
                                                print(f"3. {codigoRanking3}: {rankingEstacion3} prestamos")
                                            else:
                                                print(f"2. {codigoRanking3}: {rankingEstacion3} prestamos")
                                                print(f"3. {codigoRanking1}: {rankingEstacion1} prestamos")
                                        else:
                                            print(f"1. {codigoRanking3}: {rankingEstacion3} prestamos")
                                            if rankingEstacion1 >= rankingEstacion2:
                                                print(f"2. {codigoRanking1}: {rankingEstacion1} prestamos")
                                                print(f"3. {codigoRanking2}: {rankingEstacion2} prestamos")
                                            else:
                                                print(f"2. {codigoRanking2}: {rankingEstacion2} prestamos")
                                                print(f"3. {codigoRanking1}: {rankingEstacion1} prestamos")
                                    else:
                                        print("No se ha realizado el proceso aun, realicelo y vuelva")

                                
                except FileNotFoundError as fe:
                    print("Aun no existe ningun historial, realiza otras operaciones para empezar a agregar contenido")
            case 0:
                print("""
                  ____  ____      _     ____   ___     _     ____     ____    ___   ____      _   _  ____      _     ____  
                 / ___||  _ \    / \   / ___| |_ _|   / \   / ___|   |  _ \  / _ \ |  _ \    | | | |/ ___|    / \   |  _ \ 
                | |  _ | |_) |  / _ \  | |     | |   / _ \  \___ \   | |_) || | | || |_) |   | | | |\___ \   / _ \  | |_) |
                | |_| ||  _ <  / ___ \ | |___  | |  / ___ \  ___) |  |  __/ | |_| ||  _ <    | |_| | ___) | / ___ \ |  _ < 
                 \____||_| \_\/_/   \_\____| |___|/_/   \_\|____/   |_|     \___/ |_| \_\    \___/ |____/ /_/   \_\|_| \_\

                                                 ___  _   _          ____   ___  _  __ _____                             
                                                |_ _|| \ | |        | __ ) |_ _|| |/ /| ____|                            
                                                 | | |  \| | _____  |  _ \  | | | ' / |  _|                              
                                                 | | | |\  ||_____| | |_) | | | | . \ | |___                             
                                                |___||_| \_|        |____/ |___||_|\_\|_____|
                """)
                exit()

except ValueError as ve:
    print(f"ERROR DE CONVERSIÓN DE DATOS {ve}")
except TypeError as te:
    print(f"ERROR DE TIPO DE DATO {te}")
except Exception as e:
    print(f"ERROR GENERAL DEL SISTEMA {e}")