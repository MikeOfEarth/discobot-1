import random
import settings
import discord
from discord.ext import commands

logger= settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        print("____________________")

    @bot.command(
            aliases=['p'],
            help="Answers with pong",
            description="*Whack*",
            brief="You probably can guess what this does",
            enabled=True,
            hidden=True
    )
    async def ping(ctx):
        await ctx.send("pong")

    @bot.command()
    async def say(ctx, *what):
        if " " in str(what):
            await ctx.send(" ".join(what))
        else:
            await ctx.send("".join(what))

    @bot.command()
    async def say2(ctx, what="What?", why="Why?"):
        await ctx.send(what+" "+why)

    @bot.command()
    async def picker(ctx, *choices):
        await ctx.send('Picking between choices.....')
        await ctx.send(f'How about {random.choice(choices)}?')
    
    @bot.command()
    async def adder(ctx, *nums:int):
        await ctx.send(sum(nums))

    
    # @bot.command()
    # async def say(ctx, what = "What?"):
    #     await ctx.send(what)
        
    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()