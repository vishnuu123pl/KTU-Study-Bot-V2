from pyrogram import Client, filters
import json
import asyncio

ADMINS = [7412083181]

@Client.on_message(
    filters.command("broadcast") &
    filters.user(ADMINS)
)
async def broadcast(_, message):

    if len(message.command) < 2:

        await message.reply_text(
            "Usage:\n/broadcast Your message"
        )

        return

    text = message.text.split(
        maxsplit=1
    )[1]

    try:

        with open("users.json") as f:

            users = json.load(f)

    except:

        users = []

    sent = 0
    failed = 0

    status = await message.reply_text(
        "📢 Broadcasting..."
    )

    for user in users:

        try:

            await _.send_message(
                user,
                f"📢 Update\n\n{text}"
            )

            sent += 1

            await asyncio.sleep(0.2)

        except:

            failed += 1

    await status.edit_text(

        f"✅ Broadcast Complete\n\n"
        f"Sent: {sent}\n"
        f"Failed: {failed}"

    )
