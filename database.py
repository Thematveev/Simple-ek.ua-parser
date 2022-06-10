import psycopg2

connection = psycopg2.connect(
    host='abul.db.elephantsql.com',
    dbname='omzfpqup',
    user='omzfpqup',
    password='wwb-EZzF3yVduVYWymWNoNhpDTh8mbmx'
)
cursor = connection.cursor()

def add_item(name, link, img):
    cursor.execute('insert into items(product, link, img_link) values (%s, %s, %s);', [name, link, img])


def commit():
    connection.commit()