# Cachay Vargas Joseph Ivan
# T1 Analisis de Algoritmos
# 2026-1 abril :0
# clase para guardar cada puesto de trabajo
class PuestoDeTrabajo:
    def __init__(self, codigo, descripcion, areaSolicitante, plazasRequeridas, sueldo):
        self.codigo = codigo
        self.descripcion = descripcion
        self.areaSolicitante = areaSolicitante
        self.plazasRequeridas = plazasRequeridas
        self.sueldo = sueldo
        
    # muestra los datos del puesto
    def mostrar(self):
        print("  codigo:", self.codigo)
        print("  descripcion:", self.descripcion)
        print("  area solicitante:", self.areaSolicitante)
        print("  plazas requeridas:", self.plazasRequeridas)
        print("  sueldo: S/.", self.sueldo)
        print("  ---")


# lista donde se guardan todos los puestos
listaPuestos = []


# opcion 1: agregar un puesto nuevo
def AgregaPuesto():
    print("\n== Agregar Puesto ==")

    # pido el codigo y valido que sea numero y mayor a 0
    while True:
        entrada = input("codigo (numero entero > 0): ")
        if entrada.isdigit() and int(entrada) > 0:
            codigo = int(entrada)
            break
        print("tiene que ser un numero entero mayor a 0, intente de nuevo")

    # valido descripcion minimo 3 letras
    while True:
        descripcion = input("descripcion (min 3 letras): ")
        if len(descripcion) >= 3:
            break
        print("minimo 3 letras, intente de nuevo")

    # valido area solicitante minimo 3 letras
    while True:
        areaSolicitante = input("area solicitante (min 3 letras): ")
        if len(areaSolicitante) >= 3:
            break
        print("minimo 3 letras, intente de nuevo")

    # valido plazas requeridas
    while True:
        entrada = input("plazas requeridas (numero entero > 0): ")
        if entrada.isdigit() and int(entrada) > 0:
            plazasRequeridas = int(entrada)
            break
        print("tiene que ser un numero entero mayor a 0, intente de nuevo")

    # valido sueldo,
    while True:
        entrada = input("sueldo (mayor a 0): ")
        try:
            sueldo = float(entrada)
            if sueldo > 0:
                break
            else:
                print("el sueldo tiene que ser mayor a 0")
        except:
            print("ingrese un numero valido")

    # busqueda lineal para ver si ya existe ese codigo, descripcion o area
    for i in range(len(listaPuestos)):
        if listaPuestos[i].codigo == codigo:
            print("ya hay un puesto con ese codigo, no se puede agregar")
            return
        if listaPuestos[i].descripcion == descripcion:
            print("ya hay un puesto con esa descripcion, no se puede agregar")
            return
        if listaPuestos[i].areaSolicitante == areaSolicitante:
            print("ya hay un puesto con esa area solicitante, no se puede agregar")
            return

    # si no hay duplicados lo agrego a la lista
    nuevo = PuestoDeTrabajo(codigo, descripcion, areaSolicitante, plazasRequeridas, sueldo)
    listaPuestos.append(nuevo)
    print("puesto agregado!")


# opcion 2: mostrar todos sin ordenar
def MostrarTodo():
    print("\n== Lista de Puestos (sin ordenar) ==")
    if len(listaPuestos) == 0:
        print("no hay puestos registrados todavia")
        return
    for i in range(len(listaPuestos)):
        print("[" + str(i + 1) + "]")
        listaPuestos[i].mostrar()


# opcion 3: borrar un puesto por codigo
def BorraPuesto():
    print("\n=,= Borrar Puesto =,=")
    if len(listaPuestos) == 0:
        print("no hay puestos para borrar")
        return

    while True:
        entrada = input("codigo del puesto a eliminar: ")
        if entrada.isdigit() and int(entrada) > 0:
            codigoBuscar = int(entrada)
            break
        print("ingrese un codigo valido")

    # ordeno por codigo de mayor a menor con burbuja
    n = len(listaPuestos)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if listaPuestos[j].codigo < listaPuestos[j + 1].codigo:
                temp = listaPuestos[j]
                listaPuestos[j] = listaPuestos[j + 1]
                listaPuestos[j + 1] = temp

    # busqueda lineal para encontrar y eliminar el que coincida
    encontrado = False
    i = 0
    while i < len(listaPuestos):
        if listaPuestos[i].codigo == codigoBuscar:
            print("encontrado y eliminado :")
            listaPuestos[i].mostrar()
            listaPuestos.pop(i)
            encontrado = True
        else:
            i += 1

    if not encontrado:
        print("no se encontro ningun puesto con ese codigo :|")


# opcion 4: buscar puestos por sueldo
def BuscaSueldo():
    print("\n=.= Buscar por Sueldo =.=")
    if len(listaPuestos) == 0:
        print("no hay puestos registrados")
        return

    # ordeno por sueldo de mayor a menor con insercion
    n = len(listaPuestos)
    for i in range(1, n):
        clave = listaPuestos[i]
        j = i - 1
        # muevo los menores a la derecha
        while j >= 0 and listaPuestos[j].sueldo < clave.sueldo:
            listaPuestos[j + 1] = listaPuestos[j]
            j -= 1
        listaPuestos[j + 1] = clave

    while True:
        entrada = input("sueldo a buscar : ")
        try:
            sueldoBuscar = float(entrada)
            if sueldoBuscar > 0:
                break
            else:
                print("el sueldo tiene que ser mayor a 0")
        except:
            print("ingrese un número valido")

    # busqueda binaria (lista esta de mayor a menor)
    # si el del medio es mayor al buscado -> busco a la derecha
    # si el del medio es menor al buscado -> busco a la izquierda
    izq = 0
    der = len(listaPuestos) - 1
    indiceMedio = -1

    while izq <= der:
        medio = (izq + der) // 2
        if listaPuestos[medio].sueldo == sueldoBuscar:
            indiceMedio = medio
            break
        elif listaPuestos[medio].sueldo > sueldoBuscar:
            # el buscado es menor, esta mas a la derecha
            izq = medio + 1
        else:
            # el buscado es mayor, esta mas a la izquierda
            der = medio - 1

    if indiceMedio == -1:
        print("no se encontro ningun puesto con ese sueldo .-.")
        return

    # expando a la izquierda por si hay mas con el mismo sueldo
    inicio = indiceMedio
    while inicio > 0 and listaPuestos[inicio - 1].sueldo == sueldoBuscar:
        inicio -= 1

    # expando a la derecha igual
    fin = indiceMedio
    while fin < len(listaPuestos) - 1 and listaPuestos[fin + 1].sueldo == sueldoBuscar:
        fin += 1

    print("puestos con sueldo S/.", sueldoBuscar, ":")
    for i in range(inicio, fin + 1):
        listaPuestos[i].mostrar()


# opcion 5: ver que puestos se pueden contratar con un presupuesto
def PuestosAContratar():
    print("\n=.= Puestos a Contratar segun Presupuesto =.=")
    if len(listaPuestos) == 0:
        print("no hay puestos registrados :|")
        return

    while True:
        entrada = input("monto total a invertir en salarios: S/. ")
        try:
            montoTotal = float(entrada)
            if montoTotal > 0:
                break
            else:
                print("tiene que ser mayor a 0")
        except:
            print("ingrese un numero valido :|")

    # calculo total de cada puesto = plazas * sueldo
    # ordeno de mayor a menor con seleccion segun ese total
    n = len(listaPuestos)
    for i in range(n - 1):
        indiceMayor = i
        for j in range(i + 1, n):
            totalJ = listaPuestos[j].plazasRequeridas * listaPuestos[j].sueldo
            totalMayor = listaPuestos[indiceMayor].plazasRequeridas * listaPuestos[indiceMayor].sueldo
            if totalJ > totalMayor:
                indiceMayor = j
        temp = listaPuestos[i]
        listaPuestos[i] = listaPuestos[indiceMayor]
        listaPuestos[indiceMayor] = temp

    # voy sumando los totales y muestro los que caben en el presupuesto
    print("\npuestos que se pueden cubrir con S/.", montoTotal, ":")
    montoAcumulado = 0.0
    hayCubiertos = False

    for i in range(len(listaPuestos)):
        totalPuesto = listaPuestos[i].plazasRequeridas * listaPuestos[i].sueldo
        if montoAcumulado + totalPuesto <= montoTotal:
            montoAcumulado += totalPuesto
            print("  puesto cubierto (costo total: S/.", totalPuesto, "):")
            listaPuestos[i].mostrar()
            hayCubiertos = True

    if hayCubiertos:
        print("monto usado: S/.", montoAcumulado)
        print("monto sobrante: S/.", montoTotal - montoAcumulado)
    else:
        print("el presupuesto no alcanza para ningun puesto °-°")


# cargamo los 6 puestos de ejemplo al iniciar .- .
def cargarDatosEjemplo():
    listaPuestos.append(PuestoDeTrabajo(101, "Desarrollador Web", "Tecnologia", 3, 3500.0))
    listaPuestos.append(PuestoDeTrabajo(205, "Analista de Datos", "Inteligencia de Negocios", 2, 4200.0))
    listaPuestos.append(PuestoDeTrabajo(310, "Disenador Grafico", "Marketing", 1, 2800.0))
    listaPuestos.append(PuestoDeTrabajo(415, "Contador Senior", "Finanzas", 2, 5000.0))
    listaPuestos.append(PuestoDeTrabajo(520, "Asistente Administrativo", "Administracion", 4, 1800.0))
    listaPuestos.append(PuestoDeTrabajo(625, "Tecnico de Soporte", "Sistemas", 3, 2500.0))


# menu principal que se repite hasta que el usuario salga
def menu():
    cargarDatosEjemplo()
    opcion = ""
    while opcion != "6":
        print("\n................................")
        print("  PUESTOS DE TRABAJO")
        print("  Cachay Vargas Joseph Ivan")
        print(".................................")
        print("  1. AgregaPuesto()")
        print("  2. MostrarTodo()")
        print("  3. BorraPuesto()")
        print("  4. BuscaSueldo()")
        print("  5. PuestosAContratar()")
        print("  6. Salir")
        print(".....................................")
        opcion = input("opcion: ")

        if opcion == "1":
            AgregaPuesto()
        elif opcion == "2":
            MostrarTodo()
        elif opcion == "3":
            BorraPuesto()
        elif opcion == "4":
            BuscaSueldo()
        elif opcion == "5":
            PuestosAContratar()
        elif opcion == "6":
            print("saliendo...")
        else:
            print("opcion invalida, intente de nuevo")


menu()
