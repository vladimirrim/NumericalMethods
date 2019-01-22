from cmath import sqrt, log10

import matplotlib.pyplot as plt

N = 10 ** 3
M = 10 ** 5
step = 10 ** (-2)
stepCount = 10 ** 2


def func(z, MAX):
    s_1 = z
    s_2 = s_1 + z ** 2 / 3
    s_3 = s_2 + z ** 3 / 5
    f = s_3 - (s_3 - s_2) ** 2 / (s_3 - 2 * s_2 + s_1)
    for i in range(4, MAX):
        s_1 = s_2
        s_2 = s_3
        s_3 += z ** i / (2 * i - 1)
        if s_3 - 2 * s_2 + s_1 != 0:
            f = s_3 - (s_3 - s_2) ** 2 / (s_3 - 2 * s_2 + s_1)
    return f


def plot(name, z):
    k = [i for i in range(100, N)]
    y = []
    for x in k:
        y.append(func(z, x))
    plt.plot(k, y)
    plt.xlabel('n')
    plt.ylabel('Sn')
    plt.title('Chart')
    plt.savefig(name)
    plt.clf()


def plot_complex(name, z):
    k = [i for i in range(100, N)]
    y = []
    for x in k:
        y.append(abs(func(z, x)))
    plt.plot(k, y)
    plt.xlabel('n')
    plt.ylabel('Sn')
    plt.title('Chart')
    plt.savefig(name)
    plt.clf()

# Сходимость внутри окружности слишком быстрая
# Идём по верхней дуге единичной окружности от -1 к 1
# Погрешность постепенно увеличивается


def plot_difference():
    k = [i * -step for i in range(1, stepCount)] + [i * step for i in range(1, stepCount)]
    k.sort()
    y = []
    for x in k:
        ideal = func(x + sqrt(1 - x ** 2) * 1j, M)
        y.append(log10(1 / abs(ideal - func(x + sqrt(1 - x ** 2) * 1j, N))))
    plt.plot(k, y)
    plt.xlabel('x')
    plt.ylabel('log(1 / Rn)')
    plt.title('Chart')
    plt.savefig('Difference')
    plt.clf()


if __name__ == '__main__':
    plot('chart_-0.9.png', -0.9)
    plot_complex('chart_i.png', 1j)
    plot('chart_-1.png', -1)
    plot_complex('chart_exp.png', (1j - 1) / sqrt(2))
    # Продолжение области сходимости
    plot('chart_-1.0001.png', -1.0001)
    plot_difference()
