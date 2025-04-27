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
        replies = [
            "Hello bhai! Kaise ho? 👋",
            "Hi bhai! Kya chal raha hai? 😊",
            "Yo bhai! Sab mast? 👊",
            "Aree bhai! Kaise ho? 😊",
            "Hello! Dimaag thoda slow chal raha hai, lekin tu kaisa hai? 🤔"
        ]
        return random.choice(replies)
    
    elif "kaise ho" in user_text:
        replies = [
            "Mast bhai! Tu suna? 😎",
            "Sab theek hai bhai, tum batao? 😄",
            "Bas chill kar raha hoon bhai! Tum kya kar rahe ho? 😌",
            "Mast hoon bhai, ab batao, kaise ho tum? 😏"
        ]
        return random.choice(replies)

    elif "khana hua" in user_text:  # Corrected here for "khana hua"
        replies = [
            "Haan bhai, khana ho gaya! Tumne khaya? 🍽️",
            "Khana toh ho gaya bhai, tumne khaya? 😋",
            "Abhi toh khana khane ki soch raha hoon, tumne khaya? 🍛",
            "Haan bhai, khana khaya, ab relax hoon! 😌"
        ]
        return random.choice(replies)

    elif "kaha ho" in user_text:
        replies = [
            "Bas yahin hoon bhai, tum kaha ho? 😎",
            "Main ghar pe hoon bhai, tum kahaan? 🏠",
            "Abhi thodi der ke liye bahar gaya hoon bhai! 😅",
            "Yahin hoon bhai, ghar pe chill kar raha hoon! 😁"
        ]
        return random.choice(replies)

    elif "kya kar rhe ho" in user_text:
        replies = [
            "Bas kaam kar raha hoon, tum kya kar rahe ho? 💻",
            "Thoda chill kar raha hoon, tum batao? 😎",
            "Abhi kaam kar raha hoon, baad mein milte hain! 😌",
            "Bas apne kaam mein busy hoon, kya chal raha hai tumhare saath? 🤔"
        ]
        return random.choice(replies)

    elif "Soome ka time mhi huwa kya" in user_text:
        replies = [
            "Haha, abhi toh nahi, lekin thodi der mein soch raha hoon 😅",
            "Soch raha hoon bhai, thodi der mein so jaunga! 🛏️",
            "Abhi nahi, lekin bahut thakan ho gayi hai! 😴",
            "Soome ka time toh ho gaya hai bhai, bas phone thoda chal raha hai abhi! 😆"
        ]
        return random.choice(replies)

    elif "bye" in user_text:
        replies = [
            "Bye bhai, milte hain fir! 👋",
            "Chalo bhai, phir milenge! Take care! 😎",
            "Bye bhai, mast rehna! 👋",
            "Alvida bhai! Phir milenge! ✌️"
        ]
        return random.choice(replies)

    elif "kya scene hai" in user_text:
        replies = [
            "Scene mast hai bhai, sab chill chal raha hai! 😎",
            "Kuch khaas nahi, bas chill ho raha hai! Tum kya kar rahe ho? 😄",
            "Scene toh normal hai bhai, tu bata, kya chal raha hai? 😏"
        ]
        return random.choice(replies)

    elif "pyaar" in user_text or "love" in user_text:
        replies = [
            "Pyaar toh sabhi ko hona chahiye, bhai! 😅",
            "Pyaar mein toh sabhi ka dil dhadak raha hota hai! ❤️",
            "Love? Sabko apni family aur doston se pyaar karna chahiye! 💕"
        ]
        return random.choice(replies)

    elif "joke" in user_text or "funny" in user_text:
        replies = [
            "Ek baar ek aadmi ne bola 'mujhe joke chahiye', main bola, 'tu mujhse baat kar raha hai na?' 😂",
            "Mujhe ek joke yaad aaya, 'Mujhe apni pichli life ki yaadein chahiye', 'Kyun?' 'Aapne mujhe 1,000 baar block kiya tha!' 😜"
        ]
        return random.choice(replies)

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
