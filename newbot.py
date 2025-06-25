"""
Simple Bot to reply to Telegram messages.
"""
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from torch_chatbot import chat

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text('Hi! I am MiniBuzz, your IIT Mandi assistant. Ask me anything!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = """
🤖 *MiniBuzz - IIT Mandi Assistant*

I can help you with:
• General queries about IIT Mandi
• Hostel and campus information
• Academic questions
• Programming and coding help
• Fun conversations!

Just type your question and I'll do my best to help!
    """
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Process user message through chatbot."""
    user_message = update.message.text
    bot_response = chat(user_message)
    await update.message.reply_text(bot_response)

def main():
    """Start the bot."""
    # Replace with your new bot token from BotFather
    BOT_TOKEN = ""
    
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    # Register message handler for regular text
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # Start the Bot
    print("Bot is starting...")
    application.run_polling()

if __name__ == '__main__':
    main()