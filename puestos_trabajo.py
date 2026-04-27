# Cachay Vargas Joseph Ivan
# Evaluacion T1 - Analisis de Algoritmos y Estrategias de Programacion
# Semestre 2026-1

class PuestoDeTrabajo:
    def __init__(self, codigo, descripcion, areaSolicitante, plazasRequeridas, sueldo):
        self.codigo = codigo
        self.descripcion = descripcion
        self.areaSolicitante = areaSolicitante
        self.plazasRequeridas = plazasRequeridas
        self.sueldo = sueldo

    def mostrar(self):
        print("  Codigo          :", self.codigo)
        print("  Descripcion     :", self.descripcion)
        print("  Area Solicitante:", self.areaSolicitante)
        print("  Plazas Requeridas:", self.plazasRequeridas)
        print("  Sueldo          : S/.", self.sueldo)
        print("  -----------------------------------------")


# Lista global de puestos
listaPuestos = []


# -------------------------------------------------------
# 1 - AgregaPuesto
# -------------------------------------------------------
def AgregaPuesto():
    print("\n--- Agregar Puesto de Trabajo ---")

    # Validar codigo
    while True:
        entrada = input("Ingrese codigo (entero > 0): ")
        if entrada.isdigit() and int(entrada) > 0:
            codigo = int(entrada)
            break
        else:
            print("  ERROR: El codigo debe ser un numero entero mayor a 0.")

    # Validar descripcion
    while True:
        descripcion = input("Ingrese descripcion (minimo 3 letras): ")
        if len(descripcion) >= 3:
            break
        else:
            print("  ERROR: La descripcion debe tener al menos 3 letras.")

    # Validar areaSolicitante
    while True:
        areaSolicitante = input("Ingrese area solicitante (minimo 3 letras): ")
        if len(areaSolicitante) >= 3:
            break
        else:
            print("  ERROR: El area solicitante debe tener al menos 3 letras.")

    # Validar plazasRequeridas
    while True:
        entrada = input("Ingrese plazas requeridas (entero > 0): ")
        if entrada.isdigit() and int(entrada) > 0:
            plazasRequeridas = int(entrada)
            break
        else:
            print("  ERROR: Las plazas requeridas deben ser un numero entero mayor a 0.")

    # Validar sueldo
    while True:
        entrada = input("Ingrese sueldo (mayor a 0): ")
        try:
            sueldo = float(entrada)
            if sueldo > 0:
                break
            else:
                print("  ERROR: El sueldo debe ser mayor a 0.")
        except:
            print("  ERROR: Ingrese un valor numerico valido.")

    # Busqueda lineal para validar duplicados
    for i in range(len(listaPuestos)):
        if listaPuestos[i].codigo == codigo:
            print("  ERROR: Ya existe un puesto con ese codigo.")
            return
        if listaPuestos[i].descripcion == descripcion:
            print("  ERROR: Ya existe un puesto con esa descripcion.")
            return
        if listaPuestos[i].areaSolicitante == areaSolicitante:
            print("  ERROR: Ya existe un puesto con esa area solicitante.")
            return

    nuevoPuesto = PuestoDeTrabajo(codigo, descripcion, areaSolicitante, plazasRequeridas, sueldo)
    listaPuestos.append(nuevoPuesto)
    print("  Puesto agregado correctamente.")


# -------------------------------------------------------
# 2 - MostrarTodo
# -------------------------------------------------------
def MostrarTodo():
    print("\n--- Lista de Puestos de Trabajo (sin ordenar) ---")
    if len(listaPuestos) == 0:
        print("  No hay puestos registrados.")
        return
    for i in range(len(listaPuestos)):
        print("  [" + str(i + 1) + "]")
        listaPuestos[i].mostrar()


# -------------------------------------------------------
# 3 - BorraPuesto
# -------------------------------------------------------
def BorraPuesto():
    print("\n--- Borrar Puesto de Trabajo ---")
    if len(listaPuestos) == 0:
        print("  No hay puestos registrados.")
        return

    while True:
        entrada = input("Ingrese el codigo del puesto a eliminar: ")
        if entrada.isdigit() and int(entrada) > 0:
            codigoBuscar = int(entrada)
            break
        else:
            print("  ERROR: Ingrese un codigo valido (entero > 0).")

    # Ordenar por codigo de mayor a menor - Metodo Burbuja
    n = len(listaPuestos)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if listaPuestos[j].codigo < listaPuestos[j + 1].codigo:
                temp = listaPuestos[j]
                listaPuestos[j] = listaPuestos[j + 1]
                listaPuestos[j + 1] = temp

    # Busqueda lineal para encontrar y eliminar
    encontrado = False
    i = 0
    while i < len(listaPuestos):
        if listaPuestos[i].codigo == codigoBuscar:
            print("  Puesto encontrado y eliminado:")
            listaPuestos[i].mostrar()
            listaPuestos.pop(i)
            encontrado = True
        else:
            i += 1

    if not encontrado:
        print("  No se encontro ningun puesto con ese codigo.")


# -------------------------------------------------------
# 4 - BuscaSueldo
# -------------------------------------------------------
def BuscaSueldo():
    print("\n--- Buscar Puestos por Sueldo ---")
    if len(listaPuestos) == 0:
        print("  No hay puestos registrados.")
        return

    # Ordenar por sueldo de mayor a menor - Metodo Insercion
    n = len(listaPuestos)
    for i in range(1, n):
        clave = listaPuestos[i]
        j = i - 1
        while j >= 0 and listaPuestos[j].sueldo < clave.sueldo:
            listaPuestos[j + 1] = listaPuestos[j]
            j -= 1
        listaPuestos[j + 1] = clave

    while True:
        entrada = input("Ingrese el sueldo a buscar: ")
        try:
            sueldoBuscar = float(entrada)
            if sueldoBuscar > 0:
                break
            else:
                print("  ERROR: El sueldo debe ser mayor a 0.")
        except:
            print("  ERROR: Ingrese un valor numerico valido.")

    # Busqueda binaria para encontrar un indice con ese sueldo
    izq = 0
    der = len(listaPuestos) - 1
    indiceMedio = -1

    while izq <= der:
        medio = (izq + der) // 2
        if listaPuestos[medio].sueldo == sueldoBuscar:
            indiceMedio = medio
            break
        elif listaPuestos[medio].sueldo > sueldoBuscar:
            izq = medio + 1
        else:
            der = medio - 1

    if indiceMedio == -1:
        print("  No se encontro ningun puesto con ese sueldo.")
        return

    # Expandir hacia la izquierda y derecha para encontrar todos los coincidentes
    inicio = indiceMedio
    while inicio > 0 and listaPuestos[inicio - 1].sueldo == sueldoBuscar:
        inicio -= 1

    fin = indiceMedio
    while fin < len(listaPuestos) - 1 and listaPuestos[fin + 1].sueldo == sueldoBuscar:
        fin += 1

    print("  Puestos encontrados con sueldo S/.", sueldoBuscar, ":")
    for i in range(inicio, fin + 1):
        listaPuestos[i].mostrar()


# -------------------------------------------------------
# 5 - PuestosAContratar
# -------------------------------------------------------
def PuestosAContratar():
    print("\n--- Puestos a Contratar segun Presupuesto ---")
    if len(listaPuestos) == 0:
        print("  No hay puestos registrados.")
        return

    while True:
        entrada = input("Ingrese el monto total a invertir en salarios: ")
        try:
            montoTotal = float(entrada)
            if montoTotal > 0:
                break
            else:
                print("  ERROR: El monto debe ser mayor a 0.")
        except:
            print("  ERROR: Ingrese un valor numerico valido.")

    # Calcular total requerido por puesto = plazasRequeridas * sueldo
    # Ordenar de mayor a menor segun total requerido - Metodo Seleccion
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

    print("\n  Puestos que se pueden cubrir con S/.", montoTotal, ":")
    montoAcumulado = 0.0
    hayCubiertos = False

    for i in range(len(listaPuestos)):
        totalPuesto = listaPuestos[i].plazasRequeridas * listaPuestos[i].sueldo
        if montoAcumulado + totalPuesto <= montoTotal:
            montoAcumulado += totalPuesto
            print("  Puesto cubierto (Total requerido: S/.", totalPuesto, "):")
            listaPuestos[i].mostrar()
            hayCubiertos = True

    if hayCubiertos:
        print("  Monto total utilizado: S/.", montoAcumulado)
        print("  Monto restante       : S/.", montoTotal - montoAcumulado)
    else:
        print("  El presupuesto no alcanza para cubrir ningun puesto.")


# -------------------------------------------------------
# Carga de 6 puestos de trabajo de ejemplo
# -------------------------------------------------------
def cargarDatosEjemplo():
    listaPuestos.append(PuestoDeTrabajo(101, "Desarrollador Web", "Tecnologia", 3, 3500.0))
    listaPuestos.append(PuestoDeTrabajo(205, "Analista de Datos", "Inteligencia de Negocios", 2, 4200.0))
    listaPuestos.append(PuestoDeTrabajo(310, "Diseñador Grafico", "Marketing", 1, 2800.0))
    listaPuestos.append(PuestoDeTrabajo(415, "Contador Senior", "Finanzas", 2, 5000.0))
    listaPuestos.append(PuestoDeTrabajo(520, "Asistente Administrativo", "Administracion", 4, 1800.0))
    listaPuestos.append(PuestoDeTrabajo(625, "Tecnico de Soporte", "Sistemas", 3, 2500.0))


# -------------------------------------------------------
# Menu principal
# -------------------------------------------------------
def menu():
    cargarDatosEjemplo()
    opcion = ""
    while opcion != "6":
        print("\n========================================")
        print("   SISTEMA DE PUESTOS DE TRABAJO")
        print("   Cachay Vargas Joseph Ivan")
        print("========================================")
        print("  1. AgregaPuesto()")
        print("  2. MostrarTodo()")
        print("  3. BorraPuesto()")
        print("  4. BuscaSueldo()")
        print("  5. PuestosAContratar()")
        print("  6. Salir")
        print("========================================")
        opcion = input("Seleccione una opcion: ")

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
            print("\n  Hasta luego, Joseph!")
        else:
            print("  Opcion invalida. Intente de nuevo.")


menu()
