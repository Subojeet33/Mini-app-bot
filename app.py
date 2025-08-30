from flask import Flask
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

import os

TOKEN = "8314570135:AAHBjTgv50EDp6NAd9BdARZa3NaTN_zEq8U"

app = Flask(__name__)

# Flask route (for testing)
@app.route('/')
def home():
    return "Bot is running on Render!"

# Telegram bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton("🚀 Open Mini App", web_app={"url": "https://your-app.onrender.com/webapp"})]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Welcome! Click below to open Mini App:", reply_markup=reply_markup)

def run_bot():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    run_bot()
