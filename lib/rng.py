from discord.ext import commands

import random

class RNG():
    COINS = ['Kopf', 'Zahl']
    DICES = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣']
    MAX_DICES = 4

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def flip(self, ctx):
        await ctx.send(random.choice(RNG.COINS))

    @commands.command()
    async def roll(self, ctx, dices: str = '1'):
        try:
            n = min([int(dices), RNG.MAX_DICES])
        except Exception:
            n = 1
        await ctx.send(self.roll_dices(n))

    @staticmethod
    def roll_dices(n: int):
        dices_range = range(0, n)
        results = [random.choice(RNG.DICES) for n in dices_range]
        return ' '.join(results)

def setup(bot):
    bot.add_cog(RNG(bot))
