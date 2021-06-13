import asyncio
import re


class Process:
    def __init__(self, bot):
        self.bot = bot
        self.timer = 0

    async def process(self):
        process = await asyncio.create_subprocess_shell(
            'start.bat', stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)

        while process.returncode is None:
            data = await process.stdout.readline()
            if not data:
                break
            line = data.decode('ISO-8859-1').rstrip()
            if re.match(r'GPU1', line):
                await self.bot.send_msg(line.strip('GPU1: '))
            elif re.match(r'Eth speed', line):
                if self.timer == 20:
                    await self.bot.send_msg(line.strip('Eth speed: '))
                    self.timer = 0
                self.timer += 1
            print(line)
