from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        response = "こんにちは! ヘルプコマンドです。"

        await ctx.send(response)


async def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))
