
import json
import os
import asyncio
import sys
import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import commands
from disnake.ext.commands import Context

from helpers import checks

async def get_userinfo() -> object:
    with open('users.json', 'r') as f:
        users = json.load(f)

    return users


async def open_account(user):
    users = await get_userinfo()

    if str(user.id) in users:
        return False
    else:
        return True

# Only if you want to use variables that are in the config.json file.
if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


# Here we name the cog and create a new class for the cog.
class stats(commands.Cog, name="Statistics"):
    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.
    @commands.slash_command(
        name="check",
        description="Check payment information.",
    )
    # This will only allow non-blacklisted members to execute the command
    @checks.not_blacklisted()
    # This will only allow owners of the bot to execute the command -> config.json
    async def check(self, ctx: ApplicationCommandInteraction):
        # xd
        pass

    @commands.command(
        name="check",
        description="Check payment information.",
    )
    @checks.not_blacklisted()
    async def connect(self, ctx: Context):
        if await open_account(ctx.author) is True:  # checks if user data exists
            await ctx.reply("Your account isn't connected yet! Use the `connect` command to register.")
        else:
            user = ctx.author
            users = await get_userinfo()

            name = users[str(user.id)]["name"]
            grade = users[str(user.id)]["grade"]
            paid = users[str(user.id)]["paid"]
            #smuggler = users[str(user.id)]["smuggler"]

            em = disnake.Embed(title=f'{ctx.author.name} \'s Stats', color=disnake.Color.red())
            #if str(smuggler in users:
            #    em.add_field(name="Smuggler", value=smuggler)
            # Ill fix the smuggler code later cant be bothered
            em.add_field(name="Name", value=name)
            em.add_field(name='Grade', value=grade.capitalize())
            em.add_field(name='Paid', value="$"+str(paid))
            await ctx.reply(embed=em)



# Load cog

def setup(bot):
    bot.add_cog(stats(bot))
