import turtle as t

t.hideturtle()
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

try:
    while True:
        print('0. Stop program')
        print('1. Draw line')
        print('2. Draw parabola')
        print('3. Draw hyperbola')
        choice = int(input('Enter 0-3: '))


        if choice == 1:
            k_l, b_l = float(input('k for line: ')), float(input('b for line: '))
            draw_g(line, -300, 300)
        elif choice == 2:
            a_p, b_p, c_p = float(input('a for parabola: ')), float(input('b for parabola: ')), float(input('c for parabola: '))
            draw_g(parabola, -300, 300)
        elif choice == 3:
            k_h = float(input('k for hyperbola: '))
            draw_g(hyperbola, -300, 300)
        elif choice == 0:
            break
except ValueError:
        print('Please, retry again')

t.done()

