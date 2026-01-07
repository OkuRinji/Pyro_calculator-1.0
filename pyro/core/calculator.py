from pyro.data.models import Component,Library
from pyro.data.db_loader import db_comp_get
from sympy import symbols, Eq, nsolve

#Функция - считает небходимое содержание компонентов по двум компонентам и желаемому окислительному балансу 
def oxy_calc(oxi_id:int,fuel_id:int,balance)->tuple [float,float]:
        try:
                oxi=db_comp_get(oxi_id,"oxi")
                fuel=db_comp_get(fuel_id,"fuel")
        except Exception as e :
                raise ValueError(f"Не поучилось загрузть компоненты {e}")
        if oxi.demidov_coeff==0 or fuel.demidov_coeff==0:
                raise ValueError("Коэффициент Демидова не может быть нулевым") 
        x1, x2,  = symbols('x1 ,x2')
        equations=[
        Eq(x1/oxi.demidov_coeff - x2/fuel.demidov_coeff , balance),
        Eq(x1 + x2 , 100),]
        try:
                initial_guess = [50, 50]
                oxi_part, fuel_part = nsolve(equations, (x1, x2), initial_guess)
        except:
                raise ValueError("Не удалось решить уравнение")
        if oxi_part <0 :
                raise ValueError("Массовая доля окислителя - меньше нуля выбереите более эффективное горючее или увеличте запрашиваемый ОБ")
        elif fuel_part <0 :
                raise ValueError("Массовая доля горючего - меньше нуля выбереите более эффективный окислитель или снизьте запрашиваемый ОБ")
        return round(oxi_part,3),round(fuel_part,3)
  
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
       