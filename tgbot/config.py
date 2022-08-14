from dataclasses import dataclass

from environs import Env
import os

DB_URI = 'postgres://ioynlgrpfnrytg:ab4751269a3d014f61d9dbbcb15315afd56e2382f00ffd6c95e0046403772d82@ec2-44-206-197-71.compute-1.amazonaws.com:5432/d8958aaedan035'
import psycopg2
from psycopg2 import sql

def get_admins():
    base = psycopg2.connect(DB_URI,sslmode="require")
    cur = base.cursor()
    cur.execute('''select * from admins''')
    rows = cur.fetchall()
    admins = []
    for i in rows:
        admins.append(i[1])
    
    base.commit()
    cur.close()
    base.close()
    return admins

@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    use_redis: bool


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    misc: Miscellaneous


def load_config(path: str = None):
    env = Env()
    env.read_env(path)
    admins = get_admins()
    return Config(
        tg_bot=TgBot(
            token=os.environ['BOT_TOKEN'],
            admin_ids=list(map(int, admins)),
            use_redis=env.bool("USE_REDIS"),
            # token=env.str("BOT_TOKEN"),
            # admin_ids=list(map(int, admins)),
            # use_redis=env.bool("USE_REDIS"),
            
        ),
        db=DbConfig(
            host='',
            password='',
            user='',
            database=''
        ),
        misc=Miscellaneous()
    )



