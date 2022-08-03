from aiogram import Router
from aiogram.types import Message

from tgbot.misc.messages import inf

from tgbot.keyboards.textBtn import HomeBtn,About_libertex,About_branch_donate

from tgbot.db import update_user


aboutDonate_router = Router()


@aboutDonate_router.message(text=["Как поплнить/снять торговый счет?"])
async def user_start(message: Message):
    btn = About_branch_donate()
    await update_user.update_last_article(message.from_user.id,'Как поплнить/снять торговый счет?')
    await message.reply(inf['info_donate'],reply_markup=btn.as_markup(resize_keyboard=True))
