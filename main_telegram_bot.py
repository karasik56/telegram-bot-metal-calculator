from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import bot_token
from aiogram import Bot, Dispatcher, executor, types
from main import metal_mass_rect_tube, metal_mass_sheet
from states import Storage_value
import menu

bot = Bot(token=bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply(
        'Выберите номенклатуру, бот вернет вам массу металла', reply_markup=menu.inline_kb1)


@dp.callback_query_handler(text='btn_rect_tube')
async def process_callback_btn_rect_tube(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Введите параметры проката через запятую(сторона №1(мм),'
                                                        ' сторона №2(мм), толщина стенки(мм), длина(м).\n'
                                                        'Пример: 80,80,4,1')
    await Storage_value.storage_input_value_rect_tube.set()


@dp.callback_query_handler(text='btn_sheet')
async def process_callback_btn_sheet(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Введите параметры листа через запятую(сторона №1(мм),'
                                                        ' сторона №2(мм), толщина листа(мм).\n'
                                                        'Пример: 1250,2500,3')
    await Storage_value.storage_input_value_sheet.set()


@dp.message_handler(state=Storage_value.storage_input_value_rect_tube)
async def storage_input_value(message: types.Message, state: FSMContext):
    answer = message.text
    chat_id = message.chat.id
    await state.update_data(storage_input_value_rect_tube=answer)
    answer_list = list(map(int, answer.split(',')))
    try:
        await bot.send_message(chat_id,
                           f'масса профиля равна: {round(metal_mass_rect_tube(*answer_list), 2)} кг')
    except (TypeError, ValueError):
        await bot.send_message(chat_id, f'Данные введены некорректно')
    await state.finish()


@dp.message_handler(state=Storage_value.storage_input_value_sheet)
async def storage_input_value(message: types.Message, state: FSMContext):
    answer = message.text
    chat_id = message.chat.id
    await state.update_data(storage_input_value_sheet=answer)
    answer_list = list(map(int, answer.split(',')))
    try:
        await bot.send_message(chat_id,
                           f'масса листа равна: {round(metal_mass_sheet(*answer_list), 2)} кг')
    except (TypeError, ValueError):
        await bot.send_message(chat_id, f'Данные введены некорректно')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp)
