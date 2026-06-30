usuarios = [
    {"id": 1, "nome": "Vinicius"},
    {"id": 2, "nome": "Ana"}
]


def listar_usuarios():
    for usuario in usuarios:
        print(f"{usuario['id']} - {usuario['nome']}")


def adicionar_usuario(id, nome):
    usuarios.append({"id": id, "nome": nome})


listar_usuarios()
