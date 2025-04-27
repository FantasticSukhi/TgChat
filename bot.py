from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch Telegram Bot Token from environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Simple dummy AI response function
def local_ai_reply(user_text):
    user_text = user_text.lower()
    
    # Basic logic
    if "hello" in user_text or "hi" in user_text:
        return "Hello bhai! Kaise ho? 👋"
    elif "kaise ho" in user_text:
        return "Mast bhai! Tu suna? 😎"
    elif "bye" in user_text:
        return "Bye bhai, milte hain fir! 👋"
    else:
        return f"Tune bola '{user_text}', main kya bolun bhai 😂"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello bhai! Main ek simple AI bot hoon. Bol kya baat hai? 🔥")

# Normal message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    reply = local_ai_reply(user_text)
    await update.message.reply_text(reply)

# Main function
async def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot chal raha hai bhai 🚀")
    await app.start()
    await app.updater.start_polling()
    await app.updater.idle()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
