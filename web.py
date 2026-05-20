from flask import Flask
from threading import Thread
import os
import asyncio
from bot import main

flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bot Running"

def run():
    port = int(os.environ.get("PORT", 8000))
    flask_app.run(
        host="0.0.0.0",
        port=port,
        use_reloader=False
    )

Thread(target=run).start()
asyncio.run(main())   # ✅ was: main()
