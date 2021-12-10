from disnake.ext import commands

from exceptions import *

import json


def load_config() -> dict:
    with open("config.json") as file:
        return json.load(file)


def load_blacklist() -> dict:
    with open("blacklist.json") as file:
        return json.load(file)


def load_users() -> dict:
    with open('users.json') as file:
        return json.load(file)


def add_user_to_blacklist(user_id: str):
    with open("blacklist.json", "r+") as file:
        file_data = json.load(file)
        file_data["ids"].append(user_id)
        file.truncate(0)

        json.dump(file_data, file, indent=4)


def remove_user_from_blacklist(user_id: str):
    with open("blacklist.json", "r+") as file:
        file_data = json.load(file)
        file_data["ids"].remove(user_id)
        file.truncate(0)

        json.dump(file_data, file, indent=4)

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
