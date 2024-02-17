def exists_file(namefile, agenda):
    try:
        file = open(namefile, 'rt')
        file.close()
        agenda = open(agenda, 'rt')
        agenda.close()
    except FileNotFoundError:
        return False
    else:
        return True


def new_file(namefile, agenda):
    try:
        file = open(namefile, 'wt+')
        agenda = open(agenda, 'wt+')
    except FileExistsError:
        print('Erro na criação do arquivo')
    else:
        file.write('ID do Aluno, Nome do Aluno, Senha do Aluno, Pai, Senha Pai, Mae, Senha Mae\n')
        file.write('Exemplo: 1234, Nome Aluno, SenhaAluno, Pai1, SenhaPai1, Mae2, SenhaMae2\n')
        print('Arquivo {} criado com sucesso!\n'.format(namefile))
    finally:
        file.close()
        agenda.close()


def reuniao(namefile, horario, data):
    try:
        arquivo = open(namefile, 'a')
    except FileNotFoundError:
        print('Erro ao marcar reunião')
    else:
        arquivo.write('Horário de reunião será no horário {}, no dia {}\n'.format(horario, data))
    finally:
        arquivo.close()
