import psycopg2
from .models import Library, Component
import json
connection = psycopg2.connect( host="localhost", port="5432",user='postgres',password="Hinbrg456", dbname='pyrotech')
#Инициализация бд- создание таблица в случае если ее еще нет
def init_db(conn=connection):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS oxis (
                id SERIAL PRIMARY KEY,
                number INTEGER NOT NULL,
                name TEXT NOT NULL,
                enthalpy DOUBLE PRECISION,
                demidov_coeff DOUBLE PRECISION,
                molar_mass DOUBLE PRECISION,
                formula JSONB NOT NULL,
                UNIQUE (name)
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS fuels (
                id SERIAL PRIMARY KEY,
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
def lib_db_insert(lib:Library,conn=connection ) :
    for comp in lib:
        formula_json = json.dumps(comp.formula)
        with conn.cursor() as cur:
            if comp.type=="oxi":
                    cur.execute("""INSERT INTO 
                                oxis (number,name,enthalpy,demidov_coeff,molar_mass,formula) 
                                VALUES
                                (%s,%s,%s,%s,%s,%s)
                                """,
                            (
                                comp.number,
                                comp.name,
                                comp.enthalpy,
                                comp.demidov_coeff,
                                comp.molar_mass,
                                formula_json
                                )
                    )
            elif comp.type=="fuel":
                cur.execute("""INSERT INTO 
                                fuels (number,name,enthalpy,demidov_coeff,molar_mass,formula) 
                                VALUES
                                (%s,%s,%s,%s,%s,%s)
                                """,
                            (
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
def db_comp_get(comp_id:int,comp_type)-> Component:
    cur=connection.cursor()
    if comp_type=="oxi":
        cur.execute("""SELECT number,name,enthalpy,demidov_coeff,molar_mass,formula FROM oxis WHERE id = %s """,[comp_id])
    elif comp_type=="fuel":
        cur.execute("""SELECT number,name,enthalpy,demidov_coeff,molar_mass,formula FROM fuels WHERE id = %s """,[comp_id])
    a=cur.fetchone()
    #print(*a,type(a))
    comp=Component(comp_type,*a)
    return comp



init_db(connection)
cur=connection.cursor()
cur.execute("SELECT * FROM components")
data=cur.fetchall()
#print(data) 

from .loaders import load_library_from_excel
lib=load_library_from_excel("data/comp_lib_oxy.xlsx")
# lib_db_insert(lib)

cur.execute("SELECT * FROM components")
data=cur.fetchall()
#print(data) 
