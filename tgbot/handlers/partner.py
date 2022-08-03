from aiogram import Router,Bot
from aiogram.types import Message,FSInputFile

from tgbot.misc.messages import inf
from tgbot.config import load_config

from tgbot.keyboards.textBtn import HomeBtn,About_libertex,partner_btn

from tgbot.misc.function import auf_status,alert_admins

from tgbot.db import update_user


partner_router = Router()
config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

@partner_router.message(text=["Стать партнером Libertex"])
async def user_start(message: Message):
    btn = partner_btn()
    userid = message.from_user.id
    await update_user.update_last_article(message.from_user.id,'Стать партнером Libertex')
    photo = FSInputFile('tgbot/img/partner.png')
    await bot.send_photo(userid, photo, inf['info_partner'],reply_markup=btn.as_markup(resize_keyboard=True))

@partner_router.message(text=["Калькулятор доходности"])
async def user_start(message: Message):
    btn = partner_btn()
    await message.reply(inf['info_partner_calc'],reply_markup=btn.as_markup(resize_keyboard=True))
    
@partner_router.message(text=["Стать партнером"])
async def user_start(message: Message):
    firstName = message.from_user.first_name
    userid = message.from_user.id
    text = message.text
    btn = HomeBtn()
    await alert_admins(bot, config.tg_bot.admin_ids ,userid)
    await update_user.make_claim(userid, 'partner', 'active', '-')
    await message.reply('Отлично, '+ firstName + '! Я передал Ваш вопрос напрямую куратору наших партнеров и в скором времени он свяжется с Вами и ответит на все вопросы!',reply_markup=btn.as_markup(resize_keyboard=True))