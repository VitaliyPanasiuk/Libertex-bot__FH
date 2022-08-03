import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
from tgbot.config import  DB_URI


async def postgre_start():
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    if base:
        print('data base connect Ok!')
    cur.execute('''CREATE TABLE IF NOT EXISTS users(
        id varchar(20) primary key,
        firstName varchar(30),
        secondName varchar(30),
        userName varchar(30),
        phone varchar(15),
        lastSeen text,
        lastArticle text,
        articlelibertex int default 1,
        lessonlibertex int default 1
        )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS claims(
        claims_id serial primary key,
        user_id varchar(20) REFERENCES users(id),
        type text,
        status text,
        message text
        )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS admins(
        admin_id serial primary key,
        id text
        )''')
    
    base.commit()
    cur.close()
    base.close()
    
