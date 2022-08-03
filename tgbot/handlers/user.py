from aiogram import Router
from aiogram import Bot, types
from aiogram.types import Message, FSInputFile
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup
from tgbot.config import load_config

from tgbot.misc.messages import inf
from tgbot.misc.states import GetPhone, question
from tgbot.misc.function import auf_status,alert_admins

from tgbot.keyboards.textBtn import HomeBtn, About_libertex,backHome,send_phone,servus_study

from tgbot.db import update_user


config = load_config(".env")
user_router = Router()
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')

@user_router.message(commands=["start"])
async def user_start(message: Message, state: FSMContext):
    
    userid = message.from_user.id
    btn = HomeBtn()
    phone = send_phone()
    auf = await auf_status(userid)
    if auf:
        photo = FSInputFile('tgbot/img/start.jpg')
        await bot.send_photo(userid, photo, inf['start'],reply_markup=btn.as_markup(resize_keyboard=True))
        # await bot.send_message(userid, inf['start'],reply_markup=btn.as_markup(resize_keyboard=True))
    else:
        await bot.send_message(userid, 'Отправьте свой номер телефона', reply_markup=phone.as_markup(resize_keyboard=True))
        await state.set_state(GetPhone.get_phone)
    
@user_router.message_handler(content_types=types.ContentType.CONTACT, state=GetPhone.get_phone)
async def contacts(message: types.Message, state: FSMContext):
    userid = message.from_user.id
    firstName = message.from_user.first_name
    secondName = message.from_user.last_name
    userName = message.from_user.username
    btn = HomeBtn()
    await update_user.reg_user(userid,firstName,secondName,userName,str(message.contact.phone_number))
    await state.clear() 
    photo = FSInputFile('tgbot/img/start.jpg')
    await bot.send_photo(userid, photo, inf['start'],reply_markup=btn.as_markup(resize_keyboard=True))
    # await bot.send_message(userid, inf['start'],reply_markup=btn.as_markup(resize_keyboard=True))


@user_router.message(text=["Главное меню"])
async def user_start(message: Message):
    btn = HomeBtn()
    await message.reply('Главное меню', reply_markup=btn.as_markup(resize_keyboard=True))
    
    
@user_router.message(text=["Задать вопрос"])
async def user_start(message: Message, state: FSMContext):
    btn = backHome()
    firstName = message.from_user.first_name
    await message.reply('Здравствуйте, '+ firstName + '!' + inf['make_question'], reply_markup=btn.as_markup(resize_keyboard=True))
    await state.set_state(question.get_answer)
    
@user_router.message_handler(content_types=types.ContentType.TEXT, state=question.get_answer)
async def contacts(message: types.Message, state: FSMContext):
    userid = message.from_user.id
    firstName = message.from_user.first_name
    text = message.text
    btn = HomeBtn()
    await alert_admins(bot, config.tg_bot.admin_ids ,userid)
    await update_user.make_claim(userid, 'question', 'active', text)
    await message.reply('Отлично, '+ firstName + '!' + inf['answer_question'], reply_markup=btn.as_markup(resize_keyboard=True))
    await state.clear() 