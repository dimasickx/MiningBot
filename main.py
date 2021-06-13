import asyncio
import process
import bot_executor


def main():
    bot = bot_executor.TelegramBot()
    my_proc = process.Process(bot)

    loop = asyncio.get_event_loop()

    loop.create_task(my_proc.process())
    loop.create_task(bot.start_polling())

    loop.run_forever()


if __name__ == '__main__':
    main()
