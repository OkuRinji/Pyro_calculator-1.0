from conf import connection

with connection.cursor() as cur:
    cur.execute("DROP TABLE oxis,fuels")
    connection.commit()