from funciones import clase_hereda, clase_no_hereda, describir
# Aqui se maneja el input del usuario
def main():

    print("Bienvenido al programa manejador de tablas virtuales.\n",
          "Opciones: CLASS, DESCRIBIR, SALIR.\n")
    while True:
        user_input = input("$> ")
        if user_input.split()[0].upper() == "SALIR":
            break
        else:
            opciones = user_input.split()
            
            if opciones[0].upper() == "CLASS":
                clases(opciones[1:])
            elif opciones[0].upper() == "DESCRIBIR":
                describir(opciones[1])
            else:
                print("OPCION NO VALIDA\n",
                "Opciones: CLASS, DESCRIBIR, SALIR.\n")

# Aqui se determina si la clase a crear hereda de otra o no
def clases(opciones):
    if len(opciones) < 2:
        print("Error: Datos insuficientes para crear una clase.")
    elif opciones[1] == ":":
        clase_hereda(opciones[0], opciones[2], opciones[3:])
    else:
        clase_no_hereda(opciones[0], opciones[1:])


if __name__ == "__main__":
    main()
