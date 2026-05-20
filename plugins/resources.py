from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data import DATA
import json

CAT_LABELS = {
    "materials": "📚 Study Materials",
    "pyq": "📝 Previous Year Questions",
    "series": "📄 Series Papers",
    "model": "📖 Model Papers",
}


@Client.on_callback_query(
    filters.regex(r"^res_(\w+)_sem(\d+)_(\d+)_(\w+)_(\d+)$")
)
async def resources(_, query):

    _, branch, sem_str, year, cat, idx_str = query.data.split("_", 5)

    sem = sem_str              # sem3 ✅
    sem_no = sem.replace("sem", "")   # 3 ✅

    idx = int(idx_str)

    subjects = DATA.get(branch, {}).get(sem, [])

    if idx >= len(subjects):
        await query.answer(
            "⚠️ Subject not found.",
            show_alert=True
        )
        return

    subject_name = subjects[idx]

    text = (
        f"📚 {subject_name}\n\n"
        f"🏷 Category: {CAT_LABELS.get(cat, cat)}\n"
        f"📘 Scheme: {year}\n"
        f"📖 Semester: {sem_no}\n"
        f"🏫 Branch: {branch.upper()}\n"
    )

    try:
        with open("storage.json") as f:
            data = json.load(f)
    except:
        data = {}

    notes_key = f"notes_sem{sem_no}_{subject_name.lower()}"
    pyq_key = f"pyq_sem{sem_no}_{subject_name.lower()}"

    available = (
        notes_key in data or
        pyq_key in data
    )

    if available:

        text += "\nSelect resource below 👇"

        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "📚 Notes",
                    callback_data=f"notes_sem{sem_no}_{subject_name.lower()}"
                ),
                InlineKeyboardButton(
                    "📝 PYQ",
                    callback_data=f"pyq_sem{sem_no}_{subject_name.lower()}"
                )
            ],
            [
                InlineKeyboardButton(
                    "📄 Model",
                    callback_data=f"model_sem{sem_no}_{subject_name.lower()}"
                ),
                InlineKeyboardButton(
                    "🎥 Videos",
                    callback_data=f"video_sem{sem_no}_{subject_name.lower()}"
                )
            ],
            [
                InlineKeyboardButton(
                    "⬅ Back",
                    callback_data=f"{branch}_{sem}_{year}_{cat}"
                )
            ]
        ])

    else:

        text += (
            "\n\n⚠️ Currently not available\n"
            "Adding soon.\n"
            "Contact admin."
        )

        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "⬅ Back",
                    callback_data=f"{branch}_{sem}_{year}_{cat}"
                )
            ]
        ])

    await query.message.edit_text(
        text,
        reply_markup=buttons
    )

    await query.answer()
