import json

usuarios = []

# ========================== ARCHIVOS ==========================

def cargar_usuarios():
    try:
        with open("usuarios.json", "r") as file:
            usuarios.extend(json.load(file))
    except FileNotFoundError:
        print("No hay archivo, iniciando base vacía.")

def guardar_usuarios():
    with open("usuarios.json", "w") as file:
        json.dump(usuarios, file, indent=4)


# ========================== CRUD ==========================

def crear_usuario():
    nombre = input("Nombre: ")
    email  = input("Email: ")
    usuario = {"nombre": nombre, "email": email}
    usuarios.append(usuario)
    guardar_usuarios()
    print("Usuario creado ✔")

def listar_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for i, u in enumerate(usuarios):
        print(f"{i+1}. {u['nombre']} - {u['email']}")

def actualizar_usuario():
    listar_usuarios()
    idx = int(input("Número del usuario a actualizar: ")) - 1

    if 0 <= idx < len(usuarios):
        usuarios[idx]["nombre"] = input("Nuevo nombre: ")
        usuarios[idx]["email"]  = input("Nuevo email: ")
        guardar_usuarios()
        print("Usuario actualizado ✔")
    else:
        print("Índice inválido ❌")

def eliminar_usuario():
    listar_usuarios()
    idx = int(input("Número del usuario a eliminar: ")) - 1

    if 0 <= idx < len(usuarios):
        usuarios.pop(idx)
        guardar_usuarios()
        print("Usuario eliminado ✔")
    else:
        print("Índice inválido ❌")


# ========================== MENÚ ==========================

def menu():
    cargar_usuarios()
    while True:
        print("\n--- SISTEMA DE USUARIOS ---")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1": crear_usuario()
        elif opcion == "2": listar_usuarios()
        elif opcion == "3": actualizar_usuario()
        elif opcion == "4": eliminar_usuario()
        elif opcion == "5":
            print("Saliendo... 👋")
            break
        else:
            print("Opción inválida.")

menu()
