import json

import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import commands
from disnake.ext.commands import Context

from helpers import checks
from helpers.json_manager import account_is_open, load_users


async def open_account(user):
    users = load_users()

    if user.id in users:
        return False
    else:
        return True

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
    async def check(self, ctx: Context):
        if account_is_open(ctx.author):  # checks if user data exists
            users = load_users()
            user = users[str(ctx.author.id)]

            em = disnake.Embed(
                title=f'{ctx.author.name} \'s Stats', color=disnake.Color.red())

            em.add_field(name="Name", value=user["name"])
            em.add_field(name='Grade', value=user["grade"].title())
            em.add_field(name='Paid', value="$"+str(user["paid"]))
            em.add_field(name="Smuggler",
                         value="Yes" if user["smuggler"] else "No")
            await ctx.reply(embed=em)

        else:
            await ctx.reply("Your account isn't connected yet! Use the `connect` command to register.")

    @commands.command(
        name="stats",
        description="Check payment information serverwide",
    )
    @checks.not_blacklisted()
    async def stats(self, ctx: Context):
        with open('stats.json') as file:
            json_input = json.load(file)
        sum = 0
        for user in json_input['users']:
            sum += json_input['users'][user]['paid']
        em = disnake.Embed(
            title="Overall Server Stats", color=disnake.Color.red())
        em.add_field(name="Total Amount Raised", value="$" + str(sum))
        await ctx.reply(embed=em)



# Load cog
def setup(bot):
    bot.add_cog(stats(bot))
