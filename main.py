import json
import os

ARQUIVO = "clientes.json"


def carregar_clientes():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_clientes(clientes):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)


def cadastrar_cliente():
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    clientes = carregar_clientes()

    clientes.append({
        "nome": nome,
        "email": email,
        "telefone": telefone
    })

    salvar_clientes(clientes)

    print("\nCliente cadastrado com sucesso!\n")


def listar_clientes():
    clientes = carregar_clientes()

    if not clientes:
        print("\nNenhum cliente cadastrado.\n")
        return

    print("\n=== CLIENTES ===")

    for i, cliente in enumerate(clientes, start=1):
        print(f"""
{i}
Nome: {cliente['nome']}
Email: {cliente['email']}
Telefone: {cliente['telefone']}
-----------------------
""")


def buscar_cliente():
    busca = input("Digite o nome: ").lower()

    clientes = carregar_clientes()

    encontrados = [
        c for c in clientes
        if busca in c["nome"].lower()
    ]

    if encontrados:
        for cliente in encontrados:
            print(f"""
Nome: {cliente['nome']}
Email: {cliente['email']}
Telefone: {cliente['telefone']}
""")
    else:
        print("Cliente não encontrado.")


while True:

    print("""
1 - Cadastrar Cliente
2 - Listar Clientes
3 - Buscar Cliente
4 - Sair
""")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_cliente()

    elif opcao == "2":
        listar_clientes()

    elif opcao == "3":
        buscar_cliente()

    elif opcao == "4":
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")