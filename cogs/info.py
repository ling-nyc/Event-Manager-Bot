import disnake
from disnake.ext import commands


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['help'])
    async def _help(self, ctx):
        embedvar = disnake.Embed(title="Help Commands",description='', color=0x00ff00)

        embedvar.add_field(name='$stats', value='To see serverwide donation information.', inline=False)
        embedvar.add_field(name='$check @user', value='To check your own information', inline=False)
        embedvar.add_field(name='$connect', value='To add your data to the bot files, run this first.', inline=False)
        embedvar.add_field(name='$pay @user', value='Only for event managers and smugglers. Add money to a user\'s account.', inline=False)
        embedvar.add_field(name='$listpaid', value='Only for event managers and smugglers. Get a full list of people who paid.', inline=False)

        await ctx.send(embed=embedvar)

def setup(client):
    client.add_cog(Info(client))