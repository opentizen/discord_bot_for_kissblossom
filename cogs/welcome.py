import discord
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # 새 멤버가 서버에 들어왔을 때 자동 실행
    @commands.Cog.listener()
    async def on_member_join(self, member):
        # '환영' 채널 찾기 → 없으면 시스템 채널 사용
        channel = (
            discord.utils.get(member.guild.text_channels, name='환영') or
            discord.utils.get(member.guild.text_channels, name='general') or
            member.guild.system_channel
        )
        if not channel:
            return

        embed = discord.Embed(
            title=f'🌸 {member.display_name}님, 환영해요🌸',
            description=(
                f'💕**kissblossom**에 오신 걸 환영해요 💕\n'
                f'이제 서버 멤버가 **{member.guild.member_count}명**이 됐어요!\n\n'
                f'채팅하면 경험치가 쌓이고, `/레벨` 로 확인할 수 있어요 ✨'
            ),
            color=0xff9ecd
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text='kissblossom 🌸')
        await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Welcome(bot))
