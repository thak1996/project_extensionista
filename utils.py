def valida_int(pergunta, min, max):
    value = int(input(pergunta))
    while value < min or value > max:
        print('Valor inválido, digite um valor aceito')
        value = int(input(pergunta))
    return value

