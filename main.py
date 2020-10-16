from acciones import ingresar, registrar

"""
- Abrir asistente
- Login o registro
- Si elegimos registro, creara un usuario en la bd
- Si elegimos login, identificara al usuario y nos preguntara
- Crear nota, mostrar notas, borrarlas
"""


def iniciar():
    accion = ""
    while accion != "salir":
        if accion == "":
            print("--------------Ingresar--------------")
        else:
            print("\n--------------Ingresar--------------")

        accion = input(
            "¿Que desea hacer?\n- Ingresar (ingresar)\n- Crear usuario (crear)\n- Salir (salir)\n"
        )
        if accion.lower() == "ingresar":
            ingresar()
        elif accion.lower() == "crear":
            registrar()
        elif accion.lower() == "salir":
            break
        else:
            print("\nOpcion no valida\n")


if __name__ == "__main__":
    iniciar()
