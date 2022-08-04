from aiogram import Router
from aiogram import Bot, types
from aiogram.types import Message,FSInputFile
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup
from tgbot.config import load_config

from tgbot.misc.messages import inf
from tgbot.misc.states import GetPhone, question
from tgbot.misc.function import auf_status, alert_admins

from tgbot.keyboards.textBtn import HomeBtn, servus_trade_bot_stat, servus_study_get, About_libertex,backHome,send_phone,servus,servus_study, servus_invest,servus_trade_bot,servus_copytrade

from tgbot.db import update_user

config = load_config(".env")
servus_router = Router()
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

@servus_router.message(text=["Об услугах Libertex"])
async def user_start(message: Message, state: FSMContext):
    userid = message.from_user.id
    await update_user.update_last_article(userid,'Об услугах Libertex')
    btn = servus()
    await bot.send_message(userid, inf['info_servus'],reply_markup=btn.as_markup(resize_keyboard=True))
    
# ОБУЧЕНИЕ
@servus_router.message(text=["Обучение"])
async def user_start(message: Message, state: FSMContext):
    userid = message.from_user.id
    btn = servus_study()
    photo = FSInputFile('tgbot/img/study.png')
    await bot.send_photo(userid, photo, inf['info_servus_study'],reply_markup=btn.as_markup(resize_keyboard=True))
    
@servus_router.message(text=["Записаться на ближайший курс"])
async def user_start(message: Message):
    firstName = message.from_user.first_name
    userid = message.from_user.id
    btn = HomeBtn()
    await alert_admins(bot, config.tg_bot.admin_ids ,userid)
    await update_user.make_claim(userid, 'enroll in a course', 'active', '-')
    await message.reply('Отлично, '+ firstName + '! Я передал Ваш вопрос специалисту и в скором времени он свяжется с Вами и ответит на все вопросы!',reply_markup=btn.as_markup(resize_keyboard=True))

@servus_router.message(text=["Смотреть курс онлайн"])
async def user_start(message: Message):
    firstName = message.from_user.first_name
    userid = message.from_user.id
    btn = servus_study_get()
    await message.reply(inf['servus_course'],reply_markup=btn.as_markup(resize_keyboard=True))
    
@servus_router.message(text=["Получить весь курс обучения"])
async def user_start(message: Message):
    firstName = message.from_user.first_name
    userid = message.from_user.id
    btn = servus_study_get()
    await alert_admins(bot, config.tg_bot.admin_ids ,userid)
    await update_user.make_claim(userid, 'enroll in a course', 'active', '-')
    await message.reply('Отлично, '+ firstName + '! Я передал Ваш вопрос специалисту и в скором времени он свяжется с Вами.',reply_markup=btn.as_markup(resize_keyboard=True))

    
    
# ИНВЕСТИЦИОННЫЕ ИДЕИ
@servus_router.message(text=["Инвестиционные идеи"])
async def user_start(message: Message, state: FSMContext):
    userid = message.from_user.id
    btn = servus_invest()
    photo = FSInputFile('tgbot/img/invest.jpg')
    await bot.send_photo(userid, photo, inf['info_servus_invest'],reply_markup=btn.as_markup(resize_keyboard=True))
    
@servus_router.message(text=["Получить пример ИИ"])
async def user_start(message: Message, state: FSMContext):
    userid = message.from_user.id
    btn = servus_invest()
    photo = FSInputFile('tgbot/img/invest_ex.png')
    await bot.send_photo(userid, photo, inf['info_servus_invest_ex'],reply_markup=btn.as_markup(resize_keyboard=True))
    
@servus_router.message(text=["Статистика ИИ"])
async def user_start(message: Message, state: FSMContext):
    userid = message.from_user.id
    btn = servus_invest()
    photo = FSInputFile('tgbot/img/stat.png')
    await bot.send_photo(userid, photo, inf['info_servus_invest_stat'],reply_markup=btn.as_markup(resize_keyboard=True))
    
# ТОРГОВЫЙ БОТ
@servus_router.message(text=["Торговый робот"])
async def user_start(message: Message, state: FSMContext):
    userid = message.from_user.id
    btn = servus_trade_bot()
    photo = FSInputFile('tgbot/img/bot.png')
    await bot.send_photo(userid, photo, inf['info_servus_tradeBot'],reply_markup=btn.as_markup(resize_keyboard=True))

@servus_router.message(text=["Статистика робота"])
async def user_start(message: Message, state: FSMContext):
    userid = message.from_user.id
    btn = servus_trade_bot_stat()
    photo = FSInputFile('tgbot/img/bot_stat.png')
    await bot.send_photo(userid, photo, inf['info_servus_tradeBot_stat'],reply_markup=btn.as_markup(resize_keyboard=True))
    
# КОПИТРЕЙД
@servus_router.message(text=["Копитрейд"])
async def user_start(message: Message, state: FSMContext):
    userid = message.from_user.id
    btn = servus_copytrade()
    photo = FSInputFile('tgbot/img/copy.png')
    await bot.send_photo(userid, photo, inf['info_servus_copytrade'],reply_markup=btn.as_markup(resize_keyboard=True))
    
@servus_router.message(text=["Статистика копитрейда"])
async def user_start(message: Message, state: FSMContext):
    userid = message.from_user.id
    btn = servus_trade_bot()
    photo = FSInputFile('tgbot/img/copy_stat.png')
    await bot.send_photo(userid, photo, inf['info_servus_copytrade_stat'],reply_markup=btn.as_markup(resize_keyboard=True))