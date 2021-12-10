from json_manager import load_config

from disnake.ext import commands

from exceptions import *


def is_owner():
    async def predicate(context: commands.Context) -> bool:
        data = load_config()

        if context.author.id not in data["owners"]:
            raise UserNotOwner

        return True

    return commands.check(predicate)


def not_blacklisted():
    async def predicate(ctx: commands.Context) -> bool:
        data = load_config()

        if ctx.author.id in data["ids"]:
            raise UserBlacklisted

        return True

    return commands.check(predicate)
