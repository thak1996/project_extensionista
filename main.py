import dados
import autenticacao
import menu_tutor as tutor
import menu_aluno as aluno
import utils


dados_alunos = 'dados_alunos.txt'
agenda = 'agenda.txt'


def menu():
    if dados.exists_file(dados_alunos, agenda):
        print("Arquivos necessários localizados.")
    else:
        print('Arquivo inexistente')
        print('Criando arquivos necessários para a operação do programa')
        dados.new_file(dados_alunos, agenda)
    while True:
        print('-' * 20)
        print("Menu Principal:")
        print("1. Login")
        print("2. Sair")
        print('-' * 20)
        op = utils.valida_int("Escolha uma opção: ", 1, 2)
        if op == 1:
            sucesso, tipo_usuario, nome = autenticacao.login(dados_alunos)  # Desempacotando os valores retornados
            if sucesso:
                print("Login bem-sucedido")
                if tipo_usuario == 'Aluno':
                    aluno.menu_aluno(nome)
                elif tipo_usuario in ['Pai', 'Mãe']:
                    tutor.menu_tutor(nome)
            else:
                print("Tentativa de login falhou.")
        if op == 2:
            print("Saindo do programa...")
            break


if __name__ == '__main__':
    menu()
