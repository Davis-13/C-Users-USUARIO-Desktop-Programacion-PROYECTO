
# Guardar
# ACTUALIZAR LA RUTA
from pathlib import Path

# Librería para obtener ubicación de mi directorio
path = Path.cwd()

dir = "/Users/USUARIO/Desktop/Programacion/PROYECTO"
#dir =  str(path) + "\PROYECTO\"
filename = f"{dir}usuarios.txt"

def guardarArchivo(info):
    borrarEspacio = info.strip()
    tam = len(borrarEspacio)
    if tam > 0:
        with open(filename, "a+") as f:
            # temp =  "\n" + info
            temp =  "\n" + info
            f.writelines(temp)
    else:
        print("No se puede almacenar información vacía")

# nom =  input("Usuario: ")
# passwd =  input("Password: ")
# save = nom + "," + passwd
# guardarArchivo(save)

def leerArchivo(filename):
    lista_temp = []
    # Leer
    with open(filename, "r+") as f:
        for item in f:
            info =  item.split(',')

            # Posicion 0 - usuario
            # Posicion 1 - password
            _nombre = info[0]
            _password = info[1]

            # almacenando en lista
            lista_temp.append([_nombre, _password])
    f.close()
    return lista_temp

def listadoUser():
    lista_temp = []
    # Leer
    with open(filename, "r+") as f:
        for item in f:
            borrarEspacio = item.strip()
            tam = len(borrarEspacio)
            if tam > 0:
                info =  item.split(',')

                # Posicion 0 - usuario
                # Posicion 1 - password
                _nombre = info[0]
                tmp = info[1].split("\n")
                _password = tmp[0]

                # almacenando en lista
                lista_temp.append([_nombre, _password])
    f.close()
    return lista_temp
# ejemplos
# temp = leerArchivo(filename)
# print(temp)