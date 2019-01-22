import matplotlib.pyplot as plt

# Оценим интегралом 1/x^2 =>
# 1/n = eps => n = 1/eps => n = 10^6
N = 10 ** 6
step = 10 ** (-2)
stepCount = 10 ** 2


def func(z):
    f = 0
    for i in range(1, N):
        f += 1 / (i ** 2 - i - z)
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
    plt.savefig('chart_1a.png')
