from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Your bot token
TOKEN = "7757214401:AAFljkm-PdmfjtY10sd8e-pd6ENhRM97cVM"

# Command Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Welcome to SreeBot.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
        Here are the commands you can use:
        /start -> Welcome message
        /help -> Display this help message
        /content -> Information about playlists
        /Python -> Link to Python tutorials
        /Java -> Link to Java tutorials
        /SQL -> Link to SQL tutorials
        /contact -> Contact information
        /quote -> Receive a random motivational quote
        /joke -> Get a random joke
        """
    )

async def content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("We have various playlists and articles available on multiple topics!")

async def python(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Python tutorial link: https://www.youtube.com/watch?v=OLPbd-7Pp_8&list=PLqM7alHXFySHLJWu_Euw7pdI4ec1hHTLI")

async def java(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Java tutorial link: https://www.youtube.com/watch?v=lcJzw0JGfeE&list=PLqM7alHXFySENpNgw27MzGxLzNJuC_Kdj")

async def sql(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("SQL tutorial link: https://www.youtube.com/watch?v=cdq10dQs8ys&list=PLG5KvF1OpdCWTMMI3BMYdIuoOq_MTjB4M")

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You can contact us at support@persistventures.com or visit our website for more information.")

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quotes = [
        "Believe in yourself and all that you are.",
        "The best way to predict the future is to create it.",
        "Success is not the key to happiness. Happiness is the key to success.",
        "Don't watch the clock; do what it does. Keep going."
    ]
    import random
    await update.message.reply_text(random.choice(quotes))

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]
    import random
    await update.message.reply_text(random.choice(jokes))

# General Chat Handler
async def general_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()
    if any(greeting in user_message for greeting in ["hi", "hello", "hey", "good morning", "good evening", "how are you"]):
        await update.message.reply_text("Hello! How can I assist you today?")
    elif "thank you" in user_message or "thanks" in user_message:
        await update.message.reply_text("You're welcome! Let me know if you need further assistance.")
    elif "bye" in user_message or "goodbye" in user_message:
        await update.message.reply_text("Goodbye! Have a great day!")
    else:
        await update.message.reply_text("I'm here to help! You can ask me anything or use /help to see available commands.")

# Main function to initialize the bot
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Command Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("content", content))
    app.add_handler(CommandHandler("Python", python))
    app.add_handler(CommandHandler("Java", java))
    app.add_handler(CommandHandler("SQL", sql))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(CommandHandler("quote", quote))
    app.add_handler(CommandHandler("joke", joke))

    # General Chat Handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, general_chat))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
