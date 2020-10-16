from usuarios.Usuario import Usuario
from notas.Nota import Nota


def crear(codigo_usuario):
    print("\n--------------Crear nota--------------")
    titulo = input("Titulo: ")
    nota = input("Nota: ")
    nueva_nota = Nota(codigo_usuario, titulo, nota)
    row_count = nueva_nota.crear_nota()
    if row_count:
        print("\nLa nota se ha creado con exito.\n")


def mostrar(codigo_usuario):
    notas = Nota(codigo_usuario, "", "")
    notas_usuario = notas.buscar_notas()
    print("\n--------------Tus notas--------------")
    # if notas_usuario is None:
    # print("No ha creado ninguna nota.")
    # else:
    for nota in notas_usuario:
            print("Codigo nota:", nota[0])
            print("Titulo:", nota[2])
            print("Nota:", nota[3])
            print("Fecha:", nota[4])
            print("-------------------------------------")
    print("")


def borrar(codigo_usuario):
    mostrar(codigo_usuario)
    nota = Nota(0, "", "")
    id_nota = int(
        input("¿Cual desea borrar? (Ingrese el codigo de la nota): "))
    nota.borrar_nota(id_nota)


def main_menu(codigo_usuario):
    print("\n--------------Menu notas--------------")
    accion = ""
    while accion != "salir":
        accion = input(
            "¿Que desea hacer?\n- Crear nota (crear)\n- Mostrar notas (mostrar)\n- Borrar nota (borrar)\n- Salir (salir)\n"
        )
        if accion.lower() == "crear":
            crear(codigo_usuario)
        elif accion.lower() == "mostrar":
            mostrar(codigo_usuario)
        elif accion.lower() == "borrar":
            borrar(codigo_usuario)
        elif accion.lower() == "salir":
            break
        else:
            print("\nOpcion no valida\n")


def ingresar():
    print("\n--------------Login--------------")
    email = input("Ingrese email: ")
    passwd = input("Ingrese contraseña: ")
    usuario = Usuario("", "", email, passwd)
    info_usuario = usuario.buscar_usuario()
    if info_usuario is not None:
        main_menu(info_usuario[0])
    else:
        print("\nNo existe un usuario con esos datos\n")


def registrar():
    print("\n--------------Nuevo usuario--------------")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("Email: ")
    passwd = input("Contraseña: ")
    usuario = Usuario(nombre, apellido, email, passwd)
    row_count = usuario.crear_usuario()
    if row_count >= 1:
        info_usuario = usuario.buscar_usuario()
        main_menu(info_usuario[0])
