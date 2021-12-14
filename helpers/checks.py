import disnake
from .json_manager import load_blacklist, load_config
from disnake.ext import commands

from exceptions import *


def is_owner():
    async def predicate(context: commands.Context) -> bool:
        config = load_config()

        if context.author.id not in config["owners"]:
            raise UserNotOwner

        return True

    return commands.check(predicate)


def not_blacklisted():
    #disabled
    pass
'''
    async def predicate(ctx: commands.Context) -> bool:
        blacklist = load_blacklist()

        if ctx.author.id in blacklist:
            raise UserBlacklisted

        return True

    return commands.check(predicate)
'''
