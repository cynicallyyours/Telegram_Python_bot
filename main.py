import Constants as keys
from telegram.ext import *
import Responses as R
import pandas as pd
import sqlite3
from datetime import date


print("Bot started...")

def start_command(update, context):
	update.message.reply_text('Type something random to get started!')

def help_command(update, context):
	update.message.reply_text('I am Chembl Bot and I will help answer your questions! For each trade name, you can look at the details. To list the Trade names of drugs, type: Show me the list of Trade names')



def handle_message(update, context):
	text = str(update.message.text).lower()
	response = R.sample_responses(text)
	response = str(response)
	print(len(response))

	update.message.reply_text(response) 

def error(update, context):
	print(f"Update {update} caused error {context.error}")


def main():
	updater = Updater(keys.API_KEY, use_context=True)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start_command))
	dp.add_handler(CommandHandler("help", help_command))

	dp.add_handler(MessageHandler(Filters.text, handle_message))

	dp.add_error_handler(error)


	updater.start_polling()
	updater.idle()

main()