

def metal_mass_rect_tube(side_1, side_2, lenght, thickness_metal):
    ''' Расчет массы прямоугольного профиля, исходя из введенных пользователем данных'''
    try:
        result = 1 * 0.0157 * thickness_metal * (side_1 + side_2 - 2.86 * thickness_metal) * lenght
        return result
    except ValueError:
        return f'Данные введены некорректно'


