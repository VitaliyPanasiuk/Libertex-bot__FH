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


tg_router = Router()
config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')


@tg_router.message(text=["Трейдинг (Telegram канал)"])
async def user_start(message: Message, state: FSMContext):
    userid = message.from_user.id
    await update_user.update_last_article(userid,'💱 Обучение спекулятивному трейдингу')
    btn = servus()
    await bot.send_message(userid, inf['info_tg'],reply_markup=btn.as_markup(resize_keyboard=True))

@tg_router.message(text=["Получить доступ в телеграм канал"])
async def user_start(message: Message, state: FSMContext):
    userid = message.from_user.id
    btn = HomeBtn()
    await bot.send_message(userid, '''Ваша персональная ссылка на доступ в телеграм канал: https://t.me/+Gk2gSVGegBAzZTZi
Если у Вас будут возникать вопросы, или же Вы хотите добавить свою торговую систему к списку, свяжитесь с нами:
👨‍💼Березюк Павел (трейдер-аналитик): @Pavel_Libertex
👨‍💼Повторенко Денис (Директор филиала) @Denis_Libertex
''',reply_markup=btn.as_markup(resize_keyboard=True))
    await alert_admins(bot, config.tg_bot.admin_ids, userid)
    await update_user.make_claim(userid, 'get access to telegram channel', 'active', '-')