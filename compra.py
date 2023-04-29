

def comprar():
    productos_c = {"producto1": 10, "producto2": 15, "producto3": 20}
    carrito = {}

    while True:
        print("¿Qué desea hacer?")
        print("1. Listar productos en venta")
        print("2. Vender un producto")
        print("3. Modificar carrito")
        print("4. Eliminar un elemento del carrito")
        print("5. Salir")

        opcion_c = input("Ingrese el número de la opción que desea: ")

        if opcion_c == "1":
            print("Productos en venta:")
            for producto_c, precio_c in productos_c.items():
                print(f"{producto_c} - {precio_c} dolares")
            print("")

        elif opcion_c == "2":
            print("Productos en venta:")
            for producto_c, precio_c in productos_c.items():
                print(f"{producto_c} - {precio_c} dolares")
            print("")
            producto_c = input("Ingrese el nombre del producto que desea comprar: ")
            if producto_c in productos_c:
                cantidad_c = int(input("Ingrese la cantidad que desea comprar: "))
                if cantidad_c <= productos_c[producto_c]:
                    carrito[producto_c] = carrito.get(producto_c, 0) + cantidad_c
                    productos_c[producto_c] -= cantidad_c
                    print(f"{cantidad_c} {producto_c}(s) agregados al carrito.")
                else:
                    print("Lo sentimos, no hay suficiente stock de ese producto.")
            else:
                print("El producto ingresado no está en venta.")

        elif opcion_c == "3":
            if not carrito:
                print("El carrito está vacío.")
            else:
                print("Carrito de compras:")
                for producto_c, cantidad_c in carrito.items():
                    print(f"{cantidad_c} {producto_c}(s)")
                print("")
                producto_c = input("Ingrese el nombre del producto que desea modificar: ")
                if producto_c in carrito:
                    cantidad_c = int(input("Ingrese la nueva cantidad que desea comprar: "))
                    if cantidad_c <= productos_c[producto_c] + carrito[producto_c]:
                        productos_c[producto_c] += carrito[producto_c] - cantidad_c
                        carrito[producto_c] = cantidad_c
                        print(f"{producto_c} modificado en el carrito.")
                    else:
                        print("Lo sentimos, no hay suficiente stock de ese producto.")
                else:
                    print("El producto ingresado no está en el carrito.")

        elif opcion_c == "4":
            if not carrito:
                print("El carrito está vacío.")
            else:
                print("Carrito de compras:")
                for producto_c, cantidad_c in carrito.items():
                    print(f"{cantidad_c} {producto_c}(s)")
                print("")
                producto_c = input("Ingrese el nombre del producto que desea eliminar: ")
                if producto_c in carrito:
                    productos_c[producto_c] += carrito[producto_c]
                    del carrito[producto_c]
                    print(f"{producto_c} eliminado del carrito.")
                else:
                    print("El producto ingresado no está en el carrito.")

        elif opcion_c == "5":
            print("Gracias por su compra.")
            break

        else:
            print("Opción inválida. Por favor ingrese una opción válida.")
            print("")
    return productos_c

def main():
    comprar()

main()