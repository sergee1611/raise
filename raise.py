class Wrongname(Exception):
    pass


class Wrongdigit(Exception):
    pass


car_models = ['лада', 'уаз', 'мерседес', 'бмв', 'тойота']


def car_choice(model, engine_power):
    for car in car_models:
        if model == car:
            print(f'Поздравляю с покупкой {model} с мощностью {engine_power}')
            break
    else:
        raise Wrongname(f'Поищи {model} в другом месте')
    if not isinstance(engine_power, int):
        raise Wrongdigit(f'Вместо {engine_power} нужно ввести целое число')


try:
    car_choice('бмв', 900.0)
except Wrongname as wn:
    print(f'Нужно обновить автопарк')
    raise
except Wrongdigit as wt:
    print(f'Ошибся, с кем не бывает: {wt}')
finally:
    print('Следущий покупатель')
