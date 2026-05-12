import discord
from discord.ext import commands, tasks
import datetime
import random

# 오늘의 질문 목록 (자유롭게 추가/수정 가능!)
QUESTIONS = [
    "오늘 하루 중 가장 좋았던 순간은 무엇인가요? 🌟",
    "요즘 빠져있는 노래나 아티스트가 있나요? 🎵",
    "지금 당장 여행 갈 수 있다면 어디로 가고 싶나요? ✈️",
    "최근에 먹은 것 중 가장 맛있었던 음식은? 🍽️",
    "요즘 가장 즐겨보는 영상이나 드라마는 무엇인가요? 📺",
    "오늘의 기분을 날씨로 표현하면? ☀️🌧️❄️",
    "최근에 읽은 책이나 보고 싶은 책이 있나요? 📚",
    "지금 이 순간 가장 하고 싶은 것은? 💭",
    "좋아하는 계절과 그 이유는? 🍂",
    "오늘 나에게 해주고 싶은 말 한마디는? 💌",
    "요즘 가장 즐거운 시간은 언제인가요? 😊",
    "최근에 새로 알게 된 흥미로운 사실이 있나요? 💡",
    "나만의 스트레스 해소법이 있나요? 🧘",
    "올해 꼭 해보고 싶은 것이 있다면? 🎯",
    "나를 가장 행복하게 하는 것은 무엇인가요? 💖",
]

KST = datetime.timezone(datetime.timedelta(hours=9))

class DailyQuestion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.daily_task.start()

    def cog_unload(self):
        self.daily_task.cancel()

    # 매일 오전 9시(한국 시간)에 자동 실행
    @tasks.loop(time=datetime.time(hour=9, minute=0, tzinfo=KST))
    async def daily_task(self):
        await self.send_question()

    @daily_task.before_loop
    async def before_daily(self):
        await self.bot.wait_until_ready()

    async def send_question(self):
        for guild in self.bot.guilds:
            # '오늘의-질문' 채널 찾기 → 없으면 '일반' → 없으면 시스템 채널
            channel = (
                discord.utils.get(guild.text_channels, name='오늘의-질문') or
                discord.utils.get(guild.text_channels, name='일반') or
                guild.system_channel
            )
            if channel:
                question = random.choice(QUESTIONS)
                today = datetime.date.today().strftime('%Y년 %m월 %d일')
                embed = discord.Embed(
                    title='🌸 오늘의 질문',
                    description=f'**{question}**\n\n댓글로 자유롭게 답해보세요 💬',
                    color=0xff9ecd
                )
                embed.set_footer(text=f'kissblossom · {today}')
                await channel.send(embed=embed)

    # !질문 명령어 (수동으로 질문 보내기)
    @commands.command(name='질문')
    async def manual_question(self, ctx):
        """관리자가 수동으로 오늘의 질문 전송"""
        await self.send_question()

async def setup(bot):
    await bot.add_cog(DailyQuestion(bot))
