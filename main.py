def metal_mass_rect_tube(side_1, side_2, lenght, thickness_metal):
    """ Расчет массы прямоугольного профиля, исходя из введенных пользователем данных """
    return 1 * 0.0157 * thickness_metal * (side_1 + side_2 - 2.86 * thickness_metal) * lenght


def metal_mass_sheet(side_1, side_2, thickness_metal):
    """ Расчет массы прямоугольного металлического листа, исходя из введенных пользователем данных """
    return (7850 * side_1 * side_2 * thickness_metal) * 0.000000001
