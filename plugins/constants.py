from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = """
🎓 Welcome to KTU Study Bot

Your smart study companion for KTU students.

📚 Notes
📝 PYQs
📄 Model Papers
🎥 Resources

Select your course to continue 👇
"""

START_BUTTONS = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "🎓 B.Tech",
            callback_data="cat_materials"
        )
    ],
    [
        InlineKeyboardButton(
            "📢 Updates",
            url="https://t.me/YOUR_CHANNEL"
        ),
        InlineKeyboardButton(
            "ℹ️ About",
            callback_data="about"
        )
    ]
])
