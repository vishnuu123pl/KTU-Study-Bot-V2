from pyrogram import Client, filters
from plugins.constants import START_TEXT, START_BUTTONS
import json


@Client.on_message(filters.command("start"))
async def start(client, message):

    try:
        with open("users.json") as f:
            users = json.load(f)
    except:
        users = []

    user = message.from_user.id

    if user not in users:
        users.append(user)
        with open("users.json", "w") as f:
            json.dump(users, f)

    await message.reply_text(
        START_TEXT,
        reply_markup=START_BUTTONS
    )
