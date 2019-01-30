import discord
from discord.ext import commands

import random

class TT():
    CHECK_MARK = '✅'
    PING_PONG = '🏓'

    JOINED = 'ist dem Spiel beigetreten.'
    LEFT = 'hat das Spiel verlassen.'

    client = discord.Client()

    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def starting_message(user: discord.Member):
        text = ("---------------------------------------------------\n"
                "{ping_pong} LASST UNS TISCHTENNIS SPIELEN! {ping_pong}\n"
                "---------------------------------------------------\n"
                "{player_name} hat ein neues Spiel gestartet.\n"
                "Warte auf Spieler...")
        return text.format(ping_pong = TT.PING_PONG, player_name = user.display_name)

    @staticmethod
    def team_message(user_names):
        def build_teams(lst):
            teams = [', '.join(lst[item::2]) for item in range(2)]
            random.shuffle(teams, random.random)
            return teams
        left, right = build_teams(user_names)
        text = ("---------------------------------------------------\n"
                "{ping_pong} DIE TEAMS STEHEN! {ping_pong}\n"
                "---------------------------------------------------\n"
                "Team A: {left}\n"
                "Team B: {right}\n")
        return text.format(ping_pong = TT.PING_PONG, left = left, right = right)

    @commands.command()
    @commands.guild_only()
    async def tt(self, ctx, *, originator: discord.Member = None):
        if originator is None:
            originator = ctx.author

        message = await ctx.send(self.starting_message(originator))
        await message.add_reaction(TT.CHECK_MARK)

        def check_reaction(reaction, user: discord.Member):
            return user == originator and ctx.message.channel == reaction.message.channel and str(reaction.emoji) == '✅'

        reaction, member = await self.bot.wait_for('reaction_add', check = check_reaction)

        users = await reaction.users().flatten()
        user_names = []
        for user in users:
            if user.bot:
                continue
            user_names.append(user.display_name)
        random.shuffle(user_names, random.random)

        await message.delete()

        def check_join_leave_message(message: discord.Message):
            return message.author.bot and (message.content.endswith(TT.JOINED) or message.content.endswith(TT.LEFT))

        messages = await ctx.channel.history(limit=100).flatten()
        messages = [message for message in messages if check_join_leave_message(message)]
        for message in messages:
            await message.delete()

        await ctx.send(self.team_message(user_names))

    @client.event
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == TT.CHECK_MARK and reaction.message.author.bot and user != reaction.message.author:
            await reaction.message.channel.send("{user} {joined}".format(user = user.display_name, joined = TT.JOINED))

    @client.event
    async def on_reaction_remove(self, reaction, user):
        if reaction.emoji == TT.CHECK_MARK and reaction.message.author.bot and user != reaction.message.author:
            await reaction.message.channel.send("{user} {left}".format(user = user.display_name, left = TT.LEFT))

def setup(bot):
    bot.add_cog(TT(bot))
