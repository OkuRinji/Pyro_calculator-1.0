from models import Library,Component
from loaders import load_library_from_excel
import psycopg2
from functools import wraps
from time import perf_counter
# def timer(f):
#     @wraps(f)
#     def wrapper(*args,**kwargs):
#         start=perf_counter()
#         result=f(*args,**kwargs)
#         end=perf_counter()
#         total_time=end-start
#         print(f"Работа функции заняла {total_time} с")
#         return result
#     return wrapper

# @timer
# def item_iter(lib):
#     for comp in lib:
#         print("Имя:", comp.name)
# lib=load_library_from_excel('data/comp_lib_oxy.xlsx')
# for component in lib:
#     print(component)

connection = psycopg2.connect( host="localhost", port="5432",user='postgres',password="Hinbrg456", dbname='pyrotech')
def db_comp_get(comp_id):
    cur=connection.cursor()
    cur.execute("""SELECT number,name,enthalpy,demidov_coeff,molar_mass,formula FROM components WHERE id = %s """,[comp_id])
    a=cur.fetchone()
    print(*a,type(a))
    comp=Component(*a)

db_comp_get(2)