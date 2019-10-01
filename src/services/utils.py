import random
import operator


# funcao para testar inteiros
def try_convert(param):
    try:
        number = int(param)
        return True
    except:
        return False


# funcao para encode e decode
def encode_decode(data, option):
    if option == 1:
        return data.encode("utf-8")
    elif option == 2:
        return data.decode("utf-8")
    else:
        return None


# funcao para formar a equação e o seu resultado
def create_equation():
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}

    hardOperators = [ops["+"], ops["-"], ops["*"], ops["/"]]
    random_hardOperator = random.choice(hardOperators)

    if random_hardOperator == ops["+"]:
        operation = "+"
    elif random_hardOperator == ops["-"]:
        operation = "-"
    elif random_hardOperator == ops["*"]:
        operation = "*"
    elif random_hardOperator == ops["/"]:
        operation = "/"
        
    for x in range(1):
        l = random.randint(1, 20)

    for x in range(1):
        l1 = random.randint(1, 20)

    equation = ' '.join([str(l), operation, str(l1)])
    result = random_hardOperator(l, l1)

    return [equation, result]