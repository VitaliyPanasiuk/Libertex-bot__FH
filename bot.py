import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage

from tgbot.config import load_config
from tgbot.handlers.admin import admin_router
from tgbot.handlers.user import user_router
from tgbot.handlers.aboutApp import aboutApp_router
from tgbot.handlers.aboutBranch import aboutBranch_router
from tgbot.handlers.aboutDonate import aboutDonate_router
from tgbot.handlers.partner import partner_router
from tgbot.handlers.servus import servus_router
from tgbot.handlers.tg import tg_router
from tgbot.middlewares.config import ConfigMiddleware
from tgbot.services import broadcaster

from tgbot.db import user_db

logger = logging.getLogger(__name__)




async def on_startup(bot: Bot, admin_ids: list[int]):
    await broadcaster.broadcast(bot, admin_ids, "Бот успешно запущен")



def register_global_middlewares(dp: Dispatcher, config):
    dp.message.outer_middleware(ConfigMiddleware(config))
    dp.callback_query.outer_middleware(ConfigMiddleware(config))


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    storage = MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(storage=storage)

    for router in [
        admin_router,
        user_router,
        aboutApp_router,
        aboutBranch_router,
        aboutDonate_router,
        partner_router,
        servus_router,
        tg_router,
    ]:
        dp.include_router(router)

    register_global_middlewares(dp, config)

    await on_startup(bot, config.tg_bot.admin_ids)
    await user_db.postgre_start()
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Бот був вимкнений!")
