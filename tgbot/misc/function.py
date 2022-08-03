import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
from tgbot.config import  DB_URI
from tgbot.config import load_config
from tgbot.services import broadcaster
from aiogram import Bot, Dispatcher


config = load_config(".env")

async def auf_status(userid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    userid = str(userid)
    cur.execute('SELECT * FROM users ')
    users = cur.fetchall()
    answer = False
    for user in users:
        if user[0] == userid:
            answer = True
    base.commit()
    cur.close()
    base.close()
    return answer

async def get_list_of_users():
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    cur.execute('SELECT * FROM users ')
    users = cur.fetchall()
    answer = []
    for user in users:
        answer.append(user[0])
    cur.close()
    base.close()
    return answer

async def alert_admins(bot: Bot, admin_ids: list[int],user_id):
    await broadcaster.broadcast(bot, admin_ids, f"Поступила новая заявка/вопрос\nuser_id:{user_id}")
    
async def get_claims():
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    cur.execute('''SELECT claims_id, id, firstName, userName, phone,type,status, message
                FROM users 
                INNER JOIN claims c on users.id = c.user_id and c.status = 'active'
                ''')
    claims = cur.fetchall()
    base.commit()
    cur.close()
    base.close()
    return claims

async def get_lesson_libertex(userid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    cur.execute('SELECT * FROM users ')
    users = cur.fetchall()
    answer = []
    for user in users:
        if str(user[0]) == str(userid):
            answer = [user[7],user[8]]
    cur.close()
    base.close()
    return answer
