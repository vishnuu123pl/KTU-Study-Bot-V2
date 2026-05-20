from pyrogram import idle
from info import ADMINS   # or config.py if ADMINS is there
from pyrogram import Client

app = Client(
    "KTU",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)


async def main():

    await app.start()

    print("✅ Bot Started")

    for admin in ADMINS:

        try:

            await app.send_message(
                admin,
                "🤖 KTU Study Bot Started Successfully ✅"
            )

        except Exception as e:
            print(e)

    await idle()


app.run(main())
