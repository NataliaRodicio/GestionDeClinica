continuar = "s"
 
pacientes = []
continuar = input("Bienvenidos/as a Sistema de Gestion de Clinica, ingrese cualquier tecla o Q para terminar: ")

    
def mostrar_menu():
    print('''
        Menu:
          1. Cargar Pacientes.
          2. Mostrar todos los pacientes.
          3. Buscar paciente por historia clinica.
          4. Ordenar pacientes por numero de historia clinica.
          5. Mostrar paciente con mas dias de internacion.
          6. Mostrar paciente con menos dias de internacion.
          7. Promedio de pacientes con mas de 5 dias de internacion.
          8. Promedio de dias de internacion de todos los pacientes.
          9. Salir.
          elija una opcion: 
          
''')
    opcion = input("Elija una opcion: ")
    match opcion:
        case "1":
            cargar_paciente(pacientes)
        case "2":
            mostrar_pacientes(pacientes)
        case "3":
            buscar_pacientes(pacientes)
        case "4":
            ordenar_pacientes(pacientes)
        case "5":
            mas_dias_internacion(pacientes)
        case "6":
            menos_dias_internacion(pacientes)
        case "7":
            mas_de_5_dias(pacientes)
        case "8":
            promedio_internacion(pacientes)
        case "9":
            salir()
        case _:
            print("Incorrecto, elija una opcion valida")


def cargar_paciente(pacientes: list) -> list:
    continuar = "s"
    
    while continuar == "s":
        historia_clinica = int(input("Ingrese el Numero de Historia Clinica: "))
        nombre = input("Ingrese el Nombre del Paciente: ").title()
        edad = int(input("Ingrese la edad del paciente: "))
        diagnostico = input("Ingrese el diagnostico del paciente: ").title()
        dias_internacion = int(input("Ingrese la cantidad de dias de internacion: "))
        
        pacientes.append([historia_clinica, nombre, edad, diagnostico, dias_internacion])
        print(f"Paciente agregado: Historia clinica: {historia_clinica}, Nombre: {nombre}, Edad: {edad}, Diagnostico: {diagnostico} y Dias de Internacion: {dias_internacion}")
        
        continuar = input("¿Desea ingresar más pacientes? (s/n): ").lower()

    continuar = input("Presione Enter para volver al menú o Q para salir: ")
    if continuar.lower() == "q":
        print("Gracias por usar nuestro Sistema de Gestion de Clinica. ¡Hasta luego!")
        exit()
    
    return pacientes

def mostrar_pacientes(pacientes: list) -> list:
    print("Todos los Pacientes:")
    for fila in pacientes:
        print(fila)
    continuar = input("Presione Enter para volver al menú o Q para salir: ")
    if continuar.lower() == "q":
        print("Gracias por usar nuestro Sistema de Gestion de Clinica. ¡Hasta luego!")
        exit()
    return fila

def buscar_pacientes(pacientes):
    
    continuar = "s"
    
    while continuar == "s":
        paciente_buscado = int(input("Ingrese el numero de Historia clinica: "))
        
        for paciente in pacientes:
            if paciente[0] == paciente_buscado: 
                nombre = paciente[1]
                edad = paciente[2]
                diagnostico = paciente[3]
                dias_internacion = paciente[4]
                print(f"El paciente encontrado es: {nombre}, su edad es: {edad}, "
                      f"su diagnostico es: {diagnostico} y los dias de internacion: {dias_internacion}.")
                break
        else: 
            print("Paciente no encontrado.")
        
        continuar = input("¿Desea continuar buscando pacientes? s/n: ").lower()
    continuar = input("Presione Enter para volver al menú o Q para salir: ")
    if continuar.lower() == "q":
        print("Gracias por usar nuestro Sistema de Gestion de Clinica. ¡Hasta luego!")
        exit()

    return paciente


def ordenar_pacientes(pacientes):
    n = len(pacientes)
    for i in range(n):
        for j in range(0, n - i - 1):
            if pacientes[j][0] > pacientes[j + 1][0]:
                pacientes[j], pacientes[j + 1] = pacientes[j + 1], pacientes[j]
    
    print("Inventario ordenado por precio:")
    for paciente in pacientes:
        print(paciente)
    
    continuar = input("Presione Enter para volver al menú o Q para salir: ")
    if continuar.lower() == "q":
        print("Gracias por usar nuestro Sistema de Gestion de Clinica. ¡Hasta luego!")
        exit()
    return pacientes

def mas_dias_internacion(pacientes: list):
    if len(pacientes) > 0:  
        paciente_mas_internado = pacientes[0]  

        for paciente in pacientes:
            if paciente[4] > paciente_mas_internado[4]:  
                paciente_mas_internado = paciente  

        print(f"Paciente con más días de internación: {paciente_mas_internado[1]}, "
              f"Edad: {paciente_mas_internado[2]}, Diagnóstico: {paciente_mas_internado[3]}, "
              f"Días de Internación: {paciente_mas_internado[4]}")

    continuar = input("Presione Enter para volver al menú o Q para salir: ")
    if continuar.lower() == "q":
        print("Gracias por usar nuestro Sistema de Gestion de Clinica. ¡Hasta luego!")
        exit()

    return paciente

def menos_dias_internacion(pacientes: list):
    if len(pacientes) > 0:  
        paciente_menos_internado = pacientes[0]  

        for paciente in pacientes:
            if paciente[4] < paciente_menos_internado[4]:  
                paciente_menos_internado = paciente  

        print(f"Paciente con menos días de internación: {paciente_menos_internado[1]}, "
              f"Edad: {paciente_menos_internado[2]}, Diagnóstico: {paciente_menos_internado[3]}, "
              f"Días de Internación: {paciente_menos_internado[4]}")

    continuar = input("Presione Enter para volver al menú o Q para salir: ")
    if continuar.lower() == "q":
        print("Gracias por usar nuestro Sistema de Gestion de Clinica. ¡Hasta luego!")
        exit()
    return paciente

def mas_de_5_dias(pacientes):
    pacientes_encontrados = []  
    
    for paciente in pacientes:
        if paciente[4] > 5:  
            pacientes_encontrados.append(paciente)  
            
    if len(pacientes_encontrados) > 0:  
        print("Pacientes con más de 5 días de internación:")
        for paciente in pacientes_encontrados:
            print(f"Nombre: {paciente[1]}, Edad: {paciente[2]}, Diagnóstico: {paciente[3]}, "
                  f"Días de Internación: {paciente[4]}")
    else:
        print("No hay pacientes con más de 5 días de internación.")

    continuar = input("Presione Enter para volver al menú o Q para salir: ")
    if continuar.lower() == "q":
        print("Gracias por usar nuestro Sistema de Gestion de Clinica. ¡Hasta luego!")
        exit()
    return paciente

def promedio_internacion(pacientes: list):
    if len(pacientes) == 0:  
        print("No hay pacientes registrados.")
        return

    total_dias = 0  
    for paciente in pacientes:
        total_dias += paciente[4]  

    promedio = total_dias / len(pacientes)  
    print(f"El promedio de días de internación es: {promedio:.2f}")
    continuar = input("Presione Enter para volver al menú o Q para salir: ")
    if continuar.lower() == "q":
        print("Gracias por usar nuestro Sistema de Gestion de Clinica. ¡Hasta luego!")
        exit()
    return promedio

def salir():
    print("Gracias por usar nuestro Sistema de Gestion de Clinica. ¡Hasta luego!")
    exit()

while continuar.lower() == "":
    mostrar_menu()

while continuar.lower() == "q":
    print("Gracias por usar nuestro Sistema de Gestion de Clinica. ¡Hasta luego!")
    exit()