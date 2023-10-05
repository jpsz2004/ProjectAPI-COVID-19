def get_user_input():
    # Obtener el departamento del usuario
    departamento = input("Ingrese el nombre del departamento: ")

    # Obtener el número de registros que el usuario desea ver
    while True:
        try:
            limite_registros = int(input("Ingrese el número de registros que desea ver: "))
            if limite_registros <= 0:
                raise ValueError
            break
        except ValueError:
            print("Ingrese un número entero positivo.")

    return departamento, limite_registros