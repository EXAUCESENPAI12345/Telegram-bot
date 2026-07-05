import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running 🚀"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut Beni ✅ Bot en ligne")

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    PORT = int(os.getenv("PORT", 10000))

    # Render fournit cette variable parfois
    BASE_URL = os.getenv("RENDER_EXTERNAL_URL")

    if not BASE_URL:
        print("❌ RENDER_EXTERNAL_URL introuvable")
        return

    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{BASE_URL}/{TOKEN}"
    )

if __name__ == "__main__":
    main()
