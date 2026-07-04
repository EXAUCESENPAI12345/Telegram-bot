import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🛒 Achat", "🎮 Jeux"],
        ["💰 Finance", "⚙️ Admin"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Bienvenue 🤖\nChoisis une option :",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🛒 Achat":
        await update.message.reply_text("Achat 🛒 actif")
    elif text == "🎮 Jeux":
        await update.message.reply_text("Jeux 🎮 actif")
    elif text == "💰 Finance":
        await update.message.reply_text("Finance 💰 actif")
    elif text == "⚙️ Admin":
        await update.message.reply_text("Admin ⚙️ protégé")
    else:
        await update.message.reply_text("Commande inconnue ❌")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot en ligne 🚀")

    # IMPORTANT: lancement propre
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
