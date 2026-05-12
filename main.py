import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# .env 파일에서 토큰 불러오기
load_dotenv()

# 봇 권한 설정
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ {bot.user.name} 봇이 켜졌어요! 🌸')
    print(f'   서버 {len(bot.guilds)}개에 연결됨')

    # cogs 폴더의 기능들 자동 로드
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'   ✓ {filename} 로드 완료')
            except Exception as e:
                print(f'   ✗ {filename} 로드 실패: {e}')

# 봇 실행
bot.run(os.getenv('DISCORD_TOKEN'))
