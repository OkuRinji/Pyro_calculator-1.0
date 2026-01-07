from pyro.data.models import Component,Library
from pyro.data.db_loader import db_comp_get
from sympy import symbols, Eq, nsolve

#Функция - считает небходимое содержание компонентов по двум компонентам и желаемому окислительному балансу 
def oxy_calc(oxi_id:int,fuel_id:int,balance)->float:
        no_oxi_flag=True
        no_fuel_flag=True
        oxi=db_comp_get(oxi_id)
        fuel=db_comp_get(fuel_id)
        dem_oxi=oxi.demidov_coeff
        dem_fuel=fuel.demidov_coeff
     
        x1, x2,  = symbols('x1 ,x2')
        equations=[
        Eq(x1/dem_oxi - x2/dem_fuel , balance),
        Eq(x1 + x2 , 100),]
        initial_guess = [50, 50]
        comp_ratio = nsolve(equations, (x1, x2), initial_guess)
        return comp_ratio[0],comp_ratio[1]
  
#Для дорботки по несколько компонентов
   # for i in comp_ids:
        #         comp=db_comp_get(i)
        #         if comp.type=="oxi":
        #                 dem_oxi+=comp.demidov_coeff
        #                 no_oxi_flag=False
        #         elif comp.type=="fuel":
        #                 dem_fuel+=comp.demidov_coeff
        #                 no_fuel_flag=False
        # if no_oxi_flag:
        #         print("Добавтье хотя бы один окислитель ")
        #         return
        # elif no_fuel_flag:
        #         print("Добавтье хотя бы одно горючее ")
        #         return
       