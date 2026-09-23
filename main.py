from paciente import Paciente
pacientes: list[Paciente] =[]

def agregar_paciente()->None:
    rut = input("ingrese el rut del paciente: ")
    nombre = input("ingrese el nombre del paciente: ")
    edad = int(input("ingrese edad del paciente: "))
    print("previsiones disponibles:")
    print("1.- Fonasa")
    print("2.- isapre")
    prevision = input("Seleccione la prevision del paciente: ")
    if prevision == "1":
                prevision = "Fonasa"
    else: prevision = "isapre"

    paciente = Paciente(rut, nombre, edad, prevision)
    pacientes.append(paciente)
    print("Paciente agregado exitosamente.")

def leer_numero(mensaje:str)-> int:
     while True:
          try:
               numero = int(input(mensaje))
               return numero
          except ValueError:
               print("Por favor, ingrese un número válido.")

         
def menu ()-> int: 
       op=-1
       while op<0 or op>5:
        print("menu de opciones")
        print("1.- Agregar paciente")
        print("2- Editar paciente")
        print("3.- Eliminar paciente")
        print("4.- Imprimir paciente")
        print("5.- Imprimir todos los pacientes")
        print("0.- Salir")
        opcion = leer_numero("Seleccione una opción: ")
        return opcion

def buscar_paciente()->Paciente:
     rut = input("ingrese el R.U.T. del paciente a buscar: ")
     for paciente in pacientes: 
          if paciente.rut == rut:
               return paciente
          return None

def imprimir_paciente()->None:
     paciente=buscar_paciente()
     if paciente:
          print(paciente)
     else: 
          print("Paciente no encontrado.")

def imprimir_pacientes()->None:
     if pacientes:
          for paciente in pacientes:
               print(paciente)
     else: print("no hay pacientes registrados.")

     def editar_paciente()->None:
          paciente=buscar_paciente()
          if paciente:
               print(paciente)
               print("Menu de edicion de paciente")
               print("1.- Editar nombre")
               print("2.- Editar edad")
               print("3.- Editar prevision")
               opcion = leer_numero("Seleccione una opcion: ")
               if opcion == 1: 
                    nuevo_nombre = input("Ingrese el nuevo nombre: ")
                    paciente.nombre = nuevo_nombre
               elif opcion == 2: 
                    nueva_edad = leer_numero("Ingrese la nueva edad: ")
                    paciente.edad = nueva_edad
               elif opcion == 3:
                    print("previsiones disponibles")
                    print("1.- Fonasa")
                    print("2.- Isapre")
                    print("0.- no hacer cambios")
                    nueva_prevision = input("seleccione la nueva prevision: ")
                    if nueva_prevision == "1":
                         paciente.prevision = "Fonasa"
                    elif nueva_prevision == "2":
                         paciente.prevision = "Isapre"
                    else:
                         print("No se realizaron cambios en la previsión. ")
          else: 
               print("paciente no encontrado.")
def eliminar_paciente()->None:
     paciente=buscar_paciente()
     if paciente:
          pacientes.remove(paciente)
          print("pPaciente eliminado exitosamente. ")
     else: print("Paciente no encontrado ")

def main(): 
    op=-1
    while op!=0:
         op=menu()
         if op==1:
              print("Agregar paciente")
         elif op==2:
              print("Editando paciente")
         elif op==3:
            print ("Eliminado paciente")
         elif op==4:
              print("Imprimiendo un paciente")
              imprimir_paciente()
         elif op==5:
              print ("Imprimiendo todos los paciente")
              imprimir_pacientes()
         elif op==0: 
              print("saliendo del programa")
    

    
if __name__ == "__main__":
    main()
