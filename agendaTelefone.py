agenda = {}

def adicionar_contato():
    nome = input("Digite um nome:\n")
    numero = input("Digite um número:\n")
    apelido = input("Digite um apelido (opcional):\n")
    agenda[nome] = {"telefone": numero, "apelido": apelido if apelido else "Sem apelido"}
    print("Contato adicionado!")
    menu()

def buscar_contato():
    nome = input("Digite um nome para busca:\n")
    if nome in agenda:
        print(f"Nome: {nome}\nTelefone: {agenda[nome]['telefone']}\nApelido: {agenda[nome]['apelido']}")
    else:
        print("Contato não encontrado")
    menu()

def listar_contatos():
    if not agenda:
        print("A agenda está vazia.")
    else:
        print("Lista de contatos:")
        for nome, info in agenda.items():
            print(f"Nome: {nome} - Telefone: {info['telefone']} - Apelido: {info['apelido']}")
    menu()

def menu():
    try:
        print("\nAgenda Telefônica")
        print("1 - Adicionar Contato")
        print("2 - Buscar Contato")
        print("3 - Listar Contatos")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção:\n")

        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            buscar_contato()
        elif opcao == "3":
            listar_contatos()
        elif opcao == "4":
            print("Encerrando...")
        else:
            print("Opção Inválida!")
            menu()
    except Exception as e:
        print(f"Erro: {e}")
        menu()

menu()
