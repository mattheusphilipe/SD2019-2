# coding=utf-8
import operator
import random


# funcão para tentar conversão de um número par inteiro ou real

def int_float(number, option):
    try:
        if option == 1:
            c = int(number)
        elif option == 2:
            c = float(number)
        return True
    except:
        return False


def encode_decode(data, option):
    if option == 1:
        return data.encode("utf-8")
    elif option == 2:
        return data.decode("utf-8")
    else:
        return None


# funcao para formar a equação e o seu resultado
def fun_equacao():
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}

    hardOperators = [ops["+"], ops["-"], ops["*"], ops["/"]]
    random_hardOperator = random.choice(hardOperators)

    if random_hardOperator == ops["+"]:
        operador = "+"
    elif random_hardOperator == ops["-"]:
        operador = "-"
    elif random_hardOperator == ops["*"]:
        operador = "*"
    elif random_hardOperator == ops["/"]:
        operador = "/"


    numbers = []
    for x in range(2):
        numbers.append(random.randint(1, 20))

    equacao = ' '.join([str(numbers[0]), operador, str(numbers[1])])

    if operador == "/":
        resultado = float(random_hardOperator(numbers[0], numbers[1]))
    else:
        resultado = random_hardOperator(numbers[0], numbers[1])


    return [equacao, resultado]
