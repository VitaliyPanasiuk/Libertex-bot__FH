from aiogram import Router, Bot
from aiogram.types import Message, FSInputFile
from tgbot.config import load_config


from tgbot.misc.messages import inf

from tgbot.keyboards.textBtn import HomeBtn,About_libertex,About_branch_donate

from tgbot.db import update_user

aboutBranch_router = Router()
config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')


@aboutBranch_router.message(text=["🏦 О Филиале"])
async def user_start(message: Message):
    btn = About_branch_donate()
    userid = message.from_user.id
    await update_user.update_last_article(message.from_user.id,'🏦 О Филиале')
    
    photo = FSInputFile('tgbot/img/branch.jpg')
    await bot.send_photo(userid, photo, inf['info_branch'],reply_markup=btn.as_markup(resize_keyboard=True))
