from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

"""inline меню, 2 кнопки"""
inline_btn_rect_tube = InlineKeyboardButton('Прямоугольный профиль', callback_data='btn_rect_tube')
inline_btn_sheet = InlineKeyboardButton('Лист металлический', callback_data='btn_sheet')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_rect_tube, inline_btn_sheet)

