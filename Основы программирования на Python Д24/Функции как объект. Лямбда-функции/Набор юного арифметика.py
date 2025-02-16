def arithmetic_operation(symbol):
    return lambda x, y: eval(str(x) + symbol + str(y))