import AutomataLista
import AutomataMatriz
import time

class Main:
    from os import system
    def __init__(self, init):
        self.system('cls')
        print("                  ---------------------------------------------------")
        print("                  | Lenguajes formales y de programación Sección A- |\n                  | Luis Danniel Ernesto Castellanos Galindo        |\n                  | Carnet: 201902238                               |\n                  |                  SimpleGraph                    |")
        print("                  ---------------------------------------------------")

        print("1. Cargar lista")
        print("2. Generar lista\n")
        print("3. Cargar matriz")
        print("4. Generar matriz\n")
        print("5. Generar tabla")
        print("6. Salir")
        opcion = input("\nIngrese una opción: ")
        self.inicio(opcion,init)
    
    def inicio(self,opcion,init):
        fichero = init
        # fichero = "C:\\Users\\luisd\\Desktop\\lista1.lfp"
        if opcion=="1":
            fichero = input("Ingrese la ruta del archivo '.lfp'----> ")
            print("\nLeyendo: ---"+fichero+"---\n")
            time.sleep(1)
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
                time.sleep(1)
                AutomataLista.AutomataLista().aceptar(init,opcion)
                Main(init)
        
        elif opcion=="3":
            fichero = input("Ingrese la ruta del archivo '.lfp'----> ")
            print("\nLeyendo: ---"+fichero+"---\n")
            time.sleep(1)
            aceptacion = AutomataMatriz.AutomataMatriz().aceptar(fichero,opcion)
            if aceptacion == False:
                print("El archivo seleccionado no se encuentra. Intente de nuevo.")
                input("Presione Enter para continuar...")
                Main(None)
            else:
                input("Presione Enter para continuar...")
                Main(aceptacion)

        elif opcion=="4":
            if init == None:
                print("No se ha leído ningún archivo.")
                input("Presione Enter para continuar e ingrese una entrada: ")
                Main(None)
            else:
                print("\n")
                print("\nGenerando gráfica solicitada...")
                time.sleep(1)
                AutomataMatriz.AutomataMatriz().aceptar(init,opcion)
                Main(init)
            
        elif opcion == "5":
            print("Opción aún no disponible...")
            input("Presione Enter para continuar e ingrese otra opción: ")
            Main(init)
            
        elif opcion=="6":
            self.system('cls')
            print("\nSaliendo...")
            time.sleep(1)
            exit()
        
        else:
            opcion = input("Seleccione una opción valida [1-6]: ")
            self.inicio(opcion,init)
        
run=Main(None)