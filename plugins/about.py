from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_callback_query(filters.regex("^about$"))
async def about(_, query):

    text = """
🎓 KTU Study Bot

📚 Notes
📝 PYQ
📄 Model Papers

Built for KTU students.

Developed with ❤️
"""

    await query.message.edit_text(
        text,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅ Back", callback_data="back_start")]
        ])
    )

    await query.answer()
