import asyncio
import json
import random
import re

import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import commands
from disnake.ext.commands import Context

from helpers import checks, json_manager

# Here we name the cog and create a new class for the cog.
from helpers.json_manager import load_config, account_is_open, create_account


class payments(commands.Cog, name="Donations"):
    def __init__(self, bot: commands.Bot):
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
        if account_is_open(ctx.author):  # checks if user data exists
            await ctx.reply("You are already connected!")
        else:
            await ctx.reply(
                "It seems like your account isn't connected yet! Make sure to be careful when you do this, as there is no way for you to deregister or change anything after. ` Type your full name in chat now.`")
            try:
                msg = await self.bot.wait_for("message", check=(lambda m: m.author.id == ctx.author.id))
                name = msg.content

                await ctx.reply("Adding \"" + name + "\" to your file\nWhat is your grade? (Ex freshman, sophomore)")

                msg2 = await self.bot.wait_for("message", check=(lambda m: m.author.id == ctx.author.id))
                grade = msg2.content.lower()
                await ctx.reply("Adding \"" + grade + "\" to your file.")

            finally:
                create_account(ctx.author, name, grade)
                await ctx.reply("Connection complete. You are good to go!")

    @commands.command(
        name="pay",
        description="Confirm a payment.",
    )
    @checks.not_blacklisted()
    async def pay(self, ctx, member: disnake.Member = None, amount):
        target = member.id
        users = await load_config()
        if await account_is_open(member):  # checks if user data exists
            await ctx.reply(
                "<@!" + str(target) + "> \'s data isn't in the file yet. They need to connect their account first!")
        else:
            print(users)  # debugging
        users = await load_config()

        await ctx.reply(f'Paid {target} ${amount}.')

        users[str(target)]["paid"] += amount


# Load cog

def setup(bot):
    bot.add_cog(payments(bot))
