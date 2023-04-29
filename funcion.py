


# leer el contenido del archivo de texto desde una función
def leer_archivo():
    with open("PROYECTO/usuarios.txt", "r") as archivo:
        contenido = archivo.read()
    return contenido

print(leer_archivo()) # imprimir el contenido del archivo de texto

with open('usuarios.txt', 'r') as f:
    usuarios = f"{dir}usuarios.txt"
    

def login():
    nombre_usuario = input('Ingrese su nombre de usuario: ')
    contraseña = input('Ingrese su contraseña: ')

    if nombre_usuario in usuarios and usuarios[nombre_usuario]['contraseña'] == contraseña:
        print('Bienvenido, {}!'.format(nombre_usuario))
        return nombre_usuario
    else:
        print('Nombre de usuario o contraseña incorrectos.')
        return None

def perfil(nombre_usuario):
    if nombre_usuario in juan507:
        print("Perfil: ", nombre_usuario)
        print("Nombre: Juan Rodriguez")
        print("Apellido: Rodriguez")
        print("Edad: 25 años")
        return
    else:
        print("Perfil: ", nombre_usuario)
        print("Nombre: Maria")
        print("Apellido: Perez")
        print("Edad: 20 años")
        return

nombre_usuario = login()
if nombre_usuario:
    perfil(nombre_usuario)

def calcular_ingresos(productos_c, precio_venta, cantidad):
    total_lis = productos_c
    return ingresos
    
def acercade():
    print("\nProyecto Click Shop")
    print("\nEn este curso aprendimos una base sólida de conocimientos y habilidades que pueden aplicarse a una amplia variedad de lenguajes y proyectos de programación, tanto como en un área de trabajo profesional.")
    print("\nCreadores:", "Davis Sanchez 8-813-393,","Said Peceto 10-715-89")
    print("\nLas lecciones que aprendimos en este cuatrimestre fueron muy útiles como la estructura condicional, los diccionarios, el ciclo repetitivo, entre muchos otros temas.")

def main():
#    login()
#perfil()
    acercade()
#
main()
