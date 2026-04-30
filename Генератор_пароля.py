import random

# словарь сортировщик
d = {}
# юзер интерфейс
login = input('Имя: ').strip().title()
count = int(input('Сколько символов должно быть в вашем пароле?: '))
if count < 9:
    print("❌ Пароль слишком короткий. Минимум 9 символов.")
else:
    print('1.🔠Пароль будет сделан только из букв?')
    print('2.🔢Пароль будет сделан только из чисел?')
    print('3.#️⃣Пароль будет сделан только из символов?')
    print('4.#️⃣ 🔢 🔠Мне не важно сделай пароль из цифр, букв и символов')
    cho = int(input('Выберите вариант 1-4: ').strip())
    # опции допустимые для юзера
    opt = {
        1: 'abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ',
        2: '1234567890',
        3: '[]{}-_=+()*?:&^%$#@!;"~`/><',
        4: '1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ[]{}-_=+()*?:&^%$#@!;"~`/><'
    }
    # получение нужной опции
    pas = opt.get(cho, " ")
    # сборка пароля
    password = ''.join(random.choice(pas) for i in range(count))
    # сортировка
    lst = d.fromkeys(list(password))

    # выдача пароля
    print(f'Здравствуйте {login}, вот ваш пароль: ', *lst, sep='')
