from dataclasses import dataclass

from environs import Env

DB_URI = 'postgres://rlfdvcditosxia:550d193d8fb7962cb85178198e5f9612dbf11e12a08d2a0731adbfffb1943561@ec2-54-228-218-84.eu-west-1.compute.amazonaws.com:5432/d9s51kmjiegnth'
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
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, admins)),
            use_redis=env.bool("USE_REDIS"),
            
        ),
        db=DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASS'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME')
        ),
        misc=Miscellaneous()
    )



