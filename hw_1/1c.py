import matplotlib.pyplot as plt

step = 10 ** (-2)
stepCount = 10 ** 2


def func_a(z):
    N = 10 ** 6
    f = 0
    for i in range(1, N):
        f += 1 / (i ** 2 - i - z)
    return f


def func_b(z):
    N = 10 ** 2
    f = -1 / z + 1
    for i in range(2, N):
        f += 1 / (i ** 2 - i - z) - 1 / i / (i - 1)
    return f


if __name__ == '__main__':
    k = [i * step for i in range(stepCount // 2, 3 * stepCount // 2)]
    y = []
    for x in k:
        y.append(func_a(x) - func_b(x))
    plt.plot(k, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Difference')
    plt.savefig('chart_1c.png')
