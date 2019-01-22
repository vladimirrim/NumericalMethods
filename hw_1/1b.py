import matplotlib.pyplot as plt

# Оценим интегралом 1/x^4 =>
# 1/n^3 = eps => n = 1/(eps)^(1/3) => n = 100
N = 100
step = 10 ** (-2)
stepCount = 10 ** 2


def func(z):
    f = -1 / z + 1
    for i in range(2, N):
        f += 1 / (i ** 2 - i - z) - 1 / i / (i - 1)
    return f


if __name__ == '__main__':
    k = [i * step for i in range(stepCount // 2, 3 * stepCount // 2)]
    y = []
    for x in k:
        y.append(func(x))
    plt.plot(k, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Chart')
    plt.savefig('chart_1b.png')
