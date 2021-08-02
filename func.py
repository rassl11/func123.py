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
    id_in = cur.execute(id_in_table.format(user_id)).fetchall()
    print(id_in)
    cur.execute(update_stage_in.format(999,user_id))
    conn.commit()


    try:
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

    elif text == 'Сделать заказ' and stage == 1001:
        context.bot.send_message(chat_id = user_id,text = 'Выбирай',reply_markup = ReplyKeyboardMarkup([kitchen_button,shisha_button,bar_button,back],resize_keyboard=True))

    elif text == 'Назад' and stage == 1001:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        context.bot.send_message(chat_id = user_id,text = 'Прекрасного времени провождения😊',
                                 reply_markup = ReplyKeyboardMarkup([top_button,mid_button,bot_button,order_button],resize_keyboard=True))

#все про кальяны

    elif text == 'Кальян':
        context.bot.send_message(chat_id = user_id,text = "Какой крепости кальян",reply_markup = ReplyKeyboardMarkup([easy,medium,rare,back],resize_keyboard=True))




    elif text == 'Назад' and stage == 1:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(1001,user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([kitchen_button, shisha_button, bar_button, back],
                                                                  resize_keyboard=True))

    elif text =='Легкий' or text == 'Средний' or text == 'Крепкий':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(2, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)

        zakaz = zakaz + '\n' + text
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        context.bot.send_message(chat_id = user_id,text = 'Что по вкусам?',
                                 reply_markup = ReplyKeyboardMarkup([berry,fruit,desert,citrus,back],resize_keyboard=True))

    elif text == 'Назад' and stage == 2:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(1, user_id))
        context.bot.send_message(chat_id=user_id, text='Какой крепости кальян',
                                 reply_markup=ReplyKeyboardMarkup([easy,medium,rare,back],resize_keyboard=True))


    elif text == 'Ягодный' or text == 'Фруктовый' or text == 'Цитрусовый' or text =='Десертный':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(3, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)

        zakaz = zakaz + '\n' + text
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        context.bot.send_message(chat_id=user_id, text='Тип курения?',
                                 reply_markup=ReplyKeyboardMarkup([folga,kolaud,back], resize_keyboard=True))


    elif text == 'Назад' and stage == 3:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(2, user_id))
        context.bot.send_message(chat_id=user_id, text='Что по вкусам?',
                                 reply_markup = ReplyKeyboardMarkup([berry,fruit,desert,citrus,back],resize_keyboard=True))



    elif text == 'Калауд' or text == 'Фольга':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(4, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)

        zakaz = zakaz + '\n' + text
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        context.bot.send_message(chat_id = user_id,text = 'С холодком или без?',reply_markup = ReplyKeyboardMarkup([ice,no_ice,back],resize_keyboard=True))


    elif text == 'Назад' and stage == 4:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(3, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup = ReplyKeyboardMarkup([folga,kolaud,back],resize_keyboard=True))



    elif text == 'С холодком' or text == 'Без Холодка':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(5, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)

        zakaz = zakaz + '\n' + text
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        context.bot.send_message(chat_id = user_id, text = 'Отлично,добавляем в заказ?',
                                 reply_markup = ReplyKeyboardMarkup([add_zakaz,korzina,back],resize_keyboard=True))

    elif text == 'Назад' and stage == 5:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(4, user_id))
        context.bot.send_message(chat_id=user_id, text='С холодком или без?',
                                 reply_markup = ReplyKeyboardMarkup([ice,no_ice,back],resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 5:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cur.execute(update_stage_in.format(7, user_id))
        cena = cur.execute(cost.format('Кальян')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + 'Кальян' + ' - ' + str(cena)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog, user_id))
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        context.bot.send_message(chat_id = user_id, text = 'Продолжим?',
                                 reply_markup=ReplyKeyboardMarkup([kitchen_button, shisha_button, bar_button,korzina ,back],
                                                                  resize_keyboard=True))




# всепро кухню

    elif text=='Кухня':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(6, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([soups_hot,pasta_fasfood,salad_garnir,desserts,back]))

    elif text =='Назад' and stage == 6:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(0, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([kitchen_button, shisha_button, bar_button, back],
                                                                  resize_keyboard=True))
#ВСЕ ПРО СУПЫ

    elif text == 'Супы':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(7, user_id))
        context.bot.send_message(chat_id = user_id,text ='Наши супы',
                                 reply_markup = ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava,korzina,back],resize_keyboard=True))

    elif text == 'Назад' and stage ==7:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(6, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([soups_hot,pasta_fasfood,salad_garnir,desserts,back],
                                                                  resize_keyboard=True))


    elif text == 'Окрошка' and stage == 7:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(8, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]

        context.bot.send_photo(photo = ('https://ibb.co/tzHFGG1'),chat_id= user_id,caption='''Описание :{}
Цена: {}'''.format(a,b),reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back],resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 8:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cur.execute(update_stage_in.format(7, user_id))
        cena = cur.execute(cost.format('Окрошка')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + 'Окрошка' + ' - ' + str(cena)
        a = cur.execute(sql_set_zakaz.format(zakaz,user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))

        conn.commit()

        context.bot.send_message(chat_id = user_id,text = 'Окрошка добавлена  в заказ'.format(text),reply_markup = ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava,korzina,back],resize_keyboard=True))



    elif text == 'Назад' and stage ==8:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(7, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши супы',
                                 reply_markup=ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava, back,korzina],
                                                                  resize_keyboard=True))

    elif text == 'Кук-си' and stage == 7:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(100, user_id))
        conn.commit()
        context.bot.send_message(chat_id = user_id,text = 'asd',reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back],resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 100:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Кук-си')).fetchall()
        cena = cena[0][0]


        zakaz = zakaz + '\n' + 'Кук-си' + ' - ' + str(cena)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        conn.commit()
        context.bot.send_message(chat_id=user_id, text='Кук-си добавлена  в заказ'.format(text))
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))



    elif text == 'Назад' and stage ==100:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(7, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши супы',
                                 reply_markup=ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava, back,korzina],
                                                                  resize_keyboard=True))

    elif text =='Рамен' and stage == 7:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(101, user_id))
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        c = cur.execute(photo.format(text)).fetchall()
        c = c[0][0]

        cur.execute(update_stage_in.format(102, user_id))
        context.bot.send_photo(photo=('https://ibb.co/dWSpDVT'), chat_id=user_id, caption='''Описание :{}
Цена: {}'''.format(a, b),reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back],resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 102:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Рамен')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Рамен' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz,user_id)).fetchall()
        print(a)
        context.bot.send_message(chat_id = user_id,text = 'Рамен добавлен в заказ'.format(text))
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))




    elif text == 'Назад' and stage ==102:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(7, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши супы',
                                 reply_markup=ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava, back,korzina],
                                                                  resize_keyboard=True))

    elif text =='Мастава' and stage == 7:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(101, user_id))
        context.bot.send_message(chat_id = user_id,text ='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back],resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 101:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        cena = cur.execute(cost.format('Мастава')).fetchall()
        cena = cena[0][0]
        zakaz = zakaz + '\n' + 'Рамен' + ' - ' + str(cena)
        a = cur.execute(sql_set_zakaz.format(zakaz,user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))

        context.bot.send_message(chat_id = user_id,text = 'Мастава добавлена в заказ'.format(text))





    elif text == 'Назад' and stage ==101:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(7, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши супы',
                                 reply_markup=ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava, back,korzina],
                                                                  resize_keyboard=True))

#ВСЕ ПРО ГОРЯЧЕЕ

    elif text == 'Горячее':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(9, user_id))
        context.bot.send_message(chat_id=user_id, text='Горячие блюда',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))
    elif text == 'Назад' and stage==9:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(6, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([soups_hot,pasta_fasfood,salad_garnir,desserts,korzina,back],
                                                                  resize_keyboard=True))
    elif text == 'Рибай стейк':
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
        print(zakaz)
        cena = cur.execute(cost.format('Рибай стейк')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Рибай стейк' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz,user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id = user_id,text = 'Рибай стейк добавлен в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))


    elif text == 'Назад' and stage == 104:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(9, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))
    elif text == 'Медальоны':
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

        cena = cur.execute(cost.format('Медальоны')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Медальоны' + ' - ' + str(cena)

        a = cur.execute(sql_set_zakaz.format(zakaz,user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))

        context.bot.send_message(chat_id = user_id,text = 'Медальоны добавлены в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))


    elif text == 'Назад' and stage == 105:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(9, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))

    elif text == 'Говядина в сливочном соусе':
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
        cena = cur.execute(cost.format('Говядина в сливочном соусе')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Говядина в сливочном соусе' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz,user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id = user_id,text = 'Говядина в сливочном соусе добавлена в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))




    elif text == 'Назад' and stage == 106:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(9, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))
    elif text == 'Курица на грилле':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(107, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 107:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Курица на грилле')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Курица на грилле' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz,user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id = user_id,text = 'Курица на грилле добавлена в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))



    elif text == 'Назад' and stage == 107:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(9, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))
    elif text == 'Картошка по-домашнему':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(108, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 108:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Картошка по-домашнему')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Картошка по-домашнему' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz,user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id = user_id,text = 'Картошка по-домашнему добавлена в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))



    elif text == 'Назад' and stage == 108:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(9, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))
    elif text == 'Мясо по-китайский':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(109, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 109:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Мясо по-китайский')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Мясо по-китайский' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz,user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id = user_id,text = 'Мясо по-китайский добавлена в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))



    elif text == 'Назад' and stage == 109:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(9, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))

    elif text == 'Стейк куриный':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(110, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 110:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Стейк куриный')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Стейк куриный' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz,user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id = user_id,text = 'Стейк куриный добавлен в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                                                  resize_keyboard=True))



    elif text == 'Назад' and stage == 110:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(9, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak,korzina],
                                     resize_keyboard=True))


#ВСЕ ПРО ПАСТЫ

    elif text=='Пасты':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(11, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши пасты',
                                reply_markup=ReplyKeyboardMarkup([alfredo,boloneze,korzina,back], resize_keyboard=True))

    elif text == 'Назад' and stage == 11:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(6, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши супы',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [soups_hot,pasta_fasfood,salad_garnir, desserts,korzina, back],
                                     resize_keyboard=True))

    elif text =='Альфредо':
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
        print(zakaz)
        cena = cur.execute(cost.format('Альфредо')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Альфредо' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz,user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id = user_id,text = 'Альфредо добавлено в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([alfredo,boloneze,korzina,back], resize_keyboard=True))

    elif text == 'Назад' and stage == 111:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(11, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши пасты',
                                 reply_markup=ReplyKeyboardMarkup([alfredo,boloneze,korzina,back],resize_keyboard=True))

    elif text =='Болоньезе':
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
        print(zakaz)
        cena = cur.execute(cost.format('Болоньезе')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Болоньезе' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz,user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id = user_id,text = 'Болоньезе добавлено в заказ'.format(text),reply_markup=ReplyKeyboardMarkup([alfredo,boloneze,korzina,back], resize_keyboard=True))

    elif text == 'Назад' and stage == 112:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(11, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши пасты',
                                 reply_markup=ReplyKeyboardMarkup([alfredo,boloneze,korzina,back],resize_keyboard=True))

#ВСЕ ПРО ФАСТ-ФУД

    elif text =='Фаст-Фуд':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(14, user_id))
        context.bot.send_message(chat_id=user_id, text='Категория Фаст-Фуд',
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,korzina,back],resize_keyboard=True))

    elif text == 'Назад' and stage == 14:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(6, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши супы',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [soups_hot,pasta_fasfood,salad_garnir, desserts,korzina, back],
                                     resize_keyboard=True))

    elif text =='Буррито':
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
        print(zakaz)
        cena = cur.execute(cost.format('Буррито')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Буррито' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Буррито добавлено в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,korzina,back],resize_keyboard=True))

    elif text == 'Назад' and stage == 113:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(14, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,korzina,back],
                                                                  resize_keyboard=True))

    elif text =='Наггетсы':
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

        cena = cur.execute(cost.format('Наггетсы')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Наггетсы' + ' - ' + str(cena)

        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Наггетсы добавлены в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,korzina,back],resize_keyboard=True))


    elif text == 'Назад' and stage == 114:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(14, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,korzina,back],
                                                                  resize_keyboard=True))


    elif text =='Гарлики':
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
        print(zakaz)
        cena = cur.execute(cost.format('Гарлики')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Гарлики' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Гарлики добавлены в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,korzina,back],resize_keyboard=True))


    elif text == 'Назад' and stage == 115:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(14, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [burrito_sandwich, nuggets_garlic, korzina, back],
                                     resize_keyboard=True))
    elif text =='Куриный Сэндвич':
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
        print(zakaz)
        cena = cur.execute(cost.format('Куриный сэндвич')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Куриный сэндвич' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Куриный сэндвич добавлен в заказ'.format(text))

    elif text == 'Назад' and stage == 116:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(14, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [burrito_sandwich,nuggets_garlic,korzina,back],
                                     resize_keyboard=True))

#ВСЕ ПРО САЛАТЫ

    elif text == 'Салаты':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(17, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши Салаты',
                                 reply_markup=ReplyKeyboardMarkup([greek_achik,korzina, back],
                                                                  resize_keyboard=True))

    elif text == 'Назад' and stage == 17:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(6, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup = ReplyKeyboardMarkup([soups_hot, pasta_fasfood, salad_garnir, desserts,korzina, back], resize_keyboard=True))

    elif text == 'Греческий салат':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(118, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 118:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Греческий салат')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Греческий салат' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Греческий салат добавлен в заказ'.format(text),
                                 reply_markup = ReplyKeyboardMarkup([soups_hot, pasta_fasfood, salad_garnir, desserts,korzina, back], resize_keyboard=True))

    elif text == 'Назад' and stage == 118:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(17, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup = ReplyKeyboardMarkup([greek_achik,korzina, back], resize_keyboard=True))

    elif text == 'Ачик-чучук':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(119, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 119:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Ачик-чучук')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Ачик-чучук' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Ачик-чучук добавлен в заказ'.format(text),
                                 reply_markup = ReplyKeyboardMarkup([soups_hot, pasta_fasfood, salad_garnir, desserts,korzina, back], resize_keyboard=True))


    elif text == 'Назад' and stage == 119:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(17, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup = ReplyKeyboardMarkup([greek_achik,korzina, back], resize_keyboard=True))

#ВСЕ ПРО ГАРНИРЫ

    elif text=='Гарниры':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(20, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши гарниры',
                                 reply_markup=ReplyKeyboardMarkup([grilveg_fries,ris_derev,aydaho_back,korzina], resize_keyboard=True))

    elif text == 'Назад' and stage ==20:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(6, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',reply_markup=ReplyKeyboardMarkup(
                                     [soups_hot, pasta_fasfood, salad_garnir, desserts,korzina, back], resize_keyboard=True))

    elif text=='Овощи на грилле':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(210, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 210:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Овощи на грилле')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Овощи на грилле' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Овощи на грилле добавлены в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([grilveg_fries,ris_derev,aydaho_back,korzina], resize_keyboard=True))


    elif text == 'Назад' and stage ==210:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(20, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши гарниры',reply_markup=ReplyKeyboardMarkup([grilveg_fries, ris_derev, aydaho_back,korzina],
                                                                  resize_keyboard=True))


    elif text=='Картофель по-деревенски':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(211, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 211:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Картофель по-деревенски')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Картофель по-деревенски' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Картофель по-деревенски добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([grilveg_fries,ris_derev,aydaho_back,korzina], resize_keyboard=True))




    elif text == 'Назад' and stage ==211:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(20, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши гарниры',reply_markup=ReplyKeyboardMarkup([grilveg_fries, ris_derev, aydaho_back,korzina,],
                                                                  resize_keyboard=True))


    elif text=='Рис':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(212, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 212:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Рис')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Рис' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Рис добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([grilveg_fries,ris_derev,aydaho_back,korzina], resize_keyboard=True))


    elif text == 'Назад' and stage ==212:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(20, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши гарниры',reply_markup=ReplyKeyboardMarkup([grilveg_fries, ris_derev, aydaho_back,korzina],
                                                                  resize_keyboard=True))

    elif text=='Фри':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(213, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 213:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Фри')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Фри' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Фри добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([grilveg_fries,ris_derev,aydaho_back,korzina], resize_keyboard=True))

    elif text == 'Назад' and stage ==213:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(20, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши гарниры',reply_markup=ReplyKeyboardMarkup([grilveg_fries, ris_derev, aydaho_back,korzina],
                                                                  resize_keyboard=True))



    elif text=='Картофель айдахо':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(214, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 214:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Картофель айдахо')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Картофель айдахо' + ' - ' + str(cena)

        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Картофель айдахо добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([grilveg_fries,ris_derev,aydaho_back,korzina], resize_keyboard=True))


    elif text == 'Назад' and stage ==214:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(20, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши гарниры',reply_markup=ReplyKeyboardMarkup([grilveg_fries, ris_derev, aydaho_back,korzina],
                                                                  resize_keyboard=True))

#ВСЕ ПРО ДЕСЕРТЫ

    elif text=='Десерты':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(23, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back], resize_keyboard=True))

    elif text == 'Назад' and stage ==23:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(6, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',reply_markup=ReplyKeyboardMarkup([soups_hot, pasta_fasfood, salad_garnir, desserts,korzina, back],
                                                                  resize_keyboard=True))

    elif text == 'Чизкейк':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(240, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 240:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Чизкейк')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Чизкейк' + ' - ' + str(cena)

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Чизкейк добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back], resize_keyboard=True))


    elif text == 'Назад' and stage ==240:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(23, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши десерты',reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back,korzina],
                                                                  resize_keyboard=True))

    elif text == 'Медовик':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(241, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 241:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]

        cena = cur.execute(cost.format('Медовик')).fetchall()
        cena = cena[0][0]

        zakaz = zakaz + '\n' + 'Медовик' + ' - ' + str(cena)

        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Медовик добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back], resize_keyboard=True))



    elif text == 'Назад' and stage ==241:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(23, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши десерты',reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back,korzina,],
                                                                  resize_keyboard=True))


    elif text == 'Брауни':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(242, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 242:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Брауни')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Брауни' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Брауни добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back], resize_keyboard=True))



    elif text == 'Назад' and stage ==242:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(23, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши десерты',reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back,korzina],
                                                                  resize_keyboard=True))

#ВСЕ ПО БАРУ

    elif text == 'Бар':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([cool_hot,coffee,korzina,back], resize_keyboard=True))

    elif text == 'Назад' and stage ==26:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(0, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',reply_markup=ReplyKeyboardMarkup([kitchen_button, shisha_button, bar_button,korzina, back],
                                                                  resize_keyboard=True))
    elif text == 'Чаи':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(27, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([tea,brand_tea,back],
                                                                  resize_keyboard=True))



    elif text =='Назад' and stage ==27:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([cool_hot,coffee,korzina,back], resize_keyboard=True))

    elif text =='Наглый фрукт':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(280, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 280:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Наглый фрукт')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Наглый фрукт' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Наглый фрукт добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([cool_hot,coffee,korzina,back], resize_keyboard=True))


    elif text =='Назад' and stage ==280:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([tea,brand_tea,korzina,back], resize_keyboard=True))



    elif text =='Ягодная бергамония':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(281, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 281:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Ягодная бергамония')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Ягодная бергамония' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Ягодная бергамония добавлена в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([cool_hot,coffee,korzina,back], resize_keyboard=True))


    elif text == 'Назад' and stage == 281:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([tea, brand_tea,korzina, back], resize_keyboard=True))



    elif text == 'Черный чай':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(282, user_id))
        context.bot.send_message(chat_id=user_id, text='С Сахаром или без?',
                                 reply_markup=ReplyKeyboardMarkup([sugar,korzina, back], resize_keyboard=True))

    elif text == 'С Сахаром или без?' and stage == 282:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Черный чай')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Черный чай' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        print(a)
        context.bot.send_message(chat_id=user_id, text='Черный чай добавлен в заказ'.format(text))


    elif text=='Назад' and stage == 282:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([tea, brand_tea,korzina, back],
                                                                  resize_keyboard=True))

    elif text == 'Зеленый чай':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(283, user_id))
        context.bot.send_message(chat_id=user_id, text='С Сахаром или без?',
                                 reply_markup=ReplyKeyboardMarkup([sugar,korzina, back], resize_keyboard=True))


    elif text=='Назад' and stage == 283:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([tea, brand_tea,korzina, back],
                                                                  resize_keyboard=True))


    elif text == 'С Сахаром или без?' and stage == 283:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Зеленый чай')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Зеленый чай' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        print(a)
        context.bot.send_message(chat_id=user_id, text='Зеленый чай добавлен в заказ'.format(text))


    elif text =='С сахаром':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(29, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('С сахаром')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'С сахаром' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        print(a)
        context.bot.send_message(chat_id=user_id, text='С лимоном или без?',
                                 reply_markup=ReplyKeyboardMarkup([limon,back], resize_keyboard=True))

    elif text == 'Без':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(29, user_id))
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Без')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Без' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        print(a)
        context.bot.send_message(chat_id=user_id, text='С лимоном или без?',
                                 reply_markup=ReplyKeyboardMarkup([limon,back], resize_keyboard=True))

    elif text == 'Назад' and stage == 29:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(28, user_id))
        context.bot.send_message(chat_id=user_id, text='С Сахаром или без?',
                                 reply_markup=ReplyKeyboardMarkup([sugar, back], resize_keyboard=True))

    elif text =='С лимоном':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(30, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 30:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('С лимоном')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'С лимоном' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        print(a)
        context.bot.send_message(chat_id=user_id, text='Чай добавлен в заказ'.format(text))



    elif text =='Без лимона':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(30, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 30:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Без лимона')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Без лимона' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        print(a)
        context.bot.send_message(chat_id=user_id, text='Чай добавлен в заказ'.format(text))


    elif text =='Назад' and stage == 30:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(29, user_id))
        context.bot.send_message(chat_id=user_id, text='С лимоном или без?',
                                 reply_markup=ReplyKeyboardMarkup([limon,back], resize_keyboard=True))

#ВСЕ ПРО КОФЕ

    elif text =='Кофе':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(32, user_id))
        context.bot.send_message(chat_id=user_id, text='Кофе',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,korzina,back], resize_keyboard=True))

    elif text =='Назад' and stage == 32:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([cool_hot, coffee,korzina, back], resize_keyboard=True))


    elif text =='Американо':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(330, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 330:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Американо')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Американо' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Американо добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,korzina,back], resize_keyboard=True))


    elif text =='Назад' and stage == 330:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(32, user_id))
        context.bot.send_message(chat_id=user_id, text='Кофе',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,korzina,back], resize_keyboard=True))

    elif text =='Эспрессо':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(331, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 331:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Эспрессо')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Эспрессо' + ' - ' + str(cena)
        print(zakaz)
        a = cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        print(a)
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Эспрессо добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,korzina,back], resize_keyboard=True))


    elif text == 'Назад' and stage == 331:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(32, user_id))
        context.bot.send_message(chat_id=user_id, text='Кофе',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano, cap_latte, raf_frap,korzina, back],
                                                                  resize_keyboard=True))


    elif text =='Капучино':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(332, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 332:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Капучино')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Капучино' + ' - ' + str(cena)
        print(zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()

        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Капучино добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,korzina,back], resize_keyboard=True))


    elif text == 'Назад' and stage == 332:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(32, user_id))
        context.bot.send_message(chat_id=user_id, text='Кофе',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano, cap_latte, raf_frap,korzina, back],
                                                                  resize_keyboard=True))


    elif text =='Латте':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(333, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 333:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Латте')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Латте' + ' - ' + str(cena)
        print(zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Латте добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,korzina,back], resize_keyboard=True))


    elif text == 'Назад' and stage == 333:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(32, user_id))
        context.bot.send_message(chat_id=user_id, text='Кофе',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano, cap_latte, raf_frap,korzina, back],
                                                                  resize_keyboard=True))


    elif text =='Раф':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(334, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 334:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Раф')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Раф' + ' - ' + str(cena)
        print(zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Раф добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,korzina,back], resize_keyboard=True))


    elif text == 'Назад' and stage == 334:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(32, user_id))
        context.bot.send_message(chat_id=user_id, text='Кофе',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano, cap_latte, raf_frap,korzina, back],
                                                                  resize_keyboard=True))


    elif text =='Фраппучино':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(336, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 336:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Фраппучино')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Фраппучино' + ' - ' + str(cena)
        print(zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Фраппучино добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,korzina,back], resize_keyboard=True))




    elif text =='Назад' and stage == 336:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(32, user_id))
        context.bot.send_message(chat_id=user_id, text='Кофе',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,korzina,back], resize_keyboard=True))

#ВСЕ ПРО ЛИМОНАДЫ

    elif text =='Лимонады':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(35, user_id))
        context.bot.send_message(chat_id=user_id, text='Лимонады',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,korzina, back],
                                                                  resize_keyboard=True))

    elif text == 'Назад' and stage == 35:
        conn = sqlite3.connect('identifier.sqlite')
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([cool_hot,coffee,korzina,back], resize_keyboard=True))

    elif text == 'Йерная ягода':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(360, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 360:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Йерная ягода')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Йерная ягода' + ' - ' + str(cena)
        print(zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Йерная ягода добавлена в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,korzina, back],
                                                                  resize_keyboard=True))


    elif text == 'Назад' and stage == 360:
        conn = sqlite3.connect('identifier.sqlite')
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,korzina, back], resize_keyboard=True))


    elif text == 'Цитрус-щавель':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(361, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 361:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Цитрус-щавель')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Цитрус-щавель' + ' - ' + str(cena)
        print(zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Цитрус-щавель добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,korzina, back],
                                                                  resize_keyboard=True))


    elif text == 'Назад' and stage == 361:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши  Бар',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys, mango_ice, moh_mango,korzina, back],
                                                                  resize_keyboard=True))


    elif text == 'Манго-маракуя':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(362, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 362:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Манго-маракуя')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Манго-маракуя' + ' - ' + str(cena)
        print(zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Манго-маракуя добавлена в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,korzina, back],
                                                                  resize_keyboard=True))


    elif text == 'Назад' and stage == 362:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши  Бар',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys, mango_ice, moh_mango,korzina, back],
                                                                  resize_keyboard=True))



    elif text == 'Айс-ти':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(364, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 364:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Айс-ти')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Айс-ти' + ' - ' + str(cena)
        print(zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Айс-ти добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,korzina, back],
                                                                  resize_keyboard=True))


    elif text == 'Назад' and stage == 364:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши  Бар',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys, mango_ice, moh_mango,korzina, back],
                                                                  resize_keyboard=True))






    elif text == 'Мохито':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(365, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 365:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Мохито')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Мохито' + ' - ' + str(cena)
        print(zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Мохито добавлено в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,korzina, back],
                                                                  resize_keyboard=True))


    elif text == 'Назад' and stage == 365:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши  Бар',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys, mango_ice, moh_mango,korzina, back],
                                                                  resize_keyboard=True))


    elif text == 'Манговый айс-ти':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(366, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 366:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Манговый айс-ти')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Манговый айс-ти' + ' - ' + str(cena)
        print(zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Манговый айс-ти добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango,korzina, back],
                                                                  resize_keyboard=True))


    elif text == 'Назад' and stage == 366:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши  Бар',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys, mango_ice, moh_mango,korzina, back],
                                                                  resize_keyboard=True))


#ВСЕ ПРО НАПИТКИ
    elif text == 'Напитки':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(38, user_id))
        context.bot.send_message(chat_id=user_id, text='Напитки',
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,korzina,back],
                                                                  resize_keyboard=True))

    elif text == 'Назад' and stage == 38:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([cool_hot, coffee,korzina, back],
                                                                  resize_keyboard=True))

    elif text == 'Red bull':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(390, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 390:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Red bull')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Red bull' + ' - ' + str(cena)
        print(zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Red bull добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,korzina,back],
                                                                  resize_keyboard=True))


    elif text == 'Назад' and stage == 390:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Напитки',
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,korzina,back],
                                                                  resize_keyboard=True))



    elif text == 'Borjomi':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(391, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))


    elif text == 'Добавить в заказ' and stage == 391:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Borjomi')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Borjomi' + ' - ' + str(cena)
        print(zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Borjomi добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,korzina,back],
                                                                  resize_keyboard=True))


    elif text == 'Назад' and stage == 391:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Напитки',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with,korzina, back],
                                     resize_keyboard=True))



    elif text == 'Coca-cola':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(392, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 392:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Coca-cola')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Coca-cola' + ' - ' + str(cena)
        print(zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Coca-cola добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,korzina,back],
                                                                  resize_keyboard=True))


    elif text == 'Назад' and stage == 392:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Напитки',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with,korzina, back],
                                     resize_keyboard=True))



    elif text == 'Sprite':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(393, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 393:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Sprite')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Sprite' + ' - ' + str(cena)
        print(zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Sprite добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,korzina,back],
                                                                  resize_keyboard=True))


    elif text == 'Назад' and stage == 393:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Напитки',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with,korzina, back],
                                     resize_keyboard=True))



    elif text == 'Сок':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(394, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 394:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Сок')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Сок' + ' - ' + str(cena)
        print(zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Сок добавлен в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,korzina,back],
                                                                  resize_keyboard=True))


    elif text == 'Назад' and stage == 394:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Напитки',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with,korzina, back],
                                     resize_keyboard=True))


    elif text == 'Вода с газом':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(395, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 395:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Вода с газом')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Вода с газом' + ' - ' + str(cena)
        print(zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Вода с газом добавлена в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,korzina,back],
                                                                  resize_keyboard=True))


    elif text == 'Назад' and stage == 395:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Напитки',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with,korzina, back],
                                     resize_keyboard=True))


    elif text == 'Вода':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(396, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([add_zakaz,korzina,back], resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 396:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        zakaz = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        zakaz = zakaz[0][0]
        print(zakaz)
        cena = cur.execute(cost.format('Вода')).fetchall()
        cena = cena[0][0]
        print(cena)
        zakaz = zakaz + '\n' + 'Вода' + ' - ' + str(cena)
        print(zakaz)
        cur.execute(sql_set_zakaz.format(zakaz, user_id)).fetchall()
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        itog = itog + cena
        cur.execute(update_total_price.format(itog,user_id))
        context.bot.send_message(chat_id=user_id, text='Вода добавлена в заказ'.format(text),
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,korzina,back],
                                                                  resize_keyboard=True))


    elif text == 'Назад' and stage == 395:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Напитки',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with,korzina, back],
                                     resize_keyboard=True))




    elif text == 'Мой заказ':
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


    elif text == 'Заказать✅':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        x = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        x = x[0][0]
        a = cur.execute(table_number_in_table.format(user_id)).fetchall()
        cur.execute(update_stage_in.format(1001,user_id))

        context.bot.send_message(chat_id = user_id, text = 'Ваш заказ принят и очень скоро будет готов!',
                                 reply_markup = ReplyKeyboardMarkup([top_button,mid_button,bot_button,order_button],resize_keyboard=True))
        context.bot.send_message(chat_id = 44335784,text = 'Заказ за стол № {} , {}'.format(a[0][0],x))
        cur.execute(delete_zakaz.format(user_id))
        cur.execute(update_total_price.format(0, user_id))



    elif text == 'Очистить заказ':
        x = cur.execute(delete_zakaz.format(user_id))
        cur.execute(update_total_price.format(0,user_id))
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
        x = cur.execute(sql_get_zakaz.format(user_id)).fetchall()
        x = x[0][0]
        itog = cur.execute(set_total_price.format(user_id)).fetchall()
        itog = itog[0][0]
        a = cur.execute(table_number_in_table.format(user_id)).fetchall()
        context.bot.send_message(chat_id=user_id, text='''Прошу вас, ваш Чек
        
{}
Итоговая стоимость - {}'''.format(x,itog),
                                 reply_markup=ReplyKeyboardMarkup(
                                     [payme_click,nal,back], resize_keyboard=True,
                                     one_time_keyboard=True))
    elif text == 'Назад':
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


