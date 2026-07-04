import os
import logging
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv("BOT_TOKEN") # Mets ton token dans Render > Environment

app_flask = Flask(__name__)

@app_flask.route("/")
def home():
    return "Bot is alive"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut Beni, bot en ligne ✅")

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    # Pour Render on utilise Webhook
    PORT = int(os.getenv("PORT", 10000))
    WEBHOOK_URL = os.getenv("RENDER_EXTERNAL_URL")
    
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{WEBHOOK_URL}/{TOKEN}"
    )

if __name__ == "__main__":
    main()
