import operator
import random

def encode_decode(data, option):
    if option == 1:
        return data.encode("utf-8")
    elif option == 2:
        return data.decode("utf-8")
    else:
        return None

#funcao para formar a equação e o seu resultado
def fun_equacao():
    ops = {"+": operator.add, "-": operator.sub, "*":operator.mul, "/": operator.floordiv}

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
    for x in range(1):
        l = random.randint(1,20)

    for x in range(1):
        l1 = random.randint(1,20)

    equacao = ' '.join([str(l),operador,str(l1)])

    resultado = random_hardOperator(l,l1)

    return [equacao, resultado];


