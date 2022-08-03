import psycopg2
from psycopg2 import sql
from psycopg2.extensions import AsIs
from tgbot.config import  DB_URI
import xlwt


async def export_db():
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    sql = '''select * from users'''
    cur.execute(sql)
    rows = cur.fetchall()
    
    
    
    w = xlwt.Workbook(encoding='utf-8')
    Style = xlwt.easyxf ('font: name Times New Roman, color-index black, bold on', num_format_str='#,##0.00') # инициализация
    Ws = w.add_sheet ('Пользователи')
    Title = "ID, имя, фамилия, username, телефон, последняя активность, последний раздел"
    title = Title.split(",")
    for i in range(len(title)):
        Ws.write(0, i, title[i], Style)
        # Начать запись запросов базы данных
    for i in range(len(rows)):
        row = rows[i]
        for j in range(len(row)):
            if row[j]:
                item = row[j]
                Ws.write(i + 1, j, item, Style)
    
    path = 'tgbot/misc/users.xls'
    w.save(path)
    
    cur.execute('''SELECT claims_id, id, firstName, userName, phone,type,status, message
                FROM users 
                INNER JOIN claims c on users.id = c.user_id and c.status = 'active'
                ''')
    rows = cur.fetchall()
    
    w = xlwt.Workbook(encoding='utf-8')
    Style = xlwt.easyxf ('font: name Times New Roman, color-index black, bold on', num_format_str='#,##0.00') # инициализация
    Ws = w.add_sheet ('Заявки и вопросы')
    Title = "ID заявки,ID пользователя, имя, фамилия, username, телефон, тип завяки, статус, сообщение"
    title = Title.split(",")
    for i in range(len(title)):
        Ws.write(0, i, title[i], Style)
        # Начать запись запросов базы данных
    for i in range(len(rows)):
        row = rows[i]
        for j in range(len(row)):
            if row[j]:
                item = row[j]
                Ws.write(i + 1, j, item, Style)
    
    path = 'tgbot/misc/claims.xls'
    w.save(path)
    
    cur.close()
    base.close()