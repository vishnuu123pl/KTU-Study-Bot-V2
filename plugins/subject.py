from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data import DATA

# callback format:
# <branch>_<sem>_<year>_<cat>
# example: cse_sem3_2024_materials

@Client.on_callback_query(
    filters.regex(r"^(cse|ece|eee|ice|me|civil)_sem(\d+)_(\d+)_(\w+)$")
)
async def subject(_, query):

    parts = query.data.split("_")
    # ['cse','sem3','2024','materials']

    branch = parts[0]
    sem    = parts[1]   # e.g. "sem3"
    year   = parts[2]
    cat    = parts[3]

    # FIX: DATA is keyed by branch directly, not by year
    subjects = DATA.get(branch, {}).get(sem, [])

    if not subjects:
        await query.answer(
            "⚠️ No subjects found for this selection.",
            show_alert=True
        )
        return

    rows = []

    for idx, sub in enumerate(subjects):
        display = sub[:40]
        cb = f"res_{branch}_{sem}_{year}_{cat}_{idx}"
        rows.append([
            InlineKeyboardButton(display, callback_data=cb)
        ])

    # FIX: Back button pointed to "sub_..." which had no handler — now goes to branch selector
    rows.append([
        InlineKeyboardButton(
            "⬅ Back",
            callback_data=f"sem{sem.replace('sem','')}_{year}_{cat}"
        )
    ])

    await query.message.edit_text(
        "📚 **Select Subject**",
        reply_markup=InlineKeyboardMarkup(rows)
    )

    await query.answer()
