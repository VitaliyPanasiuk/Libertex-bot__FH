from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardButton, InlineKeyboardBuilder
from aiogram import Bot, types


def HomeBtn():
    home_buttons = ReplyKeyboardBuilder()
    home_buttons.add(
        types.KeyboardButton(text="О Приложении")
    )
    home_buttons.add(
        types.KeyboardButton(text="О Филиале")
    )
    home_buttons.add(
        types.KeyboardButton(text="Об услугах Libertex")
    )
    home_buttons.add(
        types.KeyboardButton(text="Как поплнить/снять торговый счет?")
    )
    home_buttons.add(
        types.KeyboardButton(text="Стать партнером Libertex")
    )
    home_buttons.add(
        types.KeyboardButton(text="Задать вопрос")
    )
    home_buttons.adjust(2)
    return home_buttons

def About_libertex():
    home_buttons = ReplyKeyboardBuilder()
    home_buttons.add(
        types.KeyboardButton(text="Обучение Libertex")
    )
    home_buttons.add(
        types.KeyboardButton(text="Задать вопрос")
    )
    home_buttons.add(
        types.KeyboardButton(text="Главное меню")
    )
    home_buttons.adjust(2)
    return home_buttons
def About_libertex_study():
    home_buttons = ReplyKeyboardBuilder()
    home_buttons.add(
        types.KeyboardButton(text="Давайте следующий")
    )
    home_buttons.add(
        types.KeyboardButton(text="Главное меню")
    )
    home_buttons.adjust(2)
    return home_buttons
def About_libertex_study_ifo():
    home_buttons = ReplyKeyboardBuilder()
    home_buttons.add(
        types.KeyboardButton(text="Давайте начнем")
    )
    home_buttons.add(
        types.KeyboardButton(text="Главное меню")
    )
    home_buttons.adjust(2)
    return home_buttons

def partner_btn():
    home_buttons = ReplyKeyboardBuilder()
    home_buttons.add(
        types.KeyboardButton(text="Калькулятор доходности")
    )
    home_buttons.add(
        types.KeyboardButton(text="Стать партнером")
    )
    home_buttons.add(
        types.KeyboardButton(text="Главное меню")
    )
    home_buttons.adjust(2)
    return home_buttons

def About_branch_donate():
    home_buttons = ReplyKeyboardBuilder()
    home_buttons.add(
        types.KeyboardButton(text="Задать вопрос")
    )
    home_buttons.add(
        types.KeyboardButton(text="Главное меню")
    )
    home_buttons.adjust(2)
    return home_buttons

def backHome():
    home_buttons = ReplyKeyboardBuilder()
    home_buttons.add(
        types.KeyboardButton(text="Главное меню")
    )
    return home_buttons

def send_phone():
    phone = ReplyKeyboardBuilder()
    phone.add(types.KeyboardButton(
    text="send contact",
    request_contact=True)
    )
    return phone

def servus():
    home_buttons = ReplyKeyboardBuilder()
    home_buttons.add(
        types.KeyboardButton(text="Обучение")
    )
    home_buttons.add(
        types.KeyboardButton(text="Инвестиционные идеи")
    )
    home_buttons.add(
        types.KeyboardButton(text="Торговый бот")
    )
    home_buttons.add(
        types.KeyboardButton(text="Копитрейд")
    )
    home_buttons.add(
        types.KeyboardButton(text="Главное меню")
    )
    home_buttons.adjust(2)
    return home_buttons

def servus_study():
    home_buttons = ReplyKeyboardBuilder()
    home_buttons.add(
        types.KeyboardButton(text="Задать вопрос")
    )
    home_buttons.add(
        types.KeyboardButton(text="Записаться на ближайший курс")
    )
    home_buttons.add(
        types.KeyboardButton(text="Смотреть курс онлайн")
    )
    home_buttons.add(
        types.KeyboardButton(text="Главное меню")
    )
    home_buttons.adjust(1)
    return home_buttons

def servus_study_get():
    home_buttons = ReplyKeyboardBuilder()
    home_buttons.add(
        types.KeyboardButton(text="Получить весь курс обучения")
    )
    home_buttons.add(
        types.KeyboardButton(text="Главное меню")
    )
    home_buttons.adjust(1)
    return home_buttons

def servus_invest():
    home_buttons = ReplyKeyboardBuilder()
    home_buttons.add(
        types.KeyboardButton(text="Получить пример ИИ")
    )
    home_buttons.add(
        types.KeyboardButton(text="Статистика ИИ")
    )
    home_buttons.add(
        types.KeyboardButton(text="Задать вопрос")
    )
    home_buttons.add(
        types.KeyboardButton(text="Главное меню")
    )
    home_buttons.adjust(1)
    return home_buttons

def servus_trade_bot():
    home_buttons = ReplyKeyboardBuilder()
    home_buttons.add(
        types.KeyboardButton(text="Статистика робота")
    )
    home_buttons.add(
        types.KeyboardButton(text="Задать вопрос")
    )
    home_buttons.add(
        types.KeyboardButton(text="Главное меню")
    )
    home_buttons.adjust(2)
    return home_buttons

def servus_copytrade():
    home_buttons = ReplyKeyboardBuilder()
    home_buttons.add(
        types.KeyboardButton(text="Статистика копитрейда")
    )
    home_buttons.add(
        types.KeyboardButton(text="Задать вопрос")
    )
    home_buttons.add(
        types.KeyboardButton(text="Главное меню")
    )
    home_buttons.adjust(2)
    return home_buttons

def slider():
    home_buttons = ReplyKeyboardBuilder()
    home_buttons.add(
        types.KeyboardButton(text="next")
    )
    home_buttons.add(
        types.KeyboardButton(text="Главное меню")
    )
    home_buttons.adjust(1)
    return home_buttons