# Inicializa la lista de estudiantes vacía. Debería ser una lista, no una cadena vacía.
arr = ""

# Inicializa la variable de respuesta para el menú.
resp = ""

# Bucle para mostrar el menú y ejecutar acciones hasta que el usuario elija salir (opción "0").
while (resp != "0"):
    # Bandera para verificar si se encuentra un estudiante al buscar.
    flag = 0

    # Muestra las opciones del menú.
    print("\n1. Add student")
    print("2. Search student")
    print("3. Remove student")
    print("4. Save to a file")
    print("5. Load from a file")
    print("6. Student list")
    print("0. End program")

    # Solicita al usuario que seleccione una opción del menú.
    resp = input("\n\tSelect an option: ")

    # Opción 1: Añadir un nuevo estudiante.
    if (resp == "1"):
        # Agrega una lista con ID y nombre del estudiante a la lista 'arr'.
        arr.append([input("Enter student ID: "), input("Student name`s: ").title()])

    # Opción 2: Buscar un estudiante por su ID.
    elif (resp == "2"):
        # Solicita al usuario que ingrese el ID del estudiante a buscar.
        search_name = input("Enter ID: ").title()
        
        # Recorre la lista de estudiantes para buscar el ID.
        for student in arr:
            # Si se encuentra el ID, muestra la información del estudiante.
            if (search_name == student[0]):
                print(f"\n\tStudent: {search_name}, {student[1]}")
                # Marca que se encontró al estudiante.
                flag = 1
                break
        
        # Si no se encuentra el estudiante, muestra un mensaje de no encontrado.
        if (flag == 0):
            print("Student not found")
        input()  # Espera que el usuario presione Enter para continuar.

    # Opción 3: Eliminar el último estudiante agregado.
    elif (resp == "3"):
        # Verifica si la lista no está vacía.
        if arr:
            # Elimina y muestra el último estudiante de la lista.
            print(f"Se ha eliminado a {arr.pop()}")

    # Opción 4: Guardar la lista de estudiantes en un archivo.
    elif (resp == "4"):
        # Inicializa una cadena de texto para almacenar la información de los estudiantes.
        text = ""
        for element in arr:
            # Añade cada estudiante a la cadena de texto.
            text += f"{element[0]}, {element[1]}\n"
        
        # Abre el archivo 'student_list.txt' en modo de escritura y guarda la información.
        with open("student_list.txt", "w") as xfile:
            xfile.write(text)
            print("Has been saved")

    # Opción 5: Cargar la lista de estudiantes desde un archivo.
    elif (resp == "5"):
        # Abre el archivo 'student_list.txt' en modo de lectura y lee las líneas.
        with open("student_list.txt", "r") as xfile:
            lines = xfile.readlines()
        
        # Inicializa una lista para almacenar los estudiantes.
        result = []
        for item in lines:
            # Limpia los espacios y divide cada línea en ID y nombre.
            cleaned_item = item.strip()
            split_item = cleaned_item.split(", ")
            # Añade cada estudiante a la lista 'result'.
            result.append(split_item)
        
        # Asigna la lista 'result' a 'arr'.
        arr = result

    # Opción 6: Mostrar la lista de estudiantes.
    elif (resp == "6"):
        print("Student list\n")
        # Recorre la lista de estudiantes y muestra su información.
        for student in range(len(arr)):
            print(f"ID: {arr[student][0]}, Student: {arr[student][1]}.")

# Mensaje final al terminar el programa.
print("\nFinished program\n\n")
