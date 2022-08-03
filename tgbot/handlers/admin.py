from aiogram import Router, Bot, types
from aiogram.types import Message,FSInputFile
from tgbot.config import load_config
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup

from tgbot.keyboards.textBtn import slider

from tgbot.misc.states import mailing

from tgbot.misc.function import get_list_of_users, get_claims

from tgbot.filters.admin import AdminFilter

from tgbot.db import export_db, update_user

admin_router = Router()
admin_router.message.filter(AdminFilter())

config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')


@admin_router.message(commands=["getUsers"], state="*")
async def admin_start(message: Message):
    await export_db.export_db()
    await message.reply("Вітаю, адміне!")
    file = FSInputFile('tgbot/misc/users.xls')
    await bot.send_document(message.from_user.id, file)
    
@admin_router.message(commands=["getClaims"], state="*")
async def admin_start(message: Message):
    await export_db.export_db()
    await message.reply("Вітаю, адміне!")
    file = FSInputFile('tgbot/misc/claims.xls')
    await bot.send_document(message.from_user.id, file)
    
@admin_router.message(commands=["mailing"])
async def admin_start(message: Message, state: FSMContext):
    await message.reply("Отправьте сообщение которое хотите разослать всем пользователям!")
    await state.set_state(mailing.get_answer)
    
@admin_router.message(content_types=types.ContentType.TEXT, state=mailing.get_answer)
async def admin_start(message: Message, state: FSMContext):
    text = message.text
    list_of_users = await get_list_of_users()
    
    for i in list_of_users:
        await bot.send_message(i,text)
        
    await bot.send_message(message.from_user.id,"Сообщение было разослано всем пользователям")
    

@admin_router.message(commands=["requests"], state="*")
async def admin_start(message: Message):
    claims = await get_claims()
    slider_btn = slider()
    try:
        await bot.send_message(message.from_user.id,
        f'''
        id запроса: {claims[0][0]},
user_id: {claims[0][1]},
Имя: {claims[0][2]},
Ник: @{claims[0][3]},
Телефон: {claims[0][4]},
Тип сообщения: {claims[0][5]},
Сообщение: {claims[0][7]},
        ''', reply_markup=slider_btn.as_markup(resize_keyboard=True))
        claims.pop(0)
    except:
        claims = await get_claims()
        await bot.send_message(message.from_user.id,
        f'''
        id запроса: {claims[0][0]},
user_id: {claims[0][1]},
Имя: {claims[0][2]},
Ник: @{claims[0][3]},
Телефон: {claims[0][4]},
Тип сообщения: {claims[0][5]},
Сообщение: {claims[0][7]},
        ''', reply_markup=slider_btn.as_markup(resize_keyboard=True))
        claims.pop(0)
    @admin_router.message(text=["next"])
    async def ret(message: Message, state: FSMContext):
        try:
            await bot.send_message(message.from_user.id,
        f'''
        id запроса: {claims[0][0]},
user_id: {claims[0][1]},
Имя: {claims[0][2]},
Ник: @{claims[0][3]},
Телефон: {claims[0][4]},
Тип сообщения: {claims[0][5]},
Сообщение: {claims[0][7]},
        ''', reply_markup=slider_btn.as_markup(resize_keyboard=True))
            claims.pop(0)
        except:
            await bot.send_message(message.from_user.id,"Вы просмотрели все вопросы/запросы, что бы просмотреть спиок снова - нажмите /requests")

@admin_router.message(commands=["answered"], state="*")
async def admin_start(message: Message):
    args = message.text.split(' ')
    try:
        await update_user.anwer_claim(args[1])
    except:
        await bot.send_message(message.from_user.id, 'Что-то пошло не так, проверьте ввели ли вы правильный id вопроса')
        return
    await bot.send_message(message.from_user.id, 'Статус был успешно изменён на закрытый')
    
@admin_router.message(commands=["addadmin"], state="*")
async def admin_start(message: Message):
    args = message.text.split(' ')
    try:
        await update_user.add_admin(str(args[1]))
    except:
        await bot.send_message(message.from_user.id, 'Что-то пошло не так, проверьте ввели ли вы правильный id пользователя')
        return
    await bot.send_message(message.from_user.id, 'Админ был успешно добавлен')