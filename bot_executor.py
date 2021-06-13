from aiogram import Bot, Dispatcher
from subprocess import call


class TelegramBot:
    bot = Bot(token='')
    eid = ''  # int
    switcher = False

    def __init__(self):
        self.dp = Dispatcher(self.bot)
        decorator = self.dp.message_handler(commands=['switch'])
        decorator(self.switch_mode)

    async def switch_mode(self, *args):
        path = 'C:'
        call(f"{path}{int(self.switcher)}.bat")  # script name 0.bar or 1.bat
        self.switcher = not self.switcher

    async def send_msg(self, msg):
        try:
            await self.bot.send_message(self.eid, msg)
        except Exception as e:
            print(e)

    async def start_polling(self):
        await self.dp.start_polling()


if __name__ == '__main__':
    TelegramBot()
