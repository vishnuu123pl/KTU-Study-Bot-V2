from pyrogram import Client, filters
from plugins.constants import START_TEXT, START_BUTTONS


@Client.on_callback_query(filters.regex("^back_start$"))
async def back_start(_, query):
    await query.message.edit_text(START_TEXT, reply_markup=START_BUTTONS)
    await query.answer()
