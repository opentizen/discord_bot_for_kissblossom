import discord
from discord.ext import commands
from discord import app_commands
import sqlite3
import random
import time
import os

def get_db():
    os.makedirs('data', exist_ok=True)
    conn = sqlite3.connect('data/bot.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS levels (
            user_id   INTEGER,
            guild_id  INTEGER,
            xp        INTEGER DEFAULT 0,
            level     INTEGER DEFAULT 0,
            PRIMARY KEY (user_id, guild_id)
        )
    ''')
    conn.commit()
    return conn

def xp_needed(level):
    return 100 * (level + 1)

class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cooldowns = {}

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or not message.guild:
            return

        key = (message.author.id, message.guild.id)
        now = time.time()
        if key in self.cooldowns and now - self.cooldowns[key] < 60:
            return
        self.cooldowns[key] = now

        xp_gain = random.randint(15, 25)
        conn = get_db()
        cur = conn.cursor()

        cur.execute('INSERT OR IGNORE INTO levels VALUES (?, ?, 0, 0)',
                    (message.author.id, message.guild.id))
        cur.execute('UPDATE levels SET xp = xp + ? WHERE user_id = ? AND guild_id = ?',
                    (xp_gain, message.author.id, message.guild.id))
        cur.execute('SELECT xp, level FROM levels WHERE user_id = ? AND guild_id = ?',
                    (message.author.id, message.guild.id))
        xp, level = cur.fetchone()

        if xp >= xp_needed(level):
            new_level = level + 1
            cur.execute('UPDATE levels SET level = ?, xp = 0 WHERE user_id = ? AND guild_id = ?',
                        (new_level, message.author.id, message.guild.id))
            conn.commit()
            conn.close()

            embed = discord.Embed(
                title='🎉 레벨업!',
                description=f'{message.author.mention}님이 **레벨 {new_level}**이 됐어요! 🌸',
                color=0xffb6d9
            )
            await message.channel.send(embed=embed)
        else:
            conn.commit()
            conn.close()

    # /레벨 슬래시 명령어
    @app_commands.command(name='레벨', description='내 레벨과 경험치를 확인해요')
    @app_commands.describe(member='확인할 멤버 (비워두면 본인)')
    async def check_level(self, interaction: discord.Interaction, member: discord.Member = None):
        member = member or interaction.user
        conn = get_db()
        cur = conn.cursor()
        cur.execute('SELECT xp, level FROM levels WHERE user_id = ? AND guild_id = ?',
                    (member.id, interaction.guild.id))
        result = cur.fetchone()
        conn.close()

        if not result:
            await interaction.response.send_message(
                f'**{member.display_name}**님은 아직 채팅을 안 하셨어요!', ephemeral=True)
            return

        xp, level = result
        needed = xp_needed(level)
        filled = int((xp / needed) * 10)
        bar = '█' * filled + '░' * (10 - filled)

        embed = discord.Embed(title=f'🌸 {member.display_name}님의 레벨', color=0xff9ecd)
        embed.add_field(name='레벨', value=f'**Lv.{level}**', inline=True)
        embed.add_field(name='경험치', value=f'{xp} / {needed} XP', inline=True)
        embed.add_field(name='진행도', value=f'`{bar}`', inline=False)
        embed.set_thumbnail(url=member.display_avatar.url)
        await interaction.response.send_message(embed=embed)

    # /순위 슬래시 명령어
    @app_commands.command(name='순위', description='서버 레벨 TOP 10 순위를 확인해요')
    async def leaderboard(self, interaction: discord.Interaction):
        conn = get_db()
        cur = conn.cursor()
        cur.execute('''SELECT user_id, level, xp FROM levels
                       WHERE guild_id = ?
                       ORDER BY level DESC, xp DESC LIMIT 10''',
                    (interaction.guild.id,))
        rows = cur.fetchall()
        conn.close()

        embed = discord.Embed(title='🏆 kissblossom 레벨 순위', color=0xff9ecd)
        medals = ['🥇', '🥈', '🥉']
        desc = ''
        for i, (user_id, level, xp) in enumerate(rows):
            member = interaction.guild.get_member(user_id)
            name = member.display_name if member else '알 수 없음'
            medal = medals[i] if i < 3 else f'**{i+1}.**'
            desc += f'{medal} {name} — Lv.{level} ({xp} XP)\n'

        embed.description = desc or '아직 데이터가 없어요!'
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Levels(bot))
