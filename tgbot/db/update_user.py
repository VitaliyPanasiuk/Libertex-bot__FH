import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
from tgbot.config import  DB_URI


async def reg_user(userid, firstName,lastName,userName,phone):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (userid, firstName, lastName, userName, phone)
    cur.execute('INSERT INTO users (id, firstName, secondName, userName, phone)  VALUES (%s,%s,%s,%s,%s)', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def add_admin(userid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    admins = '''select * from admins'''
    cur.execute(admins)
    rows = cur.fetchall()
    check = False
    for i in rows:
        if str(userid) == str(i[1]):
            check = True
    if check == False:
        data = (str(userid),)
        cur.execute('INSERT INTO admins (id)  VALUES (%s)', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def update_last_article(userid, article):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (article, str(userid))
    cur.execute('UPDATE users SET lastArticle = %s WHERE id = %s', data)
    
    
    base.commit()
    cur.close()
    base.close()
    
async def make_claim(userid, type, status,message):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = (userid, type, status, message)
    cur.execute('INSERT INTO claims (user_id, type, status, message)  VALUES (%s,%s,%s,%s)', data)
    
    base.commit()
    cur.close()
    base.close()
    
async def anwer_claim(claim_id):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data = ('answered', int(claim_id))
    cur.execute('UPDATE claims SET status = %s WHERE claims_id = %s', data)
    
    
    base.commit()
    cur.close()
    base.close()
async def update_article(article,lesson,userid):
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    data1 = (int(article),str(userid))
    data2 = (int(lesson),str(userid))
    cur.execute('UPDATE users SET articlelibertex = %s WHERE id = %s', data1)
    cur.execute('UPDATE users SET lessonlibertex = %s WHERE id = %s', data2)
    
    
    base.commit()
    cur.close()
    base.close()