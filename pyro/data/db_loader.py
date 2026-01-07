import psycopg2
from .models import Library, Component
import json
connection = psycopg2.connect( host="localhost", port="5432",user='postgres',password="Hinbrg456", dbname='pyrotech')
#Инициализация бд- создание таблица в случае если ее еще нет
def init_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS components (
                id SERIAL PRIMARY KEY,
                type TEXT NOT NULL CHECK (type IN ('oxi', 'fuel')),
                number INTEGER NOT NULL,
                name TEXT NOT NULL,
                enthalpy DOUBLE PRECISION,
                demidov_coeff DOUBLE PRECISION,
                molar_mass DOUBLE PRECISION,
                formula JSONB NOT NULL,
                UNIQUE (name)
            );
        """)
        conn.commit()
#Добавление списка компонентов класса Library в БД
def lib_db_insert(conn,lib:Library ) :
    for comp in lib:
        formula_json = json.dumps(comp.formula)
        with conn.cursor() as cur:
             cur.execute("""INSERT INTO 
                            components (type,number,name,enthalpy,demidov_coeff,molar_mass,formula) 
                         VALUES
                            (%s,%s,%s,%s,%s,%s,%s)
                         """,
                        (
                         comp.type,
                         comp.number,
                         comp.name,
                         comp.enthalpy,
                         comp.demidov_coeff,
                         comp.molar_mass,
                         formula_json
                         )
                )
             conn.commit()
# Получение экземпляра компонента из БД по id
def db_comp_get(comp_id:int)-> Component:
    cur=connection.cursor()
    cur.execute("""SELECT type,number,name,enthalpy,demidov_coeff,molar_mass,formula FROM components WHERE id = %s """,[comp_id])
    a=cur.fetchone()
    #print(*a,type(a))
    comp=Component(*a)
    return comp


connection = psycopg2.connect( host="localhost", port="5432",user='postgres',password="Hinbrg456", dbname='pyrotech')
init_db(connection)
cur=connection.cursor()
cur.execute("SELECT * FROM components")
data=cur.fetchall()
#print(data) 

from .loaders import load_library_from_excel
lib=load_library_from_excel("data/comp_lib_oxy.xlsx")
#lib_db_insert(connection,lib)

cur.execute("SELECT * FROM components")
data=cur.fetchall()
#print(data) 
