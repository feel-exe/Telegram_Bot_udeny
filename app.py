from aiogram import executor
from utils.set_default_commands import set_default_commands
import middlewares, filters, handlers
from loader import dp
from loader import db
from utils.db_api import db_gino


async def on_startup(dp):
    from utils.notify_admins import on_startup_notify, on_add_admins_in_bd
    await on_startup_notify(dp)

    # await on_startup_notify(dp)
    # await set_default_commands(dp)
    # await on_startup_notify(dp)
    await db_gino.on_startup(dp)
    #
    # await db.gino.drop_all()

    await db.gino.create_all()
    await on_add_admins_in_bd()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
