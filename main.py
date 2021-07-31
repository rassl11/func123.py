from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler
from const import TOKEN
from func import *

u=Updater(token=TOKEN, workers=4)
d=u.dispatcher
d.add_handler(CommandHandler('start',callback=start))
d.add_handler(MessageHandler(Filters.contact,get_contact))
d.add_handler(MessageHandler(Filters.text,callback=text_answer, run_async=True))

u.start_polling()