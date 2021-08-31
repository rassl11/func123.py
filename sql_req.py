import sqlite3
conn = sqlite3.connect('identifier.sqlite')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS Users
(
TG_ID INTEGER,
First_Name STRING,
Phone INTEGER ,
TABLE_NUMB INTEGER,
total_zakaz STRING,
Zakaz STRING,
price INTEGER,
total_price INTEGER ,
Stage INTEGER,
Comment_dish STRING,
Comment STRING,
visit INTEGER ,
cashback INTEGER,
id_tovara STRING)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Goods
(
id STRING,
Tovari STRING,
Opisanie STRING,
Cost INTEGER ,
Amount INTEGER,
Photo STRING
)

''')



get_id = '''
SELECT id
FROM Goods
WHERE Tovari = '{}'
'''

get_id_tovara = '''
SELECT id_tovara
FROM Users
WHERE TG_ID = '{}'
'''

update_id_tovara = '''
UPDATE Users
SET id_tovara = '{}'
WHERE TG_ID = '{}'
'''



first_insert = '''
INSERT INTO Users VALUES ('{}','{}',0,0,'','',0,0,0,'Отсутствует','Отсутствует',0,0,'')
'''


comment_dish = '''
SELECT Comment_dish
FROM Users
WHERE TG_ID = '{}'
'''

update_dish = '''
UPDATE Users
SET Comment_dish = '{}'
WHERE TG_ID ='{}'
'''

visit = '''
SELECT visit
FROM Users
WHERE TG_ID = '{}'
'''

update_visit = '''
UPDATE Users
SET visit = '{}'
WHERE TG_Id = '{}'
'''


cashback = '''
SELECT cashback
FROM Users
WHERE TG_ID = '{}'
'''

update_cashback = '''
UPDATE Users
SET cashback = '{}'
WHERE TG_ID = '{}'
'''

first_name = '''
UPDATE Users
SET First_name = '{}'
WHERE TG_ID = '{}'
'''

comment = '''
SELECT Comment
FROM Users
WHERE TG_ID = '{}'
'''

update_comment ='''
UPDATE Users
SET Comment = '{}'
WHERE TG_ID = '{}'
'''


update_total_zakaz = '''
UPDATE Users 
SET total_zakaz = '{}'
WHERE TG_ID = '{}'
'''

get_total_zakaz = '''
SELECT total_zakaz
FROM Users
WHERE TG_ID = '{}'
'''


get_price = '''
SELECT price
FROM Users
WHERE TG_ID = '{}'
'''

update_price = '''
UPDATE Users
SET price = '{}'
WHERE TG_ID = '{}'
'''

update_total_price = '''
UPDATE Users
SET total_price = '{}'
WHERE TG_ID = '{}'
'''

set_total_price = '''
SELECT total_price
FROM Users
WHERE TG_ID = '{}'
'''

sql_set_zakaz = '''
UPDATE Users
SET Zakaz = '{}'
WHERE TG_ID = '{}'
'''


sql_get_zakaz = '''
SELECT Zakaz
FROM Users
WHERE TG_ID = '{}'
'''

opisanie = '''
SELECT Opisanie
FROM Goods
WHERE Tovari = '{}'
'''


photo = '''
SELECT Photo
FROM Goods
WHERE Tovari = '{}'
'''

cost = '''
SELECT Cost
FROM Goods
WHERE Tovari = '{}'
'''



id_in_table = '''
SELECT TG_ID
FROM Users
WHERE TG_ID = '{}'
'''
update_mark = '''
UPDATE Users
SET Mark = '{}'
WHERE TG_ID = '{}'
'''

update_time = '''
UPDATE Users
SET day_and_time = '{}'
WHERE TG_ID = '{}'
'''

update_table_number = '''
UPDATE Users
SET TABLE_NUMB = '{}'
WHERE TG_ID = '{}'
'''
table_number_in_table = '''
SELECT TABLE_NUMB
FROM Users
WHERE TG_ID = '{}'
'''

stage_in = '''
SELECT Stage
FROM Users
WHERE TG_ID = '{}'
'''

update_stage_in = '''
UPDATE Users
SET Stage = '{}'
WHERE TG_ID = '{}'
'''

update_phone_no = '''
UPDATE Users
SET Phone = '{}'
WHERE TG_ID = '{}'
'''

delete_total_zakaz = '''
UPDATE Users
SET total_zakaz = ''
WHERE TG_ID = '{}'
'''


delete_zakaz = '''
UPDATE Users
SET Zakaz = ''
WHERE TG_ID = '{}'
'''

update_amount = '''
UPDATE Goods
SET Amount = '{}'
WHERE Tovari = '{}'
'''

blyuda = '''
SELECT Tovari
FROM Goods
'''


amount = '''
SELECT Amount
FROM Goods
WHERE Tovari = '{}'
'''

get_cashbak = '''
SELECT cashback
FROM Users
WHERE TG_ID = '{}'
'''

select_phone = '''
SELECT Phone
FROM Users
WHERE TG_ID ='{}'
'''