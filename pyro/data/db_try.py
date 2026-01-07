import psycopg2 
conn = psycopg2.connect( host="localhost", port="5432",user='postgres',password="Hinbrg456")
conn.autocommit = True
curs=conn.cursor()
curs.execute("CREATE DATABASE pyrotech;")
conn.commit()
curs.close()
conn.close()