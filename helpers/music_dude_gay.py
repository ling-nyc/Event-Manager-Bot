# My own functions because Toliver fucked them up :kekw:
import json

async def is_connected(user):

    users = await get_user_data()

    if str(user.id) in users:
        return True
    else:
        return False


async def get_user_data():
    '''with open('stats.json','r') as f:
        #users = json.load(f)'''
    with open('stats.json') as file:
        return json.load(file)["users"]