import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bienvenue sur NexamPay 🚀")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Message reçu: {update.message.text}")

def main():
    if not TOKEN:
        print("TOKEN manquant")
        return

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

    print("NexamPay en ligne 🚀")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
