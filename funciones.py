from funcion import login, perfil, ingresos, acercade
from venta import vender
from compra import comprar

def main():
    login()
    perfil()
    menuPrincipal()

opcion_h = 0

def menuPrincipal():
    while True:
        print("Bienvenido a Click Shop, ")
        print("1. Vender")
        print("2. Comprar")
        print("3. Ingresos")
        print("4. Acerca de")
        print("5. Salir")
        opcion_h = input("Ingrese el número de la opción deseada: ")

        if opcion_h == "1":
        vender()

        elif opcion_h == "2":
        comprar()

        elif opcion_h == "3":
        ingresos()

        elif opcion_h == "4":
        acercade()

        elif opcion_h == "5":
        print("Saliendo del Sistema.")
            break
    
        else:
            print("Opción inválida. Por favor ingrese una opción válida.")
            print("")
        
