from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BRANCHES = [
    ("💻 CSE",  "cse"),
    ("📡 ECE",  "ece"),
    ("🔌 EEE",  "eee"),
    ("🎛 ICE",  "ice"),
    ("⚙️ ME",   "me"),
    ("🏗 Civil","civil"),
]

# callback format: sem<N>_<year>_<cat>   e.g. sem3_2024_materials
@Client.on_callback_query(filters.regex(r"^sem(\d+)_(\d+)_(\w+)$"))
async def branch(_, query):
    parts = query.data.split("_")   # ['sem3','2024','materials']
    sem   = parts[0]                # sem3
    year  = parts[1]                # 2024
    cat   = parts[2]                # materials

    sem_no = sem.replace("sem", "")

    rows = [
        [InlineKeyboardButton(label, callback_data=f"{code}_{sem}_{year}_{cat}")]
        for label, code in BRANCHES
    ]
    rows.append([InlineKeyboardButton("⬅ Back", callback_data=f"scheme_{year}_{cat}")])

    await query.message.edit_text(
        f"📘 **Semester {sem_no}**\n\nSelect Branch 👇",
        reply_markup=InlineKeyboardMarkup(rows)
    )
    await query.answer()
