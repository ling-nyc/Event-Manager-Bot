import json


def load_config() -> dict:
    with open("stats.json") as file:
        return json.load(file)


def load_stats() -> dict:
    with open('stats.json') as file:
        return json.load(file)


def load_blacklist() -> list:
    with open("stats.json") as file:
        return json.load(file)["blacklist"]


def load_users() -> dict:
    with open('stats.json') as file:
        return json.load(file)["users"]


def create_account(user, name, grade):
    stats = load_stats()

    stats['users'][user.id] = {
        "grade": grade,
        "paid": 0,
        "name": name,
        "smuggler": False
    }

    with open('stats.json', 'w') as f:
        json.dump(stats, f)


def account_is_open(user):
    return (str(user.id) in load_users())


def add_user_to_blacklist(user_id: str):
    stats = load_stats()
    stats['blacklist'].append(user_id)

    with open("stats.json", "w") as file:
        json.dump(stats, file, indent=4)


def remove_user_from_blacklist(user_id: str):
    stats = load_stats()
    stats['blacklist'].remove(user_id)

    with open("stats.json", "w") as file:
        json.dump(stats, file, indent=4)
