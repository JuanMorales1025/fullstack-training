import json

usuarios = []

def agregar_usuario(nombre, email):
    usuario = {"nombre": nombre, "email": email}
    usuarios.append(usuario)

def listar_usuarios():
    for u in usuarios:
        print(f"- {u['nombre']} | {u['email']}")

agregar_usuario("Juan", "juan@mail.com")
agregar_usuario("Maria", "maria@mail.com")

def guardar_en_archivo():
    with open("usuarios.json", "w") as file:
        json.dump(usuarios, file, indent=4)

def cargar_usuarios():
    try:
        with open("usuarios.json", "r") as file:
            data = json.load(file)
            usuarios.extend(data)
    except FileNotFoundError:
        print("No hay archivo todavía, iniciando vacío.")
    
cargar_usuarios()

agregar_usuario("Pepito", "pepito@mail.com")

guardar_en_archivo()
listar_usuarios()
