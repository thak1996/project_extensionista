import utils
import main as file
import dados


def menu_aluno(nome):
    while True:
        print('-' * 20)
        print("Bem-vindo(a), Aluno(a) {}!".format(nome))
        print("1. Área de comunicação com a diretoria")
        print("2. Consultar presença")
        print("3. Verificar notas")
        print("4. Consultar horários de aula")
        print("5. Consultar mural de recados")
        print("6. Sair")
        print('-' * 20)
        op = utils.valida_int("Escolha uma opção: ", 1, 5)
        # Implemente as ações com base na op
        if op == 1:
            marcar_reuniao()
        if op == 2:
            consultar_presenca()
        if op == 3:
            consultar_notas()
        if op == 4:
            consultar_horario()
        if op == 5:
            consultar_recados()
        if op == 6:
            print("Saindo do Sistema.")
            break


def marcar_reuniao():
    print("Área de comunicação com a diretoria.")
    # Solicita ao usuário o horário e a data da reunião
    horario = input("Digite o horário da reunião (ex: 14h00): ")
    data = input("Digite a data da reunião (ex: 30/12/2022): ")
    dados.reuniao(file.agenda, horario, data)


def consultar_presenca():
    print("Área de comunicação com a diretoria.")


def consultar_notas():
    print("Área de consulta de notas")


def consultar_horario():
    print("Área de consulta ao horario de aula")


def consultar_recados():
    print("Área de consulta de recados")
