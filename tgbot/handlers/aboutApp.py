from aiogram import Router, Bot
from aiogram.types import Message, FSInputFile
from tgbot.config import load_config

from tgbot.misc.messages import inf,libertex_1,libertex_2,libertex_3,libertex_4,libertex_5,after_lesson
from tgbot.misc.function import get_lesson_libertex


from tgbot.keyboards.textBtn import HomeBtn,About_libertex,About_libertex_study,About_libertex_study_ifo,servus_study_reload

from tgbot.db import update_user

aboutApp_router = Router()
config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')


@aboutApp_router.message(text=["🎓 Курсы обучения"])
async def user_start(message: Message):
    userid = message.from_user.id
    btn = About_libertex()
    await update_user.update_last_article(message.from_user.id,'«🎓 Курсы обучения')
    photo = FSInputFile('tgbot/img/aboutApp.jpg')
    await bot.send_photo(userid, photo, inf['info_libertex'],reply_markup=btn.as_markup(resize_keyboard=True))
    
@aboutApp_router.message(text=["Обучение Libertex"])
async def user_start(message: Message):
    userid = message.from_user.id
    btn = About_libertex_study_ifo()
    photo = FSInputFile('tgbot/img/servus.jpg')
    await bot.send_photo(userid, photo, inf['info_libertex_study'],reply_markup=btn.as_markup(resize_keyboard=True))
    
@aboutApp_router.message(text=["Давайте начнем"])
async def user_start(message: Message):
    userid = message.from_user.id
    btn = About_libertex_study()
    await update_user.update_last_article(message.from_user.id,'🎓 Курсы обучения')
    answer = await get_lesson_libertex(userid)
    article= answer[0]
    lesson = answer[1]
    text =''
    if article == 1 and lesson == 6:
        article = 2
        lesson = 1
        await update_user.update_article(article,lesson,userid)
    elif article == 2 and lesson == 9:
        article = 3
        lesson = 1
        await update_user.update_article(article,lesson,userid)
    elif article == 3 and lesson == 12:
        article = 4
        lesson = 1
        await update_user.update_article(article,lesson,userid)
    elif article == 4 and lesson == 10:
        article = 5
        lesson = 1
        await update_user.update_article(article,lesson,userid)
    elif article == 5 and lesson == 13:
        btn = servus_study_reload()
    else:
        lesson += 1
        await update_user.update_article(article,lesson,userid)
        
    if article == 1 and lesson == 1:
        video = FSInputFile('tgbot/study/1/' + str(lesson) + '.mp4')
        await bot.send_message(userid, 'Раздел I “Первые Шаги”.', reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, libertex_1[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 2 and lesson == 1:
        video = FSInputFile('tgbot/study/2/' + str(lesson) + '.mp4')
        await bot.send_message(userid, after_lesson['1'], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, 'Раздел II “Инструменты трейдера Libertex”', reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, libertex_2[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 3 and lesson == 1:
        video = FSInputFile('tgbot/study/3/' + str(lesson) + '.mp4')
        await bot.send_message(userid, after_lesson['2'], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, 'Раздел III “Анализ графика Libertex”', reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, libertex_3[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 4 and lesson == 1:
        video = FSInputFile('tgbot/study/4/' + str(lesson) + '.mp4')
        await bot.send_message(userid, after_lesson['3'], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, 'Раздел IV “Создание торговой стратегии”', reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, libertex_4[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 5 and lesson == 1:
        video = FSInputFile('tgbot/study/5/' + str(lesson) + '.mp4')
        await bot.send_message(userid, after_lesson['4'], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, 'Раздел V “Готовые торговые стратегии для трейдера”', reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, libertex_5[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 1:
        video = FSInputFile('tgbot/study/1/' + str(lesson) + '.mp4')
        await bot.send_message(userid, libertex_1[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 2:
        video = FSInputFile('tgbot/study/2/' + str(lesson) + '.mp4')
        await bot.send_message(userid, libertex_2[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 3:
        video = FSInputFile('tgbot/study/3/' + str(lesson) + '.mp4')
        await bot.send_message(userid, libertex_3[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 4:
        video = FSInputFile('tgbot/study/4/' + str(lesson) + '.mp4')
        await bot.send_message(userid, libertex_4[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 5 and lesson < 13:
        video = FSInputFile('tgbot/study/5/' + str(lesson) + '.mp4')
        await bot.send_message(userid, libertex_5[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    else:
        await bot.send_message(userid, after_lesson['5'], reply_markup=btn.as_markup(resize_keyboard=True))
         
        
@aboutApp_router.message(text=["Давайте следующий"])
async def user_start(message: Message):
    userid = message.from_user.id
    btn = About_libertex_study()
    await update_user.update_last_article(message.from_user.id,'🎓 Курсы обучения')
    answer = await get_lesson_libertex(userid)
    article= answer[0]
    lesson = answer[1]
    text =''
    if article == 1 and lesson == 6:
        article = 2
        lesson = 1
        await update_user.update_article(article,lesson,userid)
    elif article == 2 and lesson == 9:
        article = 3
        lesson = 1
        await update_user.update_article(article,lesson,userid)
    elif article == 3 and lesson == 12:
        article = 4
        lesson = 1
        await update_user.update_article(article,lesson,userid)
    elif article == 4 and lesson == 10:
        article = 5
        lesson = 1
        await update_user.update_article(article,lesson,userid)
    elif article == 5 and lesson == 13:
        btn = servus_study_reload()
    else:
        lesson += 1
        await update_user.update_article(article,lesson,userid)
  
    if article == 1 and lesson == 1:
        video = FSInputFile('tgbot/study/1/' + str(lesson) + '.mp4')
        await bot.send_message(userid, 'Раздел I “Первые Шаги”.', reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, libertex_1[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 2 and lesson == 1:
        video = FSInputFile('tgbot/study/2/' + str(lesson) + '.mp4')
        await bot.send_message(userid, after_lesson['1'], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, 'Раздел II “Инструменты трейдера Libertex”', reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, libertex_2[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 3 and lesson == 1:
        video = FSInputFile('tgbot/study/3/' + str(lesson) + '.mp4')
        await bot.send_message(userid, after_lesson['2'], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, 'Раздел III “Анализ графика Libertex”', reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, libertex_3[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 4 and lesson == 1:
        video = FSInputFile('tgbot/study/4/' + str(lesson) + '.mp4')
        await bot.send_message(userid, after_lesson['3'], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, 'Раздел IV “Создание торговой стратегии”', reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, libertex_4[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 5 and lesson == 1:
        video = FSInputFile('tgbot/study/5/' + str(lesson) + '.mp4')
        await bot.send_message(userid, after_lesson['4'], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, 'Раздел V “Готовые торговые стратегии для трейдера”', reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, libertex_5[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 1:
        video = FSInputFile('tgbot/study/1/' + str(lesson) + '.mp4')
        await bot.send_message(userid, libertex_1[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 2:
        video = FSInputFile('tgbot/study/2/' + str(lesson) + '.mp4')
        await bot.send_message(userid, libertex_2[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 3:
        video = FSInputFile('tgbot/study/3/' + str(lesson) + '.mp4')
        await bot.send_message(userid, libertex_3[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 4:
        video = FSInputFile('tgbot/study/4/' + str(lesson) + '.mp4')
        await bot.send_message(userid, libertex_4[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 5 and lesson < 13:
        video = FSInputFile('tgbot/study/5/' + str(lesson) + '.mp4')
        await bot.send_message(userid, libertex_5[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    else:
        await bot.send_message(userid, after_lesson['5'], reply_markup=btn.as_markup(resize_keyboard=True))
       
        
@aboutApp_router.message(text=["Пройти заново"])
async def user_start(message: Message):
    userid = message.from_user.id
    btn = About_libertex_study_ifo()
    await update_user.update_article(1,0,userid)  
    answer = await get_lesson_libertex(userid)
    article= answer[0]
    lesson = answer[1]      
    if article == 1 and lesson == 6:
        article = 2
        lesson = 1
        await update_user.update_article(article,lesson,userid)
    elif article == 2 and lesson == 9:
        article = 3
        lesson = 1
        await update_user.update_article(article,lesson,userid)
    elif article == 3 and lesson == 12:
        article = 4
        lesson = 1
        await update_user.update_article(article,lesson,userid)
    elif article == 4 and lesson == 10:
        article = 5
        lesson = 1
        await update_user.update_article(article,lesson,userid)
    elif article == 5 and lesson == 13:
        btn = servus_study_reload()
    else:
        lesson += 1
        await update_user.update_article(article,lesson,userid)
  
    if article == 1 and lesson == 1:
        video = FSInputFile('tgbot/study/1/' + str(lesson) + '.mp4')
        await bot.send_message(userid, 'Раздел I “Первые Шаги”.', reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, libertex_1[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 2 and lesson == 1:
        video = FSInputFile('tgbot/study/2/' + str(lesson) + '.mp4')
        await bot.send_message(userid, after_lesson['1'], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, 'Раздел II “Инструменты трейдера Libertex”', reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, libertex_2[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 3 and lesson == 1:
        video = FSInputFile('tgbot/study/3/' + str(lesson) + '.mp4')
        await bot.send_message(userid, after_lesson['2'], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, 'Раздел III “Анализ графика Libertex”', reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, libertex_3[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 4 and lesson == 1:
        video = FSInputFile('tgbot/study/4/' + str(lesson) + '.mp4')
        await bot.send_message(userid, after_lesson['3'], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, 'Раздел IV “Создание торговой стратегии”', reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, libertex_4[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 5 and lesson == 1:
        video = FSInputFile('tgbot/study/5/' + str(lesson) + '.mp4')
        await bot.send_message(userid, after_lesson['4'], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, 'Раздел V “Готовые торговые стратегии для трейдера”', reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_message(userid, libertex_5[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 1:
        video = FSInputFile('tgbot/study/1/' + str(lesson) + '.mp4')
        await bot.send_message(userid, libertex_1[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 2:
        video = FSInputFile('tgbot/study/2/' + str(lesson) + '.mp4')
        await bot.send_message(userid, libertex_2[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 3:
        video = FSInputFile('tgbot/study/3/' + str(lesson) + '.mp4')
        await bot.send_message(userid, libertex_3[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 4:
        video = FSInputFile('tgbot/study/4/' + str(lesson) + '.mp4')
        await bot.send_message(userid, libertex_4[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    elif article == 5 and lesson < 13:
        video = FSInputFile('tgbot/study/5/' + str(lesson) + '.mp4')
        await bot.send_message(userid, libertex_5[str(lesson)], reply_markup=btn.as_markup(resize_keyboard=True))
        await bot.send_video(userid, video = video,reply_markup=btn.as_markup(resize_keyboard=True))
    else:
        await bot.send_message(userid, after_lesson['5'], reply_markup=btn.as_markup(resize_keyboard=True))
       
