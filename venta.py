
def vender():
    productos_v = []

    while True:
        print("Menu:")
        print("1. Crear producto")
        print("2. Listar productos")
        print("3. Editar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion_v = input("Ingrese una opción: ")

        if opcion_v == "1":
            nombre_v = input("Ingrese el nombre del producto: ")
            precio_v = float(input("Ingrese el precio del producto: "))
            cantidad_v = int(input("Ingrese la cantidad disponible del producto: "))

            producto_v = {"nombre": nombre_v, "precio": precio_v, "cantidad": cantidad_v}
            productos_v.append(producto_v)
            print("El producto ha sido creado exitosamente.")

        elif opcion_v == "2":
            if len(productos_v) == 0:
                print("No hay productos registrados.")
            else:
                print("Productos:")
                for i, producto_v in enumerate(productos_v):
                    print(f"{i+1}. {producto_v['nombre']} - ${producto_v['precio']} - Cantidad: {producto_v['cantidad']}")
                

        elif opcion_v == "3":
            if len(productos_v) == 0:
                print("No hay productos registrados.")
            else:
                print("Productos:")
                for i, producto_v in enumerate(productos_v):
                    print(f"{i+1}. {producto_v['nombre']} - ${producto_v['precio']} - Cantidad: {producto_v['cantidad']}")

                opcion_producto_v = int(input("Ingrese el número del producto que desea editar: "))
                if opcion_producto_v < 1 or opcion_producto_v > len(productos_v):
                    print("El número de producto ingresado no es válido.")
                else:
                    producto_v = productos_v[opcion_producto_v - 1]
                    print(f"Nombre: {producto_v['nombre']}")
                    nuevo_nombre_v = input("Ingrese el nuevo nombre del producto (Enter para dejar sin cambios): ")
                    if nuevo_nombre_v != "":
                        producto_v['nombre'] = nuevo_nombre_v

                    print(f"Precio: ${producto_v['precio']}")
                    nuevo_precio_v = input("Ingrese el nuevo precio del producto (Enter para dejar sin cambios): ")
                    if nuevo_precio_v != "":
                        producto_v['precio'] = float(nuevo_precio_v)

                    print(f"Cantidad: {producto_v['cantidad']}")
                    nueva_cantidad_v = input("Ingrese la nueva cantidad disponible del producto (Enter para dejar sin cambios): ")
                    if nueva_cantidad_v != "":
                        producto_v['cantidad'] = int(nueva_cantidad_v)

                    print("El producto ha sido actualizado exitosamente.")

        elif opcion_v == "4":
            if len(productos_v) == 0:
                print("No hay productos registrados.")
            else:
                print("Productos:")
                for i, producto_v in enumerate(productos_v):
                    print(f"{i+1}. {producto_v['nombre']} - ${producto_v['precio']} - Cantidad: {producto_v['cantidad']}")

                opcion_producto_v = int(input("Ingrese el número del producto que desea eliminar: "))
                if opcion_producto_v < 1 or opcion_producto_v > len(productos_v):
                    print("El número de producto ingresado no es válido.")
                else:
                    productos_v.pop(opcion_producto_v - 1)
                    print("El producto ha sido eliminado exitosamente.")

        elif opcion_v == "5":
            print("Saliendo del sistema de ventas.")
            break

        else:
            print("Opción inválida.")
    return productos_v

