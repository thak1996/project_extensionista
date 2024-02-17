def login(namefile):
    id_aluno = input("Digite o ID do aluno: ")

    id_valido = False
    with open(namefile, 'r') as arquivo:
        next(arquivo)  # Pula a linha do cabeçalho
        for linha in arquivo:
            partes = linha.strip().split(', ')
            if partes[0] == id_aluno:
                id_valido = True
                break

    if not id_valido:
        print("ID do aluno inválido.")
        return False, None, None

    senha = input("Digite a senha: ")
    with open(namefile, 'r') as arquivo:
        next(arquivo)  # Pula a linha do cabeçalho novamente para verificar a senha
        for linha in arquivo:
            partes = linha.strip().split(', ')
            if partes[0] == id_aluno:
                if partes[2] == senha:
                    return True, 'Aluno', partes[1]
                elif partes[4] == senha:
                    return True, 'Pai', partes[3]
                elif len(partes) > 5 and partes[6] == senha:
                    return True, 'Mãe', partes[5]
                break  # Encerra o loop se o ID foi encontrado, mesmo que a senha esteja incorreta

    print("Falha no login. Senha incorreta.")
    return False, None, None
