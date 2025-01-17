from cryptography.fernet import Fernet

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)
    print("Chave gerada e salva como 'chave.key'.")

def carregar_chave():
    with open("chave.key", "rb") as chave_file:
        return chave_file.read()

def criptografar_arquivo(nome_arquivo):
    chave = carregar_chave()
    fernet = Fernet(chave)

    with open(nome_arquivo, "rb") as file:
        dados = file.read()

    dados_criptografados = fernet.encrypt(dados)

    with open(nome_arquivo, "wb") as file:
        file.write(dados_criptografados)

    print(f"O arquivo '{nome_arquivo}' foi criptografado com sucesso!")

def descriptografar_arquivo(nome_arquivo):
    chave = carregar_chave()
    fernet = Fernet(chave)

    with open(nome_arquivo, "rb") as file:
        dados_criptografados = file.read()

    dados = fernet.decrypt(dados_criptografados)

    with open(nome_arquivo, "wb") as file:
        file.write(dados)

    print(f"O arquivo '{nome_arquivo}' foi descriptografado com sucesso!")

def main():
    print("1. Gerar chave")
    print("2. Criptografar arquivo")
    print("3. Descriptografar arquivo")
    print("4. Sair")

    while True:
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            gerar_chave()
        elif escolha == "2":
            nome_arquivo = input("Digite o nome do arquivo a ser criptografado: ")
            criptografar_arquivo(nome_arquivo)
        elif escolha == "3":
            nome_arquivo = input("Digite o nome do arquivo a ser descriptografado: ")
            descriptografar_arquivo(nome_arquivo)
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
