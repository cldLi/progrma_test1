import turtle as t

t.speed(0)
t.goto(0, 300)
t.goto(0, -300)
t.penup()
t.goto(300, 0)
t.pendown()
t.goto(-300, 0)
t.penup()
t.goto(0, 0)

def parabola(x):
    return a_p * x ** 2 + b_p * x + c_p


def line(x):
    return k_l * x + b_l


def hyperbola(x):
    if x != 0:
        return 20 * k_h / x
    else:
        return None

def draw_g(func, from_x, to_x):
    t.penup()
    for x in range(from_x, to_x + 1):
        if func(x) is not None:
            t.goto(x, func(x))
            t.pendown()
        else:
            t.penup()


print('Предупреждение: программа строит графики по пикселям!')
print('1. Нарисовать прямую')
print('2. Нарисовать параболу')
print('3. Нарисовать гиперболу')
choice = int(input('1 или 2 или 3: '))

if choice == 1:
    k_l = float(input('Введите значение k прямой: '))
    b_l = float(input('Введите значение b прямой: '))
    draw_g(line, -300, 300)
elif choice == 2:
    a_p = float(input('Введите значение a параболы: '))
    b_p = float(input('Введите значение b параблоы: '))
    c_p = float(input('Введите значение c параболы: '))
    draw_g(parabola, -300, 300)
elif choice == 3:
    k_h = float(input('Введите значение k гиперболы: '))
    draw_g(hyperbola, -300, 300)
else:
    print('Неверный выбор. Перезапустите программу')

t.done()

