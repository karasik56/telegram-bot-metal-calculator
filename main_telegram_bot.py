from config import bot_token
from aiogram import Bot, Dispatcher, executor, types
from main import metal_mass_rect_tube

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply(
        'Напиши название проката и его длину.'
        ' В ответ ты получишь его массу. Формат записи:'
        ' сторона1(мм),'
        ' сторона2(мм),'
        ' толщина металла(мм),'
        ' длина(м)')


@dp.message_handler()
async def input_prof(message: types.Message):
    try:
        metal_func_agr = list(map(int, message.text.split(',')))
        await message.answer(
            f'масса профиля равна: {round(metal_mass_rect_tube(*metal_func_agr), 2)} кг')
    except (TypeError, ValueError):
        # await message.answer(f'Данные введены некорректно')
        await message.answer_sticker('CAACAgIAAxkBAAEEwrJihTUZ12waEezFoHLLKsGNiN7ifQACDxEAAojF0Usu_WLHr8VjziQE')


if __name__ == '__main__':
    executor.start_polling(dp)
