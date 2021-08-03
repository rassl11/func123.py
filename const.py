from telegram import  KeyboardButton,ReplyKeyboardMarkup
from telegram.ext.utils import types

TOKEN = '1921581075:AAFS9AfBitFlo_Xx1gzXE2NYiECB4tBZQrg'

zakaz_list = []
phone = [KeyboardButton(text = 'Отправить номер телефона',request_contact=True)]

order_button = [KeyboardButton(text = 'Сделать заказ'),KeyboardButton(text = 'Мой заказ')]
top_button = [KeyboardButton(text='Позвать Таймгарда🏃')]
mid_button = [KeyboardButton(text='Продуть Кальян💨')]
bot_button = [KeyboardButton(text='Попросить счет💵')]
kitchen_button = [KeyboardButton(text='Кухня')]
shisha_button = [KeyboardButton(text='Кальян')]
bar_button = [KeyboardButton(text='Бар')]
add_zakaz = [KeyboardButton(text = 'Добавить в заказ')]
ready = [KeyboardButton(text = 'Заказать✅')]


korzina = [KeyboardButton(text = 'Мой заказ')]
payme_click = [KeyboardButton(text = 'Payme'),KeyboardButton(text = 'Click')]
nal = [KeyboardButton(text = 'Наличные')]

# все по кальяну

easy = [KeyboardButton(text='Легкий')]
medium = [KeyboardButton(text='Средний')]
rare = [KeyboardButton(text='Крепкий')]
berry = [KeyboardButton(text ='Ягодный')]
fruit = [KeyboardButton(text = 'Фруктовый')]
citrus = [KeyboardButton(text = 'Цитрусовый')]
desert = [KeyboardButton(text = 'Десертный')]
kolaud = [KeyboardButton(text='Калауд')]
folga = [KeyboardButton(text= 'Фольга')]
ice = [KeyboardButton(text = 'С холодком')]
no_ice = [KeyboardButton(text = 'Без Холодка')]
yes =[KeyboardButton(text = 'Да')]
no = [KeyboardButton(text = 'Главное меню')]
back = [KeyboardButton(text='Назад')]
delete = [KeyboardButton(text = 'Очистить заказ')]

# все по кухне

soups_hot = [KeyboardButton(text = "Супы"),KeyboardButton(text = 'Горячее')]
pasta_fasfood = [KeyboardButton(text = 'Пасты'),KeyboardButton(text = 'Фаст-Фуд')]
salad_garnir = [KeyboardButton(text = 'Салаты'),KeyboardButton(text = 'Гарниры')]
desserts = [KeyboardButton(text = 'Десерты')]

#категория супы

okroshka_kuksi = [KeyboardButton(text ='Окрошка'),KeyboardButton(text ='Кук-си')]
ramen_mastava = [KeyboardButton(text ='Рамен'),KeyboardButton(text ='Мастава')]

#КАТЕГОРИЯ ГОРЯЧЕЕ

ribay_medalion = [KeyboardButton(text ='Рибай стейк'),KeyboardButton(text ='Медальоны')]
beef_cream_chiken_veg = [KeyboardButton(text ='Говядина в сливочном соусе'),KeyboardButton(text ='Курица на грилле')]
home_potato_chineese_meat = [KeyboardButton(text ='Картошка по-домашнему'),KeyboardButton(text ='Мясо по-китайский')]
chicken_steak = [KeyboardButton(text ='Стейк куриный'),KeyboardButton(text ='Назад')]

#КАТЕГОРИЯ ПАСТЫ

alfredo = [KeyboardButton(text ='Альфредо')]
boloneze = [KeyboardButton(text ='Болоньезе')]

#КАТЕГОРИЯ ФАСТ-ФУД

burrito_sandwich = [KeyboardButton(text ='Буррито'),KeyboardButton(text ='Куриный Сэндвич')]
nuggets_garlic = [KeyboardButton(text ='Наггетсы'),KeyboardButton(text ='Гарлики')]

#КАТЕГОРИЯ САЛАТЫ

greek_achik = [KeyboardButton(text = 'Греческий салат'),KeyboardButton(text= 'Ачик-чучук')]

#КАТЕГОРИЯ ГАРНИРЫ

grilveg_fries = [KeyboardButton(text = 'Овощи на грилле'),KeyboardButton(text = 'Картофель по-деревенски')]
ris_derev = [KeyboardButton(text = 'Рис'),KeyboardButton(text = 'Фри')]
aydaho_back = [KeyboardButton(text = 'Картофель айдахо'),KeyboardButton(text = 'Назад')]

#КАТЕГОРИЯ ДЕСЕРТЫ

medov_chiz = [KeyboardButton(text='Медовик'),KeyboardButton(text='Чизкейк')]
brauni_back = [KeyboardButton(text = 'Брауни'),KeyboardButton(text = 'Назад')]


#ВСЕ ПО БАРУ

#ЧАИ

cool_hot = [KeyboardButton(text ='Кофе'),KeyboardButton(text = 'Чаи')] # o-eng
coffee = [KeyboardButton(text = 'Лимонады'),KeyboardButton(text = 'Напитки')]
tea = [KeyboardButton(text='Черный чай'),KeyboardButton(text='Чай зеленый')]
brand_tea = [KeyboardButton(text='Наглый фрукт'),KeyboardButton(text='Ягодная бергамония')]
sugar = [KeyboardButton(text='С сахаром'),KeyboardButton(text='Без')]
limon = [KeyboardButton(text='С лимоном'),KeyboardButton(text='Без лимона')]


#КОФЕ

esprosso_americano =[KeyboardButton(text = "Эспрессо"),KeyboardButton(text = "Американо")]
cap_latte =[KeyboardButton(text = "Капучино"),KeyboardButton(text = "Латте")]
raf_frap =[KeyboardButton(text = "Раф"),KeyboardButton(text = "Фраппучино")]


#ЛИМОНАДЫ

berry_citrys =[KeyboardButton(text = 'Йерная ягода'),KeyboardButton(text = 'Цитрус-щавель')]
mango_ice =[KeyboardButton(text = 'Манго-маракуя'),KeyboardButton(text = 'Айс-ти')]
moh_mango =[KeyboardButton(text = 'Мохито'),KeyboardButton(text = 'Манговый айс-ти')]

#НАПИТКА

bull_borjomi = [KeyboardButton(text = 'Red bull'),KeyboardButton(text = 'Borjomi')]
cola_fanta = [KeyboardButton(text = 'Coca-cola'),KeyboardButton(text = 'Fanta')]
sprite_sok = [KeyboardButton(text = 'Sprite'),KeyboardButton(text = 'Сок')]
water_with = [KeyboardButton(text = 'Вода с газом'),KeyboardButton(text = 'Вода')]




five_star = [KeyboardButton(text='⭐⭐⭐⭐⭐')]
four_star = [KeyboardButton(text="⭐⭐⭐⭐")]
three_star = [KeyboardButton(text="⭐⭐⭐")]
two_star = [KeyboardButton(text="⭐⭐")]
one_star = [KeyboardButton(text="⭐")]
restart = [KeyboardButton(text = '/start')]



TOVARI = {
    1000:'Окрошка',
    1001:'Кук-си',
    1002:'Рамен',
    1003:'Мастава',
    1004:'Рибай стейк',
    1005:'Медальоны',
    1006:'Говядина в сливочном соусе',
    1007:'Курица на грилле',
    1008:'Картошка по-домашнему',
    1009:'Мясо по-китайски',
    1010:'Стейк куриный',
    1011:'Альфредо',
    1012:'Болоньезе',
    1013:'Буррито',
    1014:'Куриный сэндвич',
    1015:'Наггетсы',
    1016:'Гарлики',
    1017:'Греческий салат',
    1018:'Ачик-чучук',
    1019:'Овощи на грилле',
    1020:'Фри',
    1021:'Рис',
    1022:'Картофель по-деревенски',
    1024:'Картофель айдахо',
    1025:'Медовик',
    1026:'Чизкейк',
    1027:'Брауни',
    1028:'Йерная ягода',
    1029:'Цитрус-щавель',
    1030:'Манго-маракуя',
    1031:'Айс-ти',
    1032:'Мохито',
    1033:'Манговый айс-ти',
    1034:'Red bull',
    1035:'Borjomi',
    1036:'Coc-cola',
    1037:'Fanta',
    1038:'Sprite',
    1039:'Вода с газом',
    1040:'Вода',
    1041:'Наглый фрукт',
    1042:'Ягодная бергамония',
    1043:'Черный чай',
    1044:'Зеленый чай',
    1045:'С лимоном',
    1046:'Эспрессо',
    1047:'Американо',
    1048:'Капучино',
    1049:'Латте',
    1050:'Раф',
    1051:'Фраппучино',
    1052:'Картофель айдахо',

}

