import AutomataLista
import time

class Main:
    from os import system
    def __init__(self, init):
        self.system('cls')
        print("                  ---------------------------------------------------")
        print("                  | Lenguajes formales y de programación Sección A- |\n                  | Luis Danniel Ernesto Castellanos Galindo        |\n                  | Carnet: 201902238                               |\n                  |                  SimpleGraph                    |")
        print("                  ---------------------------------------------------")

        print("1. Cargar Archivo")
        print("2. Generar Gráfica")
        print("3. Salir")
        opcion = input("\nIngrese una opción: ")
        self.inicio(opcion,init)
    
    def inicio(self,opcion,init):
        fichero = init
        fichero = "C:\\Users\\luisd\\Desktop\\lista1.lfp"
        if opcion=="1":
            # fichero = input("Ingrese la ruta del archivo '.txt'----> ")
            print("\nLeyendo: ---"+fichero+"---\n")
            time.sleep(1.5)
            aceptacion = AutomataLista.AutomataLista().aceptar(fichero,opcion)
            if aceptacion == False:
                print("El archivo seleccionado no se encuentra. Intente de nuevo.")
                input("Presione Enter para continuar...")
                Main(None)
            else:
                input("Presione Enter para continuar...")
                Main(aceptacion)

        elif opcion=="2":
            if init == None:
                print("No se ha leído ningún archivo.")
                input("Presione Enter para continuar e ingrese una entrada: ")
                Main(None)
            else:
                print("\n")
                print("\nGenerando gráfica solicitada...")
                time.sleep(1.5)
                AutomataLista.AutomataLista().aceptar(init,opcion)
                Main(init)
            
            
        elif opcion=="3":
            self.system('cls')
            print("\nSaliendo...")
            time.sleep(1)
            exit()
        
        else:
            opcion = input("Seleccione una opción valida [1-3]: ")
            self.inicio(opcion,init)
        
run=Main(None)