from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler
from const import TOKEN
from func import *
from const import *

u=Updater(token=TOKEN, workers=4)
d=u.dispatcher
d.add_handler(CommandHandler('start',callback=start,run_async=True))
d.add_handler(MessageHandler(Filters.contact,get_contact,run_async=True))
d.add_handler(MessageHandler(Filters.text,callback=text_answer, run_async=True))


u.start_polling()