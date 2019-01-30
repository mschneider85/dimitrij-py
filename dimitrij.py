import discord
from discord.ext import commands
from config import token
import asyncio
# import pdb; pdb.set_trace()

startup_extensions = ['lib.rng', 'lib.tt', 'lib.info', 'lib.uptime']

activity = discord.Game(name = 'Table tennis')
bot = commands.Bot( command_prefix = '!',
                    description = 'A table tennis Discord bot.',
                    activity = activity,
                    pm_help = None)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('Invite: https://discordapp.com/oauth2/authorize?&client_id={user_id}&scope=bot&permissions=3136'.format(user_id = bot.user.id))
    print('------')


@bot.command(name = 'load', hidden = True)
@commands.is_owner()
async def lib_load(ctx, *, cog: str):
    """Command which Loads a Module.
    Remember to use dot path. e.g: cogs.owner"""
    try:
        bot.load_extension(cog)
    except Exception as e:
        await ctx.send("**`ERROR:`** {type} - {e}".format(type = type(e).__name__, e = e))
    else:
        await ctx.send('**`SUCCESS`**')

@bot.command(name = 'unload', hidden = True)
@commands.is_owner()
async def lib_unload(ctx, *, cog: str):
    """Command which Unloads a Module.
    Remember to use dot path. e.g: cogs.owner"""
    try:
        bot.unload_extension(cog)
    except Exception as e:
        await ctx.send("**`ERROR:`** {type} - {e}".format(type = type(e).__name__, e = e))
    else:
        await ctx.send('**`SUCCESS`**')

@bot.command(name = 'reload', hidden = True)
@commands.is_owner()
async def lib_reload(ctx, *, cog: str):
    """Command which Reloads a Module.
    Remember to use dot path. e.g: cogs.owner"""
    try:
        bot.unload_extension(cog)
        bot.load_extension(cog)
    except Exception as e:
        await ctx.send("**`ERROR:`** {type} - {e}".format(type = type(e).__name__, e = e))
    else:
        await ctx.send('**`SUCCESS`**')

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(token)
