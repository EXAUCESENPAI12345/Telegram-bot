import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot OK 🚀 sur Render")

def main():
    if not TOKEN:
        print("❌ TOKEN manquant")
        return

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot lancé 🚀")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
