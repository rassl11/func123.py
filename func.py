import time

from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from const import *
from sql_req import *
import sqlite3



def start(update,context):
    user_id = update.message.chat_id
    name = update.message.from_user.first_name
    conn = sqlite3.connect('identifier.sqlite')
    cur = conn.cursor()
    id_in = cur.execute(id_in_table.format(user_id)).fetchall()
    print(id_in)


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



    if text.isdigit and text in allowed_tables:
        cur.execute(update_table_number.format(text, user_id))
        context.bot.send_message(chat_id = user_id,text = 'Прекрасного времени провождения😊',
                                 reply_markup = ReplyKeyboardMarkup([top_button,mid_button,bot_button,order_button],resize_keyboard=True))

    elif text == 'Сделать заказ':
        context.bot.send_message(chat_id = user_id,text = 'Выбирай',reply_markup = ReplyKeyboardMarkup([kitchen_button,shisha_button,bar_button,back],resize_keyboard=True))

    elif text == 'Назад' and stage == 0:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        context.bot.send_message(chat_id = user_id,text = 'Прекрасного времени провождения😊',
                                 reply_markup = ReplyKeyboardMarkup([top_button,mid_button,bot_button,order_button],resize_keyboard=True))

#все про кальяны

    elif text == 'Кальян':
        context.bot.send_message(chat_id = user_id,text = "Какой крепости кальян",reply_markup = ReplyKeyboardMarkup([easy,medium,rare,back],resize_keyboard=True))
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_zakaz.format(text,user_id))



    elif text == 'Назад' and stage == 1:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(0,user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([kitchen_button, shisha_button, bar_button, back],
                                                                  resize_keyboard=True))

    elif text =='Легкий' or text == 'Средний' or text == 'Крепкий':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(2, user_id))
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
        context.bot.send_message(chat_id = user_id, text = 'Отлично,добавляем в заказ??',
                                 reply_markup = ReplyKeyboardMarkup([yes,no,back],resize_keyboard=True))

    elif text == 'Назад' and stage == 5:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(4, user_id))
        context.bot.send_message(chat_id=user_id, text='С холодком или без?',
                                 reply_markup = ReplyKeyboardMarkup([ice,no_ice,back],resize_keyboard=True))




    elif text =='Да':
        context.bot.send_message(chat_id = user_id,text ='''Товар добавлен в заказ''',reply_markup = ReplyKeyboardMarkup([kitchen_button,shisha_button,bar_button,back],
                                                                                                       resize_keyboard=True))

    elif text == 'Выбрать что-нибудь еще':
        context.bot.send_message(chat_id = user_id,text = 'Выбирай',reply_markup = ReplyKeyboardMarkup([kitchen_button,shisha_button,bar_button,back],
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
                                 reply_markup = ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava,back],resize_keyboard=True))

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
Цена: {}'''.format(a,b),reply_markup=ReplyKeyboardMarkup([add_zakaz,back],resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 8:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        x = cur.execute(zakaz.format(user_id)).fetchall()

        print(x)

        x.append('Окрошка')
        x = x[0][0]
        print(x)
        conn.commit()

        context.bot.send_message(chat_id = user_id,text = 'Окрошка добавлена  в заказ'.format(text))



    elif text == 'Назад' and stage ==8:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(7, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши супы',
                                 reply_markup=ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava, back],
                                                                  resize_keyboard=True))

    elif text == 'Кук-си' and stage == 7:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(200, user_id))
        conn.commit()
        context.bot.send_message(chat_id = user_id,text = 'asd',reply_markup=ReplyKeyboardMarkup([add_zakaz,back],resize_keyboard=True))

    elif text == 'Добавить в заказ' and stage == 200:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        x = cur.execute(zakaz.format(user_id)).fetchall()

        print(x)
        x.append('Кук-си')
        x = x[0][0]
        print(x)
        conn.commit()


        context.bot.send_message(chat_id=user_id, text='Кук-си добавлена  в заказ'.format(text))


    elif text == 'Назад' and stage ==200:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(7, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши супы',
                                 reply_markup=ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava, back],
                                                                  resize_keyboard=True))

    elif text =='Рамен' and stage == 7:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        a = cur.execute(opisanie.format(text)).fetchall()
        a = a[0][0]
        b = cur.execute(cost.format(text)).fetchall()
        b = b[0][0]
        print(a)
        c = cur.execute(photo.format(text)).fetchall()
        c = c[0][0]

        cur.execute(update_stage_in.format(8, user_id))
        context.bot.send_photo(photo=('https://ibb.co/dWSpDVT'), chat_id=user_id, caption='''Описание :{}
Цена: {}'''.format(a, b))


    elif text == 'Назад' and stage ==8:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(7, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши супы',
                                 reply_markup=ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava, back],
                                                                  resize_keyboard=True))

    elif text =='Мастава' and stage == 7:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(8, user_id))
        context.bot.send_message(chat_id = user_id,text ='Добавить в корзину',
                                 reply_markup = ReplyKeyboardMarkup([yes,no,back],resize_keyboard=True))

    elif text == 'Назад' and stage ==8:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(7, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши супы',
                                 reply_markup=ReplyKeyboardMarkup([okroshka_kuksi,ramen_mastava, back],
                                                                  resize_keyboard=True))

#ВСЕ ПРО ГОРЯЧЕЕ

    elif text == 'Горячее':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(9, user_id))
        context.bot.send_message(chat_id=user_id, text='Горячие блюда',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak],
                                                                  resize_keyboard=True))
    elif text == 'Назад'and stage==9:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(6, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([soups_hot,pasta_fasfood,salad_garnir,desserts,back],
                                                                  resize_keyboard=True))
    elif text == 'Рибай стейк':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage == 10:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(9, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak],
                                                                  resize_keyboard=True))
    elif text == 'Медальоны':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage == 10:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(9, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak],
                                                                  resize_keyboard=True))

    elif text == 'Говядина в слив соусе':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage == 10:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(9, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak],
                                                                  resize_keyboard=True))
    elif text == 'Курица на гриле':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage == 10:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(9, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak],
                                                                  resize_keyboard=True))
    elif text == 'Картошка по-домашнему':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage == 10:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(9, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak],
                                                                  resize_keyboard=True))
    elif text == 'Мясо по-китайски':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage == 10:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(9, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak],
                                                                  resize_keyboard=True))

    elif text == 'Стейк куриный':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(10, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage == 10:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(9, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [ribay_medalion,beef_cream_chiken_veg,home_potato_chineese_meat,chicken_steak],
                                     resize_keyboard=True))


#ВСЕ ПРО ПАСТЫ

    elif text=='Пасты':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(11, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши пасты',
                                reply_markup=ReplyKeyboardMarkup([alfredo,boloneze,back], resize_keyboard=True))

    elif text == 'Назад' and stage == 11:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(6, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши супы',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [soups_hot,pasta_fasfood,salad_garnir, desserts, back],
                                     resize_keyboard=True))

    elif text =='Альфредо':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(12, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage == 12:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(11, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши пасты',
                                 reply_markup=ReplyKeyboardMarkup([alfredo,boloneze,back],resize_keyboard=True))

    elif text =='Болоньезе':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(12, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage == 12:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(11, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши пасты',
                                 reply_markup=ReplyKeyboardMarkup([alfredo,boloneze,back],resize_keyboard=True))

#ВСЕ ПРО ФАСТ-ФУД

    elif text =='Фаст-Фуд':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(14, user_id))
        context.bot.send_message(chat_id=user_id, text='Категория Фаст-Фуд',
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,back],resize_keyboard=True))

    elif text == 'Назад' and stage == 14:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(6, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([soups_hot,pasta_fasfood,salad_garnir,desserts,back],
                                                                  resize_keyboard=True))

    elif text =='Буррито':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(15, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage == 15:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(14, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,back],
                                                                  resize_keyboard=True))

    elif text =='Наггетсы':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(15, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage == 15:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(14, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,back],
                                                                  resize_keyboard=True))


    elif text =='Гарлики':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(15, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage == 15:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(14, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,back],
                                                                  resize_keyboard=True))

    elif text =='Куриный Сэндвич':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(15, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage == 15:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(14, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([burrito_sandwich,nuggets_garlic,back],
                                                                  resize_keyboard=True))

#ВСЕ ПРО САЛАТЫ

    elif text == 'Салаты':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(17, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши Салаты',
                                 reply_markup=ReplyKeyboardMarkup([greek_achik, back],
                                                                  resize_keyboard=True))

    elif text == 'Назад' and stage == 17:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(6, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup = ReplyKeyboardMarkup([soups_hot, pasta_fasfood, salad_garnir, desserts, back], resize_keyboard=True))

    elif text == 'Греческий салат':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(18, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage == 18:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(17, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup = ReplyKeyboardMarkup([greek_achik, back], resize_keyboard=True))

    elif text == 'Ачик-чучук':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(18, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage == 18:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(17, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup = ReplyKeyboardMarkup([greek_achik, back], resize_keyboard=True))

#ВСЕ ПРО ГАРНИРЫ

    elif text=='Гарниры':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(20, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши гарниры',
                                 reply_markup=ReplyKeyboardMarkup([grilveg_fries,ris_derev,aydaho_back], resize_keyboard=True))

    elif text == 'Назад' and stage ==20:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(6, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',reply_markup=ReplyKeyboardMarkup(
                                     [soups_hot, pasta_fasfood, salad_garnir, desserts, back], resize_keyboard=True))

    elif text=='Овощи на грилле':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(21, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage ==21:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(20, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши гарниры',reply_markup=ReplyKeyboardMarkup([grilveg_fries, ris_derev, aydaho_back],
                                                                  resize_keyboard=True))


    elif text=='Картофель по-деревенски':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(21, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage ==21:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(20, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши гарниры',reply_markup=ReplyKeyboardMarkup([grilveg_fries, ris_derev, aydaho_back],
                                                                  resize_keyboard=True))


    elif text=='Рис':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(21, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage ==21:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(20, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши гарниры',reply_markup=ReplyKeyboardMarkup([grilveg_fries, ris_derev, aydaho_back],
                                                                  resize_keyboard=True))

    elif text=='Фри':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(21, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage ==21:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(20, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши гарниры',reply_markup=ReplyKeyboardMarkup([grilveg_fries, ris_derev, aydaho_back],
                                                                  resize_keyboard=True))



    elif text=='Картофель айдахо':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(21, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage ==21:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(20, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши гарниры',reply_markup=ReplyKeyboardMarkup([grilveg_fries, ris_derev, aydaho_back],
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
        context.bot.send_message(chat_id=user_id, text='Выбирай',reply_markup=ReplyKeyboardMarkup([soups_hot, pasta_fasfood, salad_garnir, desserts, back],
                                                                  resize_keyboard=True))

    elif text == 'Чизкейк':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(24, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage ==24:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(23, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши десерты',reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back],
                                                                  resize_keyboard=True))

    elif text == 'Медовик':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(24, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage ==24:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(23, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши десерты',reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back],
                                                                  resize_keyboard=True))


    elif text == 'Брауни':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(24, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage ==24:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(23, user_id))
        context.bot.send_message(chat_id=user_id, text='Наши десерты',reply_markup=ReplyKeyboardMarkup([medov_chiz,brauni_back],
                                                                  resize_keyboard=True))

#ВСЕ ПО БАРУ

    elif text == 'Бар':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([cool_hot,coffee,back], resize_keyboard=True))

    elif text == 'Назад' and stage ==26:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(0, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',reply_markup=ReplyKeyboardMarkup([kitchen_button, shisha_button, bar_button, back],
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
                                 reply_markup=ReplyKeyboardMarkup([cool_hot,coffee,back], resize_keyboard=True))

    elif text =='Наглый фрукт':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(28, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))


    elif text =='Ягодная бергамония':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(28, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))


    elif text == 'Черный чай' or text == 'Зеленый чай':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(28, user_id))
        context.bot.send_message(chat_id=user_id, text='С Сахаром или без?',
                                 reply_markup=ReplyKeyboardMarkup([sugar, back], resize_keyboard=True))

    elif text=='Назад' and stage == 28:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Выбирай',
                                 reply_markup=ReplyKeyboardMarkup([tea, brand_tea, back],
                                                                  resize_keyboard=True))


    elif text =='С сахаром':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(29, user_id))
        context.bot.send_message(chat_id=user_id, text='С лимоном или без?',
                                 reply_markup=ReplyKeyboardMarkup([limon,back], resize_keyboard=True))

    elif text == 'Без':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(29, user_id))
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
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))


    elif text =='Без лимона':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(30, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

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
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,back], resize_keyboard=True))

    elif text =='Назад' and stage == 32:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([cool_hot, coffee, back], resize_keyboard=True))


    elif text =='Американо':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(33, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text =='Эспрессо':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(33, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text =='Капучино':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(33, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text =='Латте':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(33, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text =='Раф':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(33, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text =='Фраппучино':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(33, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))




    elif text =='Назад' and stage == 33:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(32, user_id))
        context.bot.send_message(chat_id=user_id, text='Кофе',
                                 reply_markup=ReplyKeyboardMarkup([esprosso_americano,cap_latte,raf_frap,back], resize_keyboard=True))

#ВСЕ ПРО ЛИМОНАДЫ

    elif text =='Лимонады':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(35, user_id))
        context.bot.send_message(chat_id=user_id, text='Лимонады',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango, back],
                                                                  resize_keyboard=True))

    elif text == 'Назад' and stage == 35:
        conn = sqlite3.connect('identifier.sqlite')
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([cool_hot,coffee,back], resize_keyboard=True))

    elif text == 'Йерная ягода':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(36, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Цитрус-щавель':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(36, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Манго-маракуя':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(36, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Айс-ти':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(36, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Мохито':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(36, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Манговый айс-ти':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(36, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage == 36:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(35, user_id))
        context.bot.send_message(chat_id=user_id, text='Лимонады',
                                 reply_markup=ReplyKeyboardMarkup([berry_citrys,mango_ice,moh_mango, back],
                                                                  resize_keyboard=True))

#ВСЕ ПРО НАПИТКИ
    elif text == 'Напитки':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(38, user_id))
        context.bot.send_message(chat_id=user_id, text='Напитки',
                                 reply_markup=ReplyKeyboardMarkup([bull_borjomi,cola_fanta,sprite_sok,water_with,back],
                                                                  resize_keyboard=True))

    elif text == 'Назад' and stage == 38:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(26, user_id))
        context.bot.send_message(chat_id=user_id, text='Наш Бар',
                                 reply_markup=ReplyKeyboardMarkup([cool_hot, coffee, back],
                                                                  resize_keyboard=True))

    elif text == 'Red bull':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(39, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Borjomi':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(39, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Coca-cola':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(39, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Sprite':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(39, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Сок':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(39, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Вода с газом':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(39, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Вода':
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(39, user_id))
        context.bot.send_message(chat_id=user_id, text='Добавить в корзину',
                                 reply_markup=ReplyKeyboardMarkup([yes, no, back], resize_keyboard=True))

    elif text == 'Назад' and stage == 39:
        conn = sqlite3.connect('identifier.sqlite')
        cur = conn.cursor()
        cur.execute(update_stage_in.format(38, user_id))
        context.bot.send_message(chat_id=user_id, text='Напитки',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [bull_borjomi, cola_fanta, sprite_sok, water_with, back],
                                     resize_keyboard=True))



    elif text =='Позвать Таймгарда🏃':
        a = cur.execute(table_number_in_table.format(user_id)).fetchall()
        print(a[0][0])
        context.bot.send_message(chat_id=user_id, text='Так Точно💪!')



    elif text == 'Продуть Кальян💨':
        a = cur.execute(table_number_in_table.format(user_id)).fetchall()
        context.bot.send_message(chat_id=user_id, text='Понял Принял👌')


    elif text == 'Попросить счет💵':
        a = cur.execute(table_number_in_table.format(user_id)).fetchall()
        context.bot.send_message(chat_id=user_id, text='Уже сделано! Оцените работу вашего Таймгарда',
                                 reply_markup=ReplyKeyboardMarkup(
                                     [five_star, four_star, three_star, two_star, one_star], resize_keyboard=True,
                                     one_time_keyboard=True))


    elif text == '⭐⭐⭐⭐⭐':
        cur.execute(update_mark.format(5, user_id))
        context.bot.send_message(chat_id=user_id, text='''Благодарю за доверие времени нам. Ждем вас снова!
Нажми на кнопку как придешь еще раз!''',
                                 reply_markup=ReplyKeyboardMarkup([restart],
                                                                  resize_keyboard=True,one_time_keyboard=True))
    elif text == '⭐⭐⭐⭐':
        cur.execute(update_mark.format(4, user_id))
        context.bot.send_message(chat_id=user_id, text='''Благодарю за доверие времени нам. Ждем вас снова!
Нажми на кнопку как придешь еще раз!''',
                                 reply_markup=ReplyKeyboardMarkup([restart],
                                                                  resize_keyboard=True,one_time_keyboard=True))
    elif text == '⭐⭐⭐':
        cur.execute(update_mark.format(3, user_id))
        context.bot.send_message(chat_id=user_id, text='''Благодарю за доверие времени нам. Ждем вас снова!
Нажми на кнопку как придешь еще раз!''',
                                 reply_markup=ReplyKeyboardMarkup([restart],
                                                                  resize_keyboard=True,one_time_keyboard=True))
    elif text == '⭐⭐':
        cur.execute(update_mark.format(2, user_id))
        context.bot.send_message(chat_id=user_id,text='''Благодарю за доверие времени нам. Ждем вас снова!
Нажми на кнопку как придешь еще раз!''',
                                 reply_markup=ReplyKeyboardMarkup([restart],
                                                                  resize_keyboard=True,one_time_keyboard=True))
    elif text == '⭐':
        cur.execute(update_mark.format(1, user_id))
        context.bot.send_message(chat_id=user_id, text='''Благодарю за доверие времени нам. Ждем вас снова!
Нажми на кнопку как придешь еще раз!''',
                                 reply_markup=ReplyKeyboardMarkup([restart],
                                                                  resize_keyboard=True,one_time_keyboard=True))

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
    print(zakaz_list)
