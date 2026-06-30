def login(usuario, senha):
    if usuario == "admin" and senha == "123":
        return "Login realizado"
    return "Acesso negado"


def calcular_total(preco, quantidade):
    return preco * quantidade * 0.9


print(login("admin", "123"))
print(calcular_total(50, 2))
