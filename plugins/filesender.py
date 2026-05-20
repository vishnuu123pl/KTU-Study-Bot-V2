from pyrogram import Client, filters
import json


@Client.on_callback_query(
    filters.regex(r"^(notes|pyq|model|video)_(.+)$")
)
async def send_resource(_, query):

    key = query.data.lower()

    try:

        with open("storage.json") as f:
            data = json.load(f)

    except:
        data = {}

    if key not in data:

        await query.answer(
            "⚠️ Resource not uploaded yet",
            show_alert=True
        )

        return

    files = data[key]

    for file in files:

        await query.message.reply_document(
            file["id"],
            caption=f"📄 {file['name']}"
        )

    await query.answer()
