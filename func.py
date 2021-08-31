import concurrent.futures
import time
from datetime import datetime

from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from const import *
from sql_req import *
import sqlite3

regina = 1780047686

def checking(update,context):
    user_id = update.message.chat_id
    start_hour = '12'
    start_minute = '00'
    end_hour = '14'
    end_minute = '00'
    start_time = int(start_hour) * 60 + int(start_minute)
    end_time = int(end_hour) * 60 + int(end_minute)
    current_time = datetime.now().hour * 60 + datetime.now().minute
    print(current_time)
    if start_time <= current_time and end_time >= current_time:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cur.execute(update_stage_in.format(251, user_id))
        cena = cur.execute(cost.format('Бизнес перекур')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + 'Бизнес перекур' + '-' + str(cena) + '\n' + '\n' + '*Модификаторы кальяна*: '
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text="Какой крепости кальян желаете?",
                                 reply_markup=ReplyKeyboardMarkup([rare, easy], parse_mode='Markdown',
                                                                  resize_keyboard=True))
    else:
        context.bot.send_message(chat_id=user_id, text='Бизнес перекур действует только с 12:00 до 14:00')




def start(update,context):
    conn = sqlite3.connect('identifier.sqlite')
    cur = conn.cursor()

    user_id = update.message.chat_id
    name = update.message.from_user.first_name
    conn = sqlite3.connect('identifier.sqlite')
    cur = conn.cursor()
    cur.execute(update_stage_in.format(1001,user_id))
    id_in = cur.execute(id_in_table.format(user_id)).fetchall()
    print(id_in)
    conn.commit()


    try:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        id_in = id_in[0][0]
        context.bot.send_message(text="{} Добро пожаловать в Timekeeper Service Bot, Выбери свой стол".format(name), chat_id=user_id)
    except IndexError:
        cur.execute(first_insert.format(user_id, name))
        context.bot.send_message(text="{} Добро пожаловать в Timekeeper Service Bot, Отправь свой номер телефона📱".format(name), chat_id=user_id,reply_markup=ReplyKeyboardMarkup([phone],
                                                                  resize_keyboard=True,one_time_keyboard=True))

        conn.commit()


def get_contact(update,context):
    num = update.message.contact.phone_number
    user_id = update.message.chat_id
    text = update.message.text
    conn = sqlite3.connect('identifier.sqlite')
    cur = conn.cursor()
    cur.execute(update_phone_no.format(num,user_id))
    cur.execute(update_stage_in.format(998,user_id))
    conn.commit()
    context.bot.send_message(chat_id = user_id, text = 'Отлично,теперь введите Фамилию и Имя в формате : Ф.И')


def text_answer(update,context):

    user_id = update.message.chat_id
    name = update.message.from_user.first_name
    text = update.message.text
    message_id = update.message.message_id

    conn = sqlite3.connect('identifier.sqlite')
    cur = conn.cursor()
    rasul = 44335784
    mashhur = 1561567583
    maksim = 136254696
    jenya = 1737226541
    ilnur = 653135443
    stas = 1561453505
    nigina = 246886708
    vlad = 1319090684
    timur = 34824365
    ulugbek = 1207448934

    stage = cur.execute(stage_in.format(user_id)).fetchall()
    stage = stage[0][0]
    allowed_tables = ['100','101','102','103','104','200','201','202','203','204','300','301','302','303','1998','106','107','108','11','12','13','14','1','2','3','4','5','6','7','8','9','10']


    if stage == 998:
        cur.execute(update_table_number.format(text, user_id))
        cur.execute(update_stage_in.format(1001,user_id))
        cur.execute(first_name.format(text, user_id))
        context.bot.send_message(chat_id = user_id, text = 'Отлично,теперь введите номер стола')

    elif text.isdigit() and text in allowed_tables and stage ==1001:
        cur.execute(update_table_number.format(text, user_id))
        cur.execute(update_stage_in.format(1001,user_id))
        a = cur.execute(table_number_in_table.format(user_id)).fetchall()
        # context.bot.send_message(chat_id = user_id,text = 'Прекрасного времени провождения😊',
        #                          reply_markup = ReplyKeyboardMarkup([top_button,bot_button,mid_button,order_button],resize_keyboard=True))

#         if a[0][0] == 100 or a[0][0] == 101 or a[0][0] == 102 or a[0][0] == 103 or a[0][0] == 104 or a[0][0] == 105 or \
#                 a[0][0] == 106 or a[0][0] == 107 or a[0][0] == 108:
#             cur.execute(update_stage_in.format(999, user_id))
#             context.bot.send_message(chat_id=user_id,
#                                      text='''Приветствую, меня зовут Рамиль и сегодня я буду вашим Таймгардом!💚
# Остановим время вместе😊''', reply_markup=ReplyKeyboardMarkup([top_button,bot_button,mid_button,order_button],
#                                                                       resize_keyboard=True))
#
#
#         elif a[0][0] == 11 or a[0][0] == 6 or a[0][0] == 1 or a[0][0] == 12 or a[0][0] == 7 or a[0][0] == 2 or a[0][
#             0] == 3:
#             cur.execute(update_stage_in.format(999, user_id))
#             context.bot.send_message(chat_id=user_id,
#                                      text='''Приветствую, меня зовут Ильнур и сегодня я буду вашим Таймгардом!💚
# Остановим время вместе😊''', reply_markup=ReplyKeyboardMarkup([top_button,bot_button,mid_button,order_button],
#                                                                       resize_keyboard=True))
#
#         else:

        context.bot.send_photo(chat_id=user_id,photo = ('https://ibb.co/pXGV1pr'),
                                     caption='''Приветствую, меня зовут Ильнур и сегодня я буду вашим Таймгардом!💚
Остановим время вместе😊''', reply_markup=ReplyKeyboardMarkup([top_button,bot_button,mid_button,order_button],
                                                                      resize_keyboard=True))


    elif text == 'Сделать заказ✍' and stage == 1001:
        context.bot.send_photo(chat_id = user_id,photo = ('https://ibb.co/ZWYrs1c'),caption = 'Прошу Вас, наше меню')
        context.bot.send_message(chat_id = user_id,text = 'С чего начнем😊?',
                               reply_markup = ReplyKeyboardMarkup([deserti_shisha,soups_hot,pasta_fasfood,salad_garnir,cool_hot,coffee,zakus_alco,back_korzina],resize_keyboard=True))

    elif text == '⏪Назад' and stage == 1001:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        context.bot.send_message(chat_id = user_id,text = 'Продолжим?😉',
                                 reply_markup = ReplyKeyboardMarkup([top_button,bot_button,mid_button,order_button],resize_keyboard=True))

#все про кальяны

    elif text == 'Кальян💨':

        cur.execute(update_stage_in.format(2000, user_id))
        context.bot.send_message(chat_id = user_id,text = 'Категории',reply_markup = ReplyKeyboardMarkup([celiy,biznes,back],resize_keyboard=True))

    elif text == '⏪Назад' and stage == 2000:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(1001, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😜',
                                 reply_markup=ReplyKeyboardMarkup([deserti_shisha,soups_hot,pasta_fasfood,salad_garnir,cool_hot,coffee,zakus_alco,back_korzina], resize_keyboard=True))


    elif text == 'Бизнес перекур':
        checking(update,context)

    elif text == '⏪Назад' and stage == 251:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz[0:-47]
        cena = cur.execute(cost.format('Бизнес перекур')).fetchall()
        cena = cena[0][0]
        price = cur.execute(set_total_price.format(user_id)).fetchall()
        price = price[0][0]
        cur.execute(update_total_price.format(price - cena, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id))
        cur.execute(update_stage_in.format(1001, user_id))

        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [deserti_shisha, soups_hot, pasta_fasfood, salad_garnir, cool_hot, coffee,
                                      zakus_alco, back_korzina],
                                     resize_keyboard=True))


    elif text == 'Кaльян':# a - eng
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cur.execute(update_stage_in.format(200, user_id))
        cena = cur.execute(cost.format('Кaльян')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + 'Кaльян' + '-' + str(cena) + '\n' + '\n' + '*Модификаторы кальяна*: '
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text="Какой крепости кальян желаете?",
                                 reply_markup=ReplyKeyboardMarkup([rare,easy],parse_mode = 'Markdown', resize_keyboard=True))

    elif text == '⏪Назад' and stage == 200:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz[0:-46]
        cena = cur.execute(cost.format('Целый Кальян')).fetchall()
        cena = cena[0][0]
        price = cur.execute(set_total_price.format(user_id)).fetchall()
        price = price[0][0]
        cur.execute(update_total_price.format(price - cena, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id))
        cur.execute(update_stage_in.format(1001, user_id))

        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [deserti_shisha, soups_hot, pasta_fasfood, salad_garnir, cool_hot, coffee,
                                      zakus_alco, back_korzina],
                                     resize_keyboard=True))

    elif text == 'Замена чаши':
        zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        if 'Целый Кальян' in zakaz:
            conn = sqlite3.connect('identifier.sqlite')
            cur = conn.cursor()
            zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
            zakaz = zakaz[0][0]
            print(zakaz)
            cur.execute(update_stage_in.format(250, user_id))
            cena = cur.execute(cost.format('Замена чаши')).fetchall()
            cena = cena[0][0]
            zakaz = zakaz + '\n' + 'Замена чаши' + '-' + str(cena) + '\n' + '\n' + '*Модификаторы кальяна*: '
            cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
            itog = cur.execute(set_total_price.format(user_id)).fetchall()
            itog = itog[0][0]
            itog = itog + cena

            cur.execute(update_total_price.format(itog, user_id))
            context.bot.send_message(chat_id=user_id, text="Какой крепости кальян желаете?",
                                     reply_markup=ReplyKeyboardMarkup([rare, easy], parse_mode='Markdown',
                                                                      resize_keyboard=True))
        else:
            context.bot.send_message(chat_id = user_id,text = 'Для начала вы должны заказать целый кальян и скурить его,прежде чем заказывать замену чаши!')




    elif text == '⏪Назад' and stage == 250:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz[0:-44]
        cena = cur.execute(cost.format('Замена чаши')).fetchall()
        cena = cena[0][0]
        price = cur.execute(set_total_price.format(user_id)).fetchall()
        price = price[0][0]
        cur.execute(update_total_price.format(price - cena,user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id))
        cur.execute(update_stage_in.format(1001,user_id))

        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([deserti_shisha,soups_hot,pasta_fasfood,salad_garnir,cool_hot,coffee,zakus_alco,back_korzina],
                                                                  resize_keyboard=True))

    elif (text =='Легкий⏬' or text == 'Средний➡' or text == 'Крепкий⏫') and (stage == 200 or stage == 250 or stage ==251):
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(201, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]


        zakaz = zakaz + '\n' + text[:-1]


        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        context.bot.send_message(chat_id = user_id,text = 'Что по вкусам?',
                                 reply_markup = ReplyKeyboardMarkup([berry,citrus,back],resize_keyboard=True))

    elif text == '⏪Назад' and stage == 201:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz[0:-8]


        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        cur.execute(update_stage_in.format(200, user_id))
        a = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        context.bot.send_message(chat_id=user_id, text='Какой крепости кальян',
                                 reply_markup=ReplyKeyboardMarkup([rare,easy],resize_keyboard=True))


    elif text == 'Ягодный   🍓' or text == 'Фруктовый 🍊' or text == 'Цитрусовый🍋' or text =='Десертный 🍪':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(202, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        zakaz = zakaz + '\n' + text[:-1]



        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        context.bot.send_message(chat_id=user_id, text='Тип курения?',
                                 reply_markup=ReplyKeyboardMarkup([folga,back], resize_keyboard=True))


    elif text == '⏪Назад' and stage == 202:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz[0:-11]


        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        cur.execute(update_stage_in.format(201, user_id))
        context.bot.send_message(chat_id=user_id, text='Что по вкусам?',
                                 reply_markup = ReplyKeyboardMarkup([berry,citrus,back],resize_keyboard=True))



    elif text == 'Калауд' or text == 'Фольга':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(203, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz + '\n' + text
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        context.bot.send_message(chat_id = user_id,text = 'С холодком или без?',reply_markup = ReplyKeyboardMarkup([ice,back],resize_keyboard=True))


    elif text == '⏪Назад' and stage == 203:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz[0:-7]
        cur.execute(sql_set_zakaz.format(zakaz,user_id)).fetchall()
        cur.execute(update_stage_in.format(202, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup = ReplyKeyboardMarkup([folga,back],resize_keyboard=True))



    elif text == 'С холодком ❄' or text == 'Без Холодка💥':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(204, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]


        zakaz = zakaz + '\n' + text[:-1]



        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        context.bot.send_message(chat_id=user_id, text='''Желаете оставить комментарий к Кальяну?🧐
Пример : Без персика''',
                                 reply_markup=ReplyKeyboardMarkup([commentariy, back],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 204:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(203, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        zakaz = zakaz[0:-12]


        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        context.bot.send_message(chat_id=user_id, text='С холодком или без?',
                                 reply_markup = ReplyKeyboardMarkup([ice,back],resize_keyboard=True))

    elif text !='Пропустить⏩' and stage == 204:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        x = cur.execute(update_comment.format(text,user_id))
        cur.execute(update_stage_in.format(205, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в заказ?',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text =='Пропустить⏩' and stage == 204:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(205, user_id))
        context.bot.send_message(chat_id = user_id, text ='Добавить в заказ?',reply_markup=ReplyKeyboardMarkup([add_zakaz,back_korzina],resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 205:

        context.bot.send_message(chat_id = user_id, text = 'Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([deserti_shisha,soups_hot,pasta_fasfood,salad_garnir,cool_hot,coffee,zakus_alco,back_korzina],
                                                                  resize_keyboard=True))





# всепро кухню

#ВСЕ ПРО СУПЫ

    elif text == 'Супы🍜':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(2, user_id))
        context.bot.send_message(chat_id = user_id,text ='Что-нибудь легкое?😉',
                                 reply_markup = ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava,back_korzina],resize_keyboard=True))

    elif text == '⏪Назад' and stage ==2:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(1, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([deserti_shisha,soups_hot,pasta_fasfood,salad_garnir,cool_hot,coffee,zakus_alco,back_korzina],
                                                                  resize_keyboard=True))


    elif text == 'Окрошка' and stage == 2:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(3, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_photo(photo = ('https://ibb.co/tzHFGG1'),chat_id= user_id,caption='''*Окрошка*
        
*Цена:* {}💵'''.format(b),parse_mode = 'Markdown',reply_markup=ReplyKeyboardMarkup([add_zakaz,back_korzina],resize_keyboard=True))


    elif text == '⏪Назад' and stage ==3:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(2, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 3:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(2, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Окрошка')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + 'Окрошка' + ' - ' + str(cena)  + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))


        conn.commit()

        context.bot.send_message(chat_id = user_id,text = 'Окрошка добавлена  в заказ'.format(text),
                                 reply_markup = ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava,back_korzina],resize_keyboard=True))



    elif text == 'Кук-си' and stage == 2:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(5, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage ==5:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(2, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava,back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 5:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cur.execute(update_stage_in.format(2, user_id))
        cena = cur.execute(cost.format('Кук-си')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Кук-си' + ' - ' + str(cena)  + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))


        context.bot.send_message(chat_id=user_id, text='Кук-си добавлена  в заказ'.format(text),reply_markup = ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava,back_korzina],resize_keyboard=True))



    elif text =='Рамен' and stage == 2:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(7, user_id))

        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_photo(photo=('https://ibb.co/dWSpDVT'), chat_id=user_id, caption='''*Рамен*
        
*Цена:* {}💵

Какую остроту желаете?'''.format(b),parse_mode = 'Markdown',reply_markup=ReplyKeyboardMarkup([neostr,ostr,back],resize_keyboard=True))

    elif text == '⏪Назад' and stage ==7:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(2, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava,back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Неострый❗':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(460, user_id))
        context.bot.send_message(chat_id = user_id, text = 'Отличный выбор😝',reply_markup=ReplyKeyboardMarkup([add_zakaz,back_korzina],resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 460:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cur.execute(update_stage_in.format(2, user_id))
        cena = cur.execute(cost.format('Рамен')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = '\n' + 'Рамен' + ' - ' + str(cena) + '\n' + 'Острота : Неострый' +zakaz



        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id = user_id,text = 'Рамен добавлен в заказ'.format(text),reply_markup = ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava,back_korzina],resize_keyboard=True))


    elif text == 'Средней остроты🌶':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(461, user_id))
        context.bot.send_message(chat_id = user_id, text = 'Отличный выбор😝',reply_markup=ReplyKeyboardMarkup([add_zakaz,back_korzina],resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 461:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cur.execute(update_stage_in.format(2, user_id))
        cena = cur.execute(cost.format('Рамен')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz =  '\n' + 'Рамен' + ' - ' + str(cena) + '\n' + 'Острота : Средней остроты' + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id = user_id,text = 'Рамен добавлен в заказ'.format(text),reply_markup = ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava,back_korzina],resize_keyboard=True))


    elif text == 'Острый🌶🌶':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(462, user_id))
        context.bot.send_message(chat_id = user_id, text = 'Отличный выбор😝',reply_markup=ReplyKeyboardMarkup([add_zakaz,back_korzina],resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 462:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cur.execute(update_stage_in.format(2, user_id))
        cena = cur.execute(cost.format('Рамен')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = '\n' + 'Рамен' + ' - ' + str(cena) + '\n' + 'Острота : Острый' + zakaz


        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id = user_id,text = 'Рамен добавлен в заказ'.format(text),reply_markup = ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava,back_korzina],resize_keyboard=True))




    elif text =='Мастава' and stage == 2:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(8, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/KVpNqfn'), chat_id=user_id, caption='''*Мастава*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text == '⏪Назад' and stage ==8:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(2, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava,back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 8:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(2, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cena = cur.execute(cost.format('Мастава')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + 'Мастава' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        context.bot.send_message(chat_id = user_id,text = 'Мастава добавлена в заказ'.format(text),reply_markup = ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava,back_korzina],resize_keyboard=True))


#ВСЕ ПРО ГОРЯЧЕЕ

    elif text == 'Вторые блюда🍲':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Насытимся😉',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))
    elif text == '⏪Назад' and stage==10:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(1, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([deserti_shisha,soups_hot,pasta_fasfood,salad_garnir,cool_hot,coffee,zakus_alco,back_korzina],
                                                                  resize_keyboard=True))
    elif text == 'Рибай стейк':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(310, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/F5xn2PT'), chat_id=user_id, caption='''*Рибай стейк*

*Цена:* {}💵
        
Какую степень прожарки желаете?🔥'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([medium_proj,well_done,back], resize_keyboard=True))

    elif text == '⏪Назад' and stage==310:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))


    elif text == 'Medium🔥' and stage == 310:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(311, user_id))
        context.bot.send_message(chat_id=user_id, text='Отличный выбор😝',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 311:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()

        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Рибай стейк')).fetchall()
        cena = cena[0][0]
        cur.execute(update_stage_in.format(10, user_id))
        zakaz = '\n' + 'Рибай стейк' + ' - ' + str(cena) + '\n' + 'ПРОЖАРКА : Медиум' + zakaz



        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena



        cur.execute(update_total_price.format(itog, user_id))

        context.bot.send_message(chat_id = user_id,text = 'Рибай стейк добавлен в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))


    elif text == 'Medium-Well🔥🔥':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(312, user_id))
        context.bot.send_message(chat_id=user_id, text='Отличный выбор😝',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 312:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Рибай стейк')).fetchall()
        cena = cena[0][0]
        cur.execute(update_stage_in.format(10, user_id))
        zakaz = '\n' + 'Рибай стейк' + ' - ' + str(cena) + '\n' + 'ПРОЖАРКА : Медиум-Велл' + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        context.bot.send_message(chat_id = user_id,text = 'Рибай стейк добавлен в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))


    elif text == 'Well-done🔥🔥🔥':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(312, user_id))
        context.bot.send_message(chat_id=user_id, text='Отличный выбор😝',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 312:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Рибай стейк')).fetchall()
        cena = cena[0][0]
        cur.execute(update_stage_in.format(10, user_id))
        zakaz = '\n' + 'Рибай стейк' + ' - ' + str(cena) + '\n' + 'ПРОЖАРКА : Вэл Дан' + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        context.bot.send_message(chat_id = user_id,text = 'Рибай стейк добавлен в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 11:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))







    elif text == 'Медальоны':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(12, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/sJThBFf'), chat_id=user_id, caption='''*Медальоны*

*Цена:* {}💵

Какую степень прожарки желаете?🔥'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 12:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))

    elif text == 'Medium🔥':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(300, user_id))
        context.bot.send_message(chat_id=user_id, text='Отличный выбор😝',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 300:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()

        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Медальоны')).fetchall()
        cena = cena[0][0]
        cur.execute(update_stage_in.format(10, user_id))
        zakaz = '\n' + 'Медальоны' + ' - ' + str(cena) + '\n' + 'ПРОЖАРКА : Медиум' + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        context.bot.send_message(chat_id = user_id,text = 'Медальоны добавлены в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))


    elif text == 'Medium-Well🔥🔥':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(301, user_id))
        context.bot.send_message(chat_id=user_id, text='Отличный выбор😝',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 301:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Медальоны')).fetchall()
        cena = cena[0][0]
        cur.execute(update_stage_in.format(10, user_id))
        zakaz = '\n' + 'Медальоны' + ' - ' + str(cena) + '\n' + 'ПРОЖАРКА : Медиум-Велл' + zakaz



        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        context.bot.send_message(chat_id = user_id,text = 'Медальоны добавлены в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))


    elif text == 'Well-done🔥🔥🔥':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(302, user_id))
        context.bot.send_message(chat_id=user_id, text='Отличный выбор😝',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 302:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Медальоны')).fetchall()
        cena = cena[0][0]
        cur.execute(update_stage_in.format(10, user_id))
        zakaz = '\n' + 'Медальоны' + ' - ' + str(cena) + '\n' + 'ПРОЖАРКА : Вэл Дан' + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        context.bot.send_message(chat_id = user_id,text = 'Медальоны добавлены в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))







    elif text == 'Говядина в сливочном соусе':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(13, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/bgPqFML'), chat_id=user_id, caption='''*Говядина в сливочном соусе*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 13:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Говядина в сливочном соусе')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = '\n' + 'Говядина в сливочном соусе' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id = user_id,text = 'Говядина в сливочном соусе добавлена в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))




    elif text == '⏪Назад' and stage == 13:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))
    elif text == 'Курица на гриле':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(14, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/HHRqKmY'), chat_id=user_id, caption='''*Курица на гриле*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 14:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Курица на гриле')).fetchall()
        cena = cena[0][0]
        print(cena)
        cur.execute(update_stage_in.format(10, user_id))
        zakaz = '\n' + 'Курица на гриле' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id = user_id,text = 'Курица на гриле добавлена в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 14:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))
    elif text == 'Картошка по-домашнему':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(15, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/QYtCkKT'), chat_id=user_id, caption='''*Картошка по-домашнему*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 15:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Картошка по-домашнему')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Картошка по-домашнему' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id = user_id,text = 'Картошка по-домашнему добавлена в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 15:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))
    elif text == 'Мясо по-китайски':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(16, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/hRPXcym'), chat_id=user_id, caption='''*Мясо по-китайски*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 16:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Мясо по-китайски')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = '\n' + 'Мясо по-китайски' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id = user_id,text = 'Мясо по-китайский добавлена в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 16:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))

    elif text == 'Стейк куриный':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(17, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/9GhjWXY'), chat_id=user_id, caption='''*Стейк куриный*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 17:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Стейк куриный')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = '\n' + 'Стейк куриный' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id = user_id,text = 'Стейк куриный добавлен в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 17:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                     resize_keyboard=True))


#ВСЕ ПРО ПАСТЫ

    elif text=='Пасты🍝':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(20, user_id))
        context.bot.send_message(chat_id=user_id, text='Насытимся😉',
                                reply_markup=ReplyKeyboardMarkup([alfredo_boloneze,back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 20:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(1, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [deserti_shisha,soups_hot,pasta_fasfood,salad_garnir,cool_hot,coffee,zakus_alco,back_korzina],
                                     resize_keyboard=True))

    elif text =='Альфредо':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(21, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/KDQTMpS'), chat_id=user_id, caption='''*Альфредо*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 21:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(20, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Альфредо')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = '\n' + 'Альфредо' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id = user_id,text = 'Альфредо добавлено в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([alfredo_boloneze,back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 21:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(20, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([alfredo_boloneze,back_korzina],resize_keyboard=True))

    elif text =='Болоньезе':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(22, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/cYDD7sQ'), chat_id=user_id, caption='''*Болоньезе*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 22:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(20, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Болоньезе')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = '\n' + 'Болоньезе' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id = user_id,text = 'Болоньезе добавлено в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([alfredo_boloneze,back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 22:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(20, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([alfredo_boloneze,back_korzina],resize_keyboard=True))

#ВСЕ ПРО ФАСТ-ФУД

    elif text =='Фаст-Фуд🥪':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(30, user_id))
        context.bot.send_message(chat_id=user_id, text='Покушаем😉',
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,back_korzina],resize_keyboard=True))

    elif text == '⏪Назад' and stage == 30:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(1, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [deserti_shisha,soups_hot,pasta_fasfood,salad_garnir,cool_hot,coffee,zakus_alco,back_korzina],
                                     resize_keyboard=True))

    elif text =='Буррито':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(31, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/7SQHmvM'), chat_id=user_id, caption='''*Буррито*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 31:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(30, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Буррито')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = '\n' + 'Буррито' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Буррито добавлено в заказ',
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,back_korzina],resize_keyboard=True))

    elif text == '⏪Назад' and stage == 31:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(30, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,back_korzina],
                                                                  resize_keyboard=True))

    elif text =='Наггетсы':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(32, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/HzX8yMD'), chat_id=user_id, caption='''*Наггетсы*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 32:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(30, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Наггетсы')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Наггетсы' + ' - ' + str(cena) + zakaz


        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Наггетсы добавлены в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,back_korzina],resize_keyboard=True))


    elif text == '⏪Назад' and stage == 32:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(30, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,back_korzina],
                                                                  resize_keyboard=True))


    elif text =='Гарлики':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(33, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 33:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(30, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Гарлики')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = '\n' + 'Гарлики' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Гарлики добавлены в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,back_korzina],resize_keyboard=True))


    elif text == '⏪Назад' and stage == 33:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(30, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [burrito_sandwich, nuggets_garlic, back_korzina],
                                     resize_keyboard=True))
    elif text =='Куриный сэндвич':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(34, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/vhB2kpH'), chat_id=user_id, caption='''*Куриный Сэндвич*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 34:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(30, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Куриный сэндвич')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = '\n' + 'Куриный сэндвич' + ' - ' + str(cena) + zakaz
        print(zakaz)

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Куриный сэндвич добавлен в заказ',
                                 reply_markup = ReplyKeyboardMarkup([burrito_sandwich, nuggets_garlic, back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 34:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(30, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',reply_markup = ReplyKeyboardMarkup([burrito_sandwich, nuggets_garlic, back_korzina], resize_keyboard=True))

#ВСЕ ПРО САЛАТЫ

    elif text == 'Салаты🥗':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(40, user_id))
        context.bot.send_message(chat_id=user_id, text='Перекусим?😝',
                                 reply_markup=ReplyKeyboardMarkup([greek_achik,back_korzina],
                                                                  resize_keyboard=True))

    elif text == '⏪Назад' and stage == 40:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(1, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup = ReplyKeyboardMarkup([deserti_shisha,soups_hot,pasta_fasfood,salad_garnir,cool_hot,coffee,zakus_alco,back_korzina], resize_keyboard=True))

    elif text == 'Греческий салат':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(41, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/0C5q941'), chat_id=user_id, caption='''*Греческий салат*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 41:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(40, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Греческий салат')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = '\n' + 'Греческий салат' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Греческий салат добавлен в заказ'.format(text),
                                 reply_markup = ReplyKeyboardMarkup([greek_achik,back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 41:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(40, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup = ReplyKeyboardMarkup([greek_achik,back_korzina], resize_keyboard=True))

    elif text == 'Ачик-чучук':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(42, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/1GFk2Kv'), chat_id=user_id, caption='''*Ачик-чучук*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 42:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(40, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Ачик-чучук')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Ачик-чучук' + ' - ' + str(cena) + zakaz
        print(zakaz)

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Ачик-чучук добавлен в заказ'.format(text),
                                 reply_markup = ReplyKeyboardMarkup([greek_achik,back_korzina], resize_keyboard=True))


    elif text == '⏪Назад' and stage == 42:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(40, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup = ReplyKeyboardMarkup([greek_achik,back_korzina], resize_keyboard=True))

#ВСЕ ПРО ГАРНИРЫ

    elif text=='Гарниры🍟':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(50, user_id))
        context.bot.send_message(chat_id=user_id, text='Закуски😋',
                                 reply_markup=ReplyKeyboardMarkup([aydaho_back,grilveg_fries,ris_derev,back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage ==50:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(1, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',reply_markup=ReplyKeyboardMarkup(
                                     [deserti_shisha,soups_hot,pasta_fasfood,salad_garnir,cool_hot,coffee,zakus_alco,back_korzina], resize_keyboard=True))

    elif text=='Овощи на грилле':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(51, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 51:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(50, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Овощи на гриле')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = '\n' + 'Овощи на гриле' + ' - ' + str(cena) + zakaz


        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Овощи на гриле добавлены в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([aydaho_back,grilveg_fries,ris_derev,back_korzina], resize_keyboard=True))


    elif text == '⏪Назад' and stage ==51:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(50, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',reply_markup=ReplyKeyboardMarkup([aydaho_back,grilveg_fries,ris_derev,back_korzina],
                                                                  resize_keyboard=True))


    elif text=='Картофель по-деревенски':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(52, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵
        
Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 52:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(50, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Картофель по-деревенски')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = '\n' + 'Картофель по-деревенски' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Картофель по-деревенски добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([aydaho_back,grilveg_fries,ris_derev,back_korzina], resize_keyboard=True))




    elif text == '⏪Назад' and stage ==52:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(50, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',reply_markup=ReplyKeyboardMarkup([aydaho_back,grilveg_fries,ris_derev,back_korzina],
                                                                  resize_keyboard=True))


    elif text=='Рис':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(53, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 53:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(50, user_id))

        cena = cur.execute(cost.format('Рис')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Рис' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Рис добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([aydaho_back,grilveg_fries,ris_derev,back_korzina], resize_keyboard=True))


    elif text == '⏪Назад' and stage ==53:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(50, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',reply_markup=ReplyKeyboardMarkup([aydaho_back,grilveg_fries,ris_derev,back_korzina],
                                                                  resize_keyboard=True))

    elif text=='Фри':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(54, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 54:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(50, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Фри')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Фри' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Фри добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([aydaho_back,grilveg_fries,ris_derev,back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage ==54:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(50, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши гарниры',reply_markup=ReplyKeyboardMarkup([aydaho_back,grilveg_fries,ris_derev,back_korzina],
                                                                  resize_keyboard=True))



    elif text=='Картофель айдахо':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(55, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 55:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(50, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Картофель айдахо')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Картофель айдахо' + ' - ' + str(cena) + zakaz


        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Картофель айдахо добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([aydaho_back,grilveg_fries,ris_derev,back_korzina], resize_keyboard=True))


    elif text == '⏪Назад' and stage ==55:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(50, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',reply_markup=ReplyKeyboardMarkup([aydaho_back,grilveg_fries,ris_derev,back_korzina],
                                                                  resize_keyboard=True))

#ВСЕ ПРО ДЕСЕРТЫ

    elif text=='Десерты🍰':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(60, user_id))
        context.bot.send_message(chat_id=user_id, text='Что-нибудь сладкое?😋',
                                 reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back,korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage ==60:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(1001, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',reply_markup=ReplyKeyboardMarkup([deserti_shisha,soups_hot,pasta_fasfood,salad_garnir,cool_hot,coffee,zakus_alco,back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Чизкейк':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(61, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/KVQX753'), chat_id=user_id, caption='''*Чизкейк*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 61:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(60, user_id))

        cena = cur.execute(cost.format('Чизкейк')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Чизкейк' + ' - ' + str(cena) + zakaz


        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Чизкейк добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back,korzina], resize_keyboard=True))


    elif text == '⏪Назад' and stage ==61:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(60, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back,korzina],
                                                                  resize_keyboard=True))

    elif text == 'Медовик':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(62, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/Hn51Nz5'), chat_id=user_id, caption='''*Медовик*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 62:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(60, user_id))

        cena = cur.execute(cost.format('Медовик')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Медовик' + ' - ' + str(cena) + zakaz


        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Медовик добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back,korzina], resize_keyboard=True))



    elif text == '⏪Назад' and stage ==62:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(60, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back,korzina,],
                                                                  resize_keyboard=True))


    elif text == 'Брауни':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(63, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/HKydyrf'), chat_id=user_id, caption='''*Брауни*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 63:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(60, user_id))

        cena = cur.execute(cost.format('Брауни')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Брауни' + ' - ' + str(cena) + zakaz


        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Брауни добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back,korzina], resize_keyboard=True))



    elif text == '⏪Назад' and stage ==63:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(60, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back,korzina],
                                                                  resize_keyboard=True))

#ВСЕ ПО БАРУ


    elif text == 'Чаи🫖':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(71, user_id))
        context.bot.send_message(chat_id=user_id, text='Согреемся?☀',
                                 reply_markup=ReplyKeyboardMarkup([tea,brand_tea,back_korzina],
                                                                  resize_keyboard=True))



    elif text =='⏪Назад' and stage ==71:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(70, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([deserti_shisha,soups_hot,pasta_fasfood,salad_garnir,cool_hot,coffee,zakus_alco,back_korzina], resize_keyboard=True))

    elif text =='Наглый фрукт':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(72, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/sqSwnFy'), chat_id=user_id, caption='''*Наглый фрукт*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 72:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        cur.execute(update_stage_in.format(70, user_id))
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Наглый фрукт')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = '\n' + 'Наглый фрукт' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Наглый фрукт добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([deserti_shisha,soups_hot,pasta_fasfood,salad_garnir,cool_hot,coffee,zakus_alco,back_korzina], resize_keyboard=True))


    elif text =='⏪Назад' and stage ==72:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(71, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([tea,brand_tea,back_korzina], resize_keyboard=True))



    elif text =='Ягодная бергамония':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(73, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/m4DgM95'), chat_id=user_id, caption='''*Ягодная бергамония*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 73:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(71, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Ягодная бергамония')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Ягодная бергамония' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Ягодная бергамония добавлена в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([tea, brand_tea,back_korzina], resize_keyboard=True))


    elif text == '⏪Назад' and stage == 73:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(71, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([tea,brand_tea,back_korzina], resize_keyboard=True))



    elif text == 'Чай черный':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(74, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Чай черный')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = '\n' + 'Чай черный' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id))
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='С Сахаром или без?',
                                 reply_markup=ReplyKeyboardMarkup([sugar, back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 74:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz[19:]
        y = cur.execute(set_total_price.format(user_id)).fetchall()
        y = y[0][0]

        cur.execute(sql_set_zakaz.format(zakaz, user_id))

        cur.execute(update_total_price.format(y - 15000, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        cur.execute(update_stage_in.format(71, user_id))

        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([tea,brand_tea,back_korzina],
                                                                  resize_keyboard=True))

    elif text =='С сахаром':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(75, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = '\n' + text + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        context.bot.send_message(chat_id=user_id, text='С лимоном или без?',
                                 reply_markup=ReplyKeyboardMarkup([limon,back], resize_keyboard=True))

    elif text=='⏪Назад' and stage == 75:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz[10:]
        cur.execute(sql_set_zakaz.format(zakaz,user_id))


        cur.execute(update_stage_in.format(74, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([sugar, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Без сахара':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(76, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = '\n' + text + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        context.bot.send_message(chat_id=user_id, text='С лимоном или без?',
                                 reply_markup=ReplyKeyboardMarkup([limon,back], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 76:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        zakaz = zakaz[11:]


        cur.execute(sql_set_zakaz.format(zakaz, user_id))

        cur.execute(update_stage_in.format(74, user_id))

        context.bot.send_message(chat_id=user_id, text='С Сахаром или без?',
                                 reply_markup=ReplyKeyboardMarkup([sugar, back], resize_keyboard=True))

    elif text =='С лимоном':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('С лимоном')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'С лимоном' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        cur.execute(update_stage_in.format(77, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 77:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        zakaz = zakaz[17:]
        cena = cur.execute(cost.format('С лимоном')).fetchall()
        cena = cena[0][0]
        total_price = cur.execute(set_total_price.format(user_id)).fetchall()
        total_price = total_price[0][0]
        cur.execute(update_total_price.format(total_price - cena, user_id))

        cur.execute(sql_set_zakaz.format(zakaz, user_id))

        cur.execute(update_stage_in.format(75, user_id))
        context.bot.send_message(chat_id=user_id, text='С лимоном или без?',
                                 reply_markup=ReplyKeyboardMarkup([limon, back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 77:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(71,user_id))
        context.bot.send_message(chat_id=user_id, text='Чай добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([tea,brand_tea,back_korzina], resize_keyboard=True))

    elif text =='Без лимона':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = '\n' + text + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        cur.execute(update_stage_in.format(78, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 78:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(71, user_id))
        context.bot.send_message(chat_id=user_id, text='Чай добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([tea, brand_tea, back_korzina],
                                                                  resize_keyboard=True))

    elif text == '⏪Назад' and stage == 78:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz[11:]
        cur.execute(sql_set_zakaz.format(zakaz, user_id))

        cur.execute(update_stage_in.format(76, user_id))
        context.bot.send_message(chat_id=user_id, text='С лимоном или без?',
                                 reply_markup=ReplyKeyboardMarkup([limon, back], resize_keyboard=True))





    elif text == 'Чай зеленый':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(80, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Чай зеленый')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = '\n' + 'Чай зеленый' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id))
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='С Сахаром или без?',
                                 reply_markup=ReplyKeyboardMarkup([sugar,back_korzina], resize_keyboard=True))

    elif text=='⏪Назад' and stage == 80:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz[20:]
        cena = cur.execute(cost.format('Чай зеленый')).fetchall()
        cena = cena[0][0]
        total_price = cur.execute(set_total_price.format(user_id)).fetchall()
        total_price = total_price[0][0]
        cur.execute(update_total_price.format(total_price - cena, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        cur.execute(update_stage_in.format(71, user_id))


        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([deserti_shisha,soups_hot,pasta_fasfood,salad_garnir,cool_hot,coffee,zakus_alco,back_korzina],
                                                                  resize_keyboard=True))

    elif text =='С сахаром' and stage == 80:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(81, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = '\n' + text + zakaz
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        context.bot.send_message(chat_id=user_id, text='С лимоном или без?',
                                 reply_markup=ReplyKeyboardMarkup([limon,back], resize_keyboard=True))

    elif text=='⏪Назад' and stage == 81:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        y = cur.execute(update_total_price.format(user_id)).fetchall()
        y = y[0][0]
        zakaz = zakaz[9:]

        cur.execute(sql_set_zakaz.format(zakaz, user_id))
        cur.execute(update_stage_in.format(80, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?',
                                 reply_markup=ReplyKeyboardMarkup([sugar,back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Без сахара':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(82, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = '\n' + text + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        context.bot.send_message(chat_id=user_id, text='С лимоном или без?',
                                 reply_markup=ReplyKeyboardMarkup([limon,back], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 82:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        y = cur.execute(get_price.format(user_id)).fetchall()
        y = y[0][0]

        zakaz = zakaz[11:]
        cur.execute(sql_set_zakaz.format(zakaz,user_id))



        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([tea, brand_tea, back_korzina],
                                                                  resize_keyboard=True))

    elif text =='С лимоном' and stage == 82:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('С лимоном')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'С лимоном' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        cur.execute(update_stage_in.format(83, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 83:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz[17:0]
        cena = cur.execute(cost.format('С лимоном')).fetchall()
        cena = cena[0][0]
        total_price = cur.execute(set_total_price.format(user_id)).fetchall()
        total_price = total_price[0][0]
        cur.execute(update_total_price.format(total_price - cena, user_id))

        cur.execute(sql_set_zakaz.format(zakaz, user_id))

        cur.execute(update_stage_in.format(76, user_id))
        context.bot.send_message(chat_id=user_id, text='С лимоном или без?',
                                 reply_markup=ReplyKeyboardMarkup([limon, back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 77:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        context.bot.send_message(chat_id=user_id, text='Чай добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([tea,brand_tea,back_korzina], resize_keyboard=True))

    elif text =='Без лимона':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = '\n' + text + zakaz


        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        cur.execute(update_stage_in.format(78, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 78:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        context.bot.send_message(chat_id=user_id, text='Чай добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([tea, brand_tea, back_korzina],
                                                                  resize_keyboard=True))

    elif text == '⏪Назад' and stage == 78:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz[11:]
        cur.execute(sql_set_zakaz.format(zakaz, user_id))

        cur.execute(update_stage_in.format(76, user_id))
        context.bot.send_message(chat_id=user_id, text='С лимоном или без?',
                                 reply_markup=ReplyKeyboardMarkup([limon, back], resize_keyboard=True))




#ВСЕ ПРО КОФЕ

    elif text =='Кофе☕':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(90, user_id))
        context.bot.send_message(chat_id=user_id, text='Взбодримся?😎',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,back_korzina], resize_keyboard=True))

    elif text =='⏪Назад' and stage == 90:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(70, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([deserti_shisha,soups_hot,pasta_fasfood,salad_garnir,cool_hot,coffee,zakus_alco,back_korzina], resize_keyboard=True))


    elif text =='Американо':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(91, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 91:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(90, user_id))

        cena = cur.execute(cost.format('Американо')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Американо' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Американо добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,back_korzina], resize_keyboard=True))


    elif text =='⏪Назад' and stage == 91:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(90, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,back_korzina], resize_keyboard=True))

    elif text =='Эспрессо':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(92, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 92:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cena = cur.execute(cost.format('Эспрессо')).fetchall()
        cena = cena[0][0]
        cur.execute(update_stage_in.format(90, user_id))

        zakaz = '\n' + 'Эспрессо' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Эспрессо добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,back_korzina], resize_keyboard=True))


    elif text == '⏪Назад' and stage == 92:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(90, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano, cap_latte, raf_frap,back_korzina],
                                                                  resize_keyboard=True))


    elif text =='Капучино':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(93, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 93:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(90, user_id))

        cena = cur.execute(cost.format('Капучино')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Капучино' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Капучино добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,back_korzina], resize_keyboard=True))


    elif text == '⏪Назад' and stage == 93:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(90, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano, cap_latte, raf_frap,back_korzina],
                                                                  resize_keyboard=True))


    elif text =='Латте':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(94, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 94:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(90, user_id))

        cena = cur.execute(cost.format('Латте')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Латте' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Латте добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,back_korzina], resize_keyboard=True))


    elif text == '⏪Назад' and stage == 94:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(90, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano, cap_latte, raf_frap,back_korzina],
                                                                  resize_keyboard=True))


    elif text =='Раф':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(95, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]


        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 95:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(90, user_id))

        cena = cur.execute(cost.format('Раф')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Раф' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Раф добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,back_korzina], resize_keyboard=True))


    elif text == '⏪Назад' and stage == 95:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(90, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano, cap_latte, raf_frap,back_korzina],
                                                                  resize_keyboard=True))


    elif text =='Фраппучино':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(96, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]


        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 96:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(90, user_id))

        cena = cur.execute(cost.format('Фраппучино')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Фраппучино' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Фраппучино добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,back_korzina], resize_keyboard=True))




    elif text =='⏪Назад' and stage == 96:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(90, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,back_korzina], resize_keyboard=True))

#ВСЕ ПРО ЛИМОНАДЫ

    elif text =='Лимонады🍹':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(100, user_id))
        context.bot.send_message(chat_id=user_id, text='Охладимся?🧊',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,back_korzina],
                                                                  resize_keyboard=True))

    elif text == '⏪Назад' and stage == 100:

        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(70, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([deserti_shisha,soups_hot,pasta_fasfood,salad_garnir,cool_hot,coffee,zakus_alco,back_korzina], resize_keyboard=True))

    elif text == 'Йерная ягода':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(101, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/8BPdT5q'), chat_id=user_id, caption='''*Йерная ягода*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 101:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(100, user_id))

        cena = cur.execute(cost.format('Йерная ягода')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Йерная ягода' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Йерная ягода добавлена в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,back_korzina],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 101:
        conn = sqlite3.connect('identifier.sqlite')
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(100, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,back_korzina], resize_keyboard=True))


    elif text == 'Цитрус-щавель':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(102, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/jHyXtLD'), chat_id=user_id, caption='''*Цитрус-щавель*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 102:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(100, user_id))

        cena = cur.execute(cost.format('Цитрус-щавель')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + 'Цитрус-щавель' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Цитрус-щавель добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,back_korzina],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 102:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(100, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys, mango_ice, moh_mango,back_korzina],
                                                                  resize_keyboard=True))


    elif text == 'Манго-маракуя':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(103, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/wQ8pKqY'), chat_id=user_id, caption='''*Манго-маракуя*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 103:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(100, user_id))

        cena = cur.execute(cost.format('Манго-маракуя')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + 'Манго-маракуя' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Манго-маракуя добавлена в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,back_korzina],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 103:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(100, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys, mango_ice, moh_mango,back_korzina],
                                                                  resize_keyboard=True))



    elif text == 'Айс-ти':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(104, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/2W31h25'), chat_id=user_id, caption='''*Айс-ти*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 104:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(100, user_id))

        cena = cur.execute(cost.format('Айс-ти')).fetchall()
        cena = cena[0][0]

        zakaz ='\n' + 'Айс-ти' + ' - ' + str(cena) +  zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Айс-ти добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,back_korzina],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 104:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(100, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys, mango_ice, moh_mango,back_korzina],
                                                                  resize_keyboard=True))






    elif text == 'Мохито':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(105, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/26xtWWC'), chat_id=user_id, caption='''*Мохито*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 105:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(100, user_id))

        cena = cur.execute(cost.format('Мохито')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Мохито' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Мохито добавлено в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,back_korzina],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 105:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(100, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys, mango_ice, moh_mango,back_korzina],
                                                                  resize_keyboard=True))


    elif text == 'Манговый айс-ти':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(106, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/dp1dwB7'), chat_id=user_id, caption='''*Манговый айс-ти*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 106:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Манговый айс-ти')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Манговый айс-ти' + ' - ' + str(cena) + zakaz


        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Манговый айс-ти добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,back_korzina],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 106:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(100, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys, mango_ice, moh_mango,back_korzina],
                                                                  resize_keyboard=True))


#ВСЕ ПРО НАПИТКИ
    elif text == 'Напитки🥤':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(110, user_id))
        context.bot.send_message(chat_id=user_id, text='Что будем пить?🧐',
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,back_korzina],
                                                                  resize_keyboard=True))

    elif text == '⏪Назад' and stage == 110:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(70, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([deserti_shisha,soups_hot,pasta_fasfood,salad_garnir,cool_hot,coffee,zakus_alco,back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Red bull':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(111, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 111:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(110, user_id))

        cena = cur.execute(cost.format('Red bull')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Red bull' + ' - ' + str(cena) + zakaz


        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Red bull добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,back_korzina],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 111:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(110, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,back_korzina],
                                                                  resize_keyboard=True))



    elif text == 'Borjomi':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(112, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 112:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(110, user_id))

        cena = cur.execute(cost.format('Borjomi')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + 'Borjomi' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Borjomi добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,back_korzina],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 112:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(110, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with,back_korzina],
                                     resize_keyboard=True))



    elif text == 'Coca-cola':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(113, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_message(chat_id=user_id, text='''*Coca-Cola 0.25*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 113:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(110, user_id))

        cena = cur.execute(cost.format('Coca-cola')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Coca-cola' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Coca-cola добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,back_korzina],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 113:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(110, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with,back_korzina],
                                     resize_keyboard=True))



    elif text == 'Sprite':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(114, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_message(chat_id=user_id, text='''*Sprite 0.25*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 114:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(110, user_id))

        cena = cur.execute(cost.format('Sprite')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Sprite' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Sprite добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,back_korzina],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage ==114:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(110, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with,back_korzina],
                                     resize_keyboard=True))



    elif text == 'Сок':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(115, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_message(chat_id=user_id, text='''*Сок Rich 0.2*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 115:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(110, user_id))

        cena = cur.execute(cost.format('Сок')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Сок' + ' - ' + str(cena) + zakaz


        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Сок добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,back_korzina],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 115:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(110, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with,back_korzina],
                                     resize_keyboard=True))


    elif text == 'Вода с газом':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(116, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Вода с газом 0.5*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 116:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(110, user_id))

        cena = cur.execute(cost.format('Вода с газом')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Вода с газом' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Вода с газом добавлена в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,back_korzina],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 116:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(110, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with,back_korzina],
                                     resize_keyboard=True))


    elif text == 'Вода':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(117, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Вода 0.5*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 117:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(110, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cena = cur.execute(cost.format('Вода')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + 'Вода' + ' - ' + str(cena) + zakaz


        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Вода добавлена в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,back_korzina],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 117:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(110, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with,back_korzina],
                                     resize_keyboard=True))



    elif text == 'Fanta':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(118, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Fanta 0.25*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 118:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(110, user_id))

        cena = cur.execute(cost.format('Fanta')).fetchall()
        cena = cena[0][0]

        zakaz =  '\n' + 'Fanta' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Fanta добавлена в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with, back_korzina],
                                     resize_keyboard=True))


    elif text == '⏪Назад' and stage == 118:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(110, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with, back_korzina],
                                     resize_keyboard=True))




    elif text == 'Закуски🍿':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(120,user_id))
        context.bot.send_message(chat_id = user_id, text = 'Закусим?😎',reply_markup = ReplyKeyboardMarkup([sul_kurt,pring_mindal,phist_set,back_korzina],resize_keyboard = True))

    elif text =='⏪Назад' and stage == 120:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(70, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([deserti_shisha,soups_hot,pasta_fasfood,salad_garnir,cool_hot,coffee,zakus_alco,back_korzina], resize_keyboard=True))


    elif text == 'Сулугуни':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(121, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text =='⏪Назад' and stage == 121:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(120, user_id))
        context.bot.send_message(chat_id=user_id, text = 'Продолжим?😉',reply_markup = ReplyKeyboardMarkup([sul_kurt,pring_mindal,phist_set,back_korzina] ,resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 121:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(120, user_id))

        cena = cur.execute(cost.format('Сулугуни')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Сулугуни' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Сулугуни добавлены в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup(
                                     [sul_kurt,pring_mindal,phist_set,back_korzina],
                                     resize_keyboard=True))

    elif text == 'Курт':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(122, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text =='⏪Назад' and stage == 122:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(120, user_id))
        context.bot.send_message(chat_id=user_id, text = 'Продолжим?😉',reply_markup = ReplyKeyboardMarkup([sul_kurt,pring_mindal,phist_set,back_korzina],resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 122:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(120, user_id))

        cena = cur.execute(cost.format('Курт')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Курт' + ' - ' + str(cena) + zakaz


        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Курт добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup(
                                     [sul_kurt,pring_mindal,phist_set,back_korzina],
                                     resize_keyboard=True))




    elif text == 'Pringles':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(123, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text =='⏪Назад' and stage == 123:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(120, user_id))
        context.bot.send_message(chat_id=user_id, text = 'Продолжим?😉',reply_markup = ReplyKeyboardMarkup([sul_kurt,pring_mindal,phist_set,back_korzina],resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 123:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(120, user_id))

        cena = cur.execute(cost.format('Pringles')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Pringles' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Pringles добавлены в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup(
                                     [sul_kurt,pring_mindal,phist_set,back_korzina],
                                     resize_keyboard=True))

    elif text == 'Миндаль':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(124, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text =='⏪Назад' and stage == 124:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(120, user_id))
        context.bot.send_message(chat_id=user_id, text = 'Продолжим?😉',reply_markup = ReplyKeyboardMarkup([sul_kurt,pring_mindal,phist_set,back_korzina],resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 124:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(120, user_id))

        cena = cur.execute(cost.format('Миндаль')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Миндаль' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Миндаль добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup(
                                     [sul_kurt,pring_mindal,phist_set,back_korzina],
                                     resize_keyboard=True))

    elif text == 'Фисташки':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(125, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 125:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(120, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([sul_kurt, pring_mindal, phist_set, back_korzina],resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 125:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(120, user_id))

        cena = cur.execute(cost.format('Фисташки')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Фисташки' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Фисташки добавлены в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup(
                                     [sul_kurt,pring_mindal,phist_set,back_korzina],
                                     resize_keyboard=True))
    elif text == 'Сэт грызун':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(126, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_photo(photo=('https://ibb.co/Bf9s6Rf'), chat_id=user_id, caption='''*Сэт грызун*

*Цена:* {}💵'''.format(b), parse_mode='Markdown',
                               reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))

    elif text =='⏪Назад' and stage == 126:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(120, user_id))
        context.bot.send_message(chat_id=user_id, text = 'Продолжим?😉',reply_markup = ReplyKeyboardMarkup([sul_kurt,pring_mindal,phist_set,back_korzina],resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 126:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(120, user_id))

        cena = cur.execute(cost.format('Сэт грызун')).fetchall()
        cena = cena[0][0]

        zakaz = '\n' + 'Сэт грызун' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Сэт грызун добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup(
                                     [sul_kurt,pring_mindal,phist_set,back_korzina],
                                     resize_keyboard=True))




    elif text == 'Алкоголь🥃':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(130, user_id))
        context.bot.send_message(chat_id=user_id, text='Приятного отдыха😊',
                         reply_markup=ReplyKeyboardMarkup([kokteli,hard_light,back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 130:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(70, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([deserti_shisha,soups_hot,pasta_fasfood,salad_garnir,cool_hot,coffee,zakus_alco,back_korzina],
                                                                  resize_keyboard=True))


    elif text == 'Крепкий' and stage == 130:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(131, user_id))
        context.bot.send_message(chat_id=user_id, text='Что выпьем?🧐',
                                 reply_markup=ReplyKeyboardMarkup([viski_kon,liker_rom,djin_tekila, back_korzina],
                                                                  resize_keyboard=True))

    elif text == '⏪Назад' and stage == 131:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(130, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([kokteli,hard_light,back_korzina],
                                                                  resize_keyboard=True))
#ВСЕ ПРО ВИСКИ


    elif text == 'Виски' and stage == 131:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(132, user_id))
        context.bot.send_message(chat_id=user_id, text='Отличный выбор😎',
                                 reply_markup=ReplyKeyboardMarkup([chivas_jag,jack_tull,jame_bal,back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 132:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(131, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                         reply_markup=ReplyKeyboardMarkup([viski_kon,liker_rom,djin_tekila, back_korzina], resize_keyboard=True))


    elif text == 'Jack Daniels' and stage == 132:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(133, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Jack Daniels 50 ml*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 133:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(132, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Jack Daniels')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + 'Jack Daniels' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Отличный выбор',
                                 reply_markup=ReplyKeyboardMarkup([chivas_jag, jack_tull, jame_bal, back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 133:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(132, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([chivas_jag, jack_tull, jame_bal, back_korzina],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 133:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(132, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([chivas_jag, jack_tull, jame_bal, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Chivas Regal 12' and stage == 132:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(134, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Chivas Regal 12 50 ml*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 134:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(132, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Chivas Regal 12')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + 'Chivas Regal 12' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Отличный выбор',
                                 reply_markup=ReplyKeyboardMarkup([chivas_jag, jack_tull, jame_bal, back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 134:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(132, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([chivas_jag, jack_tull, jame_bal, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Tullamore Dew' and stage == 132:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(135, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Tullamore Dew 50 ml*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 135:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(132, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Tullamore Dew')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + 'Tullamore Dew' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Отличный выбор',
                                 reply_markup=ReplyKeyboardMarkup([chivas_jag, jack_tull, jame_bal, back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 135:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(132, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([chivas_jag, jack_tull, jame_bal, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Jameson' and stage == 132:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(136, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Jameson 50 ml*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 136:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(132, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Jameson')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + 'Jameson' + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Отличный выбор',
                                 reply_markup=ReplyKeyboardMarkup([chivas_jag, jack_tull, jame_bal, back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 136:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(132, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([chivas_jag, jack_tull, jame_bal, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Jagermeister' and stage == 131:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(139, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Jagermeister 50 ml*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 139:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(131, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Jagermeister')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + "Jagermeister" + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Отличный выбор',
                                 reply_markup=ReplyKeyboardMarkup([viski_kon,liker_rom,djin_tekila,back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 139:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(131, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([viski_kon,liker_rom,djin_tekila,back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Ballantines' and stage == 132:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(137, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Ballantines 50 ml*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 137:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(132, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Ballantines')).fetchall()
        cena = cena[0][0]
        zakaz ='\n' + "Ballantines" + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Отличный выбор',
                                 reply_markup=ReplyKeyboardMarkup([chivas_jag, jack_tull, jame_bal, back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 137:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(132, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([chivas_jag, jack_tull, jame_bal, back_korzina],
                                                                  resize_keyboard=True))

#КОКТЕЙЛИ

    elif text == 'Коктейли':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(140, user_id))
        context.bot.send_message(chat_id=user_id, text='Что выпьем?😜',
                         reply_markup=ReplyKeyboardMarkup([shirin,aper_meva,gin_teq,back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 140:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(70, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([cool_hot, coffee,zakus_alco, back_korzina],
                                                                  resize_keyboard=True))


    elif text == 'Shirins Peach':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(141, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Shirins Peach*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 141:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(140, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Shirins Peach')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + "Shirins Peach" + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Отличный выбор',
                                 reply_markup=ReplyKeyboardMarkup([shirin,aper_meva,gin_teq,back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 141:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(140, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([shirin,aper_meva,gin_teq,back_korzina],
                                                                  resize_keyboard=True))


    elif text == 'Aperol spritz':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(142, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Aperol spritz*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 142:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(140, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Aperol spritz')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + "Aperol spritz" + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Отличный выбор',
                                 reply_markup=ReplyKeyboardMarkup([shirin, aper_meva, gin_teq, back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 142:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(140, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([shirin, aper_meva, gin_teq, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Gin tonic':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(143, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Gin tonic*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 143:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(140, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Gin tonic')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + "Gin tonic" + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Отличный выбор',
                                 reply_markup=ReplyKeyboardMarkup([shirin, aper_meva, gin_teq, back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 143:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(140, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([shirin, aper_meva, gin_teq, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Meva-Cheva':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(144, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Meva-Cheva*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 144:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(140, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Meva-Cheva')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + "Meva-Cheva" + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Отличный выбор',reply_markup=ReplyKeyboardMarkup([shirin, aper_meva, gin_teq, back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 144:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(140, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([shirin, aper_meva, gin_teq, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Tequila Sunrise':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(145, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Tequila Sunrise*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 145:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(145, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Tequila Sunrise')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + "Tequila Sunrise" + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Отличный выбор',
                                 reply_markup=ReplyKeyboardMarkup([shirin, aper_meva, gin_teq, back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 145:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(140, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([shirin, aper_meva, gin_teq, back_korzina],
                                                                  resize_keyboard=True))

#ВСЕ ПРО РОМ

    elif text == 'Ром':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(150, user_id))
        context.bot.send_message(chat_id=user_id, text='Что выпьем?😜',
                                 reply_markup=ReplyKeyboardMarkup([cpt,jwray,back_korzina],
                                                                  resize_keyboard=True))

    elif text == '⏪Назад' and stage == 150:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(131, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([viski_kon, liker_rom, djin_tekila, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'J.Wray Silver':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(151, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*J.Wray Silver 50 ml*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 151:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(145, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('J.Wray Silver')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + "J.Wray Silver" + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Отличный выбор',
                                 reply_markup=ReplyKeyboardMarkup([cpt,jwray,back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 151:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(150, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([cpt,jwray,back_korzina],
                                                                  resize_keyboard=True))



    elif text == 'Capitan Morgan':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(153, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Capitan Morgan 50 ml*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 153:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(145, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Capitan Morgan')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + "Capitan Morgan" + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Отличный выбор',
                                 reply_markup=ReplyKeyboardMarkup([cpt,jwray,back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 153:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(150, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([cpt,jwray,back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'J.Wray Gold':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(152, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*J.Wray Gold 50 ml*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 152:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(145, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('J.Wray Gold')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + "J.Wray Gold" + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Отличный выбор',
                                 reply_markup=ReplyKeyboardMarkup([cpt,jwray,back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 152:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(150, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([cpt,jwray,back_korzina],
                                                                  resize_keyboard=True))

#ВСЕ ПРО КОНЬЯК

    elif text == 'Коньяк':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(160, user_id))
        context.bot.send_message(chat_id=user_id, text='Что выпьем?😜',
                                 reply_markup=ReplyKeyboardMarkup([tanb, back_korzina],
                                                                  resize_keyboard=True))

    elif text == '⏪Назад' and stage == 160 :
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(131, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([viski_kon, liker_rom, djin_tekila, back_korzina],
                                                                  resize_keyboard=True))



    elif text == 'Tanbour' and stage == 160:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(161, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Tanbour 50 ml*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 161:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(160, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Tanbour')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + "Tanbour" + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Отличный выбор',
                                 reply_markup=ReplyKeyboardMarkup([tanb,back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 161:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(131, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([viski_kon, liker_rom, djin_tekila, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Текила':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(170, user_id))
        context.bot.send_message(chat_id=user_id, text='Что выпьем?😜',
                                 reply_markup=ReplyKeyboardMarkup([esp, back_korzina],
                                                                  resize_keyboard=True))

    elif text == '⏪Назад' and stage == 170:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(131, user_id))
        context.bot.send_message(chat_id=user_id, text='Приятного отдыха😊',
                                 reply_markup=ReplyKeyboardMarkup([viski_kon, liker_rom, djin_tekila, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Espolon' and stage == 170:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(171, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Espolon 50 ml*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 171:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(170, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Espolon')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + "Espolon" + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Отличный выбор',
                                 reply_markup=ReplyKeyboardMarkup([esp,back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 171:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(131, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([viski_kon, liker_rom, djin_tekila, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Джин':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(180, user_id))
        context.bot.send_message(chat_id=user_id, text='Что выпьем?😜',
                                 reply_markup=ReplyKeyboardMarkup([Bickens, back_korzina],
                                                                  resize_keyboard=True))

    elif text == '⏪Назад' and stage == 180:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(131, user_id))
        context.bot.send_message(chat_id=user_id, text='Приятного отдыха😊',
                                 reply_markup=ReplyKeyboardMarkup([viski_kon, liker_rom, djin_tekila, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Bickens' and stage == 180:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(181, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Bickens 50 ml*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 181:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(180, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Bickens')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + "Bickens" + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Отличный выбор',
                                 reply_markup=ReplyKeyboardMarkup([Bickens, back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 181:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(131, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([viski_kon, liker_rom, djin_tekila, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Легкий' and stage == 130:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(190, user_id))
        context.bot.send_message(chat_id=user_id, text='Приятного отдыха😊',
                                 reply_markup=ReplyKeyboardMarkup([vino,shamp_beer, back_korzina],
                                                                  resize_keyboard=True))

    elif text == '⏪Назад' and stage == 190:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(130, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([kokteli,hard_light,back_korzina],
                                                                  resize_keyboard=True))


    elif text == 'Вино':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(191, user_id))
        context.bot.send_message(chat_id=user_id, text='Что выпьем?😊',
                                 reply_markup=ReplyKeyboardMarkup([kond,bagiz, back_korzina],
                                                                  resize_keyboard=True))

    elif text == '⏪Назад' and stage == 191:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(190, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([vino,shamp_beer, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Kondoli Marani' and stage == 191:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(192, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Kondoli Marani 750 ml*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 192:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(191, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Kondoli Marani')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + "Kondoli Marani" + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Kondoli Marani добавлен в заказ😎',
                                 reply_markup=ReplyKeyboardMarkup([kond,bagiz, back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 192:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(191, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([kond,bagiz, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Bagizagan 0.15' and stage == 191:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(193, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Bagizagan 0.15 ml*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 193:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(191, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Bagizagan 0.15')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + "Bagizagan 0.15" + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Bagizagan 0.15 добавлен в заказ😎',
                                 reply_markup=ReplyKeyboardMarkup([kond, bagiz, back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 193:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(191, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([kond,bagiz, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Bagizagan 0.33' and stage == 191:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(195, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Bagizagan 750 ml*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 195:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(191, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Bagizagan')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + "Bagizagan" + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Bagizagan добавлен в заказ😎',
                                 reply_markup=ReplyKeyboardMarkup([kond, bagiz, back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 195:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(191, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([kond,bagiz, back_korzina],
                                                                  resize_keyboard=True))




    elif text == 'Шампанское':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(250, user_id))
        context.bot.send_message(chat_id=user_id, text='Что выпьем?😊',
                                 reply_markup=ReplyKeyboardMarkup([pamir, back_korzina],
                                                                  resize_keyboard=True))

    elif text == '⏪Назад' and stage == 250:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(190, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([vino,shamp_beer, back_korzina],
                                                                  resize_keyboard=True))


    elif text == 'Pamir 0.15' and stage == 250:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(251, user_id))

        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Pamir 150 ml*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 251:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(250, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Pamir 0.15')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + "Pamir 0.15" + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Bagizagan добавлен в заказ😎',
                                 reply_markup=ReplyKeyboardMarkup([pamir, back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 251:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(250, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([pamir, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Pamir 0.75' and stage == 250:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(252, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Pamir 0.75 ml*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 252:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(250, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Pamir')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + "Pamir" + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Pamir 0.75 добавлен в заказ😎',
                                 reply_markup=ReplyKeyboardMarkup([pamir, back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 252:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(250, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([pamir, back_korzina],
                                                                  resize_keyboard=True))




    elif text == 'Пиво':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(260, user_id))
        context.bot.send_message(chat_id=user_id, text='Что выпьем?😊',
                                 reply_markup=ReplyKeyboardMarkup([corona,hei_tub, back_korzina],
                                                                  resize_keyboard=True))

    elif text == '⏪Назад' and stage == 260:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(190, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([vino,shamp_beer, back_korzina],
                                                                  resize_keyboard=True))


    elif text == 'Corona Extra👑' and stage == 260:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(261, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        print(a)
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Corona Extra*
*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 261:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(260, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Corona Extra👑')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + "Corona Extra👑" + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Corona Extra добавлена в заказ😎',
                                 reply_markup=ReplyKeyboardMarkup([corona,hei_tub, back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 261:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(260, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([corona,hei_tub, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Heineken' and stage == 260:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(262, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 262:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(260, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Heineken')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + "Heineken" + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Heineken добавлен в заказ😎',
                                 reply_markup=ReplyKeyboardMarkup([corona, hei_tub, back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 262:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(260, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([corona, hei_tub, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Tuborg' and stage == 260:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(263, user_id))
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Цена:* {}💵

Добавить в заказ?'''.format(b), parse_mode='Markdown',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, back_korzina], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 263:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(260, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Tuborg')).fetchall()
        cena = cena[0][0]
        zakaz = '\n' + "Tuborg" + ' - ' + str(cena) + zakaz

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena


        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Tuborg добавлен в заказ😎',
                                 reply_markup=ReplyKeyboardMarkup([corona, hei_tub, back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 263:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(260, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([corona, hei_tub, back_korzina],
                                                                  resize_keyboard=True))















    elif text == 'Мой заказ📝':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        x = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        x = x[0][0]
        cur.execute(update_stage_in.format(600,user_id))
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        if len(x) != 0:
            context.bot.send_message(chat_id=user_id, text='''*Ваш заказ* :{}

*Итоговая стоимость*: {}

Желаете оставить комментарии к заказу?🧐'''.format(x, itog), parse_mode= 'Markdown',
                                     reply_markup=ReplyKeyboardMarkup([commentariy,back], resize_keyboard=True,))



        else:
            cur.execute(update_stage_in.format(1001, user_id))
            context.bot.send_message(chat_id=user_id, text='Ваш заказ пуст😔')


    elif text != 'Пропустить⏩' and text != '⏪Назад' and stage == 600:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_dish.format(text, user_id))
        y = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        y = y[0][0]
        cur.execute(update_stage_in.format(601,user_id))
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        blyuda = cur.execute(comment_dish.format(user_id)).fetchall()
        blyuda = blyuda [0][0]
        kalyan = cur.execute(comment.format(user_id)).fetchall()
        kalyan = kalyan[0][0]

        context.bot.send_message(chat_id=user_id, text='''*Ваш заказ* : {}

*Комментарий к кальяну*💨 : {}

*Комментарий к блюду*: {}

*Итоговая стоимость*: {} 💵'''.format(y,kalyan, blyuda, itog),parse_mode= 'Markdown',
                                 reply_markup=ReplyKeyboardMarkup([ready, delete, back], resize_keyboard=True))


    elif text == 'Пропустить⏩' and stage == 600:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        y = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        y = y[0][0]
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        cur.execute(update_stage_in.format(601,user_id))
        x = cur.execute(comment_dish.format(user_id)).fetchall()
        x = x [0][0]
        kalyan = cur.execute(comment.format(user_id)).fetchall()
        kalyan = kalyan[0][0]
        context.bot.send_message(chat_id=user_id, text='''*Ваш заказ* :
         
{}


*Комментарий к блюду*: {}

*Комментарий к кальяну*: {}

*Итоговая стоимость*: {} 💵'''.format(y, x,kalyan, itog),parse_mode= 'Markdown',
                                 reply_markup=ReplyKeyboardMarkup([ready, delete, back], resize_keyboard=True))

    elif text == 'Заказать✅':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        x = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        x = x[0][0]
        print(x)
        total_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        total_zakaz = total_zakaz[0][0]
        total_zakaz = total_zakaz +x
        cur.execute(update_total_zakaz.format(total_zakaz,user_id))

        a = cur.execute(get_price.format(user_id)).fetchall()
        a = a[0][0]
        price = cur.execute(set_total_price.format(user_id)).fetchall()
        price = price[0][0]
        print(price)
        price = price + a
        cur.execute(update_price.format(price,user_id))



        a = cur.execute(table_number_in_table.format(user_id)).fetchall()
        y = cur.execute(comment.format(user_id)).fetchall()
        y = y[0][0]
        cur.execute(update_total_price.format(0,user_id))
        cur.execute(delete_zakaz.format(user_id))
        cur.execute(update_stage_in.format(1001,user_id))
        c = cur.execute(comment_dish.format(user_id)).fetchall()
        c = c[0][0]

        context.bot.send_message(chat_id = user_id, text = 'Ваш заказ принят и очень скоро будет готов!',
                                 reply_markup = ReplyKeyboardMarkup([top_button,bot_button,mid_button,order_button],resize_keyboard=True))
        context.bot.send_message(chat_id = 44335784,text = '''№ СТОЛА : {}
*Заказ* : {}

*КОММЕНТАРИЙ К КАЛЬЯНУ*: {}

*Комментарий к блюдам*: {}'''.format(a[0][0], x, y,c),parse_mode= 'Markdown')

        context.bot.send_message(chat_id=vlad, text='''№ СТОЛА : {}
*Заказ* : {}

*КОММЕНТАРИЙ К КАЛЬЯНУ*: {}

*Комментарий к блюдам*: {}'''.format(a[0][0], x, y, c), parse_mode='Markdown')
        context.bot.send_message(chat_id=timur, text='''№ СТОЛА : {}
*Заказ* : {}

*КОММЕНТАРИЙ К КАЛЬЯНУ*: {}

*Комментарий к блюдам*: {}'''.format(a[0][0], x, y, c), parse_mode='Markdown')
        cur.execute(update_dish.format('Отсутствует',user_id))
        cur.execute(update_comment.format('Отсутствует', user_id))

        datetime = time.asctime()
        Logpath = 'answers.txt'
        log = open(Logpath, 'a')
        logstr = "{} | : {}".format(datetime, x)
        log.writelines(logstr)



    elif text == 'Заказать✅' and stage == 601:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        x = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        x = x[0][0]
        total_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        total_zakaz = total_zakaz[0][0]
        total_zakaz = total_zakaz + x
        cur.execute(update_total_zakaz.format(total_zakaz,user_id))
        a = cur.execute(get_price.format(user_id)).fetchall()
        a = a[0][0]
        price = cur.execute(set_total_price.format(user_id)).fetchall()
        price = price[0][0]
        price = price + a
        cur.execute(update_price.format(a,user_id))

        a = cur.execute(table_number_in_table.format(user_id)).fetchall()
        kalyan = cur.execute(comment.format(user_id)).fetchall()
        kalyan = kalyan[0][0]
        cur.execute(update_total_price.format(0, user_id))
        cur.execute(delete_zakaz.format(user_id))
        cur.execute(update_stage_in.format(1001, user_id))
        dish = cur.execute(comment_dish.format(user_id)).fetchall()
        dish = dish[0][0]

        context.bot.send_message(chat_id=user_id, text='Ваш заказ принят и очень скоро будет готов!',
                                 reply_markup=ReplyKeyboardMarkup([top_button, bot_button, mid_button, order_button],
                                                                  resize_keyboard=True))
        context.bot.send_message(chat_id=44335784, text='''№ СТОЛА : {}
*Заказ* : {}

*КОММЕНТАРИЙ К КАЛЬЯНУ*: {}

*Комментарий к блюдам*: {}'''.format(a[0][0], x, kalyan,dish),parse_mode= 'Markdown')

        context.bot.send_message(chat_id=vlad, text='''№ СТОЛА : {}
*Заказ* : {}

*КОММЕНТАРИЙ К КАЛЬЯНУ*: {}

*Комментарий к блюдам*: {}'''.format(a[0][0], x, kalyan, dish), parse_mode='Markdown')
        context.bot.send_message(chat_id=timur, text='''№ СТОЛА : {}
*Заказ* : {}

*КОММЕНТАРИЙ К КАЛЬЯНУ*: {}

*Комментарий к блюдам*: {}'''.format(a[0][0], x, kalyan, dish), parse_mode='Markdown')
        cur.execute(update_dish.format('Отсутствует',user_id))
        cur.execute(update_comment.format('Отсутствует', user_id))

        datetime = time.asctime()
        Logpath = 'answers.txt'
        log = open(Logpath, 'a')
        logstr = "{} | : {}".format(datetime, x)
        log.writelines(logstr)


    elif text == 'Очистить заказ':
        x = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        x = x[0][0]

        cur.execute(delete_zakaz.format(user_id))
        cur.execute(update_total_price.format(0,user_id))
        cur.execute(update_stage_in.format(1001,user_id))


        cur.execute(update_dish.format('Отсутствует',user_id))
        cur.execute(update_comment.format('Отсутствует', user_id))
        context.bot.send_message(chat_id = user_id,text = 'Ваш заказ очищен',reply_markup = ReplyKeyboardMarkup([top_button,bot_button,mid_button,order_button],resize_keyboard=True))



    elif text =='Позвать Таймгарда🏃':
        a = cur.execute(table_number_in_table.format(user_id)).fetchall()
        print(a[0][0])
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        print(stage)
        context.bot.send_message(chat_id=user_id, text='Так Точно💪!')
        context.bot.send_message(chat_id=regina, text='Тебя зовет стол № {}'.format(a[0][0]))



    elif text == 'Кэшбэк💵':
        x = cur.execute(get_cashbak.format(user_id)).fetchall()
        x = x[0][0]
        y = cur.execute(select_phone.format(user_id)).fetchall()
        y = y[0][0]
        context.bot.send_message(chat_id = user_id,text = '''*Номер карты:* {}
*Баланс карты:* {} 💵'''.format(y,x),parse_mode = 'Markdown',reply_markup = ReplyKeyboardMarkup([top_button,bot_button,mid_button,order_button],resize_keyboard=True))


    elif text == 'Попросить счет💵':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()

        x = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        x = x[0][0]
        y = cur.execute(get_price.format(user_id)).fetchall()
        y = y[0][0]
        y = y * 10 / 100 + y
        if len(x) != 0:
            cur.execute(delete_total_zakaz.format(user_id))
            cur.execute(update_dish.format('Отсутствует', user_id))
            cur.execute(update_comment.format('Отсутствует', user_id))
            context.bot.send_message(chat_id=user_id, text='''*Прошу вас, ваш Чек*🧾

{}
    
*Обслуживание* - 10%✅
    
*Итоговая стоимость* - {}💵 '''.format(x, y),parse_mode = 'Markdown',
                                     reply_markup=ReplyKeyboardMarkup(
                                         [payme_click, nal], resize_keyboard=True,
                                         one_time_keyboard=True))
            b = cur.execute(visit.format(user_id)).fetchall()
            cur.execute(update_price.format(0,user_id))
            cur.execute(delete_zakaz.format(user_id))
            cur.execute(update_total_price.format(0,user_id))
            b = b[0][0]
            b = b + 1
            print(type(b))
            cur.execute(update_visit.format(b,user_id))
            print(type(visit))
            if b < 10:
                c = cur.execute(cashback.format(user_id)).fetchall()
                c = c[0][0]
                c = y*3/100 +c
                cur.execute(update_cashback.format(c, user_id))
            elif b >= 10 and b <15:
                c = cur.execute(cashback.format(user_id)).fetchall()
                c = c[0][0]
                c = y*5/100 +c
                cur.execute(update_cashback.format(c,user_id))
            elif b >= 15:
                c = cur.execute(cashback.format(user_id)).fetchall()
                c = c[0][0]
                c = y * 7 / 100 + c
                cur.execute(update_cashback.format(c, user_id))



        else:
            context.bot.send_message(chat_id = user_id,text = 'Ваш заказ пуст😔')


    elif text == '⏪Назад':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(1001,user_id))
        context.bot.send_message(chat_id = user_id,text = 'Прекрасного времени провождения😊',
                                 reply_markup = ReplyKeyboardMarkup([top_button,bot_button,mid_button,order_button],resize_keyboard=True))


    elif text== 'Payme':
        context.bot.send_message(chat_id = user_id,text = 'Для оплаты нажмите на кнопку кнопку⬇',reply_markup = InlineKeyboardMarkup([oplata_1]))
        time.sleep(5)
        context.bot.delete_message(chat_id = user_id, message_id = message_id+1)
        context.bot.send_message(chat_id=user_id, text = '''Благодарим за доверие времени нам💚. Ждем вас снова!
Нажми на кнопку как придешь еще раз! ⬇''',reply_markup = ReplyKeyboardMarkup([restart],resize_keyboard=True,
                                                                    one_time_keyboard = True))


    elif text== 'Click':
        context.bot.send_message(chat_id = user_id,text = 'Для оплаты нажмите на кнопку кнопку⬇',reply_markup = InlineKeyboardMarkup([oplata_2]))
        time.sleep(5)
        context.bot.delete_message(chat_id = user_id, message_id = message_id+1)
        context.bot.send_message(chat_id=user_id, text = '''Благодарим за доверие времени нам💚. Ждем вас снова!
Нажми на кнопку как придешь еще раз! ⬇''' ,reply_markup = ReplyKeyboardMarkup([restart],resize_keyboard=True,
                                                                    one_time_keyboard = True))

    elif text == 'Наличные':
        context.bot.send_message(chat_id = user_id ,text = '''Благодарим за доверие времени нам💚. Ждем вас снова!
Нажми на кнопку как придешь еще раз! ⬇''',reply_markup = ReplyKeyboardMarkup([restart],resize_keyboard=True,one_time_keyboard=True))


    elif text.isdigit() and text not in allowed_tables:
        context.bot.send_message(chat_id = user_id,text = 'У нас нет такого стола')



    else:
        a = cur.execute(table_number_in_table.format(user_id)).fetchall()
        context.bot.send_message(chat_id = user_id,text = "Сейчас все будет!")


    conn.commit()

