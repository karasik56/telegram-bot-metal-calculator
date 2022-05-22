from aiogram.dispatcher.filters.state import StatesGroup, State


class Storage_value(StatesGroup):
    """ два хранилища состояний(для профиля и для листа) """
    storage_input_value_rect_tube = State()
    storage_input_value_sheet = State()
