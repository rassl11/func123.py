import concurrent.futures
import time

from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from const import *
from sql_req import *
import sqlite3



def start(update,context):
    conn = sqlite3.connect('identifier.sqlite')
    cur = conn.cursor()

    user_id = update.message.chat_id
    name = update.message.from_user.first_name
    conn = sqlite3.connect('identifier.sqlite')
    cur = conn.cursor()
    cur.execute(update_stage_in.format(999,user_id))
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
        context.bot.send_message(text="{} Добро пожаловать в Timekeeper Service Bot, Отправь свой номер телефона".format(name), chat_id=user_id,reply_markup=ReplyKeyboardMarkup([phone],
                                                                  resize_keyboard=True,one_time_keyboard=True))

        conn.commit()


def get_contact(update,context):
    num = update.message.contact.phone_number
    user_id = update.message.chat_id
    conn = sqlite3.connect('identifier.sqlite')
    cur = conn.cursor()
    cur.execute(update_phone_no.format(num,user_id))
    cur.execute(update_stage_in.format(999,user_id))
    conn.commit()
    context.bot.send_message(chat_id = user_id, text = 'Отлично,теперь введи номер стола')

def text_answer(update,context):
    user_id = update.message.chat_id
    name = update.message.from_user.first_name
    text = update.message.text

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
    allowed_tables = ['100','101','102','103','104','200','201','202','203','204','300','301','302','303','1998']



    if text.isdigit and text in allowed_tables and stage ==999:
        cur.execute(update_table_number.format(text, user_id))
        cur.execute(update_stage_in.format(1001,user_id))
        context.bot.send_message(chat_id = user_id,text = 'Прекрасного времени провождения😊',
                                 reply_markup = ReplyKeyboardMarkup([top_button,mid_button,bot_button,order_button],resize_keyboard=True))


    elif text == 'Сделать заказ✍' and stage == 1001:
        context.bot.send_photo(chat_id = user_id,photo = ('https://ibb.co/9NSX2BY'),caption = 'Прошу Вас, наше меню')
        context.bot.send_message(chat_id = user_id,text = 'С чего начнем😊?',
                               reply_markup = ReplyKeyboardMarkup([shisha_button,kitchen_bar,back_korzina],resize_keyboard=True))

    elif text == '⏪Назад' and stage == 1001:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        context.bot.send_message(chat_id = user_id,text = 'Продолжим?😉',
                                 reply_markup = ReplyKeyboardMarkup([top_button,mid_button,bot_button,order_button],resize_keyboard=True))

#все про кальяны

    elif text == 'Кальян💨':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cur.execute(update_stage_in.format(200, user_id))
        cena = cur.execute(cost.format('Кальян')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + 'Кальян' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Кальян' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text="Какой крепости кальян",
                                 reply_markup=ReplyKeyboardMarkup([easy, medium, rare, back], resize_keyboard=True))




    elif text == '⏪Назад' and stage == 200:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz.split()
        zakaz = zakaz[0:-3]
        zakaz = ' '.join(zakaz)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz.split()
        final_zakaz = final_zakaz[0:-3]
        final_zakaz = ' '.join(final_zakaz)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        cur.execute(update_stage_in.format(1001,user_id))
        cur.execute(update_total_price.format(0,user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([shisha_button,kitchen_bar,back_korzina],
                                                                  resize_keyboard=True))

    elif text =='Легкий' or text == 'Средний' or text == 'Крепкий':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(201, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]


        zakaz = zakaz + '\n' + text
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + text

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        context.bot.send_message(chat_id = user_id,text = 'Что по вкусам?',
                                 reply_markup = ReplyKeyboardMarkup([berry,fruit,desert,citrus,back],resize_keyboard=True))

    elif text == '⏪Назад' and stage == 201:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz.split()
        zakaz = zakaz[0:-1]
        zakaz = ' '.join(zakaz)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz.split()
        final_zakaz = final_zakaz[0:-1]
        final_zakaz = ' '.join(final_zakaz)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        cur.execute(update_stage_in.format(200, user_id))
        a = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        context.bot.send_message(chat_id=user_id, text='Какой крепости кальян',
                                 reply_markup=ReplyKeyboardMarkup([easy,medium,rare,back],resize_keyboard=True))


    elif text == 'Ягодный' or text == 'Фруктовый' or text == 'Цитрусовый' or text =='Десертный':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(202, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        zakaz = zakaz + '\n' + text

        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + text

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        context.bot.send_message(chat_id=user_id, text='Тип курения?',
                                 reply_markup=ReplyKeyboardMarkup([folga,kolaud,back], resize_keyboard=True))


    elif text == '⏪Назад' and stage == 202:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz.split()
        zakaz = zakaz[0:-1]
        zakaz = ' '.join(zakaz)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz.split()
        final_zakaz = final_zakaz[0:-1]
        final_zakaz = ' '.join(final_zakaz)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        cur.execute(update_stage_in.format(201, user_id))
        context.bot.send_message(chat_id=user_id, text='Что по вкусам?',
                                 reply_markup = ReplyKeyboardMarkup([berry,fruit,desert,citrus,back],resize_keyboard=True))



    elif text == 'Калауд' or text == 'Фольга':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(203, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        zakaz = zakaz + '\n' + text
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + text

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()


        context.bot.send_message(chat_id = user_id,text = 'С холодком или без?',reply_markup = ReplyKeyboardMarkup([ice,no_ice,back],resize_keyboard=True))


    elif text == '⏪Назад' and stage == 203:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz.split()
        zakaz = zakaz[0:-1]
        zakaz = ' '.join(zakaz)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz.split()
        final_zakaz = final_zakaz[0:-1]
        final_zakaz = ' '.join(final_zakaz)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz,user_id)).fetchall()
        cur.execute(update_stage_in.format(202, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup = ReplyKeyboardMarkup([folga,kolaud,back],resize_keyboard=True))



    elif text == 'С холодком' or text == 'Без Холодка':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(204, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]


        zakaz = zakaz + '\n' + text
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + text

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        context.bot.send_message(chat_id = user_id, text = 'Отлично,добавляем в заказ?',
                                 reply_markup = ReplyKeyboardMarkup([add_zakaz,korzina,back],resize_keyboard=True))

    elif text == '⏪Назад' and stage == 204:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(203, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz.split()
        zakaz = zakaz[0:-2]
        zakaz = ' '.join(zakaz)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz.split()
        final_zakaz = final_zakaz[0:-2]
        final_zakaz = ' '.join(final_zakaz)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        context.bot.send_message(chat_id=user_id, text='С холодком или без?',
                                 reply_markup = ReplyKeyboardMarkup([ice,no_ice,back],resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 204:

        context.bot.send_message(chat_id = user_id, text = 'Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([shisha_button,kitchen_bar,back_korzina],
                                                                  resize_keyboard=True))




# всепро кухню

    elif text=='Кухня🍽':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(1, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([soups_hot,pasta_fasfood,salad_garnir,desserts,back]))

    elif text =='⏪Назад' and stage == 1:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(1001, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([shisha_button,kitchen_bar,back_korzina],
                                                                  resize_keyboard=True))
#ВСЕ ПРО СУПЫ

    elif text == 'Супы🍜':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(2, user_id))
        context.bot.send_message(chat_id = user_id,text ='Что-нибудь легкое?😉',
                                 reply_markup = ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava,korzina,back],resize_keyboard=True))

    elif text == '⏪Назад' and stage ==2:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(1, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([soups_hot,pasta_fasfood,salad_garnir,desserts,back],
                                                                  resize_keyboard=True))


    elif text == 'Окрошка' and stage == 2:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(3, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_photo(photo = ('https://ibb.co/tzHFGG1'),chat_id= user_id,caption='''Описание :{}
Цена: {}'''.format(a,b),reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back],resize_keyboard=True))


    elif text == '⏪Назад' and stage ==3:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(2, user_id))
        context.bot.send_message(chat_id=user_id, text='Что-нибудь легкое?😉',
                                 reply_markup=ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava, back,korzina],
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
        zakaz = zakaz + '\n' + 'Окрошка' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Окрошка' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()

        context.bot.send_message(chat_id = user_id,text = 'Окрошка добавлена  в заказ'.format(text),
                                 reply_markup = ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava,korzina,back],resize_keyboard=True))



    elif text == 'Кук-си' and stage == 2:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(5, user_id))
        conn.commit()
        context.bot.send_message(chat_id = user_id,text = 'asd',reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back],resize_keyboard=True))

    elif text == '⏪Назад' and stage ==5:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(2, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([soups_hot,pasta_fasfood,salad_garnir,desserts,back],
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

        zakaz = zakaz + '\n' + 'Кук-си' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Кук-си' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Кук-си добавлена  в заказ'.format(text),reply_markup = ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava,korzina,back],resize_keyboard=True))



    elif text =='Рамен' and stage == 2:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(7, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        c = cur.execute(photo.format(text)).fetchall()
        c = c[0][0]
        context.bot.send_photo(photo=('https://ibb.co/dWSpDVT'), chat_id=user_id, caption='''Описание :{}
Цена: {}'''.format(a, b),reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back],resize_keyboard=True))

    elif text == '⏪Назад' and stage ==7:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(1, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([soups_hot,pasta_fasfood,salad_garnir,desserts,back],
                                                                  resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 7:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cur.execute(update_stage_in.format(2, user_id))
        cena = cur.execute(cost.format('Рамен')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Рамен' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Рамен' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id = user_id,text = 'Рамен добавлен в заказ'.format(text),reply_markup = ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava,korzina,back],resize_keyboard=True))




    elif text =='Мастава' and stage == 2:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(8, user_id))
        context.bot.send_message(chat_id = user_id,text ='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back],resize_keyboard=True))


    elif text == '⏪Назад' and stage ==8:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(1, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([soups_hot,pasta_fasfood,salad_garnir,desserts,back],
                                                                  resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 8:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(2, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cena = cur.execute(cost.format('Мастава')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + 'Мастава' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Мастава' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))

        context.bot.send_message(chat_id = user_id,text = 'Мастава добавлена в заказ'.format(text),reply_markup = ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava,korzina,back],resize_keyboard=True))


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
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([soups_hot,pasta_fasfood,salad_garnir,desserts,korzina,back],
                                                                  resize_keyboard=True))
    elif text == 'Рибай стейк':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(11, user_id))
        context.bot.send_message(chat_id=user_id, text='asd',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


    elif text == '⏪Назад' and stage == 11:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Насытимся😉',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 11:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(10,user_id))

        cena = cur.execute(cost.format('Рибай стейк')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Рибай стейк' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Рибай стейк' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id = user_id,text = 'Рибай стейк добавлен в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))


    elif text == 'Медальоны':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(12, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 12:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 12:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Медальоны')).fetchall()
        cena = cena[0][0]
        cur.execute(update_stage_in.format(10, user_id))
        zakaz = zakaz + '\n' + 'Медальоны' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Медальоны' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))

        context.bot.send_message(chat_id = user_id,text = 'Медальоны добавлены в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))



    elif text == 'Говядина в сливочном соусе':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(13, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


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
        zakaz = zakaz + '\n' + 'Говядина в сливочном соусе' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Говядина в сливочном соусе' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id = user_id,text = 'Говядина в сливочном соусе добавлена в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))




    elif text == '⏪Назад' and stage == 13:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))
    elif text == 'Курица на гриле':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(14, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


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
        zakaz = zakaz + '\n' + 'Курица на гриле' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Курица на гриле' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id = user_id,text = 'Курица на гриле добавлена в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 14:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))
    elif text == 'Картошка по-домашнему':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(15, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 15:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Картошка по-домашнему')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Картошка по-домашнему' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Картошка по-домашнему' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id = user_id,text = 'Картошка по-домашнему добавлена в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 15:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))
    elif text == 'Мясо по-китайски':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(16, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

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
        zakaz = zakaz + '\n' + 'Мясо по-китайски' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Мясо по-китайски' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id = user_id,text = 'Мясо по-китайский добавлена в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 16:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))

    elif text == 'Стейк куриный':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(17, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 17:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(17, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Стейк куриный')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Стейк куриный' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Стейк куриный' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id = user_id,text = 'Стейк куриный добавлен в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 17:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
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
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [soups_hot,pasta_fasfood,salad_garnir, desserts,korzina, back],
                                     resize_keyboard=True))

    elif text =='Альфредо':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(21, user_id))
        context.bot.send_message(chat_id=user_id, text='asd',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


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
        zakaz = zakaz + '\n' + 'Альфредо' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Альфредо' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id = user_id,text = 'Альфредо добавлено в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([alfredo_boloneze,back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 21:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(20, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши пасты',
                                 reply_markup=ReplyKeyboardMarkup([alfredo_boloneze,back_korzina],resize_keyboard=True))

    elif text =='Болоньезе':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(22, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


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
        zakaz = zakaz + '\n' + 'Болоньезе' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Болоньезе' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id = user_id,text = 'Болоньезе добавлено в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([alfredo_boloneze,back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 22:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(20, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши пасты',
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
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [soups_hot,pasta_fasfood,salad_garnir, desserts,korzina, back],
                                     resize_keyboard=True))

    elif text =='Буррито':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(31, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,back_korzina], resize_keyboard=True))

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
        zakaz = zakaz + '\n' + 'Буррито' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Буррито' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Буррито добавлено в заказ',
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,back_korzina],resize_keyboard=True))

    elif text == '⏪Назад' and stage == 31:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(30, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,back_korzina],
                                                                  resize_keyboard=True))

    elif text =='Наггетсы':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(32, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 32:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(30, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Наггетсы')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Наггетсы' + ' - ' + str(cena)

        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Наггетсы' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Наггетсы добавлены в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,back_korzina],resize_keyboard=True))


    elif text == '⏪Назад' and stage == 32:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(30, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,back_korzina],
                                                                  resize_keyboard=True))


    elif text =='Гарлики':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(33, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,back_korzina], resize_keyboard=True))


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
        zakaz = zakaz + '\n' + 'Гарлики' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Гарлики' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Гарлики добавлены в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,back_korzina],resize_keyboard=True))


    elif text == '⏪Назад' and stage == 33:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(30, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [burrito_sandwich, nuggets_garlic, back_korzina],
                                     resize_keyboard=True))
    elif text =='Куриный Сэндвич':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(34, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))



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
        zakaz = zakaz + '\n' + 'Куриный сэндвич' + ' - ' + str(cena)
        print(zakaz)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Куриный сэндвич' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Куриный сэндвич добавлен в заказ',
                                 reply_markup = ReplyKeyboardMarkup([burrito_sandwich, nuggets_garlic, back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 34:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(30, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',reply_markup = ReplyKeyboardMarkup([burrito_sandwich, nuggets_garlic, back_korzina], resize_keyboard=True))

#ВСЕ ПРО САЛАТЫ

    elif text == 'Салаты🥗':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(40, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши Салаты',
                                 reply_markup=ReplyKeyboardMarkup([greek_achik,korzina, back],
                                                                  resize_keyboard=True))

    elif text == '⏪Назад' and stage == 40:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(1, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup = ReplyKeyboardMarkup([soups_hot, pasta_fasfood, salad_garnir, desserts,korzina, back], resize_keyboard=True))

    elif text == 'Греческий салат':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(41, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

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
        zakaz = zakaz + '\n' + 'Греческий салат' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Греческий салат' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Греческий салат добавлен в заказ'.format(text),
                                 reply_markup = ReplyKeyboardMarkup([soups_hot, pasta_fasfood, salad_garnir, desserts,korzina, back], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 41:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(40, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup = ReplyKeyboardMarkup([greek_achik,korzina, back], resize_keyboard=True))

    elif text == 'Ачик-чучук':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(42, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 42:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(40, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Ачик-чучук')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Ачик-чучук' + ' - ' + str(cena)
        print(zakaz)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Ачик-чучук' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Ачик-чучук добавлен в заказ'.format(text),
                                 reply_markup = ReplyKeyboardMarkup([soups_hot, pasta_fasfood, salad_garnir, desserts,korzina, back], resize_keyboard=True))


    elif text == '⏪Назад' and stage == 42:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(40, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup = ReplyKeyboardMarkup([greek_achik,korzina, back], resize_keyboard=True))

#ВСЕ ПРО ГАРНИРЫ

    elif text=='Гарниры🍟':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(50, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши гарниры',
                                 reply_markup=ReplyKeyboardMarkup([grilveg_fries,ris_derev,aydaho_back,korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage ==50:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(1, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',reply_markup=ReplyKeyboardMarkup(
                                     [soups_hot, pasta_fasfood, salad_garnir, desserts,korzina, back], resize_keyboard=True))

    elif text=='Овощи на грилле':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(51, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

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
        zakaz = zakaz + '\n' + 'Овощи на гриле' + ' - ' + str(cena)

        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Овощи на гриле' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Овощи на гриле добавлены в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([grilveg_fries,ris_derev,aydaho_back,korzina], resize_keyboard=True))


    elif text == '⏪Назад' and stage ==51:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(50, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши гарниры',reply_markup=ReplyKeyboardMarkup([grilveg_fries, ris_derev, aydaho_back,korzina],
                                                                  resize_keyboard=True))


    elif text=='Картофель по-деревенски':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(52, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

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
        zakaz = zakaz + '\n' + 'Картофель по-деревенски' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Картофель по-деревенски' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Картофель по-деревенски добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([grilveg_fries,ris_derev,aydaho_back,korzina], resize_keyboard=True))




    elif text == '⏪Назад' and stage ==52:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(50, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши гарниры',reply_markup=ReplyKeyboardMarkup([grilveg_fries, ris_derev, aydaho_back,korzina,],
                                                                  resize_keyboard=True))


    elif text=='Рис':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(53, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 53:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(50, user_id))

        cena = cur.execute(cost.format('Рис')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Рис' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Рис' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Рис добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([grilveg_fries,ris_derev,aydaho_back,korzina], resize_keyboard=True))


    elif text == '⏪Назад' and stage ==53:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(50, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши гарниры',reply_markup=ReplyKeyboardMarkup([grilveg_fries, ris_derev, aydaho_back,korzina],
                                                                  resize_keyboard=True))

    elif text=='Фри':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(54, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 54:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(50, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Фри')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Фри' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Фри' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Фри добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([grilveg_fries,ris_derev,aydaho_back,korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage ==54:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(50, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши гарниры',reply_markup=ReplyKeyboardMarkup([grilveg_fries, ris_derev, aydaho_back,korzina],
                                                                  resize_keyboard=True))



    elif text=='Картофель айдахо':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(55, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 55:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(50, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Картофель айдахо')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Картофель айдахо' + ' - ' + str(cena)

        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Картофель айдахо' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Картофель айдахо добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([grilveg_fries,ris_derev,aydaho_back,korzina], resize_keyboard=True))


    elif text == '⏪Назад' and stage ==55:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(50, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши гарниры',reply_markup=ReplyKeyboardMarkup([grilveg_fries, ris_derev, aydaho_back,korzina],
                                                                  resize_keyboard=True))

#ВСЕ ПРО ДЕСЕРТЫ

    elif text=='Десерты🍰':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(60, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back], resize_keyboard=True))

    elif text == '⏪Назад' and stage ==60:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(1001, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',reply_markup=ReplyKeyboardMarkup([soups_hot, pasta_fasfood, salad_garnir, desserts,korzina, back],
                                                                  resize_keyboard=True))

    elif text == 'Чизкейк':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(61, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 61:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(60, user_id))

        cena = cur.execute(cost.format('Чизкейк')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Чизкейк' + ' - ' + str(cena)

        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Чизкейк' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Чизкейк добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back], resize_keyboard=True))


    elif text == '⏪Назад' and stage ==61:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(60, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши десерты',reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back,korzina],
                                                                  resize_keyboard=True))

    elif text == 'Медовик':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(62, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 62:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(60, user_id))

        cena = cur.execute(cost.format('Медовик')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Медовик' + ' - ' + str(cena)

        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Медовик' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Медовик добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back], resize_keyboard=True))



    elif text == '⏪Назад' and stage ==62:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(60, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши десерты',reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back,korzina,],
                                                                  resize_keyboard=True))


    elif text == 'Брауни':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(63, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 63:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(60, user_id))

        cena = cur.execute(cost.format('Брауни')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Брауни' + ' - ' + str(cena)

        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Брауни' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Брауни добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back], resize_keyboard=True))



    elif text == '⏪Назад' and stage ==63:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(60, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши десерты',reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back,korzina],
                                                                  resize_keyboard=True))

#ВСЕ ПО БАРУ

    elif text == 'Бар🥤':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(70, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([cool_hot,coffee,zakus_alco,back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage ==70:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(1001, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',reply_markup=ReplyKeyboardMarkup([shisha_button,kitchen_bar,back_korzina],
                                                                  resize_keyboard=True))
    elif text == 'Чаи':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(71, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([tea,brand_tea,back],
                                                                  resize_keyboard=True))



    elif text =='⏪Назад' and stage ==71:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(70, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([cool_hot,coffee,back_korzina], resize_keyboard=True))

    elif text =='Наглый фрукт':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(72, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


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
        zakaz = zakaz + '\n' + 'Наглый фрукт' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Наглый фрукт' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Наглый фрукт добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([cool_hot,coffee,korzina,back], resize_keyboard=True))


    elif text =='⏪Назад' and stage ==72:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(70, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([tea,brand_tea,korzina,back], resize_keyboard=True))



    elif text =='Ягодная бергамония':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(73, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 73:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(70, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Ягодная бергамония')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Ягодная бергамония' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Ягодная бергамония' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Ягодная бергамония добавлена в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([cool_hot,coffee,korzina,back], resize_keyboard=True))


    elif text == '⏪Назад' and stage == 73:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(70, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([tea, brand_tea,korzina, back], resize_keyboard=True))



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
        zakaz = zakaz + '\n' + 'Чай черный' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Чай черный' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id))
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='С Сахаром или без?',
                                 reply_markup=ReplyKeyboardMarkup([sugar, korzina, back], resize_keyboard=True))

    elif text=='⏪Назад' and stage == 74:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz.split()
        zakaz = zakaz[0:-4]
        zakaz = ' '.join(zakaz)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz.split()
        final_zakaz = final_zakaz[0:-4]
        final_zakaz = ' '.join(final_zakaz)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        cur.execute(update_stage_in.format(70, user_id))
        cur.execute(delete_total_zakaz.format(user_id))
        cur.execute(update_total_price.format(0,user_id))
        cur.execute(update_price.format(0,user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([tea, brand_tea,korzina, back],
                                                                  resize_keyboard=True))

    elif text =='С сахаром':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(75, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz + '\n' + text
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + text
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        context.bot.send_message(chat_id=user_id, text='С лимоном или без?',
                                 reply_markup=ReplyKeyboardMarkup([limon,back], resize_keyboard=True))

    elif text=='⏪Назад' and stage == 75:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cur.execute(delete_zakaz.format(user_id))
        cur.execute(delete_total_zakaz.format(user_id))
        cur.execute(update_total_price.format(0,user_id))
        cur.execute(update_price.format(0,user_id))

        cur.execute(update_stage_in.format(70, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([tea, brand_tea, korzina, back],
                                                                  resize_keyboard=True))

    elif text == 'Без сахара':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(76, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz + '\n' + text
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + text
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        context.bot.send_message(chat_id=user_id, text='С лимоном или без?',
                                 reply_markup=ReplyKeyboardMarkup([limon,back], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 76:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz.split()
        zakaz = zakaz[0:-2]
        zakaz = ' '.join(zakaz)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz.split()
        final_zakaz = final_zakaz[0:-2]
        final_zakaz = ' '.join(final_zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id))
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
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

        zakaz = zakaz + '\n' + 'С лимоном' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'С лимоном' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        cur.execute(update_stage_in.format(77, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 77:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz.split()
        zakaz = zakaz[0:-4]
        zakaz = ' '.join(zakaz)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz.split()
        final_zakaz = final_zakaz[0:-4]
        final_zakaz = ' '.join(final_zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id))
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(update_stage_in.format(75, user_id))
        context.bot.send_message(chat_id=user_id, text='С лимоном или без?',
                                 reply_markup=ReplyKeyboardMarkup([limon, back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 77:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        context.bot.send_message(chat_id=user_id, text='Чай добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([tea,brand_tea,korzina,back], resize_keyboard=True))

    elif text =='Без лимона':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz + '\n' + text
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + text
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        cur.execute(update_stage_in.format(78, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 78:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        context.bot.send_message(chat_id=user_id, text='Чай добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([tea, brand_tea, korzina, back],
                                                                  resize_keyboard=True))

    elif text == '⏪Назад' and stage == 78:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz.split()
        zakaz = zakaz[0:-2]
        zakaz = ' '.join(zakaz)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz.split()
        final_zakaz = final_zakaz[0:-2]
        final_zakaz = ' '.join(final_zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id))
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
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
        zakaz = zakaz + '\n' + 'Чай зеленый' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Чай зеленый' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id))
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='С Сахаром или без?',
                                 reply_markup=ReplyKeyboardMarkup([sugar, korzina, back], resize_keyboard=True))

    elif text=='⏪Назад' and stage == 80:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz.split()
        zakaz = zakaz[0:-4]
        zakaz = ' '.join(zakaz)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz.split()
        final_zakaz = final_zakaz[0:-4]
        final_zakaz = ' '.join(final_zakaz)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        cur.execute(update_stage_in.format(70, user_id))
        cur.execute(delete_total_zakaz.format(user_id))
        cur.execute(update_total_price.format(0,user_id))
        cur.execute(update_price.format(0,user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([tea, brand_tea,korzina, back],
                                                                  resize_keyboard=True))

    elif text =='С сахаром' and stage == 80:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(81, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz + '\n' + text
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + text
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        context.bot.send_message(chat_id=user_id, text='С лимоном или без?',
                                 reply_markup=ReplyKeyboardMarkup([limon,back], resize_keyboard=True))

    elif text=='⏪Назад' and stage == 81:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cur.execute(delete_zakaz.format(user_id))
        cur.execute(delete_total_zakaz.format(user_id))
        cur.execute(update_total_price.format(0,user_id))
        cur.execute(update_price.format(0,user_id))

        cur.execute(update_stage_in.format(70, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([tea, brand_tea, korzina, back],
                                                                  resize_keyboard=True))

    elif text == 'Без сахара':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(82, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz + '\n' + text
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + text
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        context.bot.send_message(chat_id=user_id, text='С лимоном или без?',
                                 reply_markup=ReplyKeyboardMarkup([limon,back], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 82:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(delete_zakaz.format(user_id))
        cur.execute(delete_total_zakaz.format(user_id))
        cur.execute(update_total_price.format(0,user_id))
        cur.execute(update_price.format(0,user_id))
        cur.execute(update_stage_in.format(70, user_id))

        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([tea, brand_tea, korzina, back],
                                                                  resize_keyboard=True))

    elif text =='С лимоном' and stage == 82:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('С лимоном')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'С лимоном' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'С лимоном' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        cur.execute(update_stage_in.format(83, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 83:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz.split()
        zakaz = zakaz[0:-4]
        zakaz = ' '.join(zakaz)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz.split()
        final_zakaz = final_zakaz[0:-4]
        final_zakaz = ' '.join(final_zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id))
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(update_stage_in.format(76, user_id))
        context.bot.send_message(chat_id=user_id, text='С лимоном или без?',
                                 reply_markup=ReplyKeyboardMarkup([limon, back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 77:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        context.bot.send_message(chat_id=user_id, text='Чай добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([tea,brand_tea,korzina,back], resize_keyboard=True))

    elif text =='Без лимона':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz + '\n' + text
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + text
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        cur.execute(update_stage_in.format(78, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 78:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        context.bot.send_message(chat_id=user_id, text='Чай добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([tea, brand_tea, korzina, back],
                                                                  resize_keyboard=True))

    elif text == '⏪Назад' and stage == 78:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        zakaz = zakaz.split()
        zakaz = zakaz[0:-2]
        zakaz = ' '.join(zakaz)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz.split()
        final_zakaz = final_zakaz[0:-2]
        final_zakaz = ' '.join(final_zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id))
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(update_stage_in.format(76, user_id))
        context.bot.send_message(chat_id=user_id, text='С лимоном или без?',
                                 reply_markup=ReplyKeyboardMarkup([limon, back], resize_keyboard=True))




#ВСЕ ПРО КОФЕ

    elif text =='Кофе':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(90, user_id))
        context.bot.send_message(chat_id=user_id, text='Кофе',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,korzina,back], resize_keyboard=True))

    elif text =='⏪Назад' and stage == 90:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(70, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([cool_hot, coffee,korzina, back], resize_keyboard=True))


    elif text =='Американо':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(91, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 91:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(90, user_id))

        cena = cur.execute(cost.format('Американо')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Американо' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Американо' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Американо добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,korzina,back], resize_keyboard=True))


    elif text =='⏪Назад' and stage == 91:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(90, user_id))
        context.bot.send_message(chat_id=user_id, text='Кофе',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,korzina,back], resize_keyboard=True))

    elif text =='Эспрессо':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(92, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 92:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cena = cur.execute(cost.format('Эспрессо')).fetchall()
        cena = cena[0][0]
        cur.execute(update_stage_in.format(90, user_id))

        zakaz = zakaz + '\n' + 'Эспрессо' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Эспрессо' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Эспрессо добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,korzina,back], resize_keyboard=True))


    elif text == '⏪Назад' and stage == 92:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(90, user_id))
        context.bot.send_message(chat_id=user_id, text='Кофе',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano, cap_latte, raf_frap,korzina, back],
                                                                  resize_keyboard=True))


    elif text =='Капучино':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(93, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 93:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(90, user_id))

        cena = cur.execute(cost.format('Капучино')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Капучино' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Капучино' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Капучино добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,korzina,back], resize_keyboard=True))


    elif text == '⏪Назад' and stage == 93:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(90, user_id))
        context.bot.send_message(chat_id=user_id, text='Кофе',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano, cap_latte, raf_frap,korzina, back],
                                                                  resize_keyboard=True))


    elif text =='Латте':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(94, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 94:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(90, user_id))

        cena = cur.execute(cost.format('Латте')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Латте' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Латте' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Латте добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,korzina,back], resize_keyboard=True))


    elif text == '⏪Назад' and stage == 94:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(90, user_id))
        context.bot.send_message(chat_id=user_id, text='Кофе',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano, cap_latte, raf_frap,korzina, back],
                                                                  resize_keyboard=True))


    elif text =='Раф':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(95, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 95:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(90, user_id))

        cena = cur.execute(cost.format('Раф')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Раф' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Раф' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Раф добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,korzina,back], resize_keyboard=True))


    elif text == '⏪Назад' and stage == 95:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(90, user_id))
        context.bot.send_message(chat_id=user_id, text='Кофе',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano, cap_latte, raf_frap,korzina, back],
                                                                  resize_keyboard=True))


    elif text =='Фраппучино':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(96, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 96:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(90, user_id))

        cena = cur.execute(cost.format('Фраппучино')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Фраппучино' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Фраппучино' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Фраппучино добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,korzina,back], resize_keyboard=True))




    elif text =='⏪Назад' and stage == 96:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(90, user_id))
        context.bot.send_message(chat_id=user_id, text='Кофе',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,korzina,back], resize_keyboard=True))

#ВСЕ ПРО ЛИМОНАДЫ

    elif text =='Лимонады':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(100, user_id))
        context.bot.send_message(chat_id=user_id, text='Лимонады',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,korzina, back],
                                                                  resize_keyboard=True))

    elif text == '⏪Назад' and stage == 100:

        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(70, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([cool_hot,coffee,korzina,back], resize_keyboard=True))

    elif text == 'Йерная ягода':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(101, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 101:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(100, user_id))

        cena = cur.execute(cost.format('Йерная ягода')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Йерная ягода' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Йерная ягода' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Йерная ягода добавлена в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,korzina, back],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 101:
        conn = sqlite3.connect('identifier.sqlite')
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(100, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,korzina, back], resize_keyboard=True))


    elif text == 'Цитрус-щавель':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(102, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 102:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(100, user_id))

        cena = cur.execute(cost.format('Цитрус-щавель')).fetchall()
        cena = cena[0][0]
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Цитрус-щавель' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Цитрус-щавель добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,korzina, back],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 102:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(100, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш  Бар',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys, mango_ice, moh_mango,korzina, back],
                                                                  resize_keyboard=True))


    elif text == 'Манго-маракуя':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(103, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 103:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(100, user_id))

        cena = cur.execute(cost.format('Манго-маракуя')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + 'Манго-маракуя' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Манго-маракуя' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Манго-маракуя добавлена в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,korzina, back],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 103:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(100, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши  Бар',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys, mango_ice, moh_mango,korzina, back],
                                                                  resize_keyboard=True))



    elif text == 'Айс-ти':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(104, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 104:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(100, user_id))

        cena = cur.execute(cost.format('Айс-ти')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Айс-ти' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Айс-ти' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Айс-ти добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,korzina, back],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 104:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(100, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши  Бар',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys, mango_ice, moh_mango,korzina, back],
                                                                  resize_keyboard=True))






    elif text == 'Мохито':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(105, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 105:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(100, user_id))

        cena = cur.execute(cost.format('Мохито')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Мохито' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Мохито' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Мохито добавлено в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,korzina, back],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 105:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(100, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши  Бар',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys, mango_ice, moh_mango,korzina, back],
                                                                  resize_keyboard=True))


    elif text == 'Манговый айс-ти':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(106, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 106:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Манговый айс-ти')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Манговый айс-ти' + ' - ' + str(cena)

        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Манговый айс-ти' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Манговый айс-ти добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,korzina, back],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 106:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(100, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши  Бар',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys, mango_ice, moh_mango,korzina, back],
                                                                  resize_keyboard=True))


#ВСЕ ПРО НАПИТКИ
    elif text == 'Напитки':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(110, user_id))
        context.bot.send_message(chat_id=user_id, text='Напитки',
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,korzina,back],
                                                                  resize_keyboard=True))

    elif text == '⏪Назад' and stage == 110:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(70, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([cool_hot, coffee,korzina, back],
                                                                  resize_keyboard=True))

    elif text == 'Red bull':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(111, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 111:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(110, user_id))

        cena = cur.execute(cost.format('Red bull')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Red bull' + ' - ' + str(cena)

        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Red bull' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Red bull добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,korzina,back],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 111:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(110, user_id))
        context.bot.send_message(chat_id=user_id, text='Напитки',
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,korzina,back],
                                                                  resize_keyboard=True))



    elif text == 'Borjomi':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(112, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 112:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(110, user_id))

        cena = cur.execute(cost.format('Borjomi')).fetchall()
        cena = cena[0][0]

        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Borjomi' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Borjomi добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,korzina,back],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 112:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(110, user_id))
        context.bot.send_message(chat_id=user_id, text='Напитки',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with,korzina, back],
                                     resize_keyboard=True))



    elif text == 'Coca-cola':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(113, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 113:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(110, user_id))

        cena = cur.execute(cost.format('Coca-cola')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Coca-cola' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Coca-cola' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Coca-cola добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,korzina,back],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 113:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(110, user_id))
        context.bot.send_message(chat_id=user_id, text='Напитки',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with,korzina, back],
                                     resize_keyboard=True))



    elif text == 'Sprite':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(114, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 114:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(110, user_id))

        cena = cur.execute(cost.format('Sprite')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Sprite' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Sprite' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Sprite добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,korzina,back],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage ==114:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(110, user_id))
        context.bot.send_message(chat_id=user_id, text='Напитки',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with,korzina, back],
                                     resize_keyboard=True))



    elif text == 'Сок':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(115, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 115:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(110, user_id))

        cena = cur.execute(cost.format('Сок')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Сок' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Сок' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Сок добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,korzina,back],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 115:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(110, user_id))
        context.bot.send_message(chat_id=user_id, text='Напитки',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with,korzina, back],
                                     resize_keyboard=True))


    elif text == 'Вода с газом':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(116, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 116:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(110, user_id))

        cena = cur.execute(cost.format('Вода с газом')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Вода с газом' + ' - ' + str(cena)

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Вода с газом' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Вода с газом добавлена в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,korzina,back],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 116:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(110, user_id))
        context.bot.send_message(chat_id=user_id, text='Напитки',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with,korzina, back],
                                     resize_keyboard=True))


    elif text == 'Вода':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(117, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 117:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(110, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cena = cur.execute(cost.format('Вода')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + 'Вода' + ' - ' + str(cena)

        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Вода' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz,user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo,user_id))
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Вода добавлена в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,korzina,back],
                                                                  resize_keyboard=True))


    elif text == '⏪Назад' and stage == 117:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(110, user_id))
        context.bot.send_message(chat_id=user_id, text='Напитки',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with,korzina, back],
                                     resize_keyboard=True))



    elif text == 'Fanta':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(118, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 118:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(110, user_id))

        cena = cur.execute(cost.format('Fanta')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Fanta' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Fanta' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Fanta добавлена в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with, korzina, back],
                                     resize_keyboard=True))


    elif text == '⏪Назад' and stage == 118:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(110, user_id))
        context.bot.send_message(chat_id=user_id, text='Напитки',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with, korzina, back],
                                     resize_keyboard=True))




    elif text == 'Закуски':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(120,user_id))
        context.bot.send_message(chat_id = user_id, text = 'Выбирай',reply_markup = ReplyKeyboardMarkup([sul_kurt,pring_mindal,phist_set,back_korzina]))

    elif text =='⏪Назад' and stage == 120:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(70, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([cool_hot,coffee,zakus_alco,back_korzina], resize_keyboard=True))


    elif text == 'Сулугуни':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(121, user_id))
        context.bot.send_message(chat_id=user_id, text='ф',
                         reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))


    elif text =='⏪Назад' and stage == 121:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(120, user_id))
        context.bot.send_message(chat_id=user_id, text = 'Выбирай',reply_markup = ReplyKeyboardMarkup([sul_kurt,pring_mindal,phist_set,back_korzina]))



    elif text == 'Добавить в заказ' and stage == 121:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(120, user_id))

        cena = cur.execute(cost.format('Сулугуни')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Сулугуни' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Сулугуни' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Сулугуни добавлены в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup(
                                     [sul_kurt,pring_mindal,phist_set,back_korzina],
                                     resize_keyboard=True))

    elif text == 'Курт':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(122, user_id))
        context.bot.send_message(chat_id=user_id, text='ф',
                         reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))

    elif text =='⏪Назад' and stage == 122:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(120, user_id))
        context.bot.send_message(chat_id=user_id, text = 'Выбирай',reply_markup = ReplyKeyboardMarkup([sul_kurt,pring_mindal,phist_set,back_korzina]))


    elif text == 'Добавить в заказ' and stage == 122:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(120, user_id))

        cena = cur.execute(cost.format('Курт')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Курт' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Курт' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Курт добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup(
                                     [sul_kurt,pring_mindal,phist_set,back_korzina],
                                     resize_keyboard=True))




    elif text == 'Pringles':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(123, user_id))
        context.bot.send_message(chat_id=user_id, text='ф',
                         reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))


    elif text =='⏪Назад' and stage == 123:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(120, user_id))
        context.bot.send_message(chat_id=user_id, text = 'Выбирай',reply_markup = ReplyKeyboardMarkup([sul_kurt,pring_mindal,phist_set,back_korzina]))


    elif text == 'Добавить в заказ' and stage == 123:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(120, user_id))

        cena = cur.execute(cost.format('Pringles')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Pringles' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Pringles' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Pringles добавлены в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup(
                                     [sul_kurt,pring_mindal,phist_set,back_korzina],
                                     resize_keyboard=True))

    elif text == 'Миндаль':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(124, user_id))
        context.bot.send_message(chat_id=user_id, text='ф',
                         reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))


    elif text =='⏪Назад' and stage == 124:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(120, user_id))
        context.bot.send_message(chat_id=user_id, text = 'Выбирай',reply_markup = ReplyKeyboardMarkup([sul_kurt,pring_mindal,phist_set,back_korzina]))


    elif text == 'Добавить в заказ' and stage == 124:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(120, user_id))

        cena = cur.execute(cost.format('Миндаль')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Миндаль' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Миндаль' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Миндаль добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup(
                                     [sul_kurt,pring_mindal,phist_set,back_korzina],
                                     resize_keyboard=True))

    elif text == 'Фисташки':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(125, user_id))
        context.bot.send_message(chat_id=user_id, text='ф',
                         reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 125:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(120, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([sul_kurt, pring_mindal, phist_set, back_korzina]))


    elif text == 'Добавить в заказ' and stage == 125:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(120, user_id))

        cena = cur.execute(cost.format('Фисташки')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Фисташки' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Фисташки' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Фисташки добавлены в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup(
                                     [sul_kurt,pring_mindal,phist_set,back_korzina],
                                     resize_keyboard=True))
    elif text == 'Сэт грызун':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(126, user_id))
        context.bot.send_message(chat_id=user_id, text='ф',
                         reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))

    elif text =='⏪Назад' and stage == 126:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(120, user_id))
        context.bot.send_message(chat_id=user_id, text = 'Выбирай',reply_markup = ReplyKeyboardMarkup([sul_kurt,pring_mindal,phist_set,back_korzina]))



    elif text == 'Добавить в заказ' and stage == 126:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cur.execute(update_stage_in.format(120, user_id))

        cena = cur.execute(cost.format('Сэт грызун')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Сэт грызун' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Сэт грызун' + ' - ' + str(cena)
        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))
        context.bot.send_message(chat_id=user_id, text='Сэт грызун добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup(
                                     [sul_kurt,pring_mindal,phist_set,back_korzina],
                                     resize_keyboard=True))




    elif text == 'Алкоголь':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(130, user_id))
        context.bot.send_message(chat_id=user_id, text='Приятного отдыха😊',
                         reply_markup=ReplyKeyboardMarkup([hard_light,kokteli,back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 130:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(70, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([cool_hot, coffee, zakus_alco, back_korzina],
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
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([hard_light,kokteli,back_korzina],
                                                                  resize_keyboard=True))
#ВСЕ ПРО ВИСКИ


    elif text == 'Виски' and stage == 131:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(132, user_id))
        context.bot.send_message(chat_id=user_id, text='Отличный выбор',
                                 reply_markup=ReplyKeyboardMarkup([chivas_jag,jack_tull,jame_bal,back_korzina], resize_keyboard=True))

    elif text == '⏪Назад' and stage == 132:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(131, user_id))
        context.bot.send_message(chat_id=user_id, text='Приятного отдыха😊',
                         reply_markup=ReplyKeyboardMarkup([viski_kon,liker_rom,djin_tekila, back_korzina], resize_keyboard=True))


    elif text == 'Jack Daniels' and stage == 132:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(133, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''Описание : {},
Цена : {}'''.format(a,b),reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 133:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(132, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Jack Daniels')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + 'Jack Daniels' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Jack Daniels' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
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

    elif text == 'Jack Daniels' and stage == 132:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(133, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''Описание : {},
Цена : {}'''.format(a, b), reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 133:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(132, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Jack Daniels')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + 'Jack Daniels' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Jack Daniels' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
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

    elif text == 'Chivas Regal 12' and stage == 132:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(134, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''Описание : {},
Цена : {}'''.format(a, b), reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 134:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(132, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Chivas Regal 12')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + 'Chivas Regal 12' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Chivas Regal 12' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
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
        context.bot.send_message(chat_id=user_id, text='''Описание : {},
Цена : {}'''.format(a, b), reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 135:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(132, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Tullamore Dew')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + 'Tullamore Dew' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Tullamore Dew' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
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
        context.bot.send_message(chat_id=user_id, text='''Описание : {},
Цена : {}'''.format(a, b), reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 136:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(132, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Jameson')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + 'Jameson' + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + 'Jameson' + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
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

    elif text == 'Jagermeister' and stage == 132:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(139, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''Описание : {},
Цена : {}'''.format(a, b), reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 139:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(132, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Jagermeister')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + "Jagermeister" + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + "Jagermeister" + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Отличный выбор',
                                 reply_markup=ReplyKeyboardMarkup([chivas_jag, jack_tull, jame_bal, back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 139:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(132, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([chivas_jag, jack_tull, jame_bal, back_korzina],
                                                                  resize_keyboard=True))

    elif text == 'Ballantines' and stage == 132:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(137, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''Описание : {},
Цена : {}'''.format(a, b), reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 137:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(132, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Ballantines')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + "Ballantines" + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + "Ballantines" + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
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
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
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
        context.bot.send_message(chat_id=user_id, text='''Описание : {},
Цена : {}'''.format(a, b), reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 141:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(140, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Shirins Peach')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + "Shirins Peach" + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + "Shirins Peach" + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
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
        context.bot.send_message(chat_id=user_id, text='''Описание : {},
Цена : {}'''.format(a, b), reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 142:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(140, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Aperol spritz')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + "Aperol spritz" + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + "Aperol spritz" + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
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
        context.bot.send_message(chat_id=user_id, text='''Описание : {},
Цена : {}'''.format(a, b), reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 143:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(140, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Gin tonic')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + "Gin tonic" + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + "Gin tonic" + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
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
        context.bot.send_message(chat_id=user_id, text='''Описание : {},
Цена : {}'''.format(a, b), reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 144:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(140, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Meva-Cheva')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + "Meva-Cheva" + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + "Meva-Cheva" + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Отличный выбор',
                                 reply_markup=ReplyKeyboardMarkup([shirin, aper_meva, gin_teq, back_korzina],
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
        context.bot.send_message(chat_id=user_id, text='''Описание : {},
Цена : {}'''.format(a, b), reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 145:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(145, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Tequila Sunrise')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + "Tequila Sunrise" + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + "Tequila Sunrise" + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
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
        context.bot.send_message(chat_id=user_id, text='Приятного отдыха😊',
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
        context.bot.send_message(chat_id=user_id, text='''Описание : {},
Цена : {}'''.format(a, b), reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 151:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(145, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('J.Wray Silver')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + "J.Wray Silver" + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + "J.Wray Silver" + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
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
        context.bot.send_message(chat_id=user_id, text='''Описание : {},
Цена : {}'''.format(a, b), reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 153:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(145, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Capitan Morgan')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + "Capitan Morgan" + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + "Capitan Morgan" + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
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
        context.bot.send_message(chat_id=user_id, text='''Описание : {},
Цена : {}'''.format(a, b), reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 152:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(145, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('J.Wray Gold')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + "J.Wray Gold" + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + "J.Wray Gold" + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
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
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        context.bot.send_message(chat_id=user_id, text='''Описание : {},
        Цена : {}'''.format(a, b), reply_markup=ReplyKeyboardMarkup([add_zakaz, korzina, back], resize_keyboard=True))



    elif text == 'Добавить в заказ' and stage == 161:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(160, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Tanbour')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + "Tanbour" + ' - ' + str(cena)
        final_zakaz = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        final_zakaz = final_zakaz[0][0]
        final_zakaz = final_zakaz + '\n' + "Tanbour" + ' - ' + str(cena)

        cur.execute(update_total_zakaz.format(final_zakaz, user_id))
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena

        itogo = cur.execute(get_price.format(user_id)).fetchall()
        itogo = itogo[0][0]
        itogo = itogo + cena
        cur.execute(update_price.format(itogo, user_id))
        cur.execute(update_total_price.format(itog, user_id))

        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Отличный выбор',
                                 reply_markup=ReplyKeyboardMarkup([tanb,back_korzina],
                                                                  resize_keyboard=True))



    elif text == '⏪Назад' and stage == 152:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(131, user_id))
        context.bot.send_message(chat_id=user_id, text='Продолжим?😉',
                                 reply_markup=ReplyKeyboardMarkup([viski_kon, liker_rom, djin_tekila, back_korzina],
                                                                  resize_keyboard=True))




    elif text == 'Мой заказ📝':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        x = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        x = x[0][0]
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        if len(x) != 0:
            context.bot.send_message(chat_id = user_id,text = '''Ваш заказ :{}
            
Итоговая стоимость: {}'''.format(x,itog),reply_markup = ReplyKeyboardMarkup([ready,delete,back],resize_keyboard=True))
        else:
            context.bot.send_message(chat_id = user_id,text = 'Ваш заказ пуст😔')

        y = x.split()
        print(y)
        for i in y:
            if i.isalpha():
                context.bot.send_message()



    elif text == 'Заказать✅':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        x = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        x = x[0][0]
        a = cur.execute(table_number_in_table.format(user_id)).fetchall()
        cur.execute(update_total_price.format(0,user_id))
        cur.execute(delete_zakaz.format(user_id))
        cur.execute(update_stage_in.format(1001,user_id))


        context.bot.send_message(chat_id = user_id, text = 'Ваш заказ принят и очень скоро будет готов!',
                                 reply_markup = ReplyKeyboardMarkup([top_button,mid_button,bot_button,order_button],resize_keyboard=True))
        context.bot.send_message(chat_id = 44335784,text = 'Заказ за стол № {} , {}'.format(a[0][0],x))




    elif text == 'Очистить заказ':
        cur.execute(delete_zakaz.format(user_id))
        cur.execute(update_total_price.format(0,user_id))
        cur.execute(update_stage_in.format(1001,user_id))
        context.bot.send_message(chat_id = user_id,text = 'Ваш заказ очищен',reply_markup = ReplyKeyboardMarkup([top_button,mid_button,bot_button,order_button],resize_keyboard=True))



    elif text =='Позвать Таймгарда🏃':
        a = cur.execute(table_number_in_table.format(user_id)).fetchall()
        print(a[0][0])
        context.bot.send_message(chat_id=user_id, text='Так Точно💪!')



    elif text == 'Продуть Кальян💨':
        a = cur.execute(table_number_in_table.format(user_id)).fetchall()
        context.bot.send_message(chat_id=user_id, text='Понял Принял👌')


    elif text == 'Попросить счет💵':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()

        x = cur.execute(get_total_zakaz.format(user_id)).fetchall()
        x = x[0][0]
        y = cur.execute(get_price.format(user_id)).fetchall()
        y = y[0][0]

        a = cur.execute(table_number_in_table.format(user_id)).fetchall()
        context.bot.send_message(chat_id=user_id, text='''Прошу вас, ваш Чек
        
{}
Итоговая стоимость - {}'''.format(x,y),
                                 reply_markup=ReplyKeyboardMarkup(
                                     [payme_click,nal,back], resize_keyboard=True,
                                     one_time_keyboard=True))

    elif text == '⏪Назад':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(1001,user_id))
        context.bot.send_message(chat_id = user_id,text = 'Прекрасного времени провождения😊',
                                 reply_markup = ReplyKeyboardMarkup([top_button,mid_button,bot_button,order_button],resize_keyboard=True))


    elif text.isdigit() and text not in allowed_tables:
        context.bot.send_message(chat_id = user_id,text = 'У нас нет такого стола')



    else:
        a = cur.execute(table_number_in_table.format(user_id)).fetchall()
        context.bot.send_message(chat_id = user_id,text = "Сейчас все будет!")
        datetime = time.asctime()
        Logpath = 'answers.txt'
        log = open(Logpath, 'a')
        logstr = "{} | user_id:{}, Что выбрал: {} \n".format(datetime, user_id, text)
        log.writelines(logstr)

    conn.commit()


