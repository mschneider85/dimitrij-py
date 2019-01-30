import discord
from discord.ext import commands

class INFO():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title = 'Dimitrij Ovtchabot', description = 'A table tennis Discord bot.', color = 0xeee657)

        embed.add_field(name = 'Author', value = 'Martin Schneider')

        embed.add_field(name = 'Server count', value = "{count}".format(count = len(self.bot.guilds)))

        embed.add_field(name = 'Invite', value = '[Invite link](https://discordapp.com/oauth2/authorize?&client_id={user_id}&scope=bot&permissions=0)'.format(user_id = self.bot.user.id))

        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(INFO(bot))
