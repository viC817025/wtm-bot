import discord
from discord.ext import commands

class Main(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def 延遲(self,ctx):
        await ctx.send(F'目前延遲為{round(self.bot.latency*1000)}ms')

def setup(bot):
    bot.add_cog(Main(bot))