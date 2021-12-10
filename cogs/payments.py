
import json
import os
import asyncio
import sys

from disnake import ApplicationCommandInteraction
from disnake.ext import commands
from disnake.ext.commands import Context

from helpers import checks


async def get_userinfo():
    with open('users.json') as f:
        users = json.load(f)

    return users


async def open_account(user):
    users = await get_userinfo()

    return user.id in users


async def create_account(user, name, grade):
    users = await get_userinfo()

    users[user.id]["grade"] = grade
    users[user.id]["paid"] = 0
    users[user.id]["name"] = name
    users[user.id]["smuggler"] = False

    with open('users.json', 'w') as f:
        json.dump(users, f)
    return True


# Only if you want to use variables that are in the config.json file.
if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


# Here we name the cog and create a new class for the cog.
class payments(commands.Cog, name="Donations"):
    def __init__(self, bot):
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.
    @commands.slash_command(
        name="connect",
        description="Register your account to prepare payments. You only need to do this once!",
    )
    # This will only allow non-blacklisted members to execute the command
    @checks.not_blacklisted()
    # This will only allow owners of the bot to execute the command -> config.json
    async def connect(self, ctx: ApplicationCommandInteraction):
        # await ctx.reply(users) #debugging purposes
        pass

    @commands.command(
        name="connect",
        description="Register your account to prepare payments. This is to allow us to keep track of things and manage stats.  You only need to do this once!",
    )
    @checks.not_blacklisted()
    async def connect(self, ctx: Context):
        if await open_account(ctx.author) is True:  # checks if user data exists
            await ctx.reply(
                "It seems like your account isn't connected yet! Make sure to be careful when you do this, as there is no way for you to deregister or change anything after. ` Type your full name in chat now. `")
            try:
                msg = await self.bot.wait_for("message")
                name = str(msg.content)
                await ctx.reply("Adding \"" + name + "\" to your file")
                print(name)
                await asyncio.sleep(2)
                await ctx.reply("What is your grade? (Ex freshman, sophomore)")
                msg2 = await self.bot.wait_for("message")
                grade = str(msg2.content.lower())
                print(grade)
                await ctx.reply("Adding \"" + grade + "\" to your file.")
            finally:
                await create_account(ctx.author, name, grade)
                await ctx.reply("Connection complete. You are good to go!")
        else:
            await ctx.reply("You are already connected!")


# Load cog

def setup(bot):
    bot.add_cog(payments(bot))
