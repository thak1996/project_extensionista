import menu_aluno as menu
import utils


def menu_tutor(nome):
    while True:
        print('-' * 20)
        print("Bem-vindo(a), {}!".format(nome))
        print("1. Área de comunicação com a diretoria")
        print("2. Consultar presença do aluno")
        print("3. Verificar notas")
        print("4. Consultar horários de aula")
        print("5. Consultar mural de recados")
        op = utils.valida_int("Escolha uma opção: ", 1, 5)
        print('-' * 20)
        if op == 1:
            menu.marcar_reuniao()
        if op == 2:
            menu.consultar_presenca()
        if op == 3:
            menu.consultar_notas()
        if op == 4:
            menu.consultar_horario()
        if op == 5:
            menu.consultar_recados()
        if op == 6:
            print("Saindo do Sistema.")
            break

