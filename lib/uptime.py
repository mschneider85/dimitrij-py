import discord
from discord.ext import commands
from uptime import uptime
import time

start_time = time.time()

class INFO():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'uptime')
    async def show_uptime(self, ctx):
        embed = discord.Embed(title = 'Uptime', color = 0xeee657)

        def human_time(seconds):
            minute, second = divmod(seconds, 60)
            hour, minute = divmod(minute, 60)
            day, hour = divmod(hour, 24)
            return '%d days, %02d:%02d:%02d' % (day, hour, minute, second)

        embed.add_field(name = 'Dimitrij', value = human_time(time.time() - start_time))

        embed.add_field(name = 'Raspberry Pi', value = human_time(uptime()))

        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(INFO(bot))
