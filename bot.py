import os
import requests
from telegram import Update,InlineKeyboardMarkup,InlineKeyboardButton
from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler,
    CallbackQueryHandler
)

TOKEN = os.environ['TOKEN']

like = 0
dislike = 0

def start(udpate: Update, context: CallbackContext):
    keyboard = [['Vote']]
    Update.message.reply_text('Please,press the button')