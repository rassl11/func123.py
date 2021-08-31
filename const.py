from telegram import  KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton
from telegram.ext.utils import types

TOKEN = '1921581075:AAFS9AfBitFlo_Xx1gzXE2NYiECB4tBZQrg'

zakaz_list = []
phone = [KeyboardButton(text = 'Отправить номер телефона',request_contact=True)]

order_button = [KeyboardButton(text = 'Сделать заказ✍'),KeyboardButton(text = 'Мой заказ📝')]
top_button = [KeyboardButton(text='Позвать Таймгарда🏃')]
mid_button = [KeyboardButton(text='Кэшбэк💵')]
bot_button = [KeyboardButton(text='Попросить счет💵')]
kitchen_bar = [KeyboardButton(text='Кухня🍽'),KeyboardButton(text='Бар🥤')]
shisha_button = [KeyboardButton(text='Кальян💨')]
back_korzina = [KeyboardButton(text='⏪Назад'),KeyboardButton(text='Мой заказ📝')]
add_zakaz = [KeyboardButton(text = 'Добавить в заказ')]
ready = [KeyboardButton(text = 'Заказать✅')]



korzina = [KeyboardButton(text = 'Мой заказ📝')]
payme_click = [KeyboardButton(text = 'Payme'),KeyboardButton(text = 'Click')]
nal = [KeyboardButton(text = 'Наличные')]

# все по кальяну
celiy = [KeyboardButton(text = 'Кaльян'),KeyboardButton(text = 'Замена чаши')]
biznes = [KeyboardButton(text = 'Бизнес перекур')]

commentariy = [KeyboardButton(text = 'Пропустить⏩')]

easy = [KeyboardButton(text='⏪Назад'),KeyboardButton(text='Легкий⏬')]
rare = [KeyboardButton(text='Крепкий⏫'),KeyboardButton(text='Средний➡')]
berry = [KeyboardButton(text ='Ягодный   🍓'),KeyboardButton(text = 'Фруктовый 🍊')]
citrus = [KeyboardButton(text = 'Цитрусовый🍋'),KeyboardButton(text = 'Десертный 🍪')]


folga = [KeyboardButton(text= 'Фольга'),KeyboardButton(text='Калауд')]
ice = [KeyboardButton(text = 'С холодком ❄'),KeyboardButton(text = 'Без Холодка💥')]

yes =[KeyboardButton(text = 'Да')]
no = [KeyboardButton(text = 'Главное меню')]
back = [KeyboardButton(text='⏪Назад')]
delete = [KeyboardButton(text = 'Очистить заказ')]

# все по кухне

soups_hot = [KeyboardButton(text = "Супы🍜"),KeyboardButton(text = 'Вторые блюда🍲')]
pasta_fasfood = [KeyboardButton(text = 'Пасты🍝'),KeyboardButton(text = 'Салаты🥗')]
salad_garnir = [KeyboardButton(text = 'Фаст-Фуд🥪'),KeyboardButton(text = 'Гарниры🍟')]
desserts = [KeyboardButton(text ='⏪Назад'),KeyboardButton(text = 'Десерты🍰')]
deserti_shisha =[KeyboardButton(text = 'Кальян💨'),KeyboardButton(text = 'Десерты🍰')]

#СТЕПЕНЬ ПРОЖАРКИ
medium_proj = [KeyboardButton(text = 'Medium🔥')]
well_done = [KeyboardButton(text = "Medium-Well🔥🔥"),KeyboardButton(text = 'Well-done🔥🔥🔥')]

#ОСТРОТА
neostr = [KeyboardButton(text = 'Неострый❗')]
ostr = [KeyboardButton(text = "Средней остроты🌶"),KeyboardButton(text = 'Острый🌶🌶')]

#категория супы

okroshka_kuksi = [KeyboardButton(text ='Окрошка'),KeyboardButton(text ='Кук-си')]
ramen_mastava = [KeyboardButton(text ='Рамен'),KeyboardButton(text ='Мастава')]

#КАТЕГОРИЯ ГОРЯЧЕЕ

ribay_medalion = [KeyboardButton(text ='Рибай стейк'),KeyboardButton(text ='Медальоны')]
beef_cream_chiken_veg = [KeyboardButton(text ='Говядина в сливочном соусе'),KeyboardButton(text ='Курица на гриле')]
home_potato_chineese_meat = [KeyboardButton(text ='Картошка по-домашнему'),KeyboardButton(text ='Мясо по-китайски')]
chicken_steak = [KeyboardButton(text ='⏪Назад'),KeyboardButton(text ='Стейк куриный')]

#КАТЕГОРИЯ ПАСТЫ

alfredo_boloneze = [KeyboardButton(text ='Альфредо'),KeyboardButton(text ='Болоньезе')]


#КАТЕГОРИЯ ФАСТ-ФУД

burrito_sandwich = [KeyboardButton(text ='Буррито'),KeyboardButton(text ='Куриный сэндвич')]
nuggets_garlic = [KeyboardButton(text ='Наггетсы'),KeyboardButton(text ='Гарлики')]

#КАТЕГОРИЯ САЛАТЫ

greek_achik = [KeyboardButton(text = 'Греческий салат'),KeyboardButton(text= 'Ачик-чучук')]

#КАТЕГОРИЯ ГАРНИРЫ

grilveg_fries = [KeyboardButton(text = 'Овощи на грилле'),KeyboardButton(text = 'Картофель по-деревенски')]
ris_derev = [KeyboardButton(text = 'Рис'),KeyboardButton(text = 'Фри')]
aydaho_back = [KeyboardButton(text = 'Картофель айдахо')]

#КАТЕГОРИЯ ДЕСЕРТЫ

medov_chiz = [KeyboardButton(text='Медовик'),KeyboardButton(text='Чизкейк')]
brauni_back = [KeyboardButton(text = '⏪Назад'),KeyboardButton(text = 'Брауни')]


#ВСЕ ПО БАРУ



cool_hot = [KeyboardButton(text ='Кофе☕'),KeyboardButton(text = 'Чаи🫖')] # o-eng
coffee = [KeyboardButton(text = 'Лимонады🍹'),KeyboardButton(text = 'Напитки🥤')]
zakus_alco = [KeyboardButton(text = 'Закуски🍿'),KeyboardButton(text= 'Алкоголь🥃')]


#АЛКОГОЛЬ
hard_light = [KeyboardButton(text = 'Крепкий'),KeyboardButton(text = 'Легкий')]
kokteli = [KeyboardButton(text = 'Коктейли')]


#КРЕПКИЕ

viski_kon = [KeyboardButton(text = 'Виски'),KeyboardButton(text = 'Коньяк')]
liker_rom = [KeyboardButton(text = 'Jagermeister'),KeyboardButton(text = 'Ром')]
djin_tekila = [KeyboardButton(text = 'Джин'),KeyboardButton(text = 'Текила')]

chivas_jag = [KeyboardButton(text = 'Chivas Regal 12')]
jack_tull = [KeyboardButton(text = 'Jack Daniels'),KeyboardButton(text = 'Tullamore Dew')]
jame_bal = [KeyboardButton(text = 'Jameson'),KeyboardButton(text = "Ballantines")]


#КОКТЕЙЛИ

shirin = [KeyboardButton(text = 'Shirins Peach')]
aper_meva = [KeyboardButton(text = 'Aperol spritz'),KeyboardButton(text = "Meva-Cheva")]
gin_teq = [KeyboardButton(text = 'Gin tonic'),KeyboardButton(text = "Tequila Sunrise")]


#Коньяк
tanb = [KeyboardButton(text = 'Tanbour')]

#ТЕКИЛА
esp = [KeyboardButton(text = 'Espolon')]


#ДЖИН
Bickens = [KeyboardButton(text = 'Bickens')]

#РОМ

cpt = [KeyboardButton(text = 'Capitan Morgan')]
jwray = [KeyboardButton(text = 'J.Wray Gold'),KeyboardButton(text = "J.Wray Silver")]

#ЗАКУСКИ

sul_kurt = [KeyboardButton(text ='Сулугуни'),KeyboardButton(text = 'Курт')]
pring_mindal = [KeyboardButton(text ='Pringles'),KeyboardButton(text = 'Миндаль')]
phist_set = [KeyboardButton(text ='Фисташки'),KeyboardButton(text = 'Сэт грызун')]


#ЛЕГКИЕ

vino = [KeyboardButton(text = 'Вино')]
shamp_beer = [KeyboardButton(text ='Шампанское'),KeyboardButton(text = 'Пиво')]


#ВИНО
kond = [KeyboardButton(text = 'Kondoli Marani')]
bagiz = [KeyboardButton(text ='Bagizagan 0.15'),KeyboardButton(text = 'Bagizagan 0.33')]

#пиво
corona = [KeyboardButton(text = 'Corona Extra👑')]
hei_tub = [KeyboardButton(text ='Heineken'),KeyboardButton(text = 'Tuborg')]

#ШАМПАНСКОЕ

pamir = [KeyboardButton(text ='Pamir 0.15'),KeyboardButton(text = 'Pamir 0.75')]




#ЧАИ

tea = [KeyboardButton(text='Чай черный'),KeyboardButton(text='Чай зеленый')]
brand_tea = [KeyboardButton(text='Наглый фрукт'),KeyboardButton(text='Ягодная бергамония')]
sugar = [KeyboardButton(text='С сахаром'),KeyboardButton(text='Без сахара')]
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


oplata_1 = [InlineKeyboardButton(text = 'Перейти к опате',url = 'https://transfer.paycom.uz/5fd9d96be88fb9bb61a4b2f9', callback_data= 'payme_1')]
oplata_2 = [InlineKeyboardButton(text = 'Перейти к опате',url='https://indoor.click.uz/pay?id=044220&t=0', callback_data='click_1')]



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

