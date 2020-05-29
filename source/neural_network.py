import numpy


def sigmoid(x):
    """
    Sigmoid
    """
    return 1 / (1 + numpy.exp(-x))


def write_weight():
    """
    Функция записи весов
    """
    pass


def learning(number_repeat):
    """
    Функция обучения
    """
    for i in range(number_repeat):
        pass
    write_weight()
