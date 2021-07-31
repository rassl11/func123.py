import sqlite3
conn = sqlite3.connect('identifier.sqlite')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS Users
(
day_and_time INTEGER,
TG_ID INTEGER,
First_Name STRING,
Phone INTEGER ,
TABLE_NUMB INTEGER,
Mark LIST,
Zakaz LIST,
Stage INTEGER )
''')


first_insert = '''
INSERT INTO Users VALUES (0,'{}','{}',0,0,0,'[]',0)
'''


cur.execute('''
CREATE TABLE IF NOT EXISTS Goods
(
Tovar STRING,
Opisanie STRING,
Cost INTEGER,
Amount INTEGER,
Photo STRING
)
''')


zakaz = '''
SELECT Zakaz
FROM Users
WHERE TG_ID = '{}'
'''


update_zakaz = '''
UPDATE Users
SET Zakaz = '{}'
WHERE TG_ID = '{}'
'''

opisanie = '''
SELECT Opisanie
FROM Goods
WHERE Tovar = '{}'
'''
cost = '''
SELECT Cost
FROM Goods
WHERE Tovar = '{}'
'''

photo = '''
SELECT Photo
FROM Goods
WHERE Tovar = '{}'
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
